import open3d as o3d
import numpy as np
import sys
import copy
import os

from register_fragments import make_posegraph_for_scene
from refine_registration import local_refinement
sys.path.append("../Basic")
from icp_registration import draw_registration_result
sys.path.append("../Utility")
from file import *

class matching_result:

	def __init__(self, s, t):
		self.s = s
		self.t = t
		self.success = False
		self.transformation = np.identity(4)
		self.information = np.identity(6)


# ==================================================================================
# get all scene files in the floder 'dataset'
# return a file name list sorted by number
# ==================================================================================
def get_file_names(config):
	files_list = os.listdir("dataset")
	files = []
	rgbd_files = []
	for file in files_list:
		if(file[0:10]=="realsense_"):
			files.append(join("dataset/", file, "scene/integrated.ply"))
			rgbd_files.append(join("dataset/", file))
	files.sort()
	rgbd_files.sort()
	print(rgbd_files)
	return files, rgbd_files


def read_rgbd_images(color_file, depth_file):
	color = o3d.io.read_image(color_file)
	depth = o3d.io.read_image(depth_file)
	rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
		color, depth, 
		depth_trunc=3.0, 
		convert_rgb_to_intensity=False)
	return rgbd_image


# ==================================================================================
# use fpfh feature to match between a pair of scene
# return transformation and information matrix
# ==================================================================================
def compute_transformation_fpfh(s, t, config):
	source = o3d.io.read_point_cloud(s)
	target = o3d.io.read_point_cloud(t)

	print("Computering transformation between source %s and target %s ..." % (s[18], t[18]))
	voxel_size = config["voxel_size"]
	source_fpfh = o3d.registration.compute_fpfh_feature(
		source, 
		o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size*5.0, max_nn=100))
	target_fpfh = o3d.registration.compute_fpfh_feature(
		target, 
		o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size*5.0, max_nn=100))

	result = o3d.registration.RegistrationResult()
	
	# result = o3d.registration.registration_ransac_based_on_feature_matching(
	# 	source, target, source_fpfh, target_fpfh, voxel_size*1.4, 
	# 	o3d.registration.TransformationEstimationPointToPoint(False), 4, 
	# 	[o3d.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
	# 	o3d.registration.CorrespondenceCheckerBasedOnDistance(voxel_size*1.4)], 
	# 	o3d.registration.RANSACConvergenceCriteria(4000000, 500)
	# 	)

	result = o3d.registration.registration_icp(
		source, target, 0.02, result.transformation,
		o3d.registration.TransformationEstimationPointToPlane())

	result.transformation, information = local_refinement(source, 
														  target, 
														  result.transformation, 
														  config)


	information = o3d.registration.get_information_matrix_from_point_clouds(
		source, target, voxel_size*1.4, result.transformation)

	if(result.transformation.trace() == 4.0):
		return(False, np.identity(4), np.zeros((6, 6)))

	if(information[5, 5] / min(len(source.points), len(target.points)) < 0.3):
		return(False, np.identity(4), np.zeros((6, 6)))
	# print("Transformation: ", result.transformation, information)
	
	source_visual = copy.deepcopy(source)
	target_visual = copy.deepcopy(target)
	source_visual.transform(result.transformation)
	o3d.visualization.draw_geometries([source_visual, target_visual])
	
	print("compute trans finished")
	return True, result.transformation, information


# ==================================================================================
# make pose graph for scene
# each node represents a scene
# each edge represents 
# ==================================================================================
def make_posegraph_for_scene(ply_file_names, config):
	n_files = len(ply_file_names)
	print("Number of scenes: ", n_files)

	odometry = np.identity(4)
	pose_graph = o3d.registration.PoseGraph()
	pose_graph.nodes.append(o3d.registration.PoseGraphNode(odometry))

	matching_results = {}

	for i in range(n_files):
		for j in range(i+1, n_files):
			matching_results[i*n_files + j] = matching_result(i, j)

	# compute transformation matrix for each pair
	for r in matching_results:
		s = matching_results[r].s
		t = matching_results[r].t
		source_path = ply_file_names[s]
		target_path = ply_file_names[t]

		(success, transformation, information) = \
				compute_transformation_fpfh(source_path, 
											target_path, 
											config)
		matching_results[r].success = success
		matching_results[r].transformation = transformation 
		matching_results[r].information = information

		if(t == s+1):
			odometry = np.dot(transformation, odometry)
			# odometry_inv = np.linalg.inv(odometry)
			pose_graph.nodes.append(o3d.registration.PoseGraphNode(odometry))
			pose_graph.edges.append(o3d.registration.PoseGraphEdge(s, t, 
																   transformation, 
																   information, 
																   uncertain=True))
		else:
			pose_graph.edges.append(o3d.registration.PoseGraphEdge(s, t, 
																   transformation, 
																   information, 
																   uncertain=True))

	o3d.io.write_pose_graph("./dataset/global_scene.json", pose_graph)


# ==================================================================================
# ==================================================================================
def integrate_rgb_fragments(rgbd_path, config):
	volume = o3d.integration.ScalableTSDFVolume(
								voxel_length=config["tsdf_cubic_size"] / 512.0, 
								sdf_trunc=0.04, 
								color_type=o3d.integration.TSDFVolumeColorType.RGB8)
	
	for scene_id in range(len(rgbd_path)):
		pose_graph_scene = o3d.io.read_pose_graph("./dataset/global_scene.json")
		instrinsic = o3d.io.read_pinhole_camera_intrinsic(
			join(rgbd_path[scene_id], "camera_intrinsic.json"))

		[color_files, depth_files] = get_rgbd_file_lists(rgbd_path[scene_id])

		pose_graph_fragment = o3d.io.read_pose_graph(
			join(rgbd_path[scene_id], 
				config["template_refined_posegraph_optimized"]))

		for fragment_id in range(len(pose_graph_fragment.nodes)):
			pose_graph_rgbd = o3d.io.read_pose_graph(
				join(rgbd_path[scene_id], 
					config["template_fragment_posegraph_optimized"] % fragment_id))

			for frame_id in range(len(pose_graph_rgbd.nodes)):
				frame_id_abs = fragment_id*config["n_frames_per_fragment"] + frame_id
				print("Integrate frame: ", color_files[frame_id_abs])

				rgbd = read_rgbd_images(color_files[frame_id_abs], depth_files[frame_id_abs])
				pose = np.dot(pose_graph_fragment.nodes[fragment_id].pose, 
							  pose_graph_rgbd.nodes[frame_id].pose)
				pose = np.dot(np.linalg.inv(pose), pose_graph_scene.nodes[scene_id].pose)
				volume.integrate(rgbd, instrinsic, pose)

	mesh = volume.extract_triangle_mesh()
	mesh.compute_vertex_normals()

	result_point = volume.extract_point_cloud()
	o3d.visualization.draw_geometries([result_point])

	o3d.io.write_triangle_mesh("./dataset/output_mesh.ply", mesh, False, True)
	o3d.io.write_point_cloud("./dataset/output_pointcloud.ply", result_point, False, False, False)


def run(config):
	scene_names, rgbd_path = get_file_names(config)
	make_posegraph_for_scene(scene_names, config)
	integrate_rgb_fragments(rgbd_path, config)
