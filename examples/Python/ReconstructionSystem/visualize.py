import open3d as o3d
import numpy as np


def main():

	pcd = o3d.io.read_point_cloud("dataset/realsense/scene/integrated.ply")
	print(pcd)
	print(np.asarray(pcd.points))
	o3d.visualization.draw_geometries([pcd])


if __name__ == '__main__':
	main()