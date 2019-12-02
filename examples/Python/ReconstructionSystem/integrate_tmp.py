import open3d as o3d
import numpy as np
import sys
import copy

from register_fragments import make_posegraph_for_scene
sys.path.append("../Basic")
from icp_registration import draw_registration_result
sys.path.append("../Utility")
from file import *

voxel_size = 0.05


class matching_result:

	def __init__(self, s, t):
		self.s = s
		self.t = t
		self.success = False
		self.transformation = np.identity(4)
		self.information = np.identity(6)


def read_rgbd_images(color_file, depth_file):
	color = o3d.io.read_image(color_file)
	depth = o3d.io.read_image(depth_file)
	rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
		color, depth, 
		depth_trunc=3.0, 
		convert_rgb_to_intensity=False)
	return rgbd_image


def read_ply_files():
	scene1 = o3d.io.read_point_cloud("./dataset/realsense_1/scene/integrated.ply")
	scene2 = o3d.io.read_point_cloud("./dataset/realsense_2/scene/integrated.ply")

	return scene1, scene2


def compute_trans(ply_file_names, s, t):
	source = o3d.io.read_point_cloud(ply_file_names[s])
	target = o3d.io.read_point_cloud(ply_file_names[t])
	print("Scene1: ", source)
	print("Scene2: ", target)

	print("Computering transformation ...")
	source_fpfh = o3d.registration.compute_fpfh_feature(
		source, 
		o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size*5.0, max_nn=100))
	target_fpfh = o3d.registration.compute_fpfh_feature(
		target, 
		o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size*5.0, max_nn=100))

	result = o3d.registration.registration_ransac_based_on_feature_matching(
		source, target, source_fpfh, target_fpfh, voxel_size*1.4, 
		o3d.registration.TransformationEstimationPointToPoint(False), 4, 
		[o3d.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
		o3d.registration.CorrespondenceCheckerBasedOnDistance(voxel_size*1.4)], 
		o3d.registration.RANSACConvergenceCriteria(4000000, 500)
		)

	result = o3d.registration.registration_icp(
		source, target, 0.02, result.transformation,
		o3d.registration.TransformationEstimationPointToPlane())

	information = o3d.registration.get_information_matrix_from_point_clouds(
		source, target, voxel_size*1.4, result.transformation)
	# print("Transformation: ", result.transformation, information)
	print("compute trans finished")
	return result.transformation, information


def make_posegraph(ply_file_names):
	odometry = np.identity(4)
	pose_graph = o3d.registration.PoseGraph()
	pose_graph.nodes.append(o3d.registration.PoseGraphNode(odometry))

	n_files = len(ply_file_names)

	matching_results = {}

	for i in range(n_files):
		for j in range(i+1, n_files):
			matching_results[i*n_files + j] = matching_result(i, j)

	print(matching_results)
	for r in matching_results:
		# compute_trans(ply_file_names, matching_results[r].s, matching_results[r].t)
		matching_results[r].success = True
		(matching_results[r].transformation, matching_results[r].information) = \
			compute_trans(ply_file_names, matching_results[r].s, matching_results[r].t)

	odometry = np.dot(matching_results[1].transformation, odometry)
	odometry_inv = np.linalg.inv(odometry)
	pose_graph.nodes.append(o3d.registration.PoseGraphNode(odometry_inv))
	pose_graph.edges.append(
		o3d.registration.PoseGraphEdge(0, 1, 
			matching_results[1].transformation, 
			matching_results[1].information, uncertain=True))

	o3d.io.write_pose_graph("./dataset/global_scene.json", pose_graph)


def integrate_rgb_fragments(path_images_1, path_images_2, instrinsic_1, instrinsic_2):
	poses = []
	[color_files_1, depth_files_1] = get_rgbd_file_lists(path_images_1)
	[color_files_2, depth_files_2] = get_rgbd_file_lists(path_images_2)
	n_files = len(color_files_1) + len(color_files_2)

	volume = o3d.integration.ScalableTSDFVolume(
		voxel_length=3.0/512.0, sdf_trunc=0.04, color_type=o3d.integration.TSDFVolumeColorType.RGB8)

	pose_graph_scene = o3d.io.read_pose_graph("./dataset/global_scene.json")
	pose_graph_fragment1 = o3d.io.read_pose_graph(
		"./dataset/realsense_1/scene/refined_registration_optimized.json")
	pose_graph_fragment2 = o3d.io.read_pose_graph(
		"./dataset/realsense_2/scene/refined_registration_optimized.json")

	for fragment_id in range(len(pose_graph_fragment1.nodes)):
		pose_graph_rgbd = o3d.io.read_pose_graph(
			"./dataset/realsense_1/fragments/fragment_optimized_%03d.json" % fragment_id)
		for frame_id in range(len(pose_graph_rgbd.nodes)):
			frame_id_abs = fragment_id*100 + frame_id
			print(color_files_1[frame_id_abs])
			rgbd = read_rgbd_images(color_files_1[frame_id_abs], depth_files_1[frame_id_abs])
			pose = np.dot(pose_graph_fragment1.nodes[fragment_id].pose, 
						  pose_graph_rgbd.nodes[frame_id].pose)
			pose = np.dot(pose, pose_graph_scene.nodes[0].pose)
			volume.integrate(rgbd, instrinsic_1, np.linalg.inv(pose))

	mesh = volume.extract_triangle_mesh()
	mesh.compute_vertex_normals()

	o3d.io.write_triangle_mesh("./dataset/output.ply", mesh, False, True)



def main():
	'''
	scene1, scene2 = read_ply_files()
	print("Scene1: ", scene1)
	print("Scene2: ", scene2)
	'''

	trans_init = np.identity(4)

	# o3d.visualization.draw_geometries([scene1, scene2])
	ply_file_names = ["./dataset/realsense_1/scene/integrated.ply", 
						"./dataset/realsense_2/scene/integrated.ply"]

	make_posegraph(ply_file_names)

	path_images_1 = "./dataset/realsense_1/"
	path_images_2 = "./dataset/realsense_2/"
	instrinsic_1 = o3d.io.read_pinhole_camera_intrinsic(
		"./dataset/realsense_1/camera_intrinsic.json")
	instrinsic_2 = o3d.io.read_pinhole_camera_intrinsic(
		"./dataset/realsense_2/camera_intrinsic.json")
	integrate_rgb_fragments(path_images_1, path_images_2, instrinsic_1, instrinsic_2)
	'''
	source = copy.deepcopy(scene1)
	target = copy.deepcopy(scene2)
	trans, information = compute_trans(ply_file_names, 0, 1)
	
	source.transform(trans)
	o3d.visualization.draw_geometries([source, target])
	'''



if __name__ == '__main__':
	main()