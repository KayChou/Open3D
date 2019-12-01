import open3d as o3d
import numpy as np
import sys
import copy

from register_fragments import make_posegraph_for_scene

sys.path.append("../Basic")
from icp_registration import draw_registration_result

voxel_size = 0.05


def read_ply_files():
	scene1 = o3d.io.read_point_cloud("./dataset/realsense_1/scene/integrated.ply")
	scene2 = o3d.io.read_point_cloud("./dataset/realsense_2/scene/integrated.ply")

	return scene1, scene2


def compute_trans(source, target):
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
	print("Transformation: ", result.transformation)
	return result.transformation


def main():
	scene1, scene2 = read_ply_files()
	print("Scene1: ", scene1)
	print("Scene2: ", scene2)

	trans_init = np.identity(4)

	# o3d.visualization.draw_geometries([scene1, scene2])

	source = copy.deepcopy(scene1)
	target = copy.deepcopy(scene2)
	trans = compute_trans(source, target)
	source.transform(trans)
	trans = compute_trans(source, target)

	source.transform(trans)
	o3d.visualization.draw_geometries([source, target])



if __name__ == '__main__':
	main()