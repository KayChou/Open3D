====================================
Configuration
====================================
                    template_global_mesh : scene/integrated.ply
                               max_depth : 3.0
                          depth_map_type : redwood
                              voxel_size : 0.05
        preference_loop_closure_odometry : 0.1
                   n_frames_per_fragment : 100
                              debug_mode : False
               template_global_posegraph : scene/global_registration.json
                     global_registration : ransac
                                    name : Captured frames using Realsense
                 n_keyframes_per_n_frame : 5
                         folder_fragment : fragments/
     template_global_posegraph_optimized : scene/global_registration_optimized.json
                          max_depth_diff : 0.07
                            path_dataset : dataset/realsense/
            template_fragment_pointcloud : fragments/fragment_%03d.ply
                              icp_method : color
                          path_intrinsic : dataset/realsense/camera_intrinsic.json
                               min_depth : 0.3
    template_refined_posegraph_optimized : scene/refined_registration_optimized.json
                         tsdf_cubic_size : 3.0
                  python_multi_threading : False
    preference_loop_closure_registration : 5.0
                    template_global_traj : scene/trajectory.log
                            folder_scene : scene/
   template_fragment_posegraph_optimized : fragments/fragment_optimized_%03d.json
             template_fragment_posegraph : fragments/fragment_%03d.json
              template_refined_posegraph : scene/refined_registration.json
OpenCV is detected. Using ORB + 5pt algorithm
making fragments from RGBD sequence.
Fragment 000 / 009 :: RGBD matching between frame : 0 and 1
Fragment 000 / 009 :: RGBD matching between frame : 0 and 5
Fragment 000 / 009 :: RGBD matching between frame : 0 and 10
Fragment 000 / 009 :: RGBD matching between frame : 0 and 15
Fragment 000 / 009 :: RGBD matching between frame : 0 and 20
Fragment 000 / 009 :: RGBD matching between frame : 0 and 25
Fragment 000 / 009 :: RGBD matching between frame : 0 and 30
Fragment 000 / 009 :: RGBD matching between frame : 0 and 35
Fragment 000 / 009 :: RGBD matching between frame : 0 and 40
Fragment 000 / 009 :: RGBD matching between frame : 0 and 45
Fragment 000 / 009 :: RGBD matching between frame : 0 and 50
Fragment 000 / 009 :: RGBD matching between frame : 0 and 55
Fragment 000 / 009 :: RGBD matching between frame : 0 and 60
Fragment 000 / 009 :: RGBD matching between frame : 0 and 65
Fragment 000 / 009 :: RGBD matching between frame : 0 and 70
Fragment 000 / 009 :: RGBD matching between frame : 0 and 75
Fragment 000 / 009 :: RGBD matching between frame : 0 and 80
Fragment 000 / 009 :: RGBD matching between frame : 0 and 85
Fragment 000 / 009 :: RGBD matching between frame : 0 and 90
Fragment 000 / 009 :: RGBD matching between frame : 0 and 95
Fragment 000 / 009 :: RGBD matching between frame : 1 and 2
Fragment 000 / 009 :: RGBD matching between frame : 2 and 3
Fragment 000 / 009 :: RGBD matching between frame : 3 and 4
Fragment 000 / 009 :: RGBD matching between frame : 4 and 5
Fragment 000 / 009 :: RGBD matching between frame : 5 and 6
Fragment 000 / 009 :: RGBD matching between frame : 5 and 10
Fragment 000 / 009 :: RGBD matching between frame : 5 and 15
Fragment 000 / 009 :: RGBD matching between frame : 5 and 20
Fragment 000 / 009 :: RGBD matching between frame : 5 and 25
Fragment 000 / 009 :: RGBD matching between frame : 5 and 30
Fragment 000 / 009 :: RGBD matching between frame : 5 and 35
Fragment 000 / 009 :: RGBD matching between frame : 5 and 40
Fragment 000 / 009 :: RGBD matching between frame : 5 and 45
Fragment 000 / 009 :: RGBD matching between frame : 5 and 50
Fragment 000 / 009 :: RGBD matching between frame : 5 and 55
Fragment 000 / 009 :: RGBD matching between frame : 5 and 60
Fragment 000 / 009 :: RGBD matching between frame : 5 and 65
Fragment 000 / 009 :: RGBD matching between frame : 5 and 70
Fragment 000 / 009 :: RGBD matching between frame : 5 and 75
Fragment 000 / 009 :: RGBD matching between frame : 5 and 80
Fragment 000 / 009 :: RGBD matching between frame : 5 and 85
Fragment 000 / 009 :: RGBD matching between frame : 5 and 90
Fragment 000 / 009 :: RGBD matching between frame : 5 and 95
Fragment 000 / 009 :: RGBD matching between frame : 6 and 7
Fragment 000 / 009 :: RGBD matching between frame : 7 and 8
Fragment 000 / 009 :: RGBD matching between frame : 8 and 9
Fragment 000 / 009 :: RGBD matching between frame : 9 and 10
Fragment 000 / 009 :: RGBD matching between frame : 10 and 11
Fragment 000 / 009 :: RGBD matching between frame : 10 and 15
Fragment 000 / 009 :: RGBD matching between frame : 10 and 20
Fragment 000 / 009 :: RGBD matching between frame : 10 and 25
Fragment 000 / 009 :: RGBD matching between frame : 10 and 30
Fragment 000 / 009 :: RGBD matching between frame : 10 and 35
Fragment 000 / 009 :: RGBD matching between frame : 10 and 40
Fragment 000 / 009 :: RGBD matching between frame : 10 and 45
Fragment 000 / 009 :: RGBD matching between frame : 10 and 50
Fragment 000 / 009 :: RGBD matching between frame : 10 and 55
Fragment 000 / 009 :: RGBD matching between frame : 10 and 60
Fragment 000 / 009 :: RGBD matching between frame : 10 and 65
Fragment 000 / 009 :: RGBD matching between frame : 10 and 70
Fragment 000 / 009 :: RGBD matching between frame : 10 and 75
Fragment 000 / 009 :: RGBD matching between frame : 10 and 80
Fragment 000 / 009 :: RGBD matching between frame : 10 and 85
Fragment 000 / 009 :: RGBD matching between frame : 10 and 90
Fragment 000 / 009 :: RGBD matching between frame : 10 and 95
Fragment 000 / 009 :: RGBD matching between frame : 11 and 12
Fragment 000 / 009 :: RGBD matching between frame : 12 and 13
Fragment 000 / 009 :: RGBD matching between frame : 13 and 14
Fragment 000 / 009 :: RGBD matching between frame : 14 and 15
Fragment 000 / 009 :: RGBD matching between frame : 15 and 16
Fragment 000 / 009 :: RGBD matching between frame : 15 and 20
Fragment 000 / 009 :: RGBD matching between frame : 15 and 25
Fragment 000 / 009 :: RGBD matching between frame : 15 and 30
Fragment 000 / 009 :: RGBD matching between frame : 15 and 35
Fragment 000 / 009 :: RGBD matching between frame : 15 and 40
Fragment 000 / 009 :: RGBD matching between frame : 15 and 45
Fragment 000 / 009 :: RGBD matching between frame : 15 and 50
Fragment 000 / 009 :: RGBD matching between frame : 15 and 55
Fragment 000 / 009 :: RGBD matching between frame : 15 and 60
Fragment 000 / 009 :: RGBD matching between frame : 15 and 65
Fragment 000 / 009 :: RGBD matching between frame : 15 and 70
Fragment 000 / 009 :: RGBD matching between frame : 15 and 75
Fragment 000 / 009 :: RGBD matching between frame : 15 and 80
Fragment 000 / 009 :: RGBD matching between frame : 15 and 85
Fragment 000 / 009 :: RGBD matching between frame : 15 and 90
Fragment 000 / 009 :: RGBD matching between frame : 15 and 95
Fragment 000 / 009 :: RGBD matching between frame : 16 and 17
Fragment 000 / 009 :: RGBD matching between frame : 17 and 18
Fragment 000 / 009 :: RGBD matching between frame : 18 and 19
Fragment 000 / 009 :: RGBD matching between frame : 19 and 20
Fragment 000 / 009 :: RGBD matching between frame : 20 and 21
Fragment 000 / 009 :: RGBD matching between frame : 20 and 25
Fragment 000 / 009 :: RGBD matching between frame : 20 and 30
Fragment 000 / 009 :: RGBD matching between frame : 20 and 35
Fragment 000 / 009 :: RGBD matching between frame : 20 and 40
Fragment 000 / 009 :: RGBD matching between frame : 20 and 45
Fragment 000 / 009 :: RGBD matching between frame : 20 and 50
Fragment 000 / 009 :: RGBD matching between frame : 20 and 55
Fragment 000 / 009 :: RGBD matching between frame : 20 and 60
Fragment 000 / 009 :: RGBD matching between frame : 20 and 65
Fragment 000 / 009 :: RGBD matching between frame : 20 and 70
Fragment 000 / 009 :: RGBD matching between frame : 20 and 75
Fragment 000 / 009 :: RGBD matching between frame : 20 and 80
Fragment 000 / 009 :: RGBD matching between frame : 20 and 85
Fragment 000 / 009 :: RGBD matching between frame : 20 and 90
Fragment 000 / 009 :: RGBD matching between frame : 20 and 95
Fragment 000 / 009 :: RGBD matching between frame : 21 and 22
Fragment 000 / 009 :: RGBD matching between frame : 22 and 23
Fragment 000 / 009 :: RGBD matching between frame : 23 and 24
Fragment 000 / 009 :: RGBD matching between frame : 24 and 25
Fragment 000 / 009 :: RGBD matching between frame : 25 and 26
Fragment 000 / 009 :: RGBD matching between frame : 25 and 30
Fragment 000 / 009 :: RGBD matching between frame : 25 and 35
Fragment 000 / 009 :: RGBD matching between frame : 25 and 40
Fragment 000 / 009 :: RGBD matching between frame : 25 and 45
Fragment 000 / 009 :: RGBD matching between frame : 25 and 50
Fragment 000 / 009 :: RGBD matching between frame : 25 and 55
Fragment 000 / 009 :: RGBD matching between frame : 25 and 60
Fragment 000 / 009 :: RGBD matching between frame : 25 and 65
Fragment 000 / 009 :: RGBD matching between frame : 25 and 70
Fragment 000 / 009 :: RGBD matching between frame : 25 and 75
Fragment 000 / 009 :: RGBD matching between frame : 25 and 80
Fragment 000 / 009 :: RGBD matching between frame : 25 and 85
Fragment 000 / 009 :: RGBD matching between frame : 25 and 90
Fragment 000 / 009 :: RGBD matching between frame : 25 and 95
Fragment 000 / 009 :: RGBD matching between frame : 26 and 27
Fragment 000 / 009 :: RGBD matching between frame : 27 and 28
Fragment 000 / 009 :: RGBD matching between frame : 28 and 29
Fragment 000 / 009 :: RGBD matching between frame : 29 and 30
Fragment 000 / 009 :: RGBD matching between frame : 30 and 31
Fragment 000 / 009 :: RGBD matching between frame : 30 and 35
Fragment 000 / 009 :: RGBD matching between frame : 30 and 40
Fragment 000 / 009 :: RGBD matching between frame : 30 and 45
Fragment 000 / 009 :: RGBD matching between frame : 30 and 50
Fragment 000 / 009 :: RGBD matching between frame : 30 and 55
Fragment 000 / 009 :: RGBD matching between frame : 30 and 60
Fragment 000 / 009 :: RGBD matching between frame : 30 and 65
Fragment 000 / 009 :: RGBD matching between frame : 30 and 70
Fragment 000 / 009 :: RGBD matching between frame : 30 and 75
Fragment 000 / 009 :: RGBD matching between frame : 30 and 80
Fragment 000 / 009 :: RGBD matching between frame : 30 and 85
Fragment 000 / 009 :: RGBD matching between frame : 30 and 90
Fragment 000 / 009 :: RGBD matching between frame : 30 and 95
Fragment 000 / 009 :: RGBD matching between frame : 31 and 32
Fragment 000 / 009 :: RGBD matching between frame : 32 and 33
Fragment 000 / 009 :: RGBD matching between frame : 33 and 34
Fragment 000 / 009 :: RGBD matching between frame : 34 and 35
Fragment 000 / 009 :: RGBD matching between frame : 35 and 36
Fragment 000 / 009 :: RGBD matching between frame : 35 and 40
Fragment 000 / 009 :: RGBD matching between frame : 35 and 45
Fragment 000 / 009 :: RGBD matching between frame : 35 and 50
Fragment 000 / 009 :: RGBD matching between frame : 35 and 55
Fragment 000 / 009 :: RGBD matching between frame : 35 and 60
Fragment 000 / 009 :: RGBD matching between frame : 35 and 65
Fragment 000 / 009 :: RGBD matching between frame : 35 and 70
Fragment 000 / 009 :: RGBD matching between frame : 35 and 75
Fragment 000 / 009 :: RGBD matching between frame : 35 and 80
Fragment 000 / 009 :: RGBD matching between frame : 35 and 85
Fragment 000 / 009 :: RGBD matching between frame : 35 and 90
Fragment 000 / 009 :: RGBD matching between frame : 35 and 95
Fragment 000 / 009 :: RGBD matching between frame : 36 and 37
Fragment 000 / 009 :: RGBD matching between frame : 37 and 38
Fragment 000 / 009 :: RGBD matching between frame : 38 and 39
Fragment 000 / 009 :: RGBD matching between frame : 39 and 40
Fragment 000 / 009 :: RGBD matching between frame : 40 and 41
Fragment 000 / 009 :: RGBD matching between frame : 40 and 45
Fragment 000 / 009 :: RGBD matching between frame : 40 and 50
Fragment 000 / 009 :: RGBD matching between frame : 40 and 55
Fragment 000 / 009 :: RGBD matching between frame : 40 and 60
Fragment 000 / 009 :: RGBD matching between frame : 40 and 65
Fragment 000 / 009 :: RGBD matching between frame : 40 and 70
Fragment 000 / 009 :: RGBD matching between frame : 40 and 75
Fragment 000 / 009 :: RGBD matching between frame : 40 and 80
Fragment 000 / 009 :: RGBD matching between frame : 40 and 85
Fragment 000 / 009 :: RGBD matching between frame : 40 and 90
Fragment 000 / 009 :: RGBD matching between frame : 40 and 95
Fragment 000 / 009 :: RGBD matching between frame : 41 and 42
Fragment 000 / 009 :: RGBD matching between frame : 42 and 43
Fragment 000 / 009 :: RGBD matching between frame : 43 and 44
Fragment 000 / 009 :: RGBD matching between frame : 44 and 45
Fragment 000 / 009 :: RGBD matching between frame : 45 and 46
Fragment 000 / 009 :: RGBD matching between frame : 45 and 50
Fragment 000 / 009 :: RGBD matching between frame : 45 and 55
Fragment 000 / 009 :: RGBD matching between frame : 45 and 60
Fragment 000 / 009 :: RGBD matching between frame : 45 and 65
Fragment 000 / 009 :: RGBD matching between frame : 45 and 70
Fragment 000 / 009 :: RGBD matching between frame : 45 and 75
Fragment 000 / 009 :: RGBD matching between frame : 45 and 80
Fragment 000 / 009 :: RGBD matching between frame : 45 and 85
Fragment 000 / 009 :: RGBD matching between frame : 45 and 90
Fragment 000 / 009 :: RGBD matching between frame : 45 and 95
Fragment 000 / 009 :: RGBD matching between frame : 46 and 47
Fragment 000 / 009 :: RGBD matching between frame : 47 and 48
Fragment 000 / 009 :: RGBD matching between frame : 48 and 49
Fragment 000 / 009 :: RGBD matching between frame : 49 and 50
Fragment 000 / 009 :: RGBD matching between frame : 50 and 51
Fragment 000 / 009 :: RGBD matching between frame : 50 and 55
Fragment 000 / 009 :: RGBD matching between frame : 50 and 60
Fragment 000 / 009 :: RGBD matching between frame : 50 and 65
Fragment 000 / 009 :: RGBD matching between frame : 50 and 70
Fragment 000 / 009 :: RGBD matching between frame : 50 and 75
Fragment 000 / 009 :: RGBD matching between frame : 50 and 80
Fragment 000 / 009 :: RGBD matching between frame : 50 and 85
Fragment 000 / 009 :: RGBD matching between frame : 50 and 90
Fragment 000 / 009 :: RGBD matching between frame : 50 and 95
Fragment 000 / 009 :: RGBD matching between frame : 51 and 52
Fragment 000 / 009 :: RGBD matching between frame : 52 and 53
Fragment 000 / 009 :: RGBD matching between frame : 53 and 54
Fragment 000 / 009 :: RGBD matching between frame : 54 and 55
Fragment 000 / 009 :: RGBD matching between frame : 55 and 56
Fragment 000 / 009 :: RGBD matching between frame : 55 and 60
Fragment 000 / 009 :: RGBD matching between frame : 55 and 65
Fragment 000 / 009 :: RGBD matching between frame : 55 and 70
Fragment 000 / 009 :: RGBD matching between frame : 55 and 75
Fragment 000 / 009 :: RGBD matching between frame : 55 and 80
Fragment 000 / 009 :: RGBD matching between frame : 55 and 85
Fragment 000 / 009 :: RGBD matching between frame : 55 and 90
Fragment 000 / 009 :: RGBD matching between frame : 55 and 95
Fragment 000 / 009 :: RGBD matching between frame : 56 and 57
Fragment 000 / 009 :: RGBD matching between frame : 57 and 58
Fragment 000 / 009 :: RGBD matching between frame : 58 and 59
Fragment 000 / 009 :: RGBD matching between frame : 59 and 60
Fragment 000 / 009 :: RGBD matching between frame : 60 and 61
Fragment 000 / 009 :: RGBD matching between frame : 60 and 65
Fragment 000 / 009 :: RGBD matching between frame : 60 and 70
Fragment 000 / 009 :: RGBD matching between frame : 60 and 75
Fragment 000 / 009 :: RGBD matching between frame : 60 and 80
Fragment 000 / 009 :: RGBD matching between frame : 60 and 85
Fragment 000 / 009 :: RGBD matching between frame : 60 and 90
Fragment 000 / 009 :: RGBD matching between frame : 60 and 95
Fragment 000 / 009 :: RGBD matching between frame : 61 and 62
Fragment 000 / 009 :: RGBD matching between frame : 62 and 63
Fragment 000 / 009 :: RGBD matching between frame : 63 and 64
Fragment 000 / 009 :: RGBD matching between frame : 64 and 65
Fragment 000 / 009 :: RGBD matching between frame : 65 and 66
Fragment 000 / 009 :: RGBD matching between frame : 65 and 70
Fragment 000 / 009 :: RGBD matching between frame : 65 and 75
Fragment 000 / 009 :: RGBD matching between frame : 65 and 80
Fragment 000 / 009 :: RGBD matching between frame : 65 and 85
Fragment 000 / 009 :: RGBD matching between frame : 65 and 90
Fragment 000 / 009 :: RGBD matching between frame : 65 and 95
Fragment 000 / 009 :: RGBD matching between frame : 66 and 67
Fragment 000 / 009 :: RGBD matching between frame : 67 and 68
Fragment 000 / 009 :: RGBD matching between frame : 68 and 69
Fragment 000 / 009 :: RGBD matching between frame : 69 and 70
Fragment 000 / 009 :: RGBD matching between frame : 70 and 71
Fragment 000 / 009 :: RGBD matching between frame : 70 and 75
Fragment 000 / 009 :: RGBD matching between frame : 70 and 80
Fragment 000 / 009 :: RGBD matching between frame : 70 and 85
Fragment 000 / 009 :: RGBD matching between frame : 70 and 90
Fragment 000 / 009 :: RGBD matching between frame : 70 and 95
Fragment 000 / 009 :: RGBD matching between frame : 71 and 72
Fragment 000 / 009 :: RGBD matching between frame : 72 and 73
Fragment 000 / 009 :: RGBD matching between frame : 73 and 74
Fragment 000 / 009 :: RGBD matching between frame : 74 and 75
Fragment 000 / 009 :: RGBD matching between frame : 75 and 76
Fragment 000 / 009 :: RGBD matching between frame : 75 and 80
Fragment 000 / 009 :: RGBD matching between frame : 75 and 85
Fragment 000 / 009 :: RGBD matching between frame : 75 and 90
Fragment 000 / 009 :: RGBD matching between frame : 75 and 95
Fragment 000 / 009 :: RGBD matching between frame : 76 and 77
Fragment 000 / 009 :: RGBD matching between frame : 77 and 78
Fragment 000 / 009 :: RGBD matching between frame : 78 and 79
Fragment 000 / 009 :: RGBD matching between frame : 79 and 80
Fragment 000 / 009 :: RGBD matching between frame : 80 and 81
Fragment 000 / 009 :: RGBD matching between frame : 80 and 85
Fragment 000 / 009 :: RGBD matching between frame : 80 and 90
Fragment 000 / 009 :: RGBD matching between frame : 80 and 95
Fragment 000 / 009 :: RGBD matching between frame : 81 and 82
Fragment 000 / 009 :: RGBD matching between frame : 82 and 83
Fragment 000 / 009 :: RGBD matching between frame : 83 and 84
Fragment 000 / 009 :: RGBD matching between frame : 84 and 85
Fragment 000 / 009 :: RGBD matching between frame : 85 and 86
Fragment 000 / 009 :: RGBD matching between frame : 85 and 90
Fragment 000 / 009 :: RGBD matching between frame : 85 and 95
Fragment 000 / 009 :: RGBD matching between frame : 86 and 87
Fragment 000 / 009 :: RGBD matching between frame : 87 and 88
Fragment 000 / 009 :: RGBD matching between frame : 88 and 89
Fragment 000 / 009 :: RGBD matching between frame : 89 and 90
Fragment 000 / 009 :: RGBD matching between frame : 90 and 91
Fragment 000 / 009 :: RGBD matching between frame : 90 and 95
Fragment 000 / 009 :: RGBD matching between frame : 91 and 92
Fragment 000 / 009 :: RGBD matching between frame : 92 and 93
Fragment 000 / 009 :: RGBD matching between frame : 93 and 94
Fragment 000 / 009 :: RGBD matching between frame : 94 and 95
Fragment 000 / 009 :: RGBD matching between frame : 95 and 96
Fragment 000 / 009 :: RGBD matching between frame : 96 and 97
Fragment 000 / 009 :: RGBD matching between frame : 97 and 98
Fragment 000 / 009 :: RGBD matching between frame : 98 and 99
Fragment 000 / 009 :: integrate rgbd frame 0 (1 of 100).
Fragment 000 / 009 :: integrate rgbd frame 1 (2 of 100).
Fragment 000 / 009 :: integrate rgbd frame 2 (3 of 100).
Fragment 000 / 009 :: integrate rgbd frame 3 (4 of 100).
Fragment 000 / 009 :: integrate rgbd frame 4 (5 of 100).
Fragment 000 / 009 :: integrate rgbd frame 5 (6 of 100).
Fragment 000 / 009 :: integrate rgbd frame 6 (7 of 100).
Fragment 000 / 009 :: integrate rgbd frame 7 (8 of 100).
Fragment 000 / 009 :: integrate rgbd frame 8 (9 of 100).
Fragment 000 / 009 :: integrate rgbd frame 9 (10 of 100).
Fragment 000 / 009 :: integrate rgbd frame 10 (11 of 100).
Fragment 000 / 009 :: integrate rgbd frame 11 (12 of 100).
Fragment 000 / 009 :: integrate rgbd frame 12 (13 of 100).
Fragment 000 / 009 :: integrate rgbd frame 13 (14 of 100).
Fragment 000 / 009 :: integrate rgbd frame 14 (15 of 100).
Fragment 000 / 009 :: integrate rgbd frame 15 (16 of 100).
Fragment 000 / 009 :: integrate rgbd frame 16 (17 of 100).
Fragment 000 / 009 :: integrate rgbd frame 17 (18 of 100).
Fragment 000 / 009 :: integrate rgbd frame 18 (19 of 100).
Fragment 000 / 009 :: integrate rgbd frame 19 (20 of 100).
Fragment 000 / 009 :: integrate rgbd frame 20 (21 of 100).
Fragment 000 / 009 :: integrate rgbd frame 21 (22 of 100).
Fragment 000 / 009 :: integrate rgbd frame 22 (23 of 100).
Fragment 000 / 009 :: integrate rgbd frame 23 (24 of 100).
Fragment 000 / 009 :: integrate rgbd frame 24 (25 of 100).
Fragment 000 / 009 :: integrate rgbd frame 25 (26 of 100).
Fragment 000 / 009 :: integrate rgbd frame 26 (27 of 100).
Fragment 000 / 009 :: integrate rgbd frame 27 (28 of 100).
Fragment 000 / 009 :: integrate rgbd frame 28 (29 of 100).
Fragment 000 / 009 :: integrate rgbd frame 29 (30 of 100).
Fragment 000 / 009 :: integrate rgbd frame 30 (31 of 100).
Fragment 000 / 009 :: integrate rgbd frame 31 (32 of 100).
Fragment 000 / 009 :: integrate rgbd frame 32 (33 of 100).
Fragment 000 / 009 :: integrate rgbd frame 33 (34 of 100).
Fragment 000 / 009 :: integrate rgbd frame 34 (35 of 100).
Fragment 000 / 009 :: integrate rgbd frame 35 (36 of 100).
Fragment 000 / 009 :: integrate rgbd frame 36 (37 of 100).
Fragment 000 / 009 :: integrate rgbd frame 37 (38 of 100).
Fragment 000 / 009 :: integrate rgbd frame 38 (39 of 100).
Fragment 000 / 009 :: integrate rgbd frame 39 (40 of 100).
Fragment 000 / 009 :: integrate rgbd frame 40 (41 of 100).
Fragment 000 / 009 :: integrate rgbd frame 41 (42 of 100).
Fragment 000 / 009 :: integrate rgbd frame 42 (43 of 100).
Fragment 000 / 009 :: integrate rgbd frame 43 (44 of 100).
Fragment 000 / 009 :: integrate rgbd frame 44 (45 of 100).
Fragment 000 / 009 :: integrate rgbd frame 45 (46 of 100).
Fragment 000 / 009 :: integrate rgbd frame 46 (47 of 100).
Fragment 000 / 009 :: integrate rgbd frame 47 (48 of 100).
Fragment 000 / 009 :: integrate rgbd frame 48 (49 of 100).
Fragment 000 / 009 :: integrate rgbd frame 49 (50 of 100).
Fragment 000 / 009 :: integrate rgbd frame 50 (51 of 100).
Fragment 000 / 009 :: integrate rgbd frame 51 (52 of 100).
Fragment 000 / 009 :: integrate rgbd frame 52 (53 of 100).
Fragment 000 / 009 :: integrate rgbd frame 53 (54 of 100).
Fragment 000 / 009 :: integrate rgbd frame 54 (55 of 100).
Fragment 000 / 009 :: integrate rgbd frame 55 (56 of 100).
Fragment 000 / 009 :: integrate rgbd frame 56 (57 of 100).
Fragment 000 / 009 :: integrate rgbd frame 57 (58 of 100).
Fragment 000 / 009 :: integrate rgbd frame 58 (59 of 100).
Fragment 000 / 009 :: integrate rgbd frame 59 (60 of 100).
Fragment 000 / 009 :: integrate rgbd frame 60 (61 of 100).
Fragment 000 / 009 :: integrate rgbd frame 61 (62 of 100).
Fragment 000 / 009 :: integrate rgbd frame 62 (63 of 100).
Fragment 000 / 009 :: integrate rgbd frame 63 (64 of 100).
Fragment 000 / 009 :: integrate rgbd frame 64 (65 of 100).
Fragment 000 / 009 :: integrate rgbd frame 65 (66 of 100).
Fragment 000 / 009 :: integrate rgbd frame 66 (67 of 100).
Fragment 000 / 009 :: integrate rgbd frame 67 (68 of 100).
Fragment 000 / 009 :: integrate rgbd frame 68 (69 of 100).
Fragment 000 / 009 :: integrate rgbd frame 69 (70 of 100).
Fragment 000 / 009 :: integrate rgbd frame 70 (71 of 100).
Fragment 000 / 009 :: integrate rgbd frame 71 (72 of 100).
Fragment 000 / 009 :: integrate rgbd frame 72 (73 of 100).
Fragment 000 / 009 :: integrate rgbd frame 73 (74 of 100).
Fragment 000 / 009 :: integrate rgbd frame 74 (75 of 100).
Fragment 000 / 009 :: integrate rgbd frame 75 (76 of 100).
Fragment 000 / 009 :: integrate rgbd frame 76 (77 of 100).
Fragment 000 / 009 :: integrate rgbd frame 77 (78 of 100).
Fragment 000 / 009 :: integrate rgbd frame 78 (79 of 100).
Fragment 000 / 009 :: integrate rgbd frame 79 (80 of 100).
Fragment 000 / 009 :: integrate rgbd frame 80 (81 of 100).
Fragment 000 / 009 :: integrate rgbd frame 81 (82 of 100).
Fragment 000 / 009 :: integrate rgbd frame 82 (83 of 100).
Fragment 000 / 009 :: integrate rgbd frame 83 (84 of 100).
Fragment 000 / 009 :: integrate rgbd frame 84 (85 of 100).
Fragment 000 / 009 :: integrate rgbd frame 85 (86 of 100).
Fragment 000 / 009 :: integrate rgbd frame 86 (87 of 100).
Fragment 000 / 009 :: integrate rgbd frame 87 (88 of 100).
Fragment 000 / 009 :: integrate rgbd frame 88 (89 of 100).
Fragment 000 / 009 :: integrate rgbd frame 89 (90 of 100).
Fragment 000 / 009 :: integrate rgbd frame 90 (91 of 100).
Fragment 000 / 009 :: integrate rgbd frame 91 (92 of 100).
Fragment 000 / 009 :: integrate rgbd frame 92 (93 of 100).
Fragment 000 / 009 :: integrate rgbd frame 93 (94 of 100).
Fragment 000 / 009 :: integrate rgbd frame 94 (95 of 100).
Fragment 000 / 009 :: integrate rgbd frame 95 (96 of 100).
Fragment 000 / 009 :: integrate rgbd frame 96 (97 of 100).
Fragment 000 / 009 :: integrate rgbd frame 97 (98 of 100).
Fragment 000 / 009 :: integrate rgbd frame 98 (99 of 100).
Fragment 000 / 009 :: integrate rgbd frame 99 (100 of 100).
Fragment 001 / 009 :: RGBD matching between frame : 100 and 101
Fragment 001 / 009 :: RGBD matching between frame : 100 and 105
Fragment 001 / 009 :: RGBD matching between frame : 100 and 110
Fragment 001 / 009 :: RGBD matching between frame : 100 and 115
Fragment 001 / 009 :: RGBD matching between frame : 100 and 120
Fragment 001 / 009 :: RGBD matching between frame : 100 and 125
Fragment 001 / 009 :: RGBD matching between frame : 100 and 130
Fragment 001 / 009 :: RGBD matching between frame : 100 and 135
Fragment 001 / 009 :: RGBD matching between frame : 100 and 140
Fragment 001 / 009 :: RGBD matching between frame : 100 and 145
Fragment 001 / 009 :: RGBD matching between frame : 100 and 150
Fragment 001 / 009 :: RGBD matching between frame : 100 and 155
Fragment 001 / 009 :: RGBD matching between frame : 100 and 160
Fragment 001 / 009 :: RGBD matching between frame : 100 and 165
Fragment 001 / 009 :: RGBD matching between frame : 100 and 170
Fragment 001 / 009 :: RGBD matching between frame : 100 and 175
Fragment 001 / 009 :: RGBD matching between frame : 100 and 180
Fragment 001 / 009 :: RGBD matching between frame : 100 and 185
Fragment 001 / 009 :: RGBD matching between frame : 100 and 190
Fragment 001 / 009 :: RGBD matching between frame : 100 and 195
Fragment 001 / 009 :: RGBD matching between frame : 101 and 102
Fragment 001 / 009 :: RGBD matching between frame : 102 and 103
Fragment 001 / 009 :: RGBD matching between frame : 103 and 104
Fragment 001 / 009 :: RGBD matching between frame : 104 and 105
Fragment 001 / 009 :: RGBD matching between frame : 105 and 106
Fragment 001 / 009 :: RGBD matching between frame : 105 and 110
Fragment 001 / 009 :: RGBD matching between frame : 105 and 115
Fragment 001 / 009 :: RGBD matching between frame : 105 and 120
Fragment 001 / 009 :: RGBD matching between frame : 105 and 125
Fragment 001 / 009 :: RGBD matching between frame : 105 and 130
Fragment 001 / 009 :: RGBD matching between frame : 105 and 135
Fragment 001 / 009 :: RGBD matching between frame : 105 and 140
Fragment 001 / 009 :: RGBD matching between frame : 105 and 145
Fragment 001 / 009 :: RGBD matching between frame : 105 and 150
Fragment 001 / 009 :: RGBD matching between frame : 105 and 155
Fragment 001 / 009 :: RGBD matching between frame : 105 and 160
Fragment 001 / 009 :: RGBD matching between frame : 105 and 165
Fragment 001 / 009 :: RGBD matching between frame : 105 and 170
Fragment 001 / 009 :: RGBD matching between frame : 105 and 175
Fragment 001 / 009 :: RGBD matching between frame : 105 and 180
Fragment 001 / 009 :: RGBD matching between frame : 105 and 185
Fragment 001 / 009 :: RGBD matching between frame : 105 and 190
Fragment 001 / 009 :: RGBD matching between frame : 105 and 195
Fragment 001 / 009 :: RGBD matching between frame : 106 and 107
Fragment 001 / 009 :: RGBD matching between frame : 107 and 108
Fragment 001 / 009 :: RGBD matching between frame : 108 and 109
Fragment 001 / 009 :: RGBD matching between frame : 109 and 110
Fragment 001 / 009 :: RGBD matching between frame : 110 and 111
Fragment 001 / 009 :: RGBD matching between frame : 110 and 115
Fragment 001 / 009 :: RGBD matching between frame : 110 and 120
Fragment 001 / 009 :: RGBD matching between frame : 110 and 125
Fragment 001 / 009 :: RGBD matching between frame : 110 and 130
Fragment 001 / 009 :: RGBD matching between frame : 110 and 135
Fragment 001 / 009 :: RGBD matching between frame : 110 and 140
Fragment 001 / 009 :: RGBD matching between frame : 110 and 145
Fragment 001 / 009 :: RGBD matching between frame : 110 and 150
Fragment 001 / 009 :: RGBD matching between frame : 110 and 155
Fragment 001 / 009 :: RGBD matching between frame : 110 and 160
Fragment 001 / 009 :: RGBD matching between frame : 110 and 165
Fragment 001 / 009 :: RGBD matching between frame : 110 and 170
Fragment 001 / 009 :: RGBD matching between frame : 110 and 175
Fragment 001 / 009 :: RGBD matching between frame : 110 and 180
Fragment 001 / 009 :: RGBD matching between frame : 110 and 185
Fragment 001 / 009 :: RGBD matching between frame : 110 and 190
Fragment 001 / 009 :: RGBD matching between frame : 110 and 195
Fragment 001 / 009 :: RGBD matching between frame : 111 and 112
Fragment 001 / 009 :: RGBD matching between frame : 112 and 113
Fragment 001 / 009 :: RGBD matching between frame : 113 and 114
Fragment 001 / 009 :: RGBD matching between frame : 114 and 115
Fragment 001 / 009 :: RGBD matching between frame : 115 and 116
Fragment 001 / 009 :: RGBD matching between frame : 115 and 120
Fragment 001 / 009 :: RGBD matching between frame : 115 and 125
Fragment 001 / 009 :: RGBD matching between frame : 115 and 130
Fragment 001 / 009 :: RGBD matching between frame : 115 and 135
Fragment 001 / 009 :: RGBD matching between frame : 115 and 140
Fragment 001 / 009 :: RGBD matching between frame : 115 and 145
Fragment 001 / 009 :: RGBD matching between frame : 115 and 150
Fragment 001 / 009 :: RGBD matching between frame : 115 and 155
Fragment 001 / 009 :: RGBD matching between frame : 115 and 160
Fragment 001 / 009 :: RGBD matching between frame : 115 and 165
Fragment 001 / 009 :: RGBD matching between frame : 115 and 170
Fragment 001 / 009 :: RGBD matching between frame : 115 and 175
Fragment 001 / 009 :: RGBD matching between frame : 115 and 180
Fragment 001 / 009 :: RGBD matching between frame : 115 and 185
Fragment 001 / 009 :: RGBD matching between frame : 115 and 190
Fragment 001 / 009 :: RGBD matching between frame : 115 and 195
Fragment 001 / 009 :: RGBD matching between frame : 116 and 117
Fragment 001 / 009 :: RGBD matching between frame : 117 and 118
Fragment 001 / 009 :: RGBD matching between frame : 118 and 119
Fragment 001 / 009 :: RGBD matching between frame : 119 and 120
Fragment 001 / 009 :: RGBD matching between frame : 120 and 121
Fragment 001 / 009 :: RGBD matching between frame : 120 and 125
Fragment 001 / 009 :: RGBD matching between frame : 120 and 130
Fragment 001 / 009 :: RGBD matching between frame : 120 and 135
Fragment 001 / 009 :: RGBD matching between frame : 120 and 140
Fragment 001 / 009 :: RGBD matching between frame : 120 and 145
Fragment 001 / 009 :: RGBD matching between frame : 120 and 150
Fragment 001 / 009 :: RGBD matching between frame : 120 and 155
Fragment 001 / 009 :: RGBD matching between frame : 120 and 160
Fragment 001 / 009 :: RGBD matching between frame : 120 and 165
Fragment 001 / 009 :: RGBD matching between frame : 120 and 170
Fragment 001 / 009 :: RGBD matching between frame : 120 and 175
Fragment 001 / 009 :: RGBD matching between frame : 120 and 180
Fragment 001 / 009 :: RGBD matching between frame : 120 and 185
Fragment 001 / 009 :: RGBD matching between frame : 120 and 190
Fragment 001 / 009 :: RGBD matching between frame : 120 and 195
Fragment 001 / 009 :: RGBD matching between frame : 121 and 122
Fragment 001 / 009 :: RGBD matching between frame : 122 and 123
Fragment 001 / 009 :: RGBD matching between frame : 123 and 124
Fragment 001 / 009 :: RGBD matching between frame : 124 and 125
Fragment 001 / 009 :: RGBD matching between frame : 125 and 126
Fragment 001 / 009 :: RGBD matching between frame : 125 and 130
Fragment 001 / 009 :: RGBD matching between frame : 125 and 135
Fragment 001 / 009 :: RGBD matching between frame : 125 and 140
Fragment 001 / 009 :: RGBD matching between frame : 125 and 145
Fragment 001 / 009 :: RGBD matching between frame : 125 and 150
Fragment 001 / 009 :: RGBD matching between frame : 125 and 155
Fragment 001 / 009 :: RGBD matching between frame : 125 and 160
Fragment 001 / 009 :: RGBD matching between frame : 125 and 165
Fragment 001 / 009 :: RGBD matching between frame : 125 and 170
Fragment 001 / 009 :: RGBD matching between frame : 125 and 175
Fragment 001 / 009 :: RGBD matching between frame : 125 and 180
Fragment 001 / 009 :: RGBD matching between frame : 125 and 185
Fragment 001 / 009 :: RGBD matching between frame : 125 and 190
Fragment 001 / 009 :: RGBD matching between frame : 125 and 195
Fragment 001 / 009 :: RGBD matching between frame : 126 and 127
Fragment 001 / 009 :: RGBD matching between frame : 127 and 128
Fragment 001 / 009 :: RGBD matching between frame : 128 and 129
Fragment 001 / 009 :: RGBD matching between frame : 129 and 130
Fragment 001 / 009 :: RGBD matching between frame : 130 and 131
Fragment 001 / 009 :: RGBD matching between frame : 130 and 135
Fragment 001 / 009 :: RGBD matching between frame : 130 and 140
Fragment 001 / 009 :: RGBD matching between frame : 130 and 145
Fragment 001 / 009 :: RGBD matching between frame : 130 and 150
Fragment 001 / 009 :: RGBD matching between frame : 130 and 155
Fragment 001 / 009 :: RGBD matching between frame : 130 and 160
Fragment 001 / 009 :: RGBD matching between frame : 130 and 165
Fragment 001 / 009 :: RGBD matching between frame : 130 and 170
Fragment 001 / 009 :: RGBD matching between frame : 130 and 175
Fragment 001 / 009 :: RGBD matching between frame : 130 and 180
Fragment 001 / 009 :: RGBD matching between frame : 130 and 185
Fragment 001 / 009 :: RGBD matching between frame : 130 and 190
Fragment 001 / 009 :: RGBD matching between frame : 130 and 195
Fragment 001 / 009 :: RGBD matching between frame : 131 and 132
Fragment 001 / 009 :: RGBD matching between frame : 132 and 133
Fragment 001 / 009 :: RGBD matching between frame : 133 and 134
Fragment 001 / 009 :: RGBD matching between frame : 134 and 135
Fragment 001 / 009 :: RGBD matching between frame : 135 and 136
Fragment 001 / 009 :: RGBD matching between frame : 135 and 140
Fragment 001 / 009 :: RGBD matching between frame : 135 and 145
Fragment 001 / 009 :: RGBD matching between frame : 135 and 150
Fragment 001 / 009 :: RGBD matching between frame : 135 and 155
Fragment 001 / 009 :: RGBD matching between frame : 135 and 160
Fragment 001 / 009 :: RGBD matching between frame : 135 and 165
Fragment 001 / 009 :: RGBD matching between frame : 135 and 170
Fragment 001 / 009 :: RGBD matching between frame : 135 and 175
Fragment 001 / 009 :: RGBD matching between frame : 135 and 180
Fragment 001 / 009 :: RGBD matching between frame : 135 and 185
Fragment 001 / 009 :: RGBD matching between frame : 135 and 190
Fragment 001 / 009 :: RGBD matching between frame : 135 and 195
Fragment 001 / 009 :: RGBD matching between frame : 136 and 137
Fragment 001 / 009 :: RGBD matching between frame : 137 and 138
Fragment 001 / 009 :: RGBD matching between frame : 138 and 139
Fragment 001 / 009 :: RGBD matching between frame : 139 and 140
Fragment 001 / 009 :: RGBD matching between frame : 140 and 141
Fragment 001 / 009 :: RGBD matching between frame : 140 and 145
Fragment 001 / 009 :: RGBD matching between frame : 140 and 150
Fragment 001 / 009 :: RGBD matching between frame : 140 and 155
Fragment 001 / 009 :: RGBD matching between frame : 140 and 160
Fragment 001 / 009 :: RGBD matching between frame : 140 and 165
Fragment 001 / 009 :: RGBD matching between frame : 140 and 170
Fragment 001 / 009 :: RGBD matching between frame : 140 and 175
Fragment 001 / 009 :: RGBD matching between frame : 140 and 180
Fragment 001 / 009 :: RGBD matching between frame : 140 and 185
Fragment 001 / 009 :: RGBD matching between frame : 140 and 190
Fragment 001 / 009 :: RGBD matching between frame : 140 and 195
Fragment 001 / 009 :: RGBD matching between frame : 141 and 142
Fragment 001 / 009 :: RGBD matching between frame : 142 and 143
Fragment 001 / 009 :: RGBD matching between frame : 143 and 144
Fragment 001 / 009 :: RGBD matching between frame : 144 and 145
Fragment 001 / 009 :: RGBD matching between frame : 145 and 146
Fragment 001 / 009 :: RGBD matching between frame : 145 and 150
Fragment 001 / 009 :: RGBD matching between frame : 145 and 155
Fragment 001 / 009 :: RGBD matching between frame : 145 and 160
Fragment 001 / 009 :: RGBD matching between frame : 145 and 165
Fragment 001 / 009 :: RGBD matching between frame : 145 and 170
Fragment 001 / 009 :: RGBD matching between frame : 145 and 175
Fragment 001 / 009 :: RGBD matching between frame : 145 and 180
Fragment 001 / 009 :: RGBD matching between frame : 145 and 185
Fragment 001 / 009 :: RGBD matching between frame : 145 and 190
Fragment 001 / 009 :: RGBD matching between frame : 145 and 195
Fragment 001 / 009 :: RGBD matching between frame : 146 and 147
Fragment 001 / 009 :: RGBD matching between frame : 147 and 148
Fragment 001 / 009 :: RGBD matching between frame : 148 and 149
Fragment 001 / 009 :: RGBD matching between frame : 149 and 150
Fragment 001 / 009 :: RGBD matching between frame : 150 and 151
Fragment 001 / 009 :: RGBD matching between frame : 150 and 155
Fragment 001 / 009 :: RGBD matching between frame : 150 and 160
Fragment 001 / 009 :: RGBD matching between frame : 150 and 165
Fragment 001 / 009 :: RGBD matching between frame : 150 and 170
Fragment 001 / 009 :: RGBD matching between frame : 150 and 175
Fragment 001 / 009 :: RGBD matching between frame : 150 and 180
Fragment 001 / 009 :: RGBD matching between frame : 150 and 185
Fragment 001 / 009 :: RGBD matching between frame : 150 and 190
Fragment 001 / 009 :: RGBD matching between frame : 150 and 195
Fragment 001 / 009 :: RGBD matching between frame : 151 and 152
Fragment 001 / 009 :: RGBD matching between frame : 152 and 153
Fragment 001 / 009 :: RGBD matching between frame : 153 and 154
Fragment 001 / 009 :: RGBD matching between frame : 154 and 155
Fragment 001 / 009 :: RGBD matching between frame : 155 and 156
Fragment 001 / 009 :: RGBD matching between frame : 155 and 160
Fragment 001 / 009 :: RGBD matching between frame : 155 and 165
Fragment 001 / 009 :: RGBD matching between frame : 155 and 170
Fragment 001 / 009 :: RGBD matching between frame : 155 and 175
Fragment 001 / 009 :: RGBD matching between frame : 155 and 180
Fragment 001 / 009 :: RGBD matching between frame : 155 and 185
Fragment 001 / 009 :: RGBD matching between frame : 155 and 190
Fragment 001 / 009 :: RGBD matching between frame : 155 and 195
Fragment 001 / 009 :: RGBD matching between frame : 156 and 157
Fragment 001 / 009 :: RGBD matching between frame : 157 and 158
Fragment 001 / 009 :: RGBD matching between frame : 158 and 159
Fragment 001 / 009 :: RGBD matching between frame : 159 and 160
Fragment 001 / 009 :: RGBD matching between frame : 160 and 161
Fragment 001 / 009 :: RGBD matching between frame : 160 and 165
Fragment 001 / 009 :: RGBD matching between frame : 160 and 170
Fragment 001 / 009 :: RGBD matching between frame : 160 and 175
Fragment 001 / 009 :: RGBD matching between frame : 160 and 180
Fragment 001 / 009 :: RGBD matching between frame : 160 and 185
Fragment 001 / 009 :: RGBD matching between frame : 160 and 190
Fragment 001 / 009 :: RGBD matching between frame : 160 and 195
Fragment 001 / 009 :: RGBD matching between frame : 161 and 162
Fragment 001 / 009 :: RGBD matching between frame : 162 and 163
Fragment 001 / 009 :: RGBD matching between frame : 163 and 164
Fragment 001 / 009 :: RGBD matching between frame : 164 and 165
Fragment 001 / 009 :: RGBD matching between frame : 165 and 166
Fragment 001 / 009 :: RGBD matching between frame : 165 and 170
Fragment 001 / 009 :: RGBD matching between frame : 165 and 175
Fragment 001 / 009 :: RGBD matching between frame : 165 and 180
Fragment 001 / 009 :: RGBD matching between frame : 165 and 185
Fragment 001 / 009 :: RGBD matching between frame : 165 and 190
Fragment 001 / 009 :: RGBD matching between frame : 165 and 195
Fragment 001 / 009 :: RGBD matching between frame : 166 and 167
Fragment 001 / 009 :: RGBD matching between frame : 167 and 168
Fragment 001 / 009 :: RGBD matching between frame : 168 and 169
Fragment 001 / 009 :: RGBD matching between frame : 169 and 170
Fragment 001 / 009 :: RGBD matching between frame : 170 and 171
Fragment 001 / 009 :: RGBD matching between frame : 170 and 175
Fragment 001 / 009 :: RGBD matching between frame : 170 and 180
Fragment 001 / 009 :: RGBD matching between frame : 170 and 185
Fragment 001 / 009 :: RGBD matching between frame : 170 and 190
Fragment 001 / 009 :: RGBD matching between frame : 170 and 195
Fragment 001 / 009 :: RGBD matching between frame : 171 and 172
Fragment 001 / 009 :: RGBD matching between frame : 172 and 173
Fragment 001 / 009 :: RGBD matching between frame : 173 and 174
Fragment 001 / 009 :: RGBD matching between frame : 174 and 175
Fragment 001 / 009 :: RGBD matching between frame : 175 and 176
Fragment 001 / 009 :: RGBD matching between frame : 175 and 180
Fragment 001 / 009 :: RGBD matching between frame : 175 and 185
Fragment 001 / 009 :: RGBD matching between frame : 175 and 190
Fragment 001 / 009 :: RGBD matching between frame : 175 and 195
Fragment 001 / 009 :: RGBD matching between frame : 176 and 177
Fragment 001 / 009 :: RGBD matching between frame : 177 and 178
Fragment 001 / 009 :: RGBD matching between frame : 178 and 179
Fragment 001 / 009 :: RGBD matching between frame : 179 and 180
Fragment 001 / 009 :: RGBD matching between frame : 180 and 181
Fragment 001 / 009 :: RGBD matching between frame : 180 and 185
Fragment 001 / 009 :: RGBD matching between frame : 180 and 190
Fragment 001 / 009 :: RGBD matching between frame : 180 and 195
Fragment 001 / 009 :: RGBD matching between frame : 181 and 182
Fragment 001 / 009 :: RGBD matching between frame : 182 and 183
Fragment 001 / 009 :: RGBD matching between frame : 183 and 184
Fragment 001 / 009 :: RGBD matching between frame : 184 and 185
Fragment 001 / 009 :: RGBD matching between frame : 185 and 186
Fragment 001 / 009 :: RGBD matching between frame : 185 and 190
Fragment 001 / 009 :: RGBD matching between frame : 185 and 195
Fragment 001 / 009 :: RGBD matching between frame : 186 and 187
Fragment 001 / 009 :: RGBD matching between frame : 187 and 188
Fragment 001 / 009 :: RGBD matching between frame : 188 and 189
Fragment 001 / 009 :: RGBD matching between frame : 189 and 190
Fragment 001 / 009 :: RGBD matching between frame : 190 and 191
Fragment 001 / 009 :: RGBD matching between frame : 190 and 195
Fragment 001 / 009 :: RGBD matching between frame : 191 and 192
Fragment 001 / 009 :: RGBD matching between frame : 192 and 193
Fragment 001 / 009 :: RGBD matching between frame : 193 and 194
Fragment 001 / 009 :: RGBD matching between frame : 194 and 195
Fragment 001 / 009 :: RGBD matching between frame : 195 and 196
Fragment 001 / 009 :: RGBD matching between frame : 196 and 197
Fragment 001 / 009 :: RGBD matching between frame : 197 and 198
Fragment 001 / 009 :: RGBD matching between frame : 198 and 199
Fragment 001 / 009 :: integrate rgbd frame 100 (1 of 100).
Fragment 001 / 009 :: integrate rgbd frame 101 (2 of 100).
Fragment 001 / 009 :: integrate rgbd frame 102 (3 of 100).
Fragment 001 / 009 :: integrate rgbd frame 103 (4 of 100).
Fragment 001 / 009 :: integrate rgbd frame 104 (5 of 100).
Fragment 001 / 009 :: integrate rgbd frame 105 (6 of 100).
Fragment 001 / 009 :: integrate rgbd frame 106 (7 of 100).
Fragment 001 / 009 :: integrate rgbd frame 107 (8 of 100).
Fragment 001 / 009 :: integrate rgbd frame 108 (9 of 100).
Fragment 001 / 009 :: integrate rgbd frame 109 (10 of 100).
Fragment 001 / 009 :: integrate rgbd frame 110 (11 of 100).
Fragment 001 / 009 :: integrate rgbd frame 111 (12 of 100).
Fragment 001 / 009 :: integrate rgbd frame 112 (13 of 100).
Fragment 001 / 009 :: integrate rgbd frame 113 (14 of 100).
Fragment 001 / 009 :: integrate rgbd frame 114 (15 of 100).
Fragment 001 / 009 :: integrate rgbd frame 115 (16 of 100).
Fragment 001 / 009 :: integrate rgbd frame 116 (17 of 100).
Fragment 001 / 009 :: integrate rgbd frame 117 (18 of 100).
Fragment 001 / 009 :: integrate rgbd frame 118 (19 of 100).
Fragment 001 / 009 :: integrate rgbd frame 119 (20 of 100).
Fragment 001 / 009 :: integrate rgbd frame 120 (21 of 100).
Fragment 001 / 009 :: integrate rgbd frame 121 (22 of 100).
Fragment 001 / 009 :: integrate rgbd frame 122 (23 of 100).
Fragment 001 / 009 :: integrate rgbd frame 123 (24 of 100).
Fragment 001 / 009 :: integrate rgbd frame 124 (25 of 100).
Fragment 001 / 009 :: integrate rgbd frame 125 (26 of 100).
Fragment 001 / 009 :: integrate rgbd frame 126 (27 of 100).
Fragment 001 / 009 :: integrate rgbd frame 127 (28 of 100).
Fragment 001 / 009 :: integrate rgbd frame 128 (29 of 100).
Fragment 001 / 009 :: integrate rgbd frame 129 (30 of 100).
Fragment 001 / 009 :: integrate rgbd frame 130 (31 of 100).
Fragment 001 / 009 :: integrate rgbd frame 131 (32 of 100).
Fragment 001 / 009 :: integrate rgbd frame 132 (33 of 100).
Fragment 001 / 009 :: integrate rgbd frame 133 (34 of 100).
Fragment 001 / 009 :: integrate rgbd frame 134 (35 of 100).
Fragment 001 / 009 :: integrate rgbd frame 135 (36 of 100).
Fragment 001 / 009 :: integrate rgbd frame 136 (37 of 100).
Fragment 001 / 009 :: integrate rgbd frame 137 (38 of 100).
Fragment 001 / 009 :: integrate rgbd frame 138 (39 of 100).
Fragment 001 / 009 :: integrate rgbd frame 139 (40 of 100).
Fragment 001 / 009 :: integrate rgbd frame 140 (41 of 100).
Fragment 001 / 009 :: integrate rgbd frame 141 (42 of 100).
Fragment 001 / 009 :: integrate rgbd frame 142 (43 of 100).
Fragment 001 / 009 :: integrate rgbd frame 143 (44 of 100).
Fragment 001 / 009 :: integrate rgbd frame 144 (45 of 100).
Fragment 001 / 009 :: integrate rgbd frame 145 (46 of 100).
Fragment 001 / 009 :: integrate rgbd frame 146 (47 of 100).
Fragment 001 / 009 :: integrate rgbd frame 147 (48 of 100).
Fragment 001 / 009 :: integrate rgbd frame 148 (49 of 100).
Fragment 001 / 009 :: integrate rgbd frame 149 (50 of 100).
Fragment 001 / 009 :: integrate rgbd frame 150 (51 of 100).
Fragment 001 / 009 :: integrate rgbd frame 151 (52 of 100).
Fragment 001 / 009 :: integrate rgbd frame 152 (53 of 100).
Fragment 001 / 009 :: integrate rgbd frame 153 (54 of 100).
Fragment 001 / 009 :: integrate rgbd frame 154 (55 of 100).
Fragment 001 / 009 :: integrate rgbd frame 155 (56 of 100).
Fragment 001 / 009 :: integrate rgbd frame 156 (57 of 100).
Fragment 001 / 009 :: integrate rgbd frame 157 (58 of 100).
Fragment 001 / 009 :: integrate rgbd frame 158 (59 of 100).
Fragment 001 / 009 :: integrate rgbd frame 159 (60 of 100).
Fragment 001 / 009 :: integrate rgbd frame 160 (61 of 100).
Fragment 001 / 009 :: integrate rgbd frame 161 (62 of 100).
Fragment 001 / 009 :: integrate rgbd frame 162 (63 of 100).
Fragment 001 / 009 :: integrate rgbd frame 163 (64 of 100).
Fragment 001 / 009 :: integrate rgbd frame 164 (65 of 100).
Fragment 001 / 009 :: integrate rgbd frame 165 (66 of 100).
Fragment 001 / 009 :: integrate rgbd frame 166 (67 of 100).
Fragment 001 / 009 :: integrate rgbd frame 167 (68 of 100).
Fragment 001 / 009 :: integrate rgbd frame 168 (69 of 100).
Fragment 001 / 009 :: integrate rgbd frame 169 (70 of 100).
Fragment 001 / 009 :: integrate rgbd frame 170 (71 of 100).
Fragment 001 / 009 :: integrate rgbd frame 171 (72 of 100).
Fragment 001 / 009 :: integrate rgbd frame 172 (73 of 100).
Fragment 001 / 009 :: integrate rgbd frame 173 (74 of 100).
Fragment 001 / 009 :: integrate rgbd frame 174 (75 of 100).
Fragment 001 / 009 :: integrate rgbd frame 175 (76 of 100).
Fragment 001 / 009 :: integrate rgbd frame 176 (77 of 100).
Fragment 001 / 009 :: integrate rgbd frame 177 (78 of 100).
Fragment 001 / 009 :: integrate rgbd frame 178 (79 of 100).
Fragment 001 / 009 :: integrate rgbd frame 179 (80 of 100).
Fragment 001 / 009 :: integrate rgbd frame 180 (81 of 100).
Fragment 001 / 009 :: integrate rgbd frame 181 (82 of 100).
Fragment 001 / 009 :: integrate rgbd frame 182 (83 of 100).
Fragment 001 / 009 :: integrate rgbd frame 183 (84 of 100).
Fragment 001 / 009 :: integrate rgbd frame 184 (85 of 100).
Fragment 001 / 009 :: integrate rgbd frame 185 (86 of 100).
Fragment 001 / 009 :: integrate rgbd frame 186 (87 of 100).
Fragment 001 / 009 :: integrate rgbd frame 187 (88 of 100).
Fragment 001 / 009 :: integrate rgbd frame 188 (89 of 100).
Fragment 001 / 009 :: integrate rgbd frame 189 (90 of 100).
Fragment 001 / 009 :: integrate rgbd frame 190 (91 of 100).
Fragment 001 / 009 :: integrate rgbd frame 191 (92 of 100).
Fragment 001 / 009 :: integrate rgbd frame 192 (93 of 100).
Fragment 001 / 009 :: integrate rgbd frame 193 (94 of 100).
Fragment 001 / 009 :: integrate rgbd frame 194 (95 of 100).
Fragment 001 / 009 :: integrate rgbd frame 195 (96 of 100).
Fragment 001 / 009 :: integrate rgbd frame 196 (97 of 100).
Fragment 001 / 009 :: integrate rgbd frame 197 (98 of 100).
Fragment 001 / 009 :: integrate rgbd frame 198 (99 of 100).
Fragment 001 / 009 :: integrate rgbd frame 199 (100 of 100).
Fragment 002 / 009 :: RGBD matching between frame : 200 and 201
Fragment 002 / 009 :: RGBD matching between frame : 200 and 205
Fragment 002 / 009 :: RGBD matching between frame : 200 and 210
Fragment 002 / 009 :: RGBD matching between frame : 200 and 215
Fragment 002 / 009 :: RGBD matching between frame : 200 and 220
Fragment 002 / 009 :: RGBD matching between frame : 200 and 225
Fragment 002 / 009 :: RGBD matching between frame : 200 and 230
Fragment 002 / 009 :: RGBD matching between frame : 200 and 235
Fragment 002 / 009 :: RGBD matching between frame : 200 and 240
Fragment 002 / 009 :: RGBD matching between frame : 200 and 245
Fragment 002 / 009 :: RGBD matching between frame : 200 and 250
Fragment 002 / 009 :: RGBD matching between frame : 200 and 255
Fragment 002 / 009 :: RGBD matching between frame : 200 and 260
Fragment 002 / 009 :: RGBD matching between frame : 200 and 265
Fragment 002 / 009 :: RGBD matching between frame : 200 and 270
Fragment 002 / 009 :: RGBD matching between frame : 200 and 275
Fragment 002 / 009 :: RGBD matching between frame : 200 and 280
Fragment 002 / 009 :: RGBD matching between frame : 200 and 285
Fragment 002 / 009 :: RGBD matching between frame : 200 and 290
Fragment 002 / 009 :: RGBD matching between frame : 200 and 295
Fragment 002 / 009 :: RGBD matching between frame : 201 and 202
Fragment 002 / 009 :: RGBD matching between frame : 202 and 203
Fragment 002 / 009 :: RGBD matching between frame : 203 and 204
Fragment 002 / 009 :: RGBD matching between frame : 204 and 205
Fragment 002 / 009 :: RGBD matching between frame : 205 and 206
Fragment 002 / 009 :: RGBD matching between frame : 205 and 210
Fragment 002 / 009 :: RGBD matching between frame : 205 and 215
Fragment 002 / 009 :: RGBD matching between frame : 205 and 220
Fragment 002 / 009 :: RGBD matching between frame : 205 and 225
Fragment 002 / 009 :: RGBD matching between frame : 205 and 230
Fragment 002 / 009 :: RGBD matching between frame : 205 and 235
Fragment 002 / 009 :: RGBD matching between frame : 205 and 240
Fragment 002 / 009 :: RGBD matching between frame : 205 and 245
Fragment 002 / 009 :: RGBD matching between frame : 205 and 250
Fragment 002 / 009 :: RGBD matching between frame : 205 and 255
Fragment 002 / 009 :: RGBD matching between frame : 205 and 260
Fragment 002 / 009 :: RGBD matching between frame : 205 and 265
Fragment 002 / 009 :: RGBD matching between frame : 205 and 270
Fragment 002 / 009 :: RGBD matching between frame : 205 and 275
Fragment 002 / 009 :: RGBD matching between frame : 205 and 280
Fragment 002 / 009 :: RGBD matching between frame : 205 and 285
Fragment 002 / 009 :: RGBD matching between frame : 205 and 290
Fragment 002 / 009 :: RGBD matching between frame : 205 and 295
Fragment 002 / 009 :: RGBD matching between frame : 206 and 207
Fragment 002 / 009 :: RGBD matching between frame : 207 and 208
Fragment 002 / 009 :: RGBD matching between frame : 208 and 209
Fragment 002 / 009 :: RGBD matching between frame : 209 and 210
Fragment 002 / 009 :: RGBD matching between frame : 210 and 211
Fragment 002 / 009 :: RGBD matching between frame : 210 and 215
Fragment 002 / 009 :: RGBD matching between frame : 210 and 220
Fragment 002 / 009 :: RGBD matching between frame : 210 and 225
Fragment 002 / 009 :: RGBD matching between frame : 210 and 230
Fragment 002 / 009 :: RGBD matching between frame : 210 and 235
Fragment 002 / 009 :: RGBD matching between frame : 210 and 240
Fragment 002 / 009 :: RGBD matching between frame : 210 and 245
Fragment 002 / 009 :: RGBD matching between frame : 210 and 250
Fragment 002 / 009 :: RGBD matching between frame : 210 and 255
Fragment 002 / 009 :: RGBD matching between frame : 210 and 260
Fragment 002 / 009 :: RGBD matching between frame : 210 and 265
Fragment 002 / 009 :: RGBD matching between frame : 210 and 270
Fragment 002 / 009 :: RGBD matching between frame : 210 and 275
Fragment 002 / 009 :: RGBD matching between frame : 210 and 280
Fragment 002 / 009 :: RGBD matching between frame : 210 and 285
Fragment 002 / 009 :: RGBD matching between frame : 210 and 290
Fragment 002 / 009 :: RGBD matching between frame : 210 and 295
Fragment 002 / 009 :: RGBD matching between frame : 211 and 212
Fragment 002 / 009 :: RGBD matching between frame : 212 and 213
Fragment 002 / 009 :: RGBD matching between frame : 213 and 214
Fragment 002 / 009 :: RGBD matching between frame : 214 and 215
Fragment 002 / 009 :: RGBD matching between frame : 215 and 216
Fragment 002 / 009 :: RGBD matching between frame : 215 and 220
Fragment 002 / 009 :: RGBD matching between frame : 215 and 225
Fragment 002 / 009 :: RGBD matching between frame : 215 and 230
Fragment 002 / 009 :: RGBD matching between frame : 215 and 235
Fragment 002 / 009 :: RGBD matching between frame : 215 and 240
Fragment 002 / 009 :: RGBD matching between frame : 215 and 245
Fragment 002 / 009 :: RGBD matching between frame : 215 and 250
Fragment 002 / 009 :: RGBD matching between frame : 215 and 255
Fragment 002 / 009 :: RGBD matching between frame : 215 and 260
Fragment 002 / 009 :: RGBD matching between frame : 215 and 265
Fragment 002 / 009 :: RGBD matching between frame : 215 and 270
Fragment 002 / 009 :: RGBD matching between frame : 215 and 275
Fragment 002 / 009 :: RGBD matching between frame : 215 and 280
Fragment 002 / 009 :: RGBD matching between frame : 215 and 285
Fragment 002 / 009 :: RGBD matching between frame : 215 and 290
Fragment 002 / 009 :: RGBD matching between frame : 215 and 295
Fragment 002 / 009 :: RGBD matching between frame : 216 and 217
Fragment 002 / 009 :: RGBD matching between frame : 217 and 218
Fragment 002 / 009 :: RGBD matching between frame : 218 and 219
Fragment 002 / 009 :: RGBD matching between frame : 219 and 220
Fragment 002 / 009 :: RGBD matching between frame : 220 and 221
Fragment 002 / 009 :: RGBD matching between frame : 220 and 225
Fragment 002 / 009 :: RGBD matching between frame : 220 and 230
Fragment 002 / 009 :: RGBD matching between frame : 220 and 235
Fragment 002 / 009 :: RGBD matching between frame : 220 and 240
Fragment 002 / 009 :: RGBD matching between frame : 220 and 245
Fragment 002 / 009 :: RGBD matching between frame : 220 and 250
Fragment 002 / 009 :: RGBD matching between frame : 220 and 255
Fragment 002 / 009 :: RGBD matching between frame : 220 and 260
Fragment 002 / 009 :: RGBD matching between frame : 220 and 265
Fragment 002 / 009 :: RGBD matching between frame : 220 and 270
Fragment 002 / 009 :: RGBD matching between frame : 220 and 275
Fragment 002 / 009 :: RGBD matching between frame : 220 and 280
Fragment 002 / 009 :: RGBD matching between frame : 220 and 285
Fragment 002 / 009 :: RGBD matching between frame : 220 and 290
Fragment 002 / 009 :: RGBD matching between frame : 220 and 295
Fragment 002 / 009 :: RGBD matching between frame : 221 and 222
Fragment 002 / 009 :: RGBD matching between frame : 222 and 223
Fragment 002 / 009 :: RGBD matching between frame : 223 and 224
Fragment 002 / 009 :: RGBD matching between frame : 224 and 225
Fragment 002 / 009 :: RGBD matching between frame : 225 and 226
Fragment 002 / 009 :: RGBD matching between frame : 225 and 230
Fragment 002 / 009 :: RGBD matching between frame : 225 and 235
Fragment 002 / 009 :: RGBD matching between frame : 225 and 240
Fragment 002 / 009 :: RGBD matching between frame : 225 and 245
Fragment 002 / 009 :: RGBD matching between frame : 225 and 250
Fragment 002 / 009 :: RGBD matching between frame : 225 and 255
Fragment 002 / 009 :: RGBD matching between frame : 225 and 260
Fragment 002 / 009 :: RGBD matching between frame : 225 and 265
Fragment 002 / 009 :: RGBD matching between frame : 225 and 270
Fragment 002 / 009 :: RGBD matching between frame : 225 and 275
Fragment 002 / 009 :: RGBD matching between frame : 225 and 280
Fragment 002 / 009 :: RGBD matching between frame : 225 and 285
Fragment 002 / 009 :: RGBD matching between frame : 225 and 290
Fragment 002 / 009 :: RGBD matching between frame : 225 and 295
Fragment 002 / 009 :: RGBD matching between frame : 226 and 227
Fragment 002 / 009 :: RGBD matching between frame : 227 and 228
Fragment 002 / 009 :: RGBD matching between frame : 228 and 229
Fragment 002 / 009 :: RGBD matching between frame : 229 and 230
Fragment 002 / 009 :: RGBD matching between frame : 230 and 231
Fragment 002 / 009 :: RGBD matching between frame : 230 and 235
Fragment 002 / 009 :: RGBD matching between frame : 230 and 240
Fragment 002 / 009 :: RGBD matching between frame : 230 and 245
Fragment 002 / 009 :: RGBD matching between frame : 230 and 250
Fragment 002 / 009 :: RGBD matching between frame : 230 and 255
Fragment 002 / 009 :: RGBD matching between frame : 230 and 260
Fragment 002 / 009 :: RGBD matching between frame : 230 and 265
Fragment 002 / 009 :: RGBD matching between frame : 230 and 270
Fragment 002 / 009 :: RGBD matching between frame : 230 and 275
Fragment 002 / 009 :: RGBD matching between frame : 230 and 280
Fragment 002 / 009 :: RGBD matching between frame : 230 and 285
Fragment 002 / 009 :: RGBD matching between frame : 230 and 290
Fragment 002 / 009 :: RGBD matching between frame : 230 and 295
Fragment 002 / 009 :: RGBD matching between frame : 231 and 232
Fragment 002 / 009 :: RGBD matching between frame : 232 and 233
Fragment 002 / 009 :: RGBD matching between frame : 233 and 234
Fragment 002 / 009 :: RGBD matching between frame : 234 and 235
Fragment 002 / 009 :: RGBD matching between frame : 235 and 236
Fragment 002 / 009 :: RGBD matching between frame : 235 and 240
Fragment 002 / 009 :: RGBD matching between frame : 235 and 245
Fragment 002 / 009 :: RGBD matching between frame : 235 and 250
Fragment 002 / 009 :: RGBD matching between frame : 235 and 255
Fragment 002 / 009 :: RGBD matching between frame : 235 and 260
Fragment 002 / 009 :: RGBD matching between frame : 235 and 265
Fragment 002 / 009 :: RGBD matching between frame : 235 and 270
Fragment 002 / 009 :: RGBD matching between frame : 235 and 275
Fragment 002 / 009 :: RGBD matching between frame : 235 and 280
Fragment 002 / 009 :: RGBD matching between frame : 235 and 285
Fragment 002 / 009 :: RGBD matching between frame : 235 and 290
Fragment 002 / 009 :: RGBD matching between frame : 235 and 295
Fragment 002 / 009 :: RGBD matching between frame : 236 and 237
Fragment 002 / 009 :: RGBD matching between frame : 237 and 238
Fragment 002 / 009 :: RGBD matching between frame : 238 and 239
Fragment 002 / 009 :: RGBD matching between frame : 239 and 240
Fragment 002 / 009 :: RGBD matching between frame : 240 and 241
Fragment 002 / 009 :: RGBD matching between frame : 240 and 245
Fragment 002 / 009 :: RGBD matching between frame : 240 and 250
Fragment 002 / 009 :: RGBD matching between frame : 240 and 255
Fragment 002 / 009 :: RGBD matching between frame : 240 and 260
Fragment 002 / 009 :: RGBD matching between frame : 240 and 265
Fragment 002 / 009 :: RGBD matching between frame : 240 and 270
Fragment 002 / 009 :: RGBD matching between frame : 240 and 275
Fragment 002 / 009 :: RGBD matching between frame : 240 and 280
Fragment 002 / 009 :: RGBD matching between frame : 240 and 285
Fragment 002 / 009 :: RGBD matching between frame : 240 and 290
Fragment 002 / 009 :: RGBD matching between frame : 240 and 295
Fragment 002 / 009 :: RGBD matching between frame : 241 and 242
Fragment 002 / 009 :: RGBD matching between frame : 242 and 243
Fragment 002 / 009 :: RGBD matching between frame : 243 and 244
Fragment 002 / 009 :: RGBD matching between frame : 244 and 245
Fragment 002 / 009 :: RGBD matching between frame : 245 and 246
Fragment 002 / 009 :: RGBD matching between frame : 245 and 250
Fragment 002 / 009 :: RGBD matching between frame : 245 and 255
Fragment 002 / 009 :: RGBD matching between frame : 245 and 260
Fragment 002 / 009 :: RGBD matching between frame : 245 and 265
Fragment 002 / 009 :: RGBD matching between frame : 245 and 270
Fragment 002 / 009 :: RGBD matching between frame : 245 and 275
Fragment 002 / 009 :: RGBD matching between frame : 245 and 280
Fragment 002 / 009 :: RGBD matching between frame : 245 and 285
Fragment 002 / 009 :: RGBD matching between frame : 245 and 290
Fragment 002 / 009 :: RGBD matching between frame : 245 and 295
Fragment 002 / 009 :: RGBD matching between frame : 246 and 247
Fragment 002 / 009 :: RGBD matching between frame : 247 and 248
Fragment 002 / 009 :: RGBD matching between frame : 248 and 249
Fragment 002 / 009 :: RGBD matching between frame : 249 and 250
Fragment 002 / 009 :: RGBD matching between frame : 250 and 251
Fragment 002 / 009 :: RGBD matching between frame : 250 and 255
Fragment 002 / 009 :: RGBD matching between frame : 250 and 260
Fragment 002 / 009 :: RGBD matching between frame : 250 and 265
Fragment 002 / 009 :: RGBD matching between frame : 250 and 270
Fragment 002 / 009 :: RGBD matching between frame : 250 and 275
Fragment 002 / 009 :: RGBD matching between frame : 250 and 280
Fragment 002 / 009 :: RGBD matching between frame : 250 and 285
Fragment 002 / 009 :: RGBD matching between frame : 250 and 290
Fragment 002 / 009 :: RGBD matching between frame : 250 and 295
Fragment 002 / 009 :: RGBD matching between frame : 251 and 252
Fragment 002 / 009 :: RGBD matching between frame : 252 and 253
Fragment 002 / 009 :: RGBD matching between frame : 253 and 254
Fragment 002 / 009 :: RGBD matching between frame : 254 and 255
Fragment 002 / 009 :: RGBD matching between frame : 255 and 256
Fragment 002 / 009 :: RGBD matching between frame : 255 and 260
Fragment 002 / 009 :: RGBD matching between frame : 255 and 265
Fragment 002 / 009 :: RGBD matching between frame : 255 and 270
Fragment 002 / 009 :: RGBD matching between frame : 255 and 275
Fragment 002 / 009 :: RGBD matching between frame : 255 and 280
Fragment 002 / 009 :: RGBD matching between frame : 255 and 285
Fragment 002 / 009 :: RGBD matching between frame : 255 and 290
Fragment 002 / 009 :: RGBD matching between frame : 255 and 295
Fragment 002 / 009 :: RGBD matching between frame : 256 and 257
Fragment 002 / 009 :: RGBD matching between frame : 257 and 258
Fragment 002 / 009 :: RGBD matching between frame : 258 and 259
Fragment 002 / 009 :: RGBD matching between frame : 259 and 260
Fragment 002 / 009 :: RGBD matching between frame : 260 and 261
Fragment 002 / 009 :: RGBD matching between frame : 260 and 265
Fragment 002 / 009 :: RGBD matching between frame : 260 and 270
Fragment 002 / 009 :: RGBD matching between frame : 260 and 275
Fragment 002 / 009 :: RGBD matching between frame : 260 and 280
Fragment 002 / 009 :: RGBD matching between frame : 260 and 285
Fragment 002 / 009 :: RGBD matching between frame : 260 and 290
Fragment 002 / 009 :: RGBD matching between frame : 260 and 295
Fragment 002 / 009 :: RGBD matching between frame : 261 and 262
Fragment 002 / 009 :: RGBD matching between frame : 262 and 263
Fragment 002 / 009 :: RGBD matching between frame : 263 and 264
Fragment 002 / 009 :: RGBD matching between frame : 264 and 265
Fragment 002 / 009 :: RGBD matching between frame : 265 and 266
Fragment 002 / 009 :: RGBD matching between frame : 265 and 270
Fragment 002 / 009 :: RGBD matching between frame : 265 and 275
Fragment 002 / 009 :: RGBD matching between frame : 265 and 280
Fragment 002 / 009 :: RGBD matching between frame : 265 and 285
Fragment 002 / 009 :: RGBD matching between frame : 265 and 290
Fragment 002 / 009 :: RGBD matching between frame : 265 and 295
Fragment 002 / 009 :: RGBD matching between frame : 266 and 267
Fragment 002 / 009 :: RGBD matching between frame : 267 and 268
Fragment 002 / 009 :: RGBD matching between frame : 268 and 269
Fragment 002 / 009 :: RGBD matching between frame : 269 and 270
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 275 edges.
[Open3D DEBUG] Line process weight : 33.486652
[Open3D DEBUG] [Initial     ] residual : 1.916262e+04, lambda : 1.294122e+01
[Open3D DEBUG] [Iteration 00] residual : 1.168100e+03, valid edges : 144, time : 0.002 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.152531e+03, valid edges : 144, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.152432e+03, valid edges : 144, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 1.152430e+03, valid edges : 144, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.008 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 243 edges.
[Open3D DEBUG] Line process weight : 36.401919
[Open3D DEBUG] [Initial     ] residual : 1.875269e+02, lambda : 1.415560e+01
[Open3D DEBUG] [Iteration 00] residual : 1.868457e+02, valid edges : 144, time : 0.002 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.868390e+02, valid edges : 144, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.005 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 289 edges.
[Open3D DEBUG] Line process weight : 61.238459
[Open3D DEBUG] [Initial     ] residual : 6.342089e+03, lambda : 2.203213e+01
[Open3D DEBUG] [Iteration 00] residual : 1.084951e+03, valid edges : 176, time : 0.002 sec.
[Open3D DEBUG] [Iteration 01] residual : 6.715339e+02, valid edges : 177, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 6.713689e+02, valid edges : 177, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 6.713638e+02, valid edges : 177, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.007 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 276 edges.
[Open3D DEBUG] Line process weight : 62.303346
[Open3D DEBUG] [Initial     ] residual : 9.956664e+01, lambda : 2.619504e+01
[Open3D DEBUG] [Iteration 00] residual : 9.320617e+01, valid edges : 177, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 9.292835e+01, valid edges : 177, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 9.292579e+01, valid edges : 177, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.005 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 189 edges.
[Open3D DEBUG] Line process weight : 71.560733
[Open3D DEBUG] [Initial     ] residual : 2.865412e+04, lambda : 1.776507e+01
[Open3D DEBUG] [Iteration 00] residual : 1.104708e+03, valid edges : 74, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.064056e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.060195e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 1.059070e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 04] residual : 1.058715e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 05] residual : 1.058600e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 06] residual : 1.058562e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 07] residual : 1.058550e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 08] residual : 1.058545e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 09] residual : 1.058544e+03, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * currentFragment 002 / 009 :: RGBD matching between frame : 270 and 271
Fragment 002 / 009 :: RGBD matching between frame : 270 and 275
Fragment 002 / 009 :: RGBD matching between frame : 270 and 280
Fragment 002 / 009 :: RGBD matching between frame : 270 and 285
Fragment 002 / 009 :: RGBD matching between frame : 270 and 290
Fragment 002 / 009 :: RGBD matching between frame : 270 and 295
Fragment 002 / 009 :: RGBD matching between frame : 271 and 272
Fragment 002 / 009 :: RGBD matching between frame : 272 and 273
Fragment 002 / 009 :: RGBD matching between frame : 273 and 274
Fragment 002 / 009 :: RGBD matching between frame : 274 and 275
Fragment 002 / 009 :: RGBD matching between frame : 275 and 276
Fragment 002 / 009 :: RGBD matching between frame : 275 and 280
Fragment 002 / 009 :: RGBD matching between frame : 275 and 285
Fragment 002 / 009 :: RGBD matching between frame : 275 and 290
Fragment 002 / 009 :: RGBD matching between frame : 275 and 295
Fragment 002 / 009 :: RGBD matching between frame : 276 and 277
Fragment 002 / 009 :: RGBD matching between frame : 277 and 278
Fragment 002 / 009 :: RGBD matching between frame : 278 and 279
Fragment 002 / 009 :: RGBD matching between frame : 279 and 280
Fragment 002 / 009 :: RGBD matching between frame : 280 and 281
Fragment 002 / 009 :: RGBD matching between frame : 280 and 285
Fragment 002 / 009 :: RGBD matching between frame : 280 and 290
Fragment 002 / 009 :: RGBD matching between frame : 280 and 295
Fragment 002 / 009 :: RGBD matching between frame : 281 and 282
Fragment 002 / 009 :: RGBD matching between frame : 282 and 283
Fragment 002 / 009 :: RGBD matching between frame : 283 and 284
Fragment 002 / 009 :: RGBD matching between frame : 284 and 285
Fragment 002 / 009 :: RGBD matching between frame : 285 and 286
Fragment 002 / 009 :: RGBD matching between frame : 285 and 290
Fragment 002 / 009 :: RGBD matching between frame : 285 and 295
Fragment 002 / 009 :: RGBD matching between frame : 286 and 287
Fragment 002 / 009 :: RGBD matching between frame : 287 and 288
Fragment 002 / 009 :: RGBD matching between frame : 288 and 289
Fragment 002 / 009 :: RGBD matching between frame : 289 and 290
Fragment 002 / 009 :: RGBD matching between frame : 290 and 291
Fragment 002 / 009 :: RGBD matching between frame : 290 and 295
Fragment 002 / 009 :: RGBD matching between frame : 291 and 292
Fragment 002 / 009 :: RGBD matching between frame : 292 and 293
Fragment 002 / 009 :: RGBD matching between frame : 293 and 294
Fragment 002 / 009 :: RGBD matching between frame : 294 and 295
Fragment 002 / 009 :: RGBD matching between frame : 295 and 296
Fragment 002 / 009 :: RGBD matching between frame : 296 and 297
Fragment 002 / 009 :: RGBD matching between frame : 297 and 298
Fragment 002 / 009 :: RGBD matching between frame : 298 and 299
Fragment 002 / 009 :: integrate rgbd frame 200 (1 of 100).
Fragment 002 / 009 :: integrate rgbd frame 201 (2 of 100).
Fragment 002 / 009 :: integrate rgbd frame 202 (3 of 100).
Fragment 002 / 009 :: integrate rgbd frame 203 (4 of 100).
Fragment 002 / 009 :: integrate rgbd frame 204 (5 of 100).
Fragment 002 / 009 :: integrate rgbd frame 205 (6 of 100).
Fragment 002 / 009 :: integrate rgbd frame 206 (7 of 100).
Fragment 002 / 009 :: integrate rgbd frame 207 (8 of 100).
Fragment 002 / 009 :: integrate rgbd frame 208 (9 of 100).
Fragment 002 / 009 :: integrate rgbd frame 209 (10 of 100).
Fragment 002 / 009 :: integrate rgbd frame 210 (11 of 100).
Fragment 002 / 009 :: integrate rgbd frame 211 (12 of 100).
Fragment 002 / 009 :: integrate rgbd frame 212 (13 of 100).
Fragment 002 / 009 :: integrate rgbd frame 213 (14 of 100).
Fragment 002 / 009 :: integrate rgbd frame 214 (15 of 100).
Fragment 002 / 009 :: integrate rgbd frame 215 (16 of 100).
Fragment 002 / 009 :: integrate rgbd frame 216 (17 of 100).
Fragment 002 / 009 :: integrate rgbd frame 217 (18 of 100).
Fragment 002 / 009 :: integrate rgbd frame 218 (19 of 100).
Fragment 002 / 009 :: integrate rgbd frame 219 (20 of 100).
Fragment 002 / 009 :: integrate rgbd frame 220 (21 of 100).
Fragment 002 / 009 :: integrate rgbd frame 221 (22 of 100).
Fragment 002 / 009 :: integrate rgbd frame 222 (23 of 100).
Fragment 002 / 009 :: integrate rgbd frame 223 (24 of 100).
Fragment 002 / 009 :: integrate rgbd frame 224 (25 of 100).
Fragment 002 / 009 :: integrate rgbd frame 225 (26 of 100).
Fragment 002 / 009 :: integrate rgbd frame 226 (27 of 100).
Fragment 002 / 009 :: integrate rgbd frame 227 (28 of 100).
Fragment 002 / 009 :: integrate rgbd frame 228 (29 of 100).
Fragment 002 / 009 :: integrate rgbd frame 229 (30 of 100).
Fragment 002 / 009 :: integrate rgbd frame 230 (31 of 100).
Fragment 002 / 009 :: integrate rgbd frame 231 (32 of 100).
Fragment 002 / 009 :: integrate rgbd frame 232 (33 of 100).
Fragment 002 / 009 :: integrate rgbd frame 233 (34 of 100).
Fragment 002 / 009 :: integrate rgbd frame 234 (35 of 100).
Fragment 002 / 009 :: integrate rgbd frame 235 (36 of 100).
Fragment 002 / 009 :: integrate rgbd frame 236 (37 of 100).
Fragment 002 / 009 :: integrate rgbd frame 237 (38 of 100).
Fragment 002 / 009 :: integrate rgbd frame 238 (39 of 100).
Fragment 002 / 009 :: integrate rgbd frame 239 (40 of 100).
Fragment 002 / 009 :: integrate rgbd frame 240 (41 of 100).
Fragment 002 / 009 :: integrate rgbd frame 241 (42 of 100).
Fragment 002 / 009 :: integrate rgbd frame 242 (43 of 100).
Fragment 002 / 009 :: integrate rgbd frame 243 (44 of 100).
Fragment 002 / 009 :: integrate rgbd frame 244 (45 of 100).
Fragment 002 / 009 :: integrate rgbd frame 245 (46 of 100).
Fragment 002 / 009 :: integrate rgbd frame 246 (47 of 100).
Fragment 002 / 009 :: integrate rgbd frame 247 (48 of 100).
Fragment 002 / 009 :: integrate rgbd frame 248 (49 of 100).
Fragment 002 / 009 :: integrate rgbd frame 249 (50 of 100).
Fragment 002 / 009 :: integrate rgbd frame 250 (51 of 100).
Fragment 002 / 009 :: integrate rgbd frame 251 (52 of 100).
Fragment 002 / 009 :: integrate rgbd frame 252 (53 of 100).
Fragment 002 / 009 :: integrate rgbd frame 253 (54 of 100).
Fragment 002 / 009 :: integrate rgbd frame 254 (55 of 100).
Fragment 002 / 009 :: integrate rgbd frame 255 (56 of 100).
Fragment 002 / 009 :: integrate rgbd frame 256 (57 of 100).
Fragment 002 / 009 :: integrate rgbd frame 257 (58 of 100).
Fragment 002 / 009 :: integrate rgbd frame 258 (59 of 100).
Fragment 002 / 009 :: integrate rgbd frame 259 (60 of 100).
Fragment 002 / 009 :: integrate rgbd frame 260 (61 of 100).
Fragment 002 / 009 :: integrate rgbd frame 261 (62 of 100).
Fragment 002 / 009 :: integrate rgbd frame 262 (63 of 100).
Fragment 002 / 009 :: integrate rgbd frame 263 (64 of 100).
Fragment 002 / 009 :: integrate rgbd frame 264 (65 of 100).
Fragment 002 / 009 :: integrate rgbd frame 265 (66 of 100).
Fragment 002 / 009 :: integrate rgbd frame 266 (67 of 100).
Fragment 002 / 009 :: integrate rgbd frame 267 (68 of 100).
Fragment 002 / 009 :: integrate rgbd frame 268 (69 of 100).
Fragment 002 / 009 :: integrate rgbd frame 269 (70 of 100).
Fragment 002 / 009 :: integrate rgbd frame 270 (71 of 100).
Fragment 002 / 009 :: integrate rgbd frame 271 (72 of 100).
Fragment 002 / 009 :: integrate rgbd frame 272 (73 of 100).
Fragment 002 / 009 :: integrate rgbd frame 273 (74 of 100).
Fragment 002 / 009 :: integrate rgbd frame 274 (75 of 100).
Fragment 002 / 009 :: integrate rgbd frame 275 (76 of 100).
Fragment 002 / 009 :: integrate rgbd frame 276 (77 of 100).
Fragment 002 / 009 :: integrate rgbd frame 277 (78 of 100).
Fragment 002 / 009 :: integrate rgbd frame 278 (79 of 100).
Fragment 002 / 009 :: integrate rgbd frame 279 (80 of 100).
Fragment 002 / 009 :: integrate rgbd frame 280 (81 of 100).
Fragment 002 / 009 :: integrate rgbd frame 281 (82 of 100).
Fragment 002 / 009 :: integrate rgbd frame 282 (83 of 100).
Fragment 002 / 009 :: integrate rgbd frame 283 (84 of 100).
Fragment 002 / 009 :: integrate rgbd frame 284 (85 of 100).
Fragment 002 / 009 :: integrate rgbd frame 285 (86 of 100).
Fragment 002 / 009 :: integrate rgbd frame 286 (87 of 100).
Fragment 002 / 009 :: integrate rgbd frame 287 (88 of 100).
Fragment 002 / 009 :: integrate rgbd frame 288 (89 of 100).
Fragment 002 / 009 :: integrate rgbd frame 289 (90 of 100).
Fragment 002 / 009 :: integrate rgbd frame 290 (91 of 100).
Fragment 002 / 009 :: integrate rgbd frame 291 (92 of 100).
Fragment 002 / 009 :: integrate rgbd frame 292 (93 of 100).
Fragment 002 / 009 :: integrate rgbd frame 293 (94 of 100).
Fragment 002 / 009 :: integrate rgbd frame 294 (95 of 100).
Fragment 002 / 009 :: integrate rgbd frame 295 (96 of 100).
Fragment 002 / 009 :: integrate rgbd frame 296 (97 of 100).
Fragment 002 / 009 :: integrate rgbd frame 297 (98 of 100).
Fragment 002 / 009 :: integrate rgbd frame 298 (99 of 100).
Fragment 002 / 009 :: integrate rgbd frame 299 (100 of 100).
Fragment 003 / 009 :: RGBD matching between frame : 300 and 301
Fragment 003 / 009 :: RGBD matching between frame : 300 and 305
Fragment 003 / 009 :: RGBD matching between frame : 300 and 310
Fragment 003 / 009 :: RGBD matching between frame : 300 and 315
Fragment 003 / 009 :: RGBD matching between frame : 300 and 320
Fragment 003 / 009 :: RGBD matching between frame : 300 and 325
Fragment 003 / 009 :: RGBD matching between frame : 300 and 330
Fragment 003 / 009 :: RGBD matching between frame : 300 and 335
Fragment 003 / 009 :: RGBD matching between frame : 300 and 340
Fragment 003 / 009 :: RGBD matching between frame : 300 and 345
Fragment 003 / 009 :: RGBD matching between frame : 300 and 350
Fragment 003 / 009 :: RGBD matching between frame : 300 and 355
Fragment 003 / 009 :: RGBD matching between frame : 300 and 360
Fragment 003 / 009 :: RGBD matching between frame : 300 and 365
Fragment 003 / 009 :: RGBD matching between frame : 300 and 370
Fragment 003 / 009 :: RGBD matching between frame : 300 and 375
Fragment 003 / 009 :: RGBD matching between frame : 300 and 380
Fragment 003 / 009 :: RGBD matching between frame : 300 and 385
Fragment 003 / 009 :: RGBD matching between frame : 300 and 390
Fragment 003 / 009 :: RGBD matching between frame : 300 and 395
Fragment 003 / 009 :: RGBD matching between frame : 301 and 302
Fragment 003 / 009 :: RGBD matching between frame : 302 and 303
Fragment 003 / 009 :: RGBD matching between frame : 303 and 304
Fragment 003 / 009 :: RGBD matching between frame : 304 and 305
Fragment 003 / 009 :: RGBD matching between frame : 305 and 306
Fragment 003 / 009 :: RGBD matching between frame : 305 and 310
Fragment 003 / 009 :: RGBD matching between frame : 305 and 315
Fragment 003 / 009 :: RGBD matching between frame : 305 and 320
Fragment 003 / 009 :: RGBD matching between frame : 305 and 325
Fragment 003 / 009 :: RGBD matching between frame : 305 and 330
Fragment 003 / 009 :: RGBD matching between frame : 305 and 335
Fragment 003 / 009 :: RGBD matching between frame : 305 and 340
Fragment 003 / 009 :: RGBD matching between frame : 305 and 345
Fragment 003 / 009 :: RGBD matching between frame : 305 and 350
Fragment 003 / 009 :: RGBD matching between frame : 305 and 355
Fragment 003 / 009 :: RGBD matching between frame : 305 and 360
Fragment 003 / 009 :: RGBD matching between frame : 305 and 365
Fragment 003 / 009 :: RGBD matching between frame : 305 and 370
Fragment 003 / 009 :: RGBD matching between frame : 305 and 375
Fragment 003 / 009 :: RGBD matching between frame : 305 and 380
Fragment 003 / 009 :: RGBD matching between frame : 305 and 385
Fragment 003 / 009 :: RGBD matching between frame : 305 and 390
Fragment 003 / 009 :: RGBD matching between frame : 305 and 395
Fragment 003 / 009 :: RGBD matching between frame : 306 and 307
Fragment 003 / 009 :: RGBD matching between frame : 307 and 308
Fragment 003 / 009 :: RGBD matching between frame : 308 and 309
Fragment 003 / 009 :: RGBD matching between frame : 309 and 310
Fragment 003 / 009 :: RGBD matching between frame : 310 and 311
Fragment 003 / 009 :: RGBD matching between frame : 310 and 315
Fragment 003 / 009 :: RGBD matching between frame : 310 and 320
Fragment 003 / 009 :: RGBD matching between frame : 310 and 325
Fragment 003 / 009 :: RGBD matching between frame : 310 and 330
Fragment 003 / 009 :: RGBD matching between frame : 310 and 335
Fragment 003 / 009 :: RGBD matching between frame : 310 and 340
Fragment 003 / 009 :: RGBD matching between frame : 310 and 345
Fragment 003 / 009 :: RGBD matching between frame : 310 and 350
Fragment 003 / 009 :: RGBD matching between frame : 310 and 355
Fragment 003 / 009 :: RGBD matching between frame : 310 and 360
Fragment 003 / 009 :: RGBD matching between frame : 310 and 365
Fragment 003 / 009 :: RGBD matching between frame : 310 and 370
Fragment 003 / 009 :: RGBD matching between frame : 310 and 375
Fragment 003 / 009 :: RGBD matching between frame : 310 and 380
Fragment 003 / 009 :: RGBD matching between frame : 310 and 385
Fragment 003 / 009 :: RGBD matching between frame : 310 and 390
Fragment 003 / 009 :: RGBD matching between frame : 310 and 395
Fragment 003 / 009 :: RGBD matching between frame : 311 and 312
Fragment 003 / 009 :: RGBD matching between frame : 312 and 313
Fragment 003 / 009 :: RGBD matching between frame : 313 and 314
Fragment 003 / 009 :: RGBD matching between frame : 314 and 315
Fragment 003 / 009 :: RGBD matching between frame : 315 and 316
Fragment 003 / 009 :: RGBD matching between frame : 315 and 320
Fragment 003 / 009 :: RGBD matching between frame : 315 and 325
Fragment 003 / 009 :: RGBD matching between frame : 315 and 330
Fragment 003 / 009 :: RGBD matching between frame : 315 and 335
Fragment 003 / 009 :: RGBD matching between frame : 315 and 340
Fragment 003 / 009 :: RGBD matching between frame : 315 and 345
Fragment 003 / 009 :: RGBD matching between frame : 315 and 350
Fragment 003 / 009 :: RGBD matching between frame : 315 and 355
Fragment 003 / 009 :: RGBD matching between frame : 315 and 360
Fragment 003 / 009 :: RGBD matching between frame : 315 and 365
Fragment 003 / 009 :: RGBD matching between frame : 315 and 370
Fragment 003 / 009 :: RGBD matching between frame : 315 and 375
Fragment 003 / 009 :: RGBD matching between frame : 315 and 380
Fragment 003 / 009 :: RGBD matching between frame : 315 and 385
Fragment 003 / 009 :: RGBD matching between frame : 315 and 390
Fragment 003 / 009 :: RGBD matching between frame : 315 and 395
Fragment 003 / 009 :: RGBD matching between frame : 316 and 317
Fragment 003 / 009 :: RGBD matching between frame : 317 and 318
Fragment 003 / 009 :: RGBD matching between frame : 318 and 319
Fragment 003 / 009 :: RGBD matching between frame : 319 and 320
Fragment 003 / 009 :: RGBD matching between frame : 320 and 321
Fragment 003 / 009 :: RGBD matching between frame : 320 and 325
Fragment 003 / 009 :: RGBD matching between frame : 320 and 330
Fragment 003 / 009 :: RGBD matching between frame : 320 and 335
Fragment 003 / 009 :: RGBD matching between frame : 320 and 340
Fragment 003 / 009 :: RGBD matching between frame : 320 and 345
Fragment 003 / 009 :: RGBD matching between frame : 320 and 350
Fragment 003 / 009 :: RGBD matching between frame : 320 and 355
Fragment 003 / 009 :: RGBD matching between frame : 320 and 360
Fragment 003 / 009 :: RGBD matching between frame : 320 and 365
Fragment 003 / 009 :: RGBD matching between frame : 320 and 370
Fragment 003 / 009 :: RGBD matching between frame : 320 and 375
Fragment 003 / 009 :: RGBD matching between frame : 320 and 380
Fragment 003 / 009 :: RGBD matching between frame : 320 and 385
Fragment 003 / 009 :: RGBD matching between frame : 320 and 390
Fragment 003 / 009 :: RGBD matching between frame : 320 and 395
Fragment 003 / 009 :: RGBD matching between frame : 321 and 322
Fragment 003 / 009 :: RGBD matching between frame : 322 and 323
Fragment 003 / 009 :: RGBD matching between frame : 323 and 324
Fragment 003 / 009 :: RGBD matching between frame : 324 and 325
Fragment 003 / 009 :: RGBD matching between frame : 325 and 326
Fragment 003 / 009 :: RGBD matching between frame : 325 and 330
Fragment 003 / 009 :: RGBD matching between frame : 325 and 335
Fragment 003 / 009 :: RGBD matching between frame : 325 and 340
Fragment 003 / 009 :: RGBD matching between frame : 325 and 345
Fragment 003 / 009 :: RGBD matching between frame : 325 and 350
Fragment 003 / 009 :: RGBD matching between frame : 325 and 355
Fragment 003 / 009 :: RGBD matching between frame : 325 and 360
Fragment 003 / 009 :: RGBD matching between frame : 325 and 365
Fragment 003 / 009 :: RGBD matching between frame : 325 and 370
Fragment 003 / 009 :: RGBD matching between frame : 325 and 375
Fragment 003 / 009 :: RGBD matching between frame : 325 and 380
Fragment 003 / 009 :: RGBD matching between frame : 325 and 385
Fragment 003 / 009 :: RGBD matching between frame : 325 and 390
Fragment 003 / 009 :: RGBD matching between frame : 325 and 395
Fragment 003 / 009 :: RGBD matching between frame : 326 and 327
Fragment 003 / 009 :: RGBD matching between frame : 327 and 328
Fragment 003 / 009 :: RGBD matching between frame : 328 and 329
Fragment 003 / 009 :: RGBD matching between frame : 329 and 330
Fragment 003 / 009 :: RGBD matching between frame : 330 and 331
Fragment 003 / 009 :: RGBD matching between frame : 330 and 335
Fragment 003 / 009 :: RGBD matching between frame : 330 and 340
Fragment 003 / 009 :: RGBD matching between frame : 330 and 345
Fragment 003 / 009 :: RGBD matching between frame : 330 and 350
Fragment 003 / 009 :: RGBD matching between frame : 330 and 355
Fragment 003 / 009 :: RGBD matching between frame : 330 and 360
Fragment 003 / 009 :: RGBD matching between frame : 330 and 365
Fragment 003 / 009 :: RGBD matching between frame : 330 and 370
Fragment 003 / 009 :: RGBD matching between frame : 330 and 375
Fragment 003 / 009 :: RGBD matching between frame : 330 and 380
Fragment 003 / 009 :: RGBD matching between frame : 330 and 385
Fragment 003 / 009 :: RGBD matching between frame : 330 and 390
Fragment 003 / 009 :: RGBD matching between frame : 330 and 395
Fragment 003 / 009 :: RGBD matching between frame : 331 and 332
Fragment 003 / 009 :: RGBD matching between frame : 332 and 333
Fragment 003 / 009 :: RGBD matching between frame : 333 and 334
Fragment 003 / 009 :: RGBD matching between frame : 334 and 335
Fragment 003 / 009 :: RGBD matching between frame : 335 and 336
Fragment 003 / 009 :: RGBD matching between frame : 335 and 340
Fragment 003 / 009 :: RGBD matching between frame : 335 and 345
Fragment 003 / 009 :: RGBD matching between frame : 335 and 350
Fragment 003 / 009 :: RGBD matching between frame : 335 and 355
Fragment 003 / 009 :: RGBD matching between frame : 335 and 360
Fragment 003 / 009 :: RGBD matching between frame : 335 and 365
Fragment 003 / 009 :: RGBD matching between frame : 335 and 370
Fragment 003 / 009 :: RGBD matching between frame : 335 and 375
Fragment 003 / 009 :: RGBD matching between frame : 335 and 380
Fragment 003 / 009 :: RGBD matching between frame : 335 and 385
Fragment 003 / 009 :: RGBD matching between frame : 335 and 390
Fragment 003 / 009 :: RGBD matching between frame : 335 and 395
Fragment 003 / 009 :: RGBD matching between frame : 336 and 337
Fragment 003 / 009 :: RGBD matching between frame : 337 and 338
Fragment 003 / 009 :: RGBD matching between frame : 338 and 339
Fragment 003 / 009 :: RGBD matching between frame : 339 and 340
Fragment 003 / 009 :: RGBD matching between frame : 340 and 341
Fragment 003 / 009 :: RGBD matching between frame : 340 and 345
Fragment 003 / 009 :: RGBD matching between frame : 340 and 350
Fragment 003 / 009 :: RGBD matching between frame : 340 and 355
Fragment 003 / 009 :: RGBD matching between frame : 340 and 360
Fragment 003 / 009 :: RGBD matching between frame : 340 and 365
Fragment 003 / 009 :: RGBD matching between frame : 340 and 370
Fragment 003 / 009 :: RGBD matching between frame : 340 and 375
Fragment 003 / 009 :: RGBD matching between frame : 340 and 380
Fragment 003 / 009 :: RGBD matching between frame : 340 and 385
Fragment 003 / 009 :: RGBD matching between frame : 340 and 390
Fragment 003 / 009 :: RGBD matching between frame : 340 and 395
Fragment 003 / 009 :: RGBD matching between frame : 341 and 342
Fragment 003 / 009 :: RGBD matching between frame : 342 and 343
Fragment 003 / 009 :: RGBD matching between frame : 343 and 344
Fragment 003 / 009 :: RGBD matching between frame : 344 and 345
Fragment 003 / 009 :: RGBD matching between frame : 345 and 346
Fragment 003 / 009 :: RGBD matching between frame : 345 and 350
Fragment 003 / 009 :: RGBD matching between frame : 345 and 355
Fragment 003 / 009 :: RGBD matching between frame : 345 and 360
Fragment 003 / 009 :: RGBD matching between frame : 345 and 365
Fragment 003 / 009 :: RGBD matching between frame : 345 and 370
Fragment 003 / 009 :: RGBD matching between frame : 345 and 375
Fragment 003 / 009 :: RGBD matching between frame : 345 and 380
Fragment 003 / 009 :: RGBD matching between frame : 345 and 385
Fragment 003 / 009 :: RGBD matching between frame : 345 and 390
Fragment 003 / 009 :: RGBD matching between frame : 345 and 395
Fragment 003 / 009 :: RGBD matching between frame : 346 and 347
Fragment 003 / 009 :: RGBD matching between frame : 347 and 348
Fragment 003 / 009 :: RGBD matching between frame : 348 and 349
Fragment 003 / 009 :: RGBD matching between frame : 349 and 350
Fragment 003 / 009 :: RGBD matching between frame : 350 and 351
Fragment 003 / 009 :: RGBD matching between frame : 350 and 355
Fragment 003 / 009 :: RGBD matching between frame : 350 and 360
Fragment 003 / 009 :: RGBD matching between frame : 350 and 365
Fragment 003 / 009 :: RGBD matching between frame : 350 and 370
Fragment 003 / 009 :: RGBD matching between frame : 350 and 375
Fragment 003 / 009 :: RGBD matching between frame : 350 and 380
Fragment 003 / 009 :: RGBD matching between frame : 350 and 385
Fragment 003 / 009 :: RGBD matching between frame : 350 and 390
Fragment 003 / 009 :: RGBD matching between frame : 350 and 395
Fragment 003 / 009 :: RGBD matching between frame : 351 and 352
Fragment 003 / 009 :: RGBD matching between frame : 352 and 353
Fragment 003 / 009 :: RGBD matching between frame : 353 and 354
Fragment 003 / 009 :: RGBD matching between frame : 354 and 355
Fragment 003 / 009 :: RGBD matching between frame : 355 and 356
Fragment 003 / 009 :: RGBD matching between frame : 355 and 360
Fragment 003 / 009 :: RGBD matching between frame : 355 and 365
Fragment 003 / 009 :: RGBD matching between frame : 355 and 370
Fragment 003 / 009 :: RGBD matching between frame : 355 and 375
Fragment 003 / 009 :: RGBD matching between frame : 355 and 380
Fragment 003 / 009 :: RGBD matching between frame : 355 and 385
Fragment 003 / 009 :: RGBD matching between frame : 355 and 390
Fragment 003 / 009 :: RGBD matching between frame : 355 and 395
Fragment 003 / 009 :: RGBD matching between frame : 356 and 357
Fragment 003 / 009 :: RGBD matching between frame : 357 and 358
Fragment 003 / 009 :: RGBD matching between frame : 358 and 359
Fragment 003 / 009 :: RGBD matching between frame : 359 and 360
Fragment 003 / 009 :: RGBD matching between frame : 360 and 361
Fragment 003 / 009 :: RGBD matching between frame : 360 and 365
Fragment 003 / 009 :: RGBD matching between frame : 360 and 370
Fragment 003 / 009 :: RGBD matching between frame : 360 and 375
Fragment 003 / 009 :: RGBD matching between frame : 360 and 380
Fragment 003 / 009 :: RGBD matching between frame : 360 and 385
Fragment 003 / 009 :: RGBD matching between frame : 360 and 390
Fragment 003 / 009 :: RGBD matching between frame : 360 and 395
Fragment 003 / 009 :: RGBD matching between frame : 361 and 362
Fragment 003 / 009 :: RGBD matching between frame : 362 and 363
Fragment 003 / 009 :: RGBD matching between frame : 363 and 364
Fragment 003 / 009 :: RGBD matching between frame : 364 and 365
Fragment 003 / 009 :: RGBD matching between frame : 365 and 366
Fragment 003 / 009 :: RGBD matching between frame : 365 and 370
Fragment 003 / 009 :: RGBD matching between frame : 365 and 375
Fragment 003 / 009 :: RGBD matching between frame : 365 and 380
Fragment 003 / 009 :: RGBD matching between frame : 365 and 385
Fragment 003 / 009 :: RGBD matching between frame : 365 and 390
Fragment 003 / 009 :: RGBD matching between frame : 365 and 395
Fragment 003 / 009 :: RGBD matching between frame : 366 and 367
Fragment 003 / 009 :: RGBD matching between frame : 367 and 368
Fragment 003 / 009 :: RGBD matching between frame : 368 and 369
Fragment 003 / 009 :: RGBD matching between frame : 369 and 370
Fragment 003 / 009 :: RGBD matching between frame : 370 and 371
Fragment 003 / 009 :: RGBD matching between frame : 370 and 375
Fragment 003 / 009 :: RGBD matching between frame : 370 and 380
Fragment 003 / 009 :: RGBD matching between frame : 370 and 385
Fragment 003 / 009 :: RGBD matching between frame : 370 and 390
Fragment 003 / 009 :: RGBD matching between frame : 370 and 395
Fragment 003 / 009 :: RGBD matching between frame : 371 and 372
Fragment 003 / 009 :: RGBD matching between frame : 372 and 373
Fragment 003 / 009 :: RGBD matching between frame : 373 and 374
Fragment 003 / 009 :: RGBD matching between frame : 374 and 375
Fragment 003 / 009 :: RGBD matching between frame : 375 and 376
Fragment 003 / 009 :: RGBD matching between frame : 375 and 380
Fragment 003 / 009 :: RGBD matching between frame : 375 and 385
Fragment 003 / 009 :: RGBD matching between frame : 375 and 390
Fragment 003 / 009 :: RGBD matching between frame : 375 and 395
Fragment 003 / 009 :: RGBD matching between frame : 376 and 377
Fragment 003 / 009 :: RGBD matching between frame : 377 and 378
Fragment 003 / 009 :: RGBD matching between frame : 378 and 379
Fragment 003 / 009 :: RGBD matching between frame : 379 and 380
Fragment 003 / 009 :: RGBD matching between frame : 380 and 381
Fragment 003 / 009 :: RGBD matching between frame : 380 and 385
Fragment 003 / 009 :: RGBD matching between frame : 380 and 390
Fragment 003 / 009 :: RGBD matching between frame : 380 and 395
Fragment 003 / 009 :: RGBD matching between frame : 381 and 382
Fragment 003 / 009 :: RGBD matching between frame : 382 and 383
Fragment 003 / 009 :: RGBD matching between frame : 383 and 384
Fragment 003 / 009 :: RGBD matching between frame : 384 and 385
Fragment 003 / 009 :: RGBD matching between frame : 385 and 386
Fragment 003 / 009 :: RGBD matching between frame : 385 and 390
Fragment 003 / 009 :: RGBD matching between frame : 385 and 395
Fragment 003 / 009 :: RGBD matching between frame : 386 and 387
Fragment 003 / 009 :: RGBD matching between frame : 387 and 388
Fragment 003 / 009 :: RGBD matching between frame : 388 and 389
Fragment 003 / 009 :: RGBD matching between frame : 389 and 390
Fragment 003 / 009 :: RGBD matching between frame : 390 and 391
Fragment 003 / 009 :: RGBD matching between frame : 390 and 395
Fragment 003 / 009 :: RGBD matching between frame : 391 and 392
Fragment 003 / 009 :: RGBD matching between frame : 392 and 393
Fragment 003 / 009 :: RGBD matching between frame : 393 and 394
Fragment 003 / 009 :: RGBD matching between frame : 394 and 395
Fragment 003 / 009 :: RGBD matching between frame : 395 and 396
Fragment 003 / 009 :: RGBD matching between frame : 396 and 397
Fragment 003 / 009 :: RGBD matching between frame : 397 and 398
Fragment 003 / 009 :: RGBD matching between frame : 398 and 399
Fragment 003 / 009 :: integrate rgbd frame 300 (1 of 100).
Fragment 003 / 009 :: integrate rgbd frame 301 (2 of 100).
Fragment 003 / 009 :: integrate rgbd frame 302 (3 of 100).
Fragment 003 / 009 :: integrate rgbd frame 303 (4 of 100).
Fragment 003 / 009 :: integrate rgbd frame 304 (5 of 100).
Fragment 003 / 009 :: integrate rgbd frame 305 (6 of 100).
Fragment 003 / 009 :: integrate rgbd frame 306 (7 of 100).
Fragment 003 / 009 :: integrate rgbd frame 307 (8 of 100).
Fragment 003 / 009 :: integrate rgbd frame 308 (9 of 100).
Fragment 003 / 009 :: integrate rgbd frame 309 (10 of 100).
Fragment 003 / 009 :: integrate rgbd frame 310 (11 of 100).
Fragment 003 / 009 :: integrate rgbd frame 311 (12 of 100).
Fragment 003 / 009 :: integrate rgbd frame 312 (13 of 100).
Fragment 003 / 009 :: integrate rgbd frame 313 (14 of 100).
Fragment 003 / 009 :: integrate rgbd frame 314 (15 of 100).
Fragment 003 / 009 :: integrate rgbd frame 315 (16 of 100).
Fragment 003 / 009 :: integrate rgbd frame 316 (17 of 100).
Fragment 003 / 009 :: integrate rgbd frame 317 (18 of 100).
Fragment 003 / 009 :: integrate rgbd frame 318 (19 of 100).
Fragment 003 / 009 :: integrate rgbd frame 319 (20 of 100).
Fragment 003 / 009 :: integrate rgbd frame 320 (21 of 100).
Fragment 003 / 009 :: integrate rgbd frame 321 (22 of 100).
Fragment 003 / 009 :: integrate rgbd frame 322 (23 of 100).
Fragment 003 / 009 :: integrate rgbd frame 323 (24 of 100).
Fragment 003 / 009 :: integrate rgbd frame 324 (25 of 100).
Fragment 003 / 009 :: integrate rgbd frame 325 (26 of 100).
Fragment 003 / 009 :: integrate rgbd frame 326 (27 of 100).
Fragment 003 / 009 :: integrate rgbd frame 327 (28 of 100).
Fragment 003 / 009 :: integrate rgbd frame 328 (29 of 100).
Fragment 003 / 009 :: integrate rgbd frame 329 (30 of 100).
Fragment 003 / 009 :: integrate rgbd frame 330 (31 of 100).
Fragment 003 / 009 :: integrate rgbd frame 331 (32 of 100).
Fragment 003 / 009 :: integrate rgbd frame 332 (33 of 100).
Fragment 003 / 009 :: integrate rgbd frame 333 (34 of 100).
Fragment 003 / 009 :: integrate rgbd frame 334 (35 of 100).
Fragment 003 / 009 :: integrate rgbd frame 335 (36 of 100).
Fragment 003 / 009 :: integrate rgbd frame 336 (37 of 100).
Fragment 003 / 009 :: integrate rgbd frame 337 (38 of 100).
Fragment 003 / 009 :: integrate rgbd frame 338 (39 of 100).
Fragment 003 / 009 :: integrate rgbd frame 339 (40 of 100).
Fragment 003 / 009 :: integrate rgbd frame 340 (41 of 100).
Fragment 003 / 009 :: integrate rgbd frame 341 (42 of 100).
Fragment 003 / 009 :: integrate rgbd frame 342 (43 of 100).
Fragment 003 / 009 :: integrate rgbd frame 343 (44 of 100).
Fragment 003 / 009 :: integrate rgbd frame 344 (45 of 100).
Fragment 003 / 009 :: integrate rgbd frame 345 (46 of 100).
Fragment 003 / 009 :: integrate rgbd frame 346 (47 of 100).
Fragment 003 / 009 :: integrate rgbd frame 347 (48 of 100).
Fragment 003 / 009 :: integrate rgbd frame 348 (49 of 100).
Fragment 003 / 009 :: integrate rgbd frame 349 (50 of 100).
Fragment 003 / 009 :: integrate rgbd frame 350 (51 of 100).
Fragment 003 / 009 :: integrate rgbd frame 351 (52 of 100).
Fragment 003 / 009 :: integrate rgbd frame 352 (53 of 100).
Fragment 003 / 009 :: integrate rgbd frame 353 (54 of 100).
Fragment 003 / 009 :: integrate rgbd frame 354 (55 of 100).
Fragment 003 / 009 :: integrate rgbd frame 355 (56 of 100).
Fragment 003 / 009 :: integrate rgbd frame 356 (57 of 100).
Fragment 003 / 009 :: integrate rgbd frame 357 (58 of 100).
Fragment 003 / 009 :: integrate rgbd frame 358 (59 of 100).
Fragment 003 / 009 :: integrate rgbd frame 359 (60 of 100).
Fragment 003 / 009 :: integrate rgbd frame 360 (61 of 100).
Fragment 003 / 009 :: integrate rgbd frame 361 (62 of 100).
Fragment 003 / 009 :: integrate rgbd frame 362 (63 of 100).
Fragment 003 / 009 :: integrate rgbd frame 363 (64 of 100).
Fragment 003 / 009 :: integrate rgbd frame 364 (65 of 100).
Fragment 003 / 009 :: integrate rgbd frame 365 (66 of 100).
Fragment 003 / 009 :: integrate rgbd frame 366 (67 of 100).
Fragment 003 / 009 :: integrate rgbd frame 367 (68 of 100).
Fragment 003 / 009 :: integrate rgbd frame 368 (69 of 100).
Fragment 003 / 009 :: integrate rgbd frame 369 (70 of 100).
Fragment 003 / 009 :: integrate rgbd frame 370 (71 of 100).
Fragment 003 / 009 :: integrate rgbd frame 371 (72 of 100).
Fragment 003 / 009 :: integrate rgbd frame 372 (73 of 100).
Fragment 003 / 009 :: integrate rgbd frame 373 (74 of 100).
Fragment 003 / 009 :: integrate rgbd frame 374 (75 of 100).
Fragment 003 / 009 :: integrate rgbd frame 375 (76 of 100).
Fragment 003 / 009 :: integrate rgbd frame 376 (77 of 100).
Fragment 003 / 009 :: integrate rgbd frame 377 (78 of 100).
Fragment 003 / 009 :: integrate rgbd frame 378 (79 of 100).
Fragment 003 / 009 :: integrate rgbd frame 379 (80 of 100).
Fragment 003 / 009 :: integrate rgbd frame 380 (81 of 100).
Fragment 003 / 009 :: integrate rgbd frame 381 (82 of 100).
Fragment 003 / 009 :: integrate rgbd frame 382 (83 of 100).
Fragment 003 / 009 :: integrate rgbd frame 383 (84 of 100).
Fragment 003 / 009 :: integrate rgbd frame 384 (85 of 100).
Fragment 003 / 009 :: integrate rgbd frame 385 (86 of 100).
Fragment 003 / 009 :: integrate rgbd frame 386 (87 of 100).
Fragment 003 / 009 :: integrate rgbd frame 387 (88 of 100).
Fragment 003 / 009 :: integrate rgbd frame 388 (89 of 100).
Fragment 003 / 009 :: integrate rgbd frame 389 (90 of 100).
Fragment 003 / 009 :: integrate rgbd frame 390 (91 of 100).
Fragment 003 / 009 :: integrate rgbd frame 391 (92 of 100).
Fragment 003 / 009 :: integrate rgbd frame 392 (93 of 100).
Fragment 003 / 009 :: integrate rgbd frame 393 (94 of 100).
Fragment 003 / 009 :: integrate rgbd frame 394 (95 of 100).
Fragment 003 / 009 :: integrate rgbd frame 395 (96 of 100).
Fragment 003 / 009 :: integrate rgbd frame 396 (97 of 100).
Fragment 003 / 009 :: integrate rgbd frame 397 (98 of 100).
Fragment 003 / 009 :: integrate rgbd frame 398 (99 of 100).
Fragment 003 / 009 :: integrate rgbd frame 399 (100 of 100).
Fragment 004 / 009 :: RGBD matching between frame : 400 and 401
Fragment 004 / 009 :: RGBD matching between frame : 400 and 405
Fragment 004 / 009 :: RGBD matching between frame : 400 and 410
Fragment 004 / 009 :: RGBD matching between frame : 400 and 415
Fragment 004 / 009 :: RGBD matching between frame : 400 and 420
Fragment 004 / 009 :: RGBD matching between frame : 400 and 425
Fragment 004 / 009 :: RGBD matching between frame : 400 and 430
Fragment 004 / 009 :: RGBD matching between frame : 400 and 435
Fragment 004 / 009 :: RGBD matching between frame : 400 and 440
Fragment 004 / 009 :: RGBD matching between frame : 400 and 445
Fragment 004 / 009 :: RGBD matching between frame : 400 and 450
Fragment 004 / 009 :: RGBD matching between frame : 400 and 455
Fragment 004 / 009 :: RGBD matching between frame : 400 and 460
Fragment 004 / 009 :: RGBD matching between frame : 400 and 465
Fragment 004 / 009 :: RGBD matching between frame : 400 and 470
Fragment 004 / 009 :: RGBD matching between frame : 400 and 475
Fragment 004 / 009 :: RGBD matching between frame : 400 and 480
Fragment 004 / 009 :: RGBD matching between frame : 400 and 485
Fragment 004 / 009 :: RGBD matching between frame : 400 and 490
Fragment 004 / 009 :: RGBD matching between frame : 400 and 495
Fragment 004 / 009 :: RGBD matching between frame : 401 and 402
Fragment 004 / 009 :: RGBD matching between frame : 402 and 403
Fragment 004 / 009 :: RGBD matching between frame : 403 and 404
Fragment 004 / 009 :: RGBD matching between frame : 404 and 405
Fragment 004 / 009 :: RGBD matching between frame : 405 and 406
Fragment 004 / 009 :: RGBD matching between frame : 405 and 410
Fragment 004 / 009 :: RGBD matching between frame : 405 and 415
Fragment 004 / 009 :: RGBD matching between frame : 405 and 420
Fragment 004 / 009 :: RGBD matching between frame : 405 and 425
Fragment 004 / 009 :: RGBD matching between frame : 405 and 430
Fragment 004 / 009 :: RGBD matching between frame : 405 and 435
Fragment 004 / 009 :: RGBD matching between frame : 405 and 440
Fragment 004 / 009 :: RGBD matching between frame : 405 and 445
Fragment 004 / 009 :: RGBD matching between frame : 405 and 450
Fragment 004 / 009 :: RGBD matching between frame : 405 and 455
Fragment 004 / 009 :: RGBD matching between frame : 405 and 460
Fragment 004 / 009 :: RGBD matching between frame : 405 and 465
Fragment 004 / 009 :: RGBD matching between frame : 405 and 470
Fragment 004 / 009 :: RGBD matching between frame : 405 and 475
Fragment 004 / 009 :: RGBD matching between frame : 405 and 480
Fragment 004 / 009 :: RGBD matching between frame : 405 and 485
Fragment 004 / 009 :: RGBD matching between frame : 405 and 490
Fragment 004 / 009 :: RGBD matching between frame : 405 and 495
Fragment 004 / 009 :: RGBD matching between frame : 406 and 407
Fragment 004 / 009 :: RGBD matching between frame : 407 and 408
Fragment 004 / 009 :: RGBD matching between frame : 408 and 409
Fragment 004 / 009 :: RGBD matching between frame : 409 and 410
Fragment 004 / 009 :: RGBD matching between frame : 410 and 411
Fragment 004 / 009 :: RGBD matching between frame : 410 and 415
Fragment 004 / 009 :: RGBD matching between frame : 410 and 420
Fragment 004 / 009 :: RGBD matching between frame : 410 and 425
Fragment 004 / 009 :: RGBD matching between frame : 410 and 430
Fragment 004 / 009 :: RGBD matching between frame : 410 and 435
Fragment 004 / 009 :: RGBD matching between frame : 410 and 440
Fragment 004 / 009 :: RGBD matching between frame : 410 and 445
Fragment 004 / 009 :: RGBD matching between frame : 410 and 450
Fragment 004 / 009 :: RGBD matching between frame : 410 and 455
Fragment 004 / 009 :: RGBD matching between frame : 410 and 460
Fragment 004 / 009 :: RGBD matching between frame : 410 and 465
Fragment 004 / 009 :: RGBD matching between frame : 410 and 470
Fragment 004 / 009 :: RGBD matching between frame : 410 and 475
Fragment 004 / 009 :: RGBD matching between frame : 410 and 480
Fragment 004 / 009 :: RGBD matching between frame : 410 and 485
Fragment 004 / 009 :: RGBD matching between frame : 410 and 490
Fragment 004 / 009 :: RGBD matching between frame : 410 and 495
Fragment 004 / 009 :: RGBD matching between frame : 411 and 412
Fragment 004 / 009 :: RGBD matching between frame : 412 and 413
Fragment 004 / 009 :: RGBD matching between frame : 413 and 414
Fragment 004 / 009 :: RGBD matching between frame : 414 and 415
Fragment 004 / 009 :: RGBD matching between frame : 415 and 416
Fragment 004 / 009 :: RGBD matching between frame : 415 and 420
Fragment 004 / 009 :: RGBD matching between frame : 415 and 425
Fragment 004 / 009 :: RGBD matching between frame : 415 and 430
Fragment 004 / 009 :: RGBD matching between frame : 415 and 435
Fragment 004 / 009 :: RGBD matching between frame : 415 and 440
Fragment 004 / 009 :: RGBD matching between frame : 415 and 445
Fragment 004 / 009 :: RGBD matching between frame : 415 and 450
Fragment 004 / 009 :: RGBD matching between frame : 415 and 455
Fragment 004 / 009 :: RGBD matching between frame : 415 and 460
Fragment 004 / 009 :: RGBD matching between frame : 415 and 465
Fragment 004 / 009 :: RGBD matching between frame : 415 and 470
Fragment 004 / 009 :: RGBD matching between frame : 415 and 475
Fragment 004 / 009 :: RGBD matching between frame : 415 and 480
Fragment 004 / 009 :: RGBD matching between frame : 415 and 485
Fragment 004 / 009 :: RGBD matching between frame : 415 and 490
Fragment 004 / 009 :: RGBD matching between frame : 415 and 495
Fragment 004 / 009 :: RGBD matching between frame : 416 and 417
Fragment 004 / 009 :: RGBD matching between frame : 417 and 418
Fragment 004 / 009 :: RGBD matching between frame : 418 and 419
Fragment 004 / 009 :: RGBD matching between frame : 419 and 420
Fragment 004 / 009 :: RGBD matching between frame : 420 and 421
Fragment 004 / 009 :: RGBD matching between frame : 420 and 425
Fragment 004 / 009 :: RGBD matching between frame : 420 and 430
Fragment 004 / 009 :: RGBD matching between frame : 420 and 435
Fragment 004 / 009 :: RGBD matching between frame : 420 and 440
Fragment 004 / 009 :: RGBD matching between frame : 420 and 445
Fragment 004 / 009 :: RGBD matching between frame : 420 and 450
Fragment 004 / 009 :: RGBD matching between frame : 420 and 455
Fragment 004 / 009 :: RGBD matching between frame : 420 and 460
Fragment 004 / 009 :: RGBD matching between frame : 420 and 465
Fragment 004 / 009 :: RGBD matching between frame : 420 and 470
Fragment 004 / 009 :: RGBD matching between frame : 420 and 475
Fragment 004 / 009 :: RGBD matching between frame : 420 and 480
Fragment 004 / 009 :: RGBD matching between frame : 420 and 485
Fragment 004 / 009 :: RGBD matching between frame : 420 and 490
Fragment 004 / 009 :: RGBD matching between frame : 420 and 495
Fragment 004 / 009 :: RGBD matching between frame : 421 and 422
Fragment 004 / 009 :: RGBD matching between frame : 422 and 423
Fragment 004 / 009 :: RGBD matching between frame : 423 and 424
Fragment 004 / 009 :: RGBD matching between frame : 424 and 425
Fragment 004 / 009 :: RGBD matching between frame : 425 and 426
Fragment 004 / 009 :: RGBD matching between frame : 425 and 430
Fragment 004 / 009 :: RGBD matching between frame : 425 and 435
Fragment 004 / 009 :: RGBD matching between frame : 425 and 440
Fragment 004 / 009 :: RGBD matching between frame : 425 and 445
Fragment 004 / 009 :: RGBD matching between frame : 425 and 450
Fragment 004 / 009 :: RGBD matching between frame : 425 and 455
Fragment 004 / 009 :: RGBD matching between frame : 425 and 460
Fragment 004 / 009 :: RGBD matching between frame : 425 and 465
Fragment 004 / 009 :: RGBD matching between frame : 425 and 470
Fragment 004 / 009 :: RGBD matching between frame : 425 and 475
Fragment 004 / 009 :: RGBD matching between frame : 425 and 480
Fragment 004 / 009 :: RGBD matching between frame : 425 and 485
Fragment 004 / 009 :: RGBD matching between frame : 425 and 490
Fragment 004 / 009 :: RGBD matching between frame : 425 and 495
Fragment 004 / 009 :: RGBD matching between frame : 426 and 427
Fragment 004 / 009 :: RGBD matching between frame : 427 and 428
Fragment 004 / 009 :: RGBD matching between frame : 428 and 429
Fragment 004 / 009 :: RGBD matching between frame : 429 and 430
Fragment 004 / 009 :: RGBD matching between frame : 430 and 431
Fragment 004 / 009 :: RGBD matching between frame : 430 and 435
Fragment 004 / 009 :: RGBD matching between frame : 430 and 440
Fragment 004 / 009 :: RGBD matching between frame : 430 and 445
Fragment 004 / 009 :: RGBD matching between frame : 430 and 450
Fragment 004 / 009 :: RGBD matching between frame : 430 and 455
Fragment 004 / 009 :: RGBD matching between frame : 430 and 460
Fragment 004 / 009 :: RGBD matching between frame : 430 and 465
Fragment 004 / 009 :: RGBD matching between frame : 430 and 470
Fragment 004 / 009 :: RGBD matching between frame : 430 and 475
Fragment 004 / 009 :: RGBD matching between frame : 430 and 480
Fragment 004 / 009 :: RGBD matching between frame : 430 and 485
Fragment 004 / 009 :: RGBD matching between frame : 430 and 490
Fragment 004 / 009 :: RGBD matching between frame : 430 and 495
Fragment 004 / 009 :: RGBD matching between frame : 431 and 432
Fragment 004 / 009 :: RGBD matching between frame : 432 and 433
Fragment 004 / 009 :: RGBD matching between frame : 433 and 434
Fragment 004 / 009 :: RGBD matching between frame : 434 and 435
Fragment 004 / 009 :: RGBD matching between frame : 435 and 436
Fragment 004 / 009 :: RGBD matching between frame : 435 and 440
Fragment 004 / 009 :: RGBD matching between frame : 435 and 445
Fragment 004 / 009 :: RGBD matching between frame : 435 and 450
Fragment 004 / 009 :: RGBD matching between frame : 435 and 455
Fragment 004 / 009 :: RGBD matching between frame : 435 and 460
Fragment 004 / 009 :: RGBD matching between frame : 435 and 465
Fragment 004 / 009 :: RGBD matching between frame : 435 and 470
Fragment 004 / 009 :: RGBD matching between frame : 435 and 475
Fragment 004 / 009 :: RGBD matching between frame : 435 and 480
Fragment 004 / 009 :: RGBD matching between frame : 435 and 485
Fragment 004 / 009 :: RGBD matching between frame : 435 and 490
Fragment 004 / 009 :: RGBD matching between frame : 435 and 495
Fragment 004 / 009 :: RGBD matching between frame : 436 and 437
Fragment 004 / 009 :: RGBD matching between frame : 437 and 438
Fragment 004 / 009 :: RGBD matching between frame : 438 and 439
Fragment 004 / 009 :: RGBD matching between frame : 439 and 440
Fragment 004 / 009 :: RGBD matching between frame : 440 and 441
Fragment 004 / 009 :: RGBD matching between frame : 440 and 445
Fragment 004 / 009 :: RGBD matching between frame : 440 and 450
Fragment 004 / 009 :: RGBD matching between frame : 440 and 455
Fragment 004 / 009 :: RGBD matching between frame : 440 and 460
Fragment 004 / 009 :: RGBD matching between frame : 440 and 465
Fragment 004 / 009 :: RGBD matching between frame : 440 and 470
Fragment 004 / 009 :: RGBD matching between frame : 440 and 475
Fragment 004 / 009 :: RGBD matching between frame : 440 and 480
Fragment 004 / 009 :: RGBD matching between frame : 440 and 485
Fragment 004 / 009 :: RGBD matching between frame : 440 and 490
Fragment 004 / 009 :: RGBD matching between frame : 440 and 495
Fragment 004 / 009 :: RGBD matching between frame : 441 and 442
Fragment 004 / 009 :: RGBD matching between frame : 442 and 443
Fragment 004 / 009 :: RGBD matching between frame : 443 and 444
Fragment 004 / 009 :: RGBD matching between frame : 444 and 445
Fragment 004 / 009 :: RGBD matching between frame : 445 and 446
Fragment 004 / 009 :: RGBD matching between frame : 445 and 450
Fragment 004 / 009 :: RGBD matching between frame : 445 and 455
Fragment 004 / 009 :: RGBD matching between frame : 445 and 460
Fragment 004 / 009 :: RGBD matching between frame : 445 and 465
Fragment 004 / 009 :: RGBD matching between frame : 445 and 470
Fragment 004 / 009 :: RGBD matching between frame : 445 and 475
Fragment 004 / 009 :: RGBD matching between frame : 445 and 480
Fragment 004 / 009 :: RGBD matching between frame : 445 and 485
Fragment 004 / 009 :: RGBD matching between frame : 445 and 490
Fragment 004 / 009 :: RGBD matching between frame : 445 and 495
Fragment 004 / 009 :: RGBD matching between frame : 446 and 447
Fragment 004 / 009 :: RGBD matching between frame : 447 and 448
Fragment 004 / 009 :: RGBD matching between frame : 448 and 449
Fragment 004 / 009 :: RGBD matching between frame : 449 and 450
Fragment 004 / 009 :: RGBD matching between frame : 450 and 451
Fragment 004 / 009 :: RGBD matching between frame : 450 and 455
Fragment 004 / 009 :: RGBD matching between frame : 450 and 460
Fragment 004 / 009 :: RGBD matching between frame : 450 and 465
Fragment 004 / 009 :: RGBD matching between frame : 450 and 470
Fragment 004 / 009 :: RGBD matching between frame : 450 and 475
Fragment 004 / 009 :: RGBD matching between frame : 450 and 480
Fragment 004 / 009 :: RGBD matching between frame : 450 and 485
Fragment 004 / 009 :: RGBD matching between frame : 450 and 490
Fragment 004 / 009 :: RGBD matching between frame : 450 and 495
Fragment 004 / 009 :: RGBD matching between frame : 451 and 452
Fragment 004 / 009 :: RGBD matching between frame : 452 and 453
Fragment 004 / 009 :: RGBD matching between frame : 453 and 454
Fragment 004 / 009 :: RGBD matching between frame : 454 and 455
Fragment 004 / 009 :: RGBD matching between frame : 455 and 456
Fragment 004 / 009 :: RGBD matching between frame : 455 and 460
Fragment 004 / 009 :: RGBD matching between frame : 455 and 465
Fragment 004 / 009 :: RGBD matching between frame : 455 and 470
Fragment 004 / 009 :: RGBD matching between frame : 455 and 475
Fragment 004 / 009 :: RGBD matching between frame : 455 and 480
Fragment 004 / 009 :: RGBD matching between frame : 455 and 485
Fragment 004 / 009 :: RGBD matching between frame : 455 and 490
Fragment 004 / 009 :: RGBD matching between frame : 455 and 495
Fragment 004 / 009 :: RGBD matching between frame : 456 and 457
Fragment 004 / 009 :: RGBD matching between frame : 457 and 458
Fragment 004 / 009 :: RGBD matching between frame : 458 and 459
Fragment 004 / 009 :: RGBD matching between frame : 459 and 460
Fragment 004 / 009 :: RGBD matching between frame : 460 and 461
Fragment 004 / 009 :: RGBD matching between frame : 460 and 465
Fragment 004 / 009 :: RGBD matching between frame : 460 and 470
Fragment 004 / 009 :: RGBD matching between frame : 460 and 475
Fragment 004 / 009 :: RGBD matching between frame : 460 and 480
Fragment 004 / 009 :: RGBD matching between frame : 460 and 485
Fragment 004 / 009 :: RGBD matching between frame : 460 and 490
Fragment 004 / 009 :: RGBD matching between frame : 460 and 495
Fragment 004 / 009 :: RGBD matching between frame : 461 and 462
Fragment 004 / 009 :: RGBD matching between frame : 462 and 463
Fragment 004 / 009 :: RGBD matching between frame : 463 and 464
Fragment 004 / 009 :: RGBD matching between frame : 464 and 465
Fragment 004 / 009 :: RGBD matching between frame : 465 and 466
Fragment 004 / 009 :: RGBD matching between frame : 465 and 470
Fragment 004 / 009 :: RGBD matching between frame : 465 and 475
Fragment 004 / 009 :: RGBD matching between frame : 465 and 480
Fragment 004 / 009 :: RGBD matching between frame : 465 and 485
Fragment 004 / 009 :: RGBD matching between frame : 465 and 490
Fragment 004 / 009 :: RGBD matching between frame : 465 and 495
Fragment 004 / 009 :: RGBD matching between frame : 466 and 467
Fragment 004 / 009 :: RGBD matching between frame : 467 and 468
Fragment 004 / 009 :: RGBD matching between frame : 468 and 469
Fragment 004 / 009 :: RGBD matching between frame : 469 and 470
Fragment 004 / 009 :: RGBD matching between frame : 470 and 471
Fragment 004 / 009 :: RGBD matching between frame : 470 and 475
Fragment 004 / 009 :: RGBD matching between frame : 470 and 480
Fragment 004 / 009 :: RGBD matching between frame : 470 and 485
_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.012 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 175 edges.
[Open3D DEBUG] Line process weight : 75.253993
[Open3D DEBUG] [Initial     ] residual : 1.353551e+02, lambda : 1.917793e+01
[Open3D DEBUG] [Iteration 00] residual : 1.344006e+02, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.343933e+02, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.343920e+02, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 1.343916e+02, valid edges : 76, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.005 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 208 edges.
[Open3D DEBUG] Line process weight : 73.122069
[Open3D DEBUG] [Initial     ] residual : 3.316899e+05, lambda : 2.150542e+01
[Open3D DEBUG] [Iteration 00] residual : 2.084534e+03, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 2.057916e+03, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 2.056641e+03, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 2.056521e+03, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] [Iteration 04] residual : 2.056509e+03, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.007 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 180 edges.
[Open3D DEBUG] Line process weight : 79.439668
[Open3D DEBUG] [Initial     ] residual : 1.124743e+02, lambda : 2.193154e+01
[Open3D DEBUG] [Iteration 00] residual : 1.071811e+02, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.071456e+02, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.071452e+02, valid edges : 81, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.004 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 203 edges.
[Open3D DEBUG] Line process weight : 29.219827
[Open3D DEBUG] [Initial     ] residual : 2.904530e+04, lambda : 1.013153e+01
[Open3D DEBUG] [Iteration 00] residual : 1.008300e+03, valid edges : 71, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.002525e+03, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.000574e+03, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 9.994532e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 04] residual : 9.989084e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 05] residual : 9.986606e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 06] residual : 9.985419e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 07] residual : 9.984811e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 08] residual : 9.984486e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 09] residual : 9.984307e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 10] residual : 9.984206e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 11] residual : 9.984149e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 12] residual : 9.984117e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 13] residual : 9.984098e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 14] residual : 9.984088e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000Fragment 004 / 009 :: RGBD matching between frame : 470 and 490
Fragment 004 / 009 :: RGBD matching between frame : 470 and 495
Fragment 004 / 009 :: RGBD matching between frame : 471 and 472
Fragment 004 / 009 :: RGBD matching between frame : 472 and 473
Fragment 004 / 009 :: RGBD matching between frame : 473 and 474
Fragment 004 / 009 :: RGBD matching between frame : 474 and 475
Fragment 004 / 009 :: RGBD matching between frame : 475 and 476
Fragment 004 / 009 :: RGBD matching between frame : 475 and 480
Fragment 004 / 009 :: RGBD matching between frame : 475 and 485
Fragment 004 / 009 :: RGBD matching between frame : 475 and 490
Fragment 004 / 009 :: RGBD matching between frame : 475 and 495
Fragment 004 / 009 :: RGBD matching between frame : 476 and 477
Fragment 004 / 009 :: RGBD matching between frame : 477 and 478
Fragment 004 / 009 :: RGBD matching between frame : 478 and 479
Fragment 004 / 009 :: RGBD matching between frame : 479 and 480
Fragment 004 / 009 :: RGBD matching between frame : 480 and 481
Fragment 004 / 009 :: RGBD matching between frame : 480 and 485
Fragment 004 / 009 :: RGBD matching between frame : 480 and 490
Fragment 004 / 009 :: RGBD matching between frame : 480 and 495
Fragment 004 / 009 :: RGBD matching between frame : 481 and 482
Fragment 004 / 009 :: RGBD matching between frame : 482 and 483
Fragment 004 / 009 :: RGBD matching between frame : 483 and 484
Fragment 004 / 009 :: RGBD matching between frame : 484 and 485
Fragment 004 / 009 :: RGBD matching between frame : 485 and 486
Fragment 004 / 009 :: RGBD matching between frame : 485 and 490
Fragment 004 / 009 :: RGBD matching between frame : 485 and 495
Fragment 004 / 009 :: RGBD matching between frame : 486 and 487
Fragment 004 / 009 :: RGBD matching between frame : 487 and 488
Fragment 004 / 009 :: RGBD matching between frame : 488 and 489
Fragment 004 / 009 :: RGBD matching between frame : 489 and 490
Fragment 004 / 009 :: RGBD matching between frame : 490 and 491
Fragment 004 / 009 :: RGBD matching between frame : 490 and 495
Fragment 004 / 009 :: RGBD matching between frame : 491 and 492
Fragment 004 / 009 :: RGBD matching between frame : 492 and 493
Fragment 004 / 009 :: RGBD matching between frame : 493 and 494
Fragment 004 / 009 :: RGBD matching between frame : 494 and 495
Fragment 004 / 009 :: RGBD matching between frame : 495 and 496
Fragment 004 / 009 :: RGBD matching between frame : 496 and 497
Fragment 004 / 009 :: RGBD matching between frame : 497 and 498
Fragment 004 / 009 :: RGBD matching between frame : 498 and 499
Fragment 004 / 009 :: integrate rgbd frame 400 (1 of 100).
Fragment 004 / 009 :: integrate rgbd frame 401 (2 of 100).
Fragment 004 / 009 :: integrate rgbd frame 402 (3 of 100).
Fragment 004 / 009 :: integrate rgbd frame 403 (4 of 100).
Fragment 004 / 009 :: integrate rgbd frame 404 (5 of 100).
Fragment 004 / 009 :: integrate rgbd frame 405 (6 of 100).
Fragment 004 / 009 :: integrate rgbd frame 406 (7 of 100).
Fragment 004 / 009 :: integrate rgbd frame 407 (8 of 100).
Fragment 004 / 009 :: integrate rgbd frame 408 (9 of 100).
Fragment 004 / 009 :: integrate rgbd frame 409 (10 of 100).
Fragment 004 / 009 :: integrate rgbd frame 410 (11 of 100).
Fragment 004 / 009 :: integrate rgbd frame 411 (12 of 100).
Fragment 004 / 009 :: integrate rgbd frame 412 (13 of 100).
Fragment 004 / 009 :: integrate rgbd frame 413 (14 of 100).
Fragment 004 / 009 :: integrate rgbd frame 414 (15 of 100).
Fragment 004 / 009 :: integrate rgbd frame 415 (16 of 100).
Fragment 004 / 009 :: integrate rgbd frame 416 (17 of 100).
Fragment 004 / 009 :: integrate rgbd frame 417 (18 of 100).
Fragment 004 / 009 :: integrate rgbd frame 418 (19 of 100).
Fragment 004 / 009 :: integrate rgbd frame 419 (20 of 100).
Fragment 004 / 009 :: integrate rgbd frame 420 (21 of 100).
Fragment 004 / 009 :: integrate rgbd frame 421 (22 of 100).
Fragment 004 / 009 :: integrate rgbd frame 422 (23 of 100).
Fragment 004 / 009 :: integrate rgbd frame 423 (24 of 100).
Fragment 004 / 009 :: integrate rgbd frame 424 (25 of 100).
Fragment 004 / 009 :: integrate rgbd frame 425 (26 of 100).
Fragment 004 / 009 :: integrate rgbd frame 426 (27 of 100).
Fragment 004 / 009 :: integrate rgbd frame 427 (28 of 100).
Fragment 004 / 009 :: integrate rgbd frame 428 (29 of 100).
Fragment 004 / 009 :: integrate rgbd frame 429 (30 of 100).
Fragment 004 / 009 :: integrate rgbd frame 430 (31 of 100).
Fragment 004 / 009 :: integrate rgbd frame 431 (32 of 100).
Fragment 004 / 009 :: integrate rgbd frame 432 (33 of 100).
Fragment 004 / 009 :: integrate rgbd frame 433 (34 of 100).
Fragment 004 / 009 :: integrate rgbd frame 434 (35 of 100).
Fragment 004 / 009 :: integrate rgbd frame 435 (36 of 100).
Fragment 004 / 009 :: integrate rgbd frame 436 (37 of 100).
Fragment 004 / 009 :: integrate rgbd frame 437 (38 of 100).
Fragment 004 / 009 :: integrate rgbd frame 438 (39 of 100).
Fragment 004 / 009 :: integrate rgbd frame 439 (40 of 100).
Fragment 004 / 009 :: integrate rgbd frame 440 (41 of 100).
Fragment 004 / 009 :: integrate rgbd frame 441 (42 of 100).
Fragment 004 / 009 :: integrate rgbd frame 442 (43 of 100).
Fragment 004 / 009 :: integrate rgbd frame 443 (44 of 100).
Fragment 004 / 009 :: integrate rgbd frame 444 (45 of 100).
Fragment 004 / 009 :: integrate rgbd frame 445 (46 of 100).
Fragment 004 / 009 :: integrate rgbd frame 446 (47 of 100).
Fragment 004 / 009 :: integrate rgbd frame 447 (48 of 100).
Fragment 004 / 009 :: integrate rgbd frame 448 (49 of 100).
Fragment 004 / 009 :: integrate rgbd frame 449 (50 of 100).
Fragment 004 / 009 :: integrate rgbd frame 450 (51 of 100).
Fragment 004 / 009 :: integrate rgbd frame 451 (52 of 100).
Fragment 004 / 009 :: integrate rgbd frame 452 (53 of 100).
Fragment 004 / 009 :: integrate rgbd frame 453 (54 of 100).
Fragment 004 / 009 :: integrate rgbd frame 454 (55 of 100).
Fragment 004 / 009 :: integrate rgbd frame 455 (56 of 100).
Fragment 004 / 009 :: integrate rgbd frame 456 (57 of 100).
Fragment 004 / 009 :: integrate rgbd frame 457 (58 of 100).
Fragment 004 / 009 :: integrate rgbd frame 458 (59 of 100).
Fragment 004 / 009 :: integrate rgbd frame 459 (60 of 100).
Fragment 004 / 009 :: integrate rgbd frame 460 (61 of 100).
Fragment 004 / 009 :: integrate rgbd frame 461 (62 of 100).
Fragment 004 / 009 :: integrate rgbd frame 462 (63 of 100).
Fragment 004 / 009 :: integrate rgbd frame 463 (64 of 100).
Fragment 004 / 009 :: integrate rgbd frame 464 (65 of 100).
Fragment 004 / 009 :: integrate rgbd frame 465 (66 of 100).
Fragment 004 / 009 :: integrate rgbd frame 466 (67 of 100).
Fragment 004 / 009 :: integrate rgbd frame 467 (68 of 100).
Fragment 004 / 009 :: integrate rgbd frame 468 (69 of 100).
Fragment 004 / 009 :: integrate rgbd frame 469 (70 of 100).
Fragment 004 / 009 :: integrate rgbd frame 470 (71 of 100).
Fragment 004 / 009 :: integrate rgbd frame 471 (72 of 100).
Fragment 004 / 009 :: integrate rgbd frame 472 (73 of 100).
Fragment 004 / 009 :: integrate rgbd frame 473 (74 of 100).
Fragment 004 / 009 :: integrate rgbd frame 474 (75 of 100).
Fragment 004 / 009 :: integrate rgbd frame 475 (76 of 100).
Fragment 004 / 009 :: integrate rgbd frame 476 (77 of 100).
Fragment 004 / 009 :: integrate rgbd frame 477 (78 of 100).
Fragment 004 / 009 :: integrate rgbd frame 478 (79 of 100).
Fragment 004 / 009 :: integrate rgbd frame 479 (80 of 100).
Fragment 004 / 009 :: integrate rgbd frame 480 (81 of 100).
Fragment 004 / 009 :: integrate rgbd frame 481 (82 of 100).
Fragment 004 / 009 :: integrate rgbd frame 482 (83 of 100).
Fragment 004 / 009 :: integrate rgbd frame 483 (84 of 100).
Fragment 004 / 009 :: integrate rgbd frame 484 (85 of 100).
Fragment 004 / 009 :: integrate rgbd frame 485 (86 of 100).
Fragment 004 / 009 :: integrate rgbd frame 486 (87 of 100).
Fragment 004 / 009 :: integrate rgbd frame 487 (88 of 100).
Fragment 004 / 009 :: integrate rgbd frame 488 (89 of 100).
Fragment 004 / 009 :: integrate rgbd frame 489 (90 of 100).
Fragment 004 / 009 :: integrate rgbd frame 490 (91 of 100).
Fragment 004 / 009 :: integrate rgbd frame 491 (92 of 100).
Fragment 004 / 009 :: integrate rgbd frame 492 (93 of 100).
Fragment 004 / 009 :: integrate rgbd frame 493 (94 of 100).
Fragment 004 / 009 :: integrate rgbd frame 494 (95 of 100).
Fragment 004 / 009 :: integrate rgbd frame 495 (96 of 100).
Fragment 004 / 009 :: integrate rgbd frame 496 (97 of 100).
Fragment 004 / 009 :: integrate rgbd frame 497 (98 of 100).
Fragment 004 / 009 :: integrate rgbd frame 498 (99 of 100).
Fragment 004 / 009 :: integrate rgbd frame 499 (100 of 100).
Fragment 005 / 009 :: RGBD matching between frame : 500 and 501
Fragment 005 / 009 :: RGBD matching between frame : 500 and 505
Fragment 005 / 009 :: RGBD matching between frame : 500 and 510
Fragment 005 / 009 :: RGBD matching between frame : 500 and 515
Fragment 005 / 009 :: RGBD matching between frame : 500 and 520
Fragment 005 / 009 :: RGBD matching between frame : 500 and 525
Fragment 005 / 009 :: RGBD matching between frame : 500 and 530
Fragment 005 / 009 :: RGBD matching between frame : 500 and 535
Fragment 005 / 009 :: RGBD matching between frame : 500 and 540
Fragment 005 / 009 :: RGBD matching between frame : 500 and 545
Fragment 005 / 009 :: RGBD matching between frame : 500 and 550
Fragment 005 / 009 :: RGBD matching between frame : 500 and 555
Fragment 005 / 009 :: RGBD matching between frame : 500 and 560
Fragment 005 / 009 :: RGBD matching between frame : 500 and 565
Fragment 005 / 009 :: RGBD matching between frame : 500 and 570
Fragment 005 / 009 :: RGBD matching between frame : 500 and 575
Fragment 005 / 009 :: RGBD matching between frame : 500 and 580
Fragment 005 / 009 :: RGBD matching between frame : 500 and 585
Fragment 005 / 009 :: RGBD matching between frame : 500 and 590
Fragment 005 / 009 :: RGBD matching between frame : 500 and 595
Fragment 005 / 009 :: RGBD matching between frame : 501 and 502
Fragment 005 / 009 :: RGBD matching between frame : 502 and 503
Fragment 005 / 009 :: RGBD matching between frame : 503 and 504
Fragment 005 / 009 :: RGBD matching between frame : 504 and 505
Fragment 005 / 009 :: RGBD matching between frame : 505 and 506
Fragment 005 / 009 :: RGBD matching between frame : 505 and 510
Fragment 005 / 009 :: RGBD matching between frame : 505 and 515
Fragment 005 / 009 :: RGBD matching between frame : 505 and 520
Fragment 005 / 009 :: RGBD matching between frame : 505 and 525
Fragment 005 / 009 :: RGBD matching between frame : 505 and 530
Fragment 005 / 009 :: RGBD matching between frame : 505 and 535
Fragment 005 / 009 :: RGBD matching between frame : 505 and 540
Fragment 005 / 009 :: RGBD matching between frame : 505 and 545
Fragment 005 / 009 :: RGBD matching between frame : 505 and 550
Fragment 005 / 009 :: RGBD matching between frame : 505 and 555
Fragment 005 / 009 :: RGBD matching between frame : 505 and 560
Fragment 005 / 009 :: RGBD matching between frame : 505 and 565
Fragment 005 / 009 :: RGBD matching between frame : 505 and 570
Fragment 005 / 009 :: RGBD matching between frame : 505 and 575
Fragment 005 / 009 :: RGBD matching between frame : 505 and 580
Fragment 005 / 009 :: RGBD matching between frame : 505 and 585
Fragment 005 / 009 :: RGBD matching between frame : 505 and 590
Fragment 005 / 009 :: RGBD matching between frame : 505 and 595
Fragment 005 / 009 :: RGBD matching between frame : 506 and 507
Fragment 005 / 009 :: RGBD matching between frame : 507 and 508
Fragment 005 / 009 :: RGBD matching between frame : 508 and 509
Fragment 005 / 009 :: RGBD matching between frame : 509 and 510
Fragment 005 / 009 :: RGBD matching between frame : 510 and 511
Fragment 005 / 009 :: RGBD matching between frame : 510 and 515
Fragment 005 / 009 :: RGBD matching between frame : 510 and 520
Fragment 005 / 009 :: RGBD matching between frame : 510 and 525
Fragment 005 / 009 :: RGBD matching between frame : 510 and 530
Fragment 005 / 009 :: RGBD matching between frame : 510 and 535
Fragment 005 / 009 :: RGBD matching between frame : 510 and 540
Fragment 005 / 009 :: RGBD matching between frame : 510 and 545
Fragment 005 / 009 :: RGBD matching between frame : 510 and 550
Fragment 005 / 009 :: RGBD matching between frame : 510 and 555
Fragment 005 / 009 :: RGBD matching between frame : 510 and 560
Fragment 005 / 009 :: RGBD matching between frame : 510 and 565
Fragment 005 / 009 :: RGBD matching between frame : 510 and 570
Fragment 005 / 009 :: RGBD matching between frame : 510 and 575
Fragment 005 / 009 :: RGBD matching between frame : 510 and 580
Fragment 005 / 009 :: RGBD matching between frame : 510 and 585
Fragment 005 / 009 :: RGBD matching between frame : 510 and 590
Fragment 005 / 009 :: RGBD matching between frame : 510 and 595
Fragment 005 / 009 :: RGBD matching between frame : 511 and 512
Fragment 005 / 009 :: RGBD matching between frame : 512 and 513
Fragment 005 / 009 :: RGBD matching between frame : 513 and 514
Fragment 005 / 009 :: RGBD matching between frame : 514 and 515
Fragment 005 / 009 :: RGBD matching between frame : 515 and 516
Fragment 005 / 009 :: RGBD matching between frame : 515 and 520
Fragment 005 / 009 :: RGBD matching between frame : 515 and 525
Fragment 005 / 009 :: RGBD matching between frame : 515 and 530
Fragment 005 / 009 :: RGBD matching between frame : 515 and 535
Fragment 005 / 009 :: RGBD matching between frame : 515 and 540
Fragment 005 / 009 :: RGBD matching between frame : 515 and 545
Fragment 005 / 009 :: RGBD matching between frame : 515 and 550
Fragment 005 / 009 :: RGBD matching between frame : 515 and 555
Fragment 005 / 009 :: RGBD matching between frame : 515 and 560
Fragment 005 / 009 :: RGBD matching between frame : 515 and 565
Fragment 005 / 009 :: RGBD matching between frame : 515 and 570
Fragment 005 / 009 :: RGBD matching between frame : 515 and 575
Fragment 005 / 009 :: RGBD matching between frame : 515 and 580
Fragment 005 / 009 :: RGBD matching between frame : 515 and 585
Fragment 005 / 009 :: RGBD matching between frame : 515 and 590
Fragment 005 / 009 :: RGBD matching between frame : 515 and 595
Fragment 005 / 009 :: RGBD matching between frame : 516 and 517
Fragment 005 / 009 :: RGBD matching between frame : 517 and 518
Fragment 005 / 009 :: RGBD matching between frame : 518 and 519
Fragment 005 / 009 :: RGBD matching between frame : 519 and 520
Fragment 005 / 009 :: RGBD matching between frame : 520 and 521
Fragment 005 / 009 :: RGBD matching between frame : 520 and 525
Fragment 005 / 009 :: RGBD matching between frame : 520 and 530
Fragment 005 / 009 :: RGBD matching between frame : 520 and 535
Fragment 005 / 009 :: RGBD matching between frame : 520 and 540
Fragment 005 / 009 :: RGBD matching between frame : 520 and 545
Fragment 005 / 009 :: RGBD matching between frame : 520 and 550
Fragment 005 / 009 :: RGBD matching between frame : 520 and 555
Fragment 005 / 009 :: RGBD matching between frame : 520 and 560
Fragment 005 / 009 :: RGBD matching between frame : 520 and 565
Fragment 005 / 009 :: RGBD matching between frame : 520 and 570
Fragment 005 / 009 :: RGBD matching between frame : 520 and 575
Fragment 005 / 009 :: RGBD matching between frame : 520 and 580
Fragment 005 / 009 :: RGBD matching between frame : 520 and 585
Fragment 005 / 009 :: RGBD matching between frame : 520 and 590
Fragment 005 / 009 :: RGBD matching between frame : 520 and 595
Fragment 005 / 009 :: RGBD matching between frame : 521 and 522
Fragment 005 / 009 :: RGBD matching between frame : 522 and 523
Fragment 005 / 009 :: RGBD matching between frame : 523 and 524
Fragment 005 / 009 :: RGBD matching between frame : 524 and 525
Fragment 005 / 009 :: RGBD matching between frame : 525 and 526
Fragment 005 / 009 :: RGBD matching between frame : 525 and 530
Fragment 005 / 009 :: RGBD matching between frame : 525 and 535
Fragment 005 / 009 :: RGBD matching between frame : 525 and 540
Fragment 005 / 009 :: RGBD matching between frame : 525 and 545
Fragment 005 / 009 :: RGBD matching between frame : 525 and 550
Fragment 005 / 009 :: RGBD matching between frame : 525 and 555
Fragment 005 / 009 :: RGBD matching between frame : 525 and 560
Fragment 005 / 009 :: RGBD matching between frame : 525 and 565
Fragment 005 / 009 :: RGBD matching between frame : 525 and 570
Fragment 005 / 009 :: RGBD matching between frame : 525 and 575
Fragment 005 / 009 :: RGBD matching between frame : 525 and 580
Fragment 005 / 009 :: RGBD matching between frame : 525 and 585
Fragment 005 / 009 :: RGBD matching between frame : 525 and 590
Fragment 005 / 009 :: RGBD matching between frame : 525 and 595
Fragment 005 / 009 :: RGBD matching between frame : 526 and 527
Fragment 005 / 009 :: RGBD matching between frame : 527 and 528
Fragment 005 / 009 :: RGBD matching between frame : 528 and 529
Fragment 005 / 009 :: RGBD matching between frame : 529 and 530
Fragment 005 / 009 :: RGBD matching between frame : 530 and 531
Fragment 005 / 009 :: RGBD matching between frame : 530 and 535
Fragment 005 / 009 :: RGBD matching between frame : 530 and 540
Fragment 005 / 009 :: RGBD matching between frame : 530 and 545
Fragment 005 / 009 :: RGBD matching between frame : 530 and 550
Fragment 005 / 009 :: RGBD matching between frame : 530 and 555
Fragment 005 / 009 :: RGBD matching between frame : 530 and 560
Fragment 005 / 009 :: RGBD matching between frame : 530 and 565
Fragment 005 / 009 :: RGBD matching between frame : 530 and 570
Fragment 005 / 009 :: RGBD matching between frame : 530 and 575
Fragment 005 / 009 :: RGBD matching between frame : 530 and 580
Fragment 005 / 009 :: RGBD matching between frame : 530 and 585
Fragment 005 / 009 :: RGBD matching between frame : 530 and 590
Fragment 005 / 009 :: RGBD matching between frame : 530 and 595
Fragment 005 / 009 :: RGBD matching between frame : 531 and 532
Fragment 005 / 009 :: RGBD matching between frame : 532 and 533
Fragment 005 / 009 :: RGBD matching between frame : 533 and 534
Fragment 005 / 009 :: RGBD matching between frame : 534 and 535
Fragment 005 / 009 :: RGBD matching between frame : 535 and 536
Fragment 005 / 009 :: RGBD matching between frame : 535 and 540
Fragment 005 / 009 :: RGBD matching between frame : 535 and 545
Fragment 005 / 009 :: RGBD matching between frame : 535 and 550
Fragment 005 / 009 :: RGBD matching between frame : 535 and 555
Fragment 005 / 009 :: RGBD matching between frame : 535 and 560
Fragment 005 / 009 :: RGBD matching between frame : 535 and 565
Fragment 005 / 009 :: RGBD matching between frame : 535 and 570
Fragment 005 / 009 :: RGBD matching between frame : 535 and 575
Fragment 005 / 009 :: RGBD matching between frame : 535 and 580
Fragment 005 / 009 :: RGBD matching between frame : 535 and 585
Fragment 005 / 009 :: RGBD matching between frame : 535 and 590
Fragment 005 / 009 :: RGBD matching between frame : 535 and 595
Fragment 005 / 009 :: RGBD matching between frame : 536 and 537
Fragment 005 / 009 :: RGBD matching between frame : 537 and 538
Fragment 005 / 009 :: RGBD matching between frame : 538 and 539
Fragment 005 / 009 :: RGBD matching between frame : 539 and 540
Fragment 005 / 009 :: RGBD matching between frame : 540 and 541
Fragment 005 / 009 :: RGBD matching between frame : 540 and 545
Fragment 005 / 009 :: RGBD matching between frame : 540 and 550
Fragment 005 / 009 :: RGBD matching between frame : 540 and 555
Fragment 005 / 009 :: RGBD matching between frame : 540 and 560
Fragment 005 / 009 :: RGBD matching between frame : 540 and 565
Fragment 005 / 009 :: RGBD matching between frame : 540 and 570
Fragment 005 / 009 :: RGBD matching between frame : 540 and 575
Fragment 005 / 009 :: RGBD matching between frame : 540 and 580
Fragment 005 / 009 :: RGBD matching between frame : 540 and 585
Fragment 005 / 009 :: RGBD matching between frame : 540 and 590
Fragment 005 / 009 :: RGBD matching between frame : 540 and 595
Fragment 005 / 009 :: RGBD matching between frame : 541 and 542
Fragment 005 / 009 :: RGBD matching between frame : 542 and 543
Fragment 005 / 009 :: RGBD matching between frame : 543 and 544
Fragment 005 / 009 :: RGBD matching between frame : 544 and 545
Fragment 005 / 009 :: RGBD matching between frame : 545 and 546
Fragment 005 / 009 :: RGBD matching between frame : 545 and 550
Fragment 005 / 009 :: RGBD matching between frame : 545 and 555
Fragment 005 / 009 :: RGBD matching between frame : 545 and 560
Fragment 005 / 009 :: RGBD matching between frame : 545 and 565
Fragment 005 / 009 :: RGBD matching between frame : 545 and 570
Fragment 005 / 009 :: RGBD matching between frame : 545 and 575
Fragment 005 / 009 :: RGBD matching between frame : 545 and 580
Fragment 005 / 009 :: RGBD matching between frame : 545 and 585
Fragment 005 / 009 :: RGBD matching between frame : 545 and 590
Fragment 005 / 009 :: RGBD matching between frame : 545 and 595
Fragment 005 / 009 :: RGBD matching between frame : 546 and 547
Fragment 005 / 009 :: RGBD matching between frame : 547 and 548
Fragment 005 / 009 :: RGBD matching between frame : 548 and 549
Fragment 005 / 009 :: RGBD matching between frame : 549 and 550
Fragment 005 / 009 :: RGBD matching between frame : 550 and 551
Fragment 005 / 009 :: RGBD matching between frame : 550 and 555
Fragment 005 / 009 :: RGBD matching between frame : 550 and 560
Fragment 005 / 009 :: RGBD matching between frame : 550 and 565
Fragment 005 / 009 :: RGBD matching between frame : 550 and 570
Fragment 005 / 009 :: RGBD matching between frame : 550 and 575
Fragment 005 / 009 :: RGBD matching between frame : 550 and 580
Fragment 005 / 009 :: RGBD matching between frame : 550 and 585
Fragment 005 / 009 :: RGBD matching between frame : 550 and 590
Fragment 005 / 009 :: RGBD matching between frame : 550 and 595
Fragment 005 / 009 :: RGBD matching between frame : 551 and 552
Fragment 005 / 009 :: RGBD matching between frame : 552 and 553
Fragment 005 / 009 :: RGBD matching between frame : 553 and 554
Fragment 005 / 009 :: RGBD matching between frame : 554 and 555
Fragment 005 / 009 :: RGBD matching between frame : 555 and 556
Fragment 005 / 009 :: RGBD matching between frame : 555 and 560
Fragment 005 / 009 :: RGBD matching between frame : 555 and 565
Fragment 005 / 009 :: RGBD matching between frame : 555 and 570
Fragment 005 / 009 :: RGBD matching between frame : 555 and 575
Fragment 005 / 009 :: RGBD matching between frame : 555 and 580
Fragment 005 / 009 :: RGBD matching between frame : 555 and 585
Fragment 005 / 009 :: RGBD matching between frame : 555 and 590
Fragment 005 / 009 :: RGBD matching between frame : 555 and 595
Fragment 005 / 009 :: RGBD matching between frame : 556 and 557
Fragment 005 / 009 :: RGBD matching between frame : 557 and 558
Fragment 005 / 009 :: RGBD matching between frame : 558 and 559
Fragment 005 / 009 :: RGBD matching between frame : 559 and 560
Fragment 005 / 009 :: RGBD matching between frame : 560 and 561
Fragment 005 / 009 :: RGBD matching between frame : 560 and 565
Fragment 005 / 009 :: RGBD matching between frame : 560 and 570
Fragment 005 / 009 :: RGBD matching between frame : 560 and 575
Fragment 005 / 009 :: RGBD matching between frame : 560 and 580
Fragment 005 / 009 :: RGBD matching between frame : 560 and 585
Fragment 005 / 009 :: RGBD matching between frame : 560 and 590
Fragment 005 / 009 :: RGBD matching between frame : 560 and 595
Fragment 005 / 009 :: RGBD matching between frame : 561 and 562
Fragment 005 / 009 :: RGBD matching between frame : 562 and 563
Fragment 005 / 009 :: RGBD matching between frame : 563 and 564
Fragment 005 / 009 :: RGBD matching between frame : 564 and 565
Fragment 005 / 009 :: RGBD matching between frame : 565 and 566
Fragment 005 / 009 :: RGBD matching between frame : 565 and 570
Fragment 005 / 009 :: RGBD matching between frame : 565 and 575
Fragment 005 / 009 :: RGBD matching between frame : 565 and 580
Fragment 005 / 009 :: RGBD matching between frame : 565 and 585
Fragment 005 / 009 :: RGBD matching between frame : 565 and 590
Fragment 005 / 009 :: RGBD matching between frame : 565 and 595
Fragment 005 / 009 :: RGBD matching between frame : 566 and 567
Fragment 005 / 009 :: RGBD matching between frame : 567 and 568
Fragment 005 / 009 :: RGBD matching between frame : 568 and 569
Fragment 005 / 009 :: RGBD matching between frame : 569 and 570
Fragment 005 / 009 :: RGBD matching between frame : 570 and 571
Fragment 005 / 009 :: RGBD matching between frame : 570 and 575
Fragment 005 / 009 :: RGBD matching between frame : 570 and 580
Fragment 005 / 009 :: RGBD matching between frame : 570 and 585
Fragment 005 / 009 :: RGBD matching between frame : 570 and 590
Fragment 005 / 009 :: RGBD matching between frame : 570 and 595
Fragment 005 / 009 :: RGBD matching between frame : 571 and 572
000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.020 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 171 edges.
[Open3D DEBUG] Line process weight : 32.521690
[Open3D DEBUG] [Initial     ] residual : 1.941222e+02, lambda : 1.035821e+01
[Open3D DEBUG] [Iteration 00] residual : 1.885576e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.831088e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.823024e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 1.821679e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 04] residual : 1.821474e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 05] residual : 1.821412e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 06] residual : 1.821389e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 07] residual : 1.821379e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] [Iteration 08] residual : 1.821375e+02, valid edges : 72, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.011 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 179 edges.
[Open3D DEBUG] Line process weight : 22.393214
[Open3D DEBUG] [Initial     ] residual : 7.200325e+04, lambda : 7.128003e+00
[Open3D DEBUG] [Iteration 00] residual : 5.212772e+02, valid edges : 64, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 4.446190e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 02] residual : 4.230021e+02, valid edges : 70, time : 0.002 sec.
[Open3D DEBUG] [Iteration 03] residual : 4.187438e+02, valid edges : 70, time : 0.002 sec.
[Open3D DEBUG] [Iteration 04] residual : 4.169354e+02, valid edges : 70, time : 0.002 sec.
[Open3D DEBUG] [Iteration 05] residual : 4.157074e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 06] residual : 4.148299e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 07] residual : 4.142673e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 08] residual : 4.139532e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 09] residual : 4.137974e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 10] residual : 4.137259e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 11] residual : 4.136938e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 12] residual : 4.136786e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 13] residual : 4.136699e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 14] residual : 4.136634e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 15] residual : 4.136573e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 16] residual : 4.136506e+02, valid edges : 67, time : 0.003 sec.
[Open3D DEBUG] [Iteration 17] residual : 4.136428e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 18] residual : 4.136337e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 19] residual : 4.136230e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 20] residual : 4.136102e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 21] residual : 4.135951e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 22] residual : 4.135775e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 23] residual : 4.135569e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 24] residual : 4.135334e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 25] residual : 4.135067e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 26] residual : 4.134778e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 27] residual : 4.134438e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 28] residual : 4.134076e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 29] residual : 4.133742e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 30] residual : 4.133339e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 31] residual : 4.132950e+02, valid edges : 67, time : 0.006 sec.
[Open3D DEBUG] [Iteration 32] residual : 4.132540e+02, valid edges : 67, time : 0.002 sec.
[Open3D DEBUG] [Iteration 33] residual : 4.132015e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 34] residual : 4.131205e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 35] residual : 4.129486e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 36] residual : 4.124169e+02, valid edges : 67, time : 0.005 sec.
[Open3D DEBUG] [Iteration 37] residual : 4.104727e+02, valid edges : 67, time : 0.001 sec.
[Open3D DEBUG] [Iteration 38] residual : 4.055572e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 39] residual : 4.027412e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 40] residual : 4.017551e+02, valid edges : 68, time : 0.004 sec.
[Open3D DEBUG] [Iteration 41] residual : 4.014967e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 42] residual : 4.012795e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 43] residual : 4.011441e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 44] residual : 4.009296e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 45] residual : 4.008753e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 46] residual : 4.007073e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 47] residual : 4.006467e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 48] residual : 4.004369e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 49] residual : 4.002752e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 50] residual : 3.999319e+02, valid edges : 68, time : 0.004 sec.
[Open3D DEBUG] [Iteration 51] residual : 3.997847e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 52] residual : 3.996954e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 53] residual : 3.993479e+02, valid edges : 68, time : 0.003 sec.
[Open3D DEBUG] [Iteration 54] residual : 3.991677e+02, valid edges : 68, time : 0.003 sec.
[Open3D DEBUG] [Iteration 55] residual : 3.990383e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 56] residual : 3.989604e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 57] residual : 3.988493e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 58] residual : 3.987581e+02, valid edges : 68, time : 0.003 sec.
[Open3D DEBUG] [Iteration 59] residual : 3.987193e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 60] residual : 3.986415e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 61] residual : 3.986220e+02, valid edges : 68, time : 0.003 sec.
[Open3D DEBUG] [Iteration 62] residual : 3.986003e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 63] residual : 3.985860e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 64] residual : 3.985787e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 65] residual : 3.985771e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 66] residual : 3.985707e+02, valid edges : 68, time : 0.002 sec.
[Open3D DEBUG] [Iteration 67] residual : 3.985688e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 68] residual : 3.985678e+02, valid edges : 68, time : 0.005 sec.
[Open3D DEBUG] [Iteration 69] residual : 3.985671e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 70] residual : 3.985667e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.129 Fragment 005 / 009 :: RGBD matching between frame : 572 and 573
Fragment 005 / 009 :: RGBD matching between frame : 573 and 574
Fragment 005 / 009 :: RGBD matching between frame : 574 and 575
Fragment 005 / 009 :: RGBD matching between frame : 575 and 576
Fragment 005 / 009 :: RGBD matching between frame : 575 and 580
Fragment 005 / 009 :: RGBD matching between frame : 575 and 585
Fragment 005 / 009 :: RGBD matching between frame : 575 and 590
Fragment 005 / 009 :: RGBD matching between frame : 575 and 595
Fragment 005 / 009 :: RGBD matching between frame : 576 and 577
Fragment 005 / 009 :: RGBD matching between frame : 577 and 578
Fragment 005 / 009 :: RGBD matching between frame : 578 and 579
Fragment 005 / 009 :: RGBD matching between frame : 579 and 580
Fragment 005 / 009 :: RGBD matching between frame : 580 and 581
Fragment 005 / 009 :: RGBD matching between frame : 580 and 585
Fragment 005 / 009 :: RGBD matching between frame : 580 and 590
Fragment 005 / 009 :: RGBD matching between frame : 580 and 595
Fragment 005 / 009 :: RGBD matching between frame : 581 and 582
Fragment 005 / 009 :: RGBD matching between frame : 582 and 583
Fragment 005 / 009 :: RGBD matching between frame : 583 and 584
Fragment 005 / 009 :: RGBD matching between frame : 584 and 585
Fragment 005 / 009 :: RGBD matching between frame : 585 and 586
Fragment 005 / 009 :: RGBD matching between frame : 585 and 590
Fragment 005 / 009 :: RGBD matching between frame : 585 and 595
Fragment 005 / 009 :: RGBD matching between frame : 586 and 587
Fragment 005 / 009 :: RGBD matching between frame : 587 and 588
Fragment 005 / 009 :: RGBD matching between frame : 588 and 589
Fragment 005 / 009 :: RGBD matching between frame : 589 and 590
Fragment 005 / 009 :: RGBD matching between frame : 590 and 591
Fragment 005 / 009 :: RGBD matching between frame : 590 and 595
Fragment 005 / 009 :: RGBD matching between frame : 591 and 592
Fragment 005 / 009 :: RGBD matching between frame : 592 and 593
Fragment 005 / 009 :: RGBD matching between frame : 593 and 594
Fragment 005 / 009 :: RGBD matching between frame : 594 and 595
Fragment 005 / 009 :: RGBD matching between frame : 595 and 596
Fragment 005 / 009 :: RGBD matching between frame : 596 and 597
Fragment 005 / 009 :: RGBD matching between frame : 597 and 598
Fragment 005 / 009 :: RGBD matching between frame : 598 and 599
Fragment 005 / 009 :: integrate rgbd frame 500 (1 of 100).
Fragment 005 / 009 :: integrate rgbd frame 501 (2 of 100).
Fragment 005 / 009 :: integrate rgbd frame 502 (3 of 100).
Fragment 005 / 009 :: integrate rgbd frame 503 (4 of 100).
Fragment 005 / 009 :: integrate rgbd frame 504 (5 of 100).
Fragment 005 / 009 :: integrate rgbd frame 505 (6 of 100).
Fragment 005 / 009 :: integrate rgbd frame 506 (7 of 100).
Fragment 005 / 009 :: integrate rgbd frame 507 (8 of 100).
Fragment 005 / 009 :: integrate rgbd frame 508 (9 of 100).
Fragment 005 / 009 :: integrate rgbd frame 509 (10 of 100).
Fragment 005 / 009 :: integrate rgbd frame 510 (11 of 100).
Fragment 005 / 009 :: integrate rgbd frame 511 (12 of 100).
Fragment 005 / 009 :: integrate rgbd frame 512 (13 of 100).
Fragment 005 / 009 :: integrate rgbd frame 513 (14 of 100).
Fragment 005 / 009 :: integrate rgbd frame 514 (15 of 100).
Fragment 005 / 009 :: integrate rgbd frame 515 (16 of 100).
Fragment 005 / 009 :: integrate rgbd frame 516 (17 of 100).
Fragment 005 / 009 :: integrate rgbd frame 517 (18 of 100).
Fragment 005 / 009 :: integrate rgbd frame 518 (19 of 100).
Fragment 005 / 009 :: integrate rgbd frame 519 (20 of 100).
Fragment 005 / 009 :: integrate rgbd frame 520 (21 of 100).
Fragment 005 / 009 :: integrate rgbd frame 521 (22 of 100).
Fragment 005 / 009 :: integrate rgbd frame 522 (23 of 100).
Fragment 005 / 009 :: integrate rgbd frame 523 (24 of 100).
Fragment 005 / 009 :: integrate rgbd frame 524 (25 of 100).
Fragment 005 / 009 :: integrate rgbd frame 525 (26 of 100).
Fragment 005 / 009 :: integrate rgbd frame 526 (27 of 100).
Fragment 005 / 009 :: integrate rgbd frame 527 (28 of 100).
Fragment 005 / 009 :: integrate rgbd frame 528 (29 of 100).
Fragment 005 / 009 :: integrate rgbd frame 529 (30 of 100).
Fragment 005 / 009 :: integrate rgbd frame 530 (31 of 100).
Fragment 005 / 009 :: integrate rgbd frame 531 (32 of 100).
Fragment 005 / 009 :: integrate rgbd frame 532 (33 of 100).
Fragment 005 / 009 :: integrate rgbd frame 533 (34 of 100).
Fragment 005 / 009 :: integrate rgbd frame 534 (35 of 100).
Fragment 005 / 009 :: integrate rgbd frame 535 (36 of 100).
Fragment 005 / 009 :: integrate rgbd frame 536 (37 of 100).
Fragment 005 / 009 :: integrate rgbd frame 537 (38 of 100).
Fragment 005 / 009 :: integrate rgbd frame 538 (39 of 100).
Fragment 005 / 009 :: integrate rgbd frame 539 (40 of 100).
Fragment 005 / 009 :: integrate rgbd frame 540 (41 of 100).
Fragment 005 / 009 :: integrate rgbd frame 541 (42 of 100).
Fragment 005 / 009 :: integrate rgbd frame 542 (43 of 100).
Fragment 005 / 009 :: integrate rgbd frame 543 (44 of 100).
Fragment 005 / 009 :: integrate rgbd frame 544 (45 of 100).
Fragment 005 / 009 :: integrate rgbd frame 545 (46 of 100).
Fragment 005 / 009 :: integrate rgbd frame 546 (47 of 100).
Fragment 005 / 009 :: integrate rgbd frame 547 (48 of 100).
Fragment 005 / 009 :: integrate rgbd frame 548 (49 of 100).
Fragment 005 / 009 :: integrate rgbd frame 549 (50 of 100).
Fragment 005 / 009 :: integrate rgbd frame 550 (51 of 100).
Fragment 005 / 009 :: integrate rgbd frame 551 (52 of 100).
Fragment 005 / 009 :: integrate rgbd frame 552 (53 of 100).
Fragment 005 / 009 :: integrate rgbd frame 553 (54 of 100).
Fragment 005 / 009 :: integrate rgbd frame 554 (55 of 100).
Fragment 005 / 009 :: integrate rgbd frame 555 (56 of 100).
Fragment 005 / 009 :: integrate rgbd frame 556 (57 of 100).
Fragment 005 / 009 :: integrate rgbd frame 557 (58 of 100).
Fragment 005 / 009 :: integrate rgbd frame 558 (59 of 100).
Fragment 005 / 009 :: integrate rgbd frame 559 (60 of 100).
Fragment 005 / 009 :: integrate rgbd frame 560 (61 of 100).
Fragment 005 / 009 :: integrate rgbd frame 561 (62 of 100).
Fragment 005 / 009 :: integrate rgbd frame 562 (63 of 100).
Fragment 005 / 009 :: integrate rgbd frame 563 (64 of 100).
Fragment 005 / 009 :: integrate rgbd frame 564 (65 of 100).
Fragment 005 / 009 :: integrate rgbd frame 565 (66 of 100).
Fragment 005 / 009 :: integrate rgbd frame 566 (67 of 100).
Fragment 005 / 009 :: integrate rgbd frame 567 (68 of 100).
Fragment 005 / 009 :: integrate rgbd frame 568 (69 of 100).
Fragment 005 / 009 :: integrate rgbd frame 569 (70 of 100).
Fragment 005 / 009 :: integrate rgbd frame 570 (71 of 100).
Fragment 005 / 009 :: integrate rgbd frame 571 (72 of 100).
Fragment 005 / 009 :: integrate rgbd frame 572 (73 of 100).
Fragment 005 / 009 :: integrate rgbd frame 573 (74 of 100).
Fragment 005 / 009 :: integrate rgbd frame 574 (75 of 100).
Fragment 005 / 009 :: integrate rgbd frame 575 (76 of 100).
Fragment 005 / 009 :: integrate rgbd frame 576 (77 of 100).
Fragment 005 / 009 :: integrate rgbd frame 577 (78 of 100).
Fragment 005 / 009 :: integrate rgbd frame 578 (79 of 100).
Fragment 005 / 009 :: integrate rgbd frame 579 (80 of 100).
Fragment 005 / 009 :: integrate rgbd frame 580 (81 of 100).
Fragment 005 / 009 :: integrate rgbd frame 581 (82 of 100).
Fragment 005 / 009 :: integrate rgbd frame 582 (83 of 100).
Fragment 005 / 009 :: integrate rgbd frame 583 (84 of 100).
Fragment 005 / 009 :: integrate rgbd frame 584 (85 of 100).
Fragment 005 / 009 :: integrate rgbd frame 585 (86 of 100).
Fragment 005 / 009 :: integrate rgbd frame 586 (87 of 100).
Fragment 005 / 009 :: integrate rgbd frame 587 (88 of 100).
Fragment 005 / 009 :: integrate rgbd frame 588 (89 of 100).
Fragment 005 / 009 :: integrate rgbd frame 589 (90 of 100).
Fragment 005 / 009 :: integrate rgbd frame 590 (91 of 100).
Fragment 005 / 009 :: integrate rgbd frame 591 (92 of 100).
Fragment 005 / 009 :: integrate rgbd frame 592 (93 of 100).
Fragment 005 / 009 :: integrate rgbd frame 593 (94 of 100).
Fragment 005 / 009 :: integrate rgbd frame 594 (95 of 100).
Fragment 005 / 009 :: integrate rgbd frame 595 (96 of 100).
Fragment 005 / 009 :: integrate rgbd frame 596 (97 of 100).
Fragment 005 / 009 :: integrate rgbd frame 597 (98 of 100).
Fragment 005 / 009 :: integrate rgbd frame 598 (99 of 100).
Fragment 005 / 009 :: integrate rgbd frame 599 (100 of 100).
Fragment 006 / 009 :: RGBD matching between frame : 600 and 601
Fragment 006 / 009 :: RGBD matching between frame : 600 and 605
Fragment 006 / 009 :: RGBD matching between frame : 600 and 610
Fragment 006 / 009 :: RGBD matching between frame : 600 and 615
Fragment 006 / 009 :: RGBD matching between frame : 600 and 620
Fragment 006 / 009 :: RGBD matching between frame : 600 and 625
Fragment 006 / 009 :: RGBD matching between frame : 600 and 630
Fragment 006 / 009 :: RGBD matching between frame : 600 and 635
Fragment 006 / 009 :: RGBD matching between frame : 600 and 640
Fragment 006 / 009 :: RGBD matching between frame : 600 and 645
Fragment 006 / 009 :: RGBD matching between frame : 600 and 650
Fragment 006 / 009 :: RGBD matching between frame : 600 and 655
Fragment 006 / 009 :: RGBD matching between frame : 600 and 660
Fragment 006 / 009 :: RGBD matching between frame : 600 and 665
Fragment 006 / 009 :: RGBD matching between frame : 600 and 670
Fragment 006 / 009 :: RGBD matching between frame : 600 and 675
Fragment 006 / 009 :: RGBD matching between frame : 600 and 680
Fragment 006 / 009 :: RGBD matching between frame : 600 and 685
Fragment 006 / 009 :: RGBD matching between frame : 600 and 690
Fragment 006 / 009 :: RGBD matching between frame : 600 and 695
Fragment 006 / 009 :: RGBD matching between frame : 601 and 602
Fragment 006 / 009 :: RGBD matching between frame : 602 and 603
Fragment 006 / 009 :: RGBD matching between frame : 603 and 604
Fragment 006 / 009 :: RGBD matching between frame : 604 and 605
Fragment 006 / 009 :: RGBD matching between frame : 605 and 606
Fragment 006 / 009 :: RGBD matching between frame : 605 and 610
Fragment 006 / 009 :: RGBD matching between frame : 605 and 615
Fragment 006 / 009 :: RGBD matching between frame : 605 and 620
Fragment 006 / 009 :: RGBD matching between frame : 605 and 625
Fragment 006 / 009 :: RGBD matching between frame : 605 and 630
Fragment 006 / 009 :: RGBD matching between frame : 605 and 635
Fragment 006 / 009 :: RGBD matching between frame : 605 and 640
Fragment 006 / 009 :: RGBD matching between frame : 605 and 645
Fragment 006 / 009 :: RGBD matching between frame : 605 and 650
Fragment 006 / 009 :: RGBD matching between frame : 605 and 655
Fragment 006 / 009 :: RGBD matching between frame : 605 and 660
Fragment 006 / 009 :: RGBD matching between frame : 605 and 665
Fragment 006 / 009 :: RGBD matching between frame : 605 and 670
Fragment 006 / 009 :: RGBD matching between frame : 605 and 675
Fragment 006 / 009 :: RGBD matching between frame : 605 and 680
Fragment 006 / 009 :: RGBD matching between frame : 605 and 685
Fragment 006 / 009 :: RGBD matching between frame : 605 and 690
Fragment 006 / 009 :: RGBD matching between frame : 605 and 695
Fragment 006 / 009 :: RGBD matching between frame : 606 and 607
Fragment 006 / 009 :: RGBD matching between frame : 607 and 608
Fragment 006 / 009 :: RGBD matching between frame : 608 and 609
Fragment 006 / 009 :: RGBD matching between frame : 609 and 610
Fragment 006 / 009 :: RGBD matching between frame : 610 and 611
Fragment 006 / 009 :: RGBD matching between frame : 610 and 615
Fragment 006 / 009 :: RGBD matching between frame : 610 and 620
Fragment 006 / 009 :: RGBD matching between frame : 610 and 625
Fragment 006 / 009 :: RGBD matching between frame : 610 and 630
Fragment 006 / 009 :: RGBD matching between frame : 610 and 635
Fragment 006 / 009 :: RGBD matching between frame : 610 and 640
Fragment 006 / 009 :: RGBD matching between frame : 610 and 645
Fragment 006 / 009 :: RGBD matching between frame : 610 and 650
Fragment 006 / 009 :: RGBD matching between frame : 610 and 655
Fragment 006 / 009 :: RGBD matching between frame : 610 and 660
Fragment 006 / 009 :: RGBD matching between frame : 610 and 665
Fragment 006 / 009 :: RGBD matching between frame : 610 and 670
Fragment 006 / 009 :: RGBD matching between frame : 610 and 675
Fragment 006 / 009 :: RGBD matching between frame : 610 and 680
Fragment 006 / 009 :: RGBD matching between frame : 610 and 685
Fragment 006 / 009 :: RGBD matching between frame : 610 and 690
Fragment 006 / 009 :: RGBD matching between frame : 610 and 695
Fragment 006 / 009 :: RGBD matching between frame : 611 and 612
Fragment 006 / 009 :: RGBD matching between frame : 612 and 613
Fragment 006 / 009 :: RGBD matching between frame : 613 and 614
Fragment 006 / 009 :: RGBD matching between frame : 614 and 615
Fragment 006 / 009 :: RGBD matching between frame : 615 and 616
Fragment 006 / 009 :: RGBD matching between frame : 615 and 620
Fragment 006 / 009 :: RGBD matching between frame : 615 and 625
Fragment 006 / 009 :: RGBD matching between frame : 615 and 630
Fragment 006 / 009 :: RGBD matching between frame : 615 and 635
Fragment 006 / 009 :: RGBD matching between frame : 615 and 640
Fragment 006 / 009 :: RGBD matching between frame : 615 and 645
Fragment 006 / 009 :: RGBD matching between frame : 615 and 650
Fragment 006 / 009 :: RGBD matching between frame : 615 and 655
Fragment 006 / 009 :: RGBD matching between frame : 615 and 660
Fragment 006 / 009 :: RGBD matching between frame : 615 and 665
Fragment 006 / 009 :: RGBD matching between frame : 615 and 670
Fragment 006 / 009 :: RGBD matching between frame : 615 and 675
Fragment 006 / 009 :: RGBD matching between frame : 615 and 680
Fragment 006 / 009 :: RGBD matching between frame : 615 and 685
Fragment 006 / 009 :: RGBD matching between frame : 615 and 690
Fragment 006 / 009 :: RGBD matching between frame : 615 and 695
Fragment 006 / 009 :: RGBD matching between frame : 616 and 617
Fragment 006 / 009 :: RGBD matching between frame : 617 and 618
Fragment 006 / 009 :: RGBD matching between frame : 618 and 619
Fragment 006 / 009 :: RGBD matching between frame : 619 and 620
Fragment 006 / 009 :: RGBD matching between frame : 620 and 621
Fragment 006 / 009 :: RGBD matching between frame : 620 and 625
Fragment 006 / 009 :: RGBD matching between frame : 620 and 630
Fragment 006 / 009 :: RGBD matching between frame : 620 and 635
Fragment 006 / 009 :: RGBD matching between frame : 620 and 640
Fragment 006 / 009 :: RGBD matching between frame : 620 and 645
Fragment 006 / 009 :: RGBD matching between frame : 620 and 650
Fragment 006 / 009 :: RGBD matching between frame : 620 and 655
Fragment 006 / 009 :: RGBD matching between frame : 620 and 660
Fragment 006 / 009 :: RGBD matching between frame : 620 and 665
Fragment 006 / 009 :: RGBD matching between frame : 620 and 670
Fragment 006 / 009 :: RGBD matching between frame : 620 and 675
Fragment 006 / 009 :: RGBD matching between frame : 620 and 680
Fragment 006 / 009 :: RGBD matching between frame : 620 and 685
Fragment 006 / 009 :: RGBD matching between frame : 620 and 690
Fragment 006 / 009 :: RGBD matching between frame : 620 and 695
Fragment 006 / 009 :: RGBD matching between frame : 621 and 622
Fragment 006 / 009 :: RGBD matching between frame : 622 and 623
Fragment 006 / 009 :: RGBD matching between frame : 623 and 624
Fragment 006 / 009 :: RGBD matching between frame : 624 and 625
Fragment 006 / 009 :: RGBD matching between frame : 625 and 626
Fragment 006 / 009 :: RGBD matching between frame : 625 and 630
Fragment 006 / 009 :: RGBD matching between frame : 625 and 635
Fragment 006 / 009 :: RGBD matching between frame : 625 and 640
Fragment 006 / 009 :: RGBD matching between frame : 625 and 645
Fragment 006 / 009 :: RGBD matching between frame : 625 and 650
Fragment 006 / 009 :: RGBD matching between frame : 625 and 655
Fragment 006 / 009 :: RGBD matching between frame : 625 and 660
Fragment 006 / 009 :: RGBD matching between frame : 625 and 665
Fragment 006 / 009 :: RGBD matching between frame : 625 and 670
Fragment 006 / 009 :: RGBD matching between frame : 625 and 675
Fragment 006 / 009 :: RGBD matching between frame : 625 and 680
Fragment 006 / 009 :: RGBD matching between frame : 625 and 685
Fragment 006 / 009 :: RGBD matching between frame : 625 and 690
Fragment 006 / 009 :: RGBD matching between frame : 625 and 695
Fragment 006 / 009 :: RGBD matching between frame : 626 and 627
Fragment 006 / 009 :: RGBD matching between frame : 627 and 628
Fragment 006 / 009 :: RGBD matching between frame : 628 and 629
Fragment 006 / 009 :: RGBD matching between frame : 629 and 630
Fragment 006 / 009 :: RGBD matching between frame : 630 and 631
Fragment 006 / 009 :: RGBD matching between frame : 630 and 635
Fragment 006 / 009 :: RGBD matching between frame : 630 and 640
Fragment 006 / 009 :: RGBD matching between frame : 630 and 645
Fragment 006 / 009 :: RGBD matching between frame : 630 and 650
Fragment 006 / 009 :: RGBD matching between frame : 630 and 655
Fragment 006 / 009 :: RGBD matching between frame : 630 and 660
Fragment 006 / 009 :: RGBD matching between frame : 630 and 665
Fragment 006 / 009 :: RGBD matching between frame : 630 and 670
Fragment 006 / 009 :: RGBD matching between frame : 630 and 675
Fragment 006 / 009 :: RGBD matching between frame : 630 and 680
Fragment 006 / 009 :: RGBD matching between frame : 630 and 685
Fragment 006 / 009 :: RGBD matching between frame : 630 and 690
Fragment 006 / 009 :: RGBD matching between frame : 630 and 695
Fragment 006 / 009 :: RGBD matching between frame : 631 and 632
Fragment 006 / 009 :: RGBD matching between frame : 632 and 633
Fragment 006 / 009 :: RGBD matching between frame : 633 and 634
Fragment 006 / 009 :: RGBD matching between frame : 634 and 635
Fragment 006 / 009 :: RGBD matching between frame : 635 and 636
Fragment 006 / 009 :: RGBD matching between frame : 635 and 640
Fragment 006 / 009 :: RGBD matching between frame : 635 and 645
Fragment 006 / 009 :: RGBD matching between frame : 635 and 650
Fragment 006 / 009 :: RGBD matching between frame : 635 and 655
Fragment 006 / 009 :: RGBD matching between frame : 635 and 660
Fragment 006 / 009 :: RGBD matching between frame : 635 and 665
Fragment 006 / 009 :: RGBD matching between frame : 635 and 670
Fragment 006 / 009 :: RGBD matching between frame : 635 and 675
Fragment 006 / 009 :: RGBD matching between frame : 635 and 680
Fragment 006 / 009 :: RGBD matching between frame : 635 and 685
Fragment 006 / 009 :: RGBD matching between frame : 635 and 690
Fragment 006 / 009 :: RGBD matching between frame : 635 and 695
Fragment 006 / 009 :: RGBD matching between frame : 636 and 637
Fragment 006 / 009 :: RGBD matching between frame : 637 and 638
Fragment 006 / 009 :: RGBD matching between frame : 638 and 639
Fragment 006 / 009 :: RGBD matching between frame : 639 and 640
Fragment 006 / 009 :: RGBD matching between frame : 640 and 641
Fragment 006 / 009 :: RGBD matching between frame : 640 and 645
Fragment 006 / 009 :: RGBD matching between frame : 640 and 650
Fragment 006 / 009 :: RGBD matching between frame : 640 and 655
Fragment 006 / 009 :: RGBD matching between frame : 640 and 660
Fragment 006 / 009 :: RGBD matching between frame : 640 and 665
Fragment 006 / 009 :: RGBD matching between frame : 640 and 670
Fragment 006 / 009 :: RGBD matching between frame : 640 and 675
Fragment 006 / 009 :: RGBD matching between frame : 640 and 680
Fragment 006 / 009 :: RGBD matching between frame : 640 and 685
Fragment 006 / 009 :: RGBD matching between frame : 640 and 690
Fragment 006 / 009 :: RGBD matching between frame : 640 and 695
Fragment 006 / 009 :: RGBD matching between frame : 641 and 642
Fragment 006 / 009 :: RGBD matching between frame : 642 and 643
Fragment 006 / 009 :: RGBD matching between frame : 643 and 644
Fragment 006 / 009 :: RGBD matching between frame : 644 and 645
Fragment 006 / 009 :: RGBD matching between frame : 645 and 646
Fragment 006 / 009 :: RGBD matching between frame : 645 and 650
Fragment 006 / 009 :: RGBD matching between frame : 645 and 655
Fragment 006 / 009 :: RGBD matching between frame : 645 and 660
Fragment 006 / 009 :: RGBD matching between frame : 645 and 665
Fragment 006 / 009 :: RGBD matching between frame : 645 and 670
Fragment 006 / 009 :: RGBD matching between frame : 645 and 675
Fragment 006 / 009 :: RGBD matching between frame : 645 and 680
Fragment 006 / 009 :: RGBD matching between frame : 645 and 685
Fragment 006 / 009 :: RGBD matching between frame : 645 and 690
Fragment 006 / 009 :: RGBD matching between frame : 645 and 695
Fragment 006 / 009 :: RGBD matching between frame : 646 and 647
Fragment 006 / 009 :: RGBD matching between frame : 647 and 648
Fragment 006 / 009 :: RGBD matching between frame : 648 and 649
Fragment 006 / 009 :: RGBD matching between frame : 649 and 650
Fragment 006 / 009 :: RGBD matching between frame : 650 and 651
Fragment 006 / 009 :: RGBD matching between frame : 650 and 655
Fragment 006 / 009 :: RGBD matching between frame : 650 and 660
Fragment 006 / 009 :: RGBD matching between frame : 650 and 665
Fragment 006 / 009 :: RGBD matching between frame : 650 and 670
Fragment 006 / 009 :: RGBD matching between frame : 650 and 675
Fragment 006 / 009 :: RGBD matching between frame : 650 and 680
Fragment 006 / 009 :: RGBD matching between frame : 650 and 685
Fragment 006 / 009 :: RGBD matching between frame : 650 and 690
Fragment 006 / 009 :: RGBD matching between frame : 650 and 695
Fragment 006 / 009 :: RGBD matching between frame : 651 and 652
Fragment 006 / 009 :: RGBD matching between frame : 652 and 653
Fragment 006 / 009 :: RGBD matching between frame : 653 and 654
Fragment 006 / 009 :: RGBD matching between frame : 654 and 655
Fragment 006 / 009 :: RGBD matching between frame : 655 and 656
Fragment 006 / 009 :: RGBD matching between frame : 655 and 660
Fragment 006 / 009 :: RGBD matching between frame : 655 and 665
Fragment 006 / 009 :: RGBD matching between frame : 655 and 670
Fragment 006 / 009 :: RGBD matching between frame : 655 and 675
Fragment 006 / 009 :: RGBD matching between frame : 655 and 680
Fragment 006 / 009 :: RGBD matching between frame : 655 and 685
Fragment 006 / 009 :: RGBD matching between frame : 655 and 690
Fragment 006 / 009 :: RGBD matching between frame : 655 and 695
Fragment 006 / 009 :: RGBD matching between frame : 656 and 657
Fragment 006 / 009 :: RGBD matching between frame : 657 and 658
Fragment 006 / 009 :: RGBD matching between frame : 658 and 659
Fragment 006 / 009 :: RGBD matching between frame : 659 and 660
Fragment 006 / 009 :: RGBD matching between frame : 660 and 661
Fragment 006 / 009 :: RGBD matching between frame : 660 and 665
Fragment 006 / 009 :: RGBD matching between frame : 660 and 670
Fragment 006 / 009 :: RGBD matching between frame : 660 and 675
Fragment 006 / 009 :: RGBD matching between frame : 660 and 680
Fragment 006 / 009 :: RGBD matching between frame : 660 and 685
Fragment 006 / 009 :: RGBD matching between frame : 660 and 690
Fragment 006 / 009 :: RGBD matching between frame : 660 and 695
Fragment 006 / 009 :: RGBD matching between frame : 661 and 662
Fragment 006 / 009 :: RGBD matching between frame : 662 and 663
Fragment 006 / 009 :: RGBD matching between frame : 663 and 664
Fragment 006 / 009 :: RGBD matching between frame : 664 and 665
Fragment 006 / 009 :: RGBD matching between frame : 665 and 666
Fragment 006 / 009 :: RGBD matching between frame : 665 and 670
Fragment 006 / 009 :: RGBD matching between frame : 665 and 675
Fragment 006 / 009 :: RGBD matching between frame : 665 and 680
Fragment 006 / 009 :: RGBD matching between frame : 665 and 685
Fragment 006 / 009 :: RGBD matching between frame : 665 and 690
Fragment 006 / 009 :: RGBD matching between frame : 665 and 695
Fragment 006 / 009 :: RGBD matching between frame : 666 and 667
Fragment 006 / 009 :: RGBD matching between frame : 667 and 668
Fragment 006 / 009 :: RGBD matching between frame : 668 and 669
Fragment 006 / 009 :: RGBD matching between frame : 669 and 670
Fragment 006 / 009 :: RGBD matching between frame : 670 and 671
Fragment 006 / 009 :: RGBD matching between frame : 670 and 675
Fragment 006 / 009 :: RGBD matching between frame : 670 and 680
Fragment 006 / 009 :: RGBD matching between frame : 670 and 685
Fragment 006 / 009 :: RGBD matching between frame : 670 and 690
Fragment 006 / 009 :: RGBD matching between frame : 670 and 695
Fragment 006 / 009 :: RGBD matching between frame : 671 and 672
Fragment 006 / 009 :: RGBD matching between frame : 672 and 673
Fragment 006 / 009 :: RGBD matching between frame : 673 and 674
Fragment 006 / 009 :: RGBD matching between frame : 674 and 675
sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 167 edges.
[Open3D DEBUG] Line process weight : 23.340384
[Open3D DEBUG] [Initial     ] residual : 1.897741e+02, lambda : 1.036070e+01
[Open3D DEBUG] [Iteration 00] residual : 1.859363e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.853137e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.852516e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 1.852185e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 04] residual : 1.851866e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 05] residual : 1.851605e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 06] residual : 1.851418e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 07] residual : 1.851290e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 08] residual : 1.851205e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 09] residual : 1.851147e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 10] residual : 1.851109e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 11] residual : 1.851082e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 12] residual : 1.851064e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 13] residual : 1.851051e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 14] residual : 1.851043e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 15] residual : 1.851037e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 16] residual : 1.851033e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 17] residual : 1.851030e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] [Iteration 18] residual : 1.851028e+02, valid edges : 68, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.022 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 269 edges.
[Open3D DEBUG] Line process weight : 69.257657
[Open3D DEBUG] [Initial     ] residual : 1.115479e+04, lambda : 2.688187e+01
[Open3D DEBUG] [Iteration 00] residual : 9.429497e+02, valid edges : 158, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 9.031759e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 8.962391e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 8.917369e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 04] residual : 8.882062e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 05] residual : 8.852298e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 06] residual : 8.827301e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 07] residual : 8.807523e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 08] residual : 8.793334e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 09] residual : 8.784281e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 10] residual : 8.779144e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 11] residual : 8.776517e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 12] residual : 8.775280e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 13] residual : 8.774732e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 14] residual : 8.774500e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 15] residual : 8.774404e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 16] residual : 8.774365e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 17] residual : 8.774350e+02, valid edges : 160, time : 0.002 sec.
[Open3D DEBUG] CurrenFragment 006 / 009 :: RGBD matching between frame : 675 and 676
Fragment 006 / 009 :: RGBD matching between frame : 675 and 680
Fragment 006 / 009 :: RGBD matching between frame : 675 and 685
Fragment 006 / 009 :: RGBD matching between frame : 675 and 690
Fragment 006 / 009 :: RGBD matching between frame : 675 and 695
Fragment 006 / 009 :: RGBD matching between frame : 676 and 677
Fragment 006 / 009 :: RGBD matching between frame : 677 and 678
Fragment 006 / 009 :: RGBD matching between frame : 678 and 679
Fragment 006 / 009 :: RGBD matching between frame : 679 and 680
Fragment 006 / 009 :: RGBD matching between frame : 680 and 681
Fragment 006 / 009 :: RGBD matching between frame : 680 and 685
Fragment 006 / 009 :: RGBD matching between frame : 680 and 690
Fragment 006 / 009 :: RGBD matching between frame : 680 and 695
Fragment 006 / 009 :: RGBD matching between frame : 681 and 682
Fragment 006 / 009 :: RGBD matching between frame : 682 and 683
Fragment 006 / 009 :: RGBD matching between frame : 683 and 684
Fragment 006 / 009 :: RGBD matching between frame : 684 and 685
Fragment 006 / 009 :: RGBD matching between frame : 685 and 686
Fragment 006 / 009 :: RGBD matching between frame : 685 and 690
Fragment 006 / 009 :: RGBD matching between frame : 685 and 695
Fragment 006 / 009 :: RGBD matching between frame : 686 and 687
Fragment 006 / 009 :: RGBD matching between frame : 687 and 688
Fragment 006 / 009 :: RGBD matching between frame : 688 and 689
Fragment 006 / 009 :: RGBD matching between frame : 689 and 690
Fragment 006 / 009 :: RGBD matching between frame : 690 and 691
Fragment 006 / 009 :: RGBD matching between frame : 690 and 695
Fragment 006 / 009 :: RGBD matching between frame : 691 and 692
Fragment 006 / 009 :: RGBD matching between frame : 692 and 693
Fragment 006 / 009 :: RGBD matching between frame : 693 and 694
Fragment 006 / 009 :: RGBD matching between frame : 694 and 695
Fragment 006 / 009 :: RGBD matching between frame : 695 and 696
Fragment 006 / 009 :: RGBD matching between frame : 696 and 697
Fragment 006 / 009 :: RGBD matching between frame : 697 and 698
Fragment 006 / 009 :: RGBD matching between frame : 698 and 699
Fragment 006 / 009 :: integrate rgbd frame 600 (1 of 100).
Fragment 006 / 009 :: integrate rgbd frame 601 (2 of 100).
Fragment 006 / 009 :: integrate rgbd frame 602 (3 of 100).
Fragment 006 / 009 :: integrate rgbd frame 603 (4 of 100).
Fragment 006 / 009 :: integrate rgbd frame 604 (5 of 100).
Fragment 006 / 009 :: integrate rgbd frame 605 (6 of 100).
Fragment 006 / 009 :: integrate rgbd frame 606 (7 of 100).
Fragment 006 / 009 :: integrate rgbd frame 607 (8 of 100).
Fragment 006 / 009 :: integrate rgbd frame 608 (9 of 100).
Fragment 006 / 009 :: integrate rgbd frame 609 (10 of 100).
Fragment 006 / 009 :: integrate rgbd frame 610 (11 of 100).
Fragment 006 / 009 :: integrate rgbd frame 611 (12 of 100).
Fragment 006 / 009 :: integrate rgbd frame 612 (13 of 100).
Fragment 006 / 009 :: integrate rgbd frame 613 (14 of 100).
Fragment 006 / 009 :: integrate rgbd frame 614 (15 of 100).
Fragment 006 / 009 :: integrate rgbd frame 615 (16 of 100).
Fragment 006 / 009 :: integrate rgbd frame 616 (17 of 100).
Fragment 006 / 009 :: integrate rgbd frame 617 (18 of 100).
Fragment 006 / 009 :: integrate rgbd frame 618 (19 of 100).
Fragment 006 / 009 :: integrate rgbd frame 619 (20 of 100).
Fragment 006 / 009 :: integrate rgbd frame 620 (21 of 100).
Fragment 006 / 009 :: integrate rgbd frame 621 (22 of 100).
Fragment 006 / 009 :: integrate rgbd frame 622 (23 of 100).
Fragment 006 / 009 :: integrate rgbd frame 623 (24 of 100).
Fragment 006 / 009 :: integrate rgbd frame 624 (25 of 100).
Fragment 006 / 009 :: integrate rgbd frame 625 (26 of 100).
Fragment 006 / 009 :: integrate rgbd frame 626 (27 of 100).
Fragment 006 / 009 :: integrate rgbd frame 627 (28 of 100).
Fragment 006 / 009 :: integrate rgbd frame 628 (29 of 100).
Fragment 006 / 009 :: integrate rgbd frame 629 (30 of 100).
Fragment 006 / 009 :: integrate rgbd frame 630 (31 of 100).
Fragment 006 / 009 :: integrate rgbd frame 631 (32 of 100).
Fragment 006 / 009 :: integrate rgbd frame 632 (33 of 100).
Fragment 006 / 009 :: integrate rgbd frame 633 (34 of 100).
Fragment 006 / 009 :: integrate rgbd frame 634 (35 of 100).
Fragment 006 / 009 :: integrate rgbd frame 635 (36 of 100).
Fragment 006 / 009 :: integrate rgbd frame 636 (37 of 100).
Fragment 006 / 009 :: integrate rgbd frame 637 (38 of 100).
Fragment 006 / 009 :: integrate rgbd frame 638 (39 of 100).
Fragment 006 / 009 :: integrate rgbd frame 639 (40 of 100).
Fragment 006 / 009 :: integrate rgbd frame 640 (41 of 100).
Fragment 006 / 009 :: integrate rgbd frame 641 (42 of 100).
Fragment 006 / 009 :: integrate rgbd frame 642 (43 of 100).
Fragment 006 / 009 :: integrate rgbd frame 643 (44 of 100).
Fragment 006 / 009 :: integrate rgbd frame 644 (45 of 100).
Fragment 006 / 009 :: integrate rgbd frame 645 (46 of 100).
Fragment 006 / 009 :: integrate rgbd frame 646 (47 of 100).
Fragment 006 / 009 :: integrate rgbd frame 647 (48 of 100).
Fragment 006 / 009 :: integrate rgbd frame 648 (49 of 100).
Fragment 006 / 009 :: integrate rgbd frame 649 (50 of 100).
Fragment 006 / 009 :: integrate rgbd frame 650 (51 of 100).
Fragment 006 / 009 :: integrate rgbd frame 651 (52 of 100).
Fragment 006 / 009 :: integrate rgbd frame 652 (53 of 100).
Fragment 006 / 009 :: integrate rgbd frame 653 (54 of 100).
Fragment 006 / 009 :: integrate rgbd frame 654 (55 of 100).
Fragment 006 / 009 :: integrate rgbd frame 655 (56 of 100).
Fragment 006 / 009 :: integrate rgbd frame 656 (57 of 100).
Fragment 006 / 009 :: integrate rgbd frame 657 (58 of 100).
Fragment 006 / 009 :: integrate rgbd frame 658 (59 of 100).
Fragment 006 / 009 :: integrate rgbd frame 659 (60 of 100).
Fragment 006 / 009 :: integrate rgbd frame 660 (61 of 100).
Fragment 006 / 009 :: integrate rgbd frame 661 (62 of 100).
Fragment 006 / 009 :: integrate rgbd frame 662 (63 of 100).
Fragment 006 / 009 :: integrate rgbd frame 663 (64 of 100).
Fragment 006 / 009 :: integrate rgbd frame 664 (65 of 100).
Fragment 006 / 009 :: integrate rgbd frame 665 (66 of 100).
Fragment 006 / 009 :: integrate rgbd frame 666 (67 of 100).
Fragment 006 / 009 :: integrate rgbd frame 667 (68 of 100).
Fragment 006 / 009 :: integrate rgbd frame 668 (69 of 100).
Fragment 006 / 009 :: integrate rgbd frame 669 (70 of 100).
Fragment 006 / 009 :: integrate rgbd frame 670 (71 of 100).
Fragment 006 / 009 :: integrate rgbd frame 671 (72 of 100).
Fragment 006 / 009 :: integrate rgbd frame 672 (73 of 100).
Fragment 006 / 009 :: integrate rgbd frame 673 (74 of 100).
Fragment 006 / 009 :: integrate rgbd frame 674 (75 of 100).
Fragment 006 / 009 :: integrate rgbd frame 675 (76 of 100).
Fragment 006 / 009 :: integrate rgbd frame 676 (77 of 100).
Fragment 006 / 009 :: integrate rgbd frame 677 (78 of 100).
Fragment 006 / 009 :: integrate rgbd frame 678 (79 of 100).
Fragment 006 / 009 :: integrate rgbd frame 679 (80 of 100).
Fragment 006 / 009 :: integrate rgbd frame 680 (81 of 100).
Fragment 006 / 009 :: integrate rgbd frame 681 (82 of 100).
Fragment 006 / 009 :: integrate rgbd frame 682 (83 of 100).
Fragment 006 / 009 :: integrate rgbd frame 683 (84 of 100).
Fragment 006 / 009 :: integrate rgbd frame 684 (85 of 100).
Fragment 006 / 009 :: integrate rgbd frame 685 (86 of 100).
Fragment 006 / 009 :: integrate rgbd frame 686 (87 of 100).
Fragment 006 / 009 :: integrate rgbd frame 687 (88 of 100).
Fragment 006 / 009 :: integrate rgbd frame 688 (89 of 100).
Fragment 006 / 009 :: integrate rgbd frame 689 (90 of 100).
Fragment 006 / 009 :: integrate rgbd frame 690 (91 of 100).
Fragment 006 / 009 :: integrate rgbd frame 691 (92 of 100).
Fragment 006 / 009 :: integrate rgbd frame 692 (93 of 100).
Fragment 006 / 009 :: integrate rgbd frame 693 (94 of 100).
Fragment 006 / 009 :: integrate rgbd frame 694 (95 of 100).
Fragment 006 / 009 :: integrate rgbd frame 695 (96 of 100).
Fragment 006 / 009 :: integrate rgbd frame 696 (97 of 100).
Fragment 006 / 009 :: integrate rgbd frame 697 (98 of 100).
Fragment 006 / 009 :: integrate rgbd frame 698 (99 of 100).
Fragment 006 / 009 :: integrate rgbd frame 699 (100 of 100).
Fragment 007 / 009 :: RGBD matching between frame : 700 and 701
Fragment 007 / 009 :: RGBD matching between frame : 700 and 705
Fragment 007 / 009 :: RGBD matching between frame : 700 and 710
Fragment 007 / 009 :: RGBD matching between frame : 700 and 715
Fragment 007 / 009 :: RGBD matching between frame : 700 and 720
Fragment 007 / 009 :: RGBD matching between frame : 700 and 725
Fragment 007 / 009 :: RGBD matching between frame : 700 and 730
Fragment 007 / 009 :: RGBD matching between frame : 700 and 735
Fragment 007 / 009 :: RGBD matching between frame : 700 and 740
Fragment 007 / 009 :: RGBD matching between frame : 700 and 745
Fragment 007 / 009 :: RGBD matching between frame : 700 and 750
Fragment 007 / 009 :: RGBD matching between frame : 700 and 755
Fragment 007 / 009 :: RGBD matching between frame : 700 and 760
Fragment 007 / 009 :: RGBD matching between frame : 700 and 765
Fragment 007 / 009 :: RGBD matching between frame : 700 and 770
Fragment 007 / 009 :: RGBD matching between frame : 700 and 775
Fragment 007 / 009 :: RGBD matching between frame : 700 and 780
Fragment 007 / 009 :: RGBD matching between frame : 700 and 785
Fragment 007 / 009 :: RGBD matching between frame : 700 and 790
Fragment 007 / 009 :: RGBD matching between frame : 700 and 795
Fragment 007 / 009 :: RGBD matching between frame : 701 and 702
Fragment 007 / 009 :: RGBD matching between frame : 702 and 703
Fragment 007 / 009 :: RGBD matching between frame : 703 and 704
Fragment 007 / 009 :: RGBD matching between frame : 704 and 705
Fragment 007 / 009 :: RGBD matching between frame : 705 and 706
Fragment 007 / 009 :: RGBD matching between frame : 705 and 710
Fragment 007 / 009 :: RGBD matching between frame : 705 and 715
Fragment 007 / 009 :: RGBD matching between frame : 705 and 720
Fragment 007 / 009 :: RGBD matching between frame : 705 and 725
Fragment 007 / 009 :: RGBD matching between frame : 705 and 730
Fragment 007 / 009 :: RGBD matching between frame : 705 and 735
Fragment 007 / 009 :: RGBD matching between frame : 705 and 740
Fragment 007 / 009 :: RGBD matching between frame : 705 and 745
Fragment 007 / 009 :: RGBD matching between frame : 705 and 750
Fragment 007 / 009 :: RGBD matching between frame : 705 and 755
Fragment 007 / 009 :: RGBD matching between frame : 705 and 760
Fragment 007 / 009 :: RGBD matching between frame : 705 and 765
Fragment 007 / 009 :: RGBD matching between frame : 705 and 770
Fragment 007 / 009 :: RGBD matching between frame : 705 and 775
Fragment 007 / 009 :: RGBD matching between frame : 705 and 780
Fragment 007 / 009 :: RGBD matching between frame : 705 and 785
Fragment 007 / 009 :: RGBD matching between frame : 705 and 790
Fragment 007 / 009 :: RGBD matching between frame : 705 and 795
Fragment 007 / 009 :: RGBD matching between frame : 706 and 707
Fragment 007 / 009 :: RGBD matching between frame : 707 and 708
Fragment 007 / 009 :: RGBD matching between frame : 708 and 709
Fragment 007 / 009 :: RGBD matching between frame : 709 and 710
Fragment 007 / 009 :: RGBD matching between frame : 710 and 711
Fragment 007 / 009 :: RGBD matching between frame : 710 and 715
Fragment 007 / 009 :: RGBD matching between frame : 710 and 720
Fragment 007 / 009 :: RGBD matching between frame : 710 and 725
Fragment 007 / 009 :: RGBD matching between frame : 710 and 730
Fragment 007 / 009 :: RGBD matching between frame : 710 and 735
Fragment 007 / 009 :: RGBD matching between frame : 710 and 740
Fragment 007 / 009 :: RGBD matching between frame : 710 and 745
Fragment 007 / 009 :: RGBD matching between frame : 710 and 750
Fragment 007 / 009 :: RGBD matching between frame : 710 and 755
Fragment 007 / 009 :: RGBD matching between frame : 710 and 760
Fragment 007 / 009 :: RGBD matching between frame : 710 and 765
Fragment 007 / 009 :: RGBD matching between frame : 710 and 770
Fragment 007 / 009 :: RGBD matching between frame : 710 and 775
Fragment 007 / 009 :: RGBD matching between frame : 710 and 780
Fragment 007 / 009 :: RGBD matching between frame : 710 and 785
Fragment 007 / 009 :: RGBD matching between frame : 710 and 790
Fragment 007 / 009 :: RGBD matching between frame : 710 and 795
Fragment 007 / 009 :: RGBD matching between frame : 711 and 712
Fragment 007 / 009 :: RGBD matching between frame : 712 and 713
Fragment 007 / 009 :: RGBD matching between frame : 713 and 714
Fragment 007 / 009 :: RGBD matching between frame : 714 and 715
Fragment 007 / 009 :: RGBD matching between frame : 715 and 716
Fragment 007 / 009 :: RGBD matching between frame : 715 and 720
Fragment 007 / 009 :: RGBD matching between frame : 715 and 725
Fragment 007 / 009 :: RGBD matching between frame : 715 and 730
Fragment 007 / 009 :: RGBD matching between frame : 715 and 735
Fragment 007 / 009 :: RGBD matching between frame : 715 and 740
Fragment 007 / 009 :: RGBD matching between frame : 715 and 745
Fragment 007 / 009 :: RGBD matching between frame : 715 and 750
Fragment 007 / 009 :: RGBD matching between frame : 715 and 755
Fragment 007 / 009 :: RGBD matching between frame : 715 and 760
Fragment 007 / 009 :: RGBD matching between frame : 715 and 765
Fragment 007 / 009 :: RGBD matching between frame : 715 and 770
Fragment 007 / 009 :: RGBD matching between frame : 715 and 775
Fragment 007 / 009 :: RGBD matching between frame : 715 and 780
Fragment 007 / 009 :: RGBD matching between frame : 715 and 785
Fragment 007 / 009 :: RGBD matching between frame : 715 and 790
Fragment 007 / 009 :: RGBD matching between frame : 715 and 795
Fragment 007 / 009 :: RGBD matching between frame : 716 and 717
Fragment 007 / 009 :: RGBD matching between frame : 717 and 718
Fragment 007 / 009 :: RGBD matching between frame : 718 and 719
Fragment 007 / 009 :: RGBD matching between frame : 719 and 720
Fragment 007 / 009 :: RGBD matching between frame : 720 and 721
Fragment 007 / 009 :: RGBD matching between frame : 720 and 725
Fragment 007 / 009 :: RGBD matching between frame : 720 and 730
Fragment 007 / 009 :: RGBD matching between frame : 720 and 735
Fragment 007 / 009 :: RGBD matching between frame : 720 and 740
Fragment 007 / 009 :: RGBD matching between frame : 720 and 745
Fragment 007 / 009 :: RGBD matching between frame : 720 and 750
Fragment 007 / 009 :: RGBD matching between frame : 720 and 755
Fragment 007 / 009 :: RGBD matching between frame : 720 and 760
Fragment 007 / 009 :: RGBD matching between frame : 720 and 765
Fragment 007 / 009 :: RGBD matching between frame : 720 and 770
Fragment 007 / 009 :: RGBD matching between frame : 720 and 775
Fragment 007 / 009 :: RGBD matching between frame : 720 and 780
Fragment 007 / 009 :: RGBD matching between frame : 720 and 785
Fragment 007 / 009 :: RGBD matching between frame : 720 and 790
Fragment 007 / 009 :: RGBD matching between frame : 720 and 795
Fragment 007 / 009 :: RGBD matching between frame : 721 and 722
Fragment 007 / 009 :: RGBD matching between frame : 722 and 723
Fragment 007 / 009 :: RGBD matching between frame : 723 and 724
Fragment 007 / 009 :: RGBD matching between frame : 724 and 725
Fragment 007 / 009 :: RGBD matching between frame : 725 and 726
Fragment 007 / 009 :: RGBD matching between frame : 725 and 730
Fragment 007 / 009 :: RGBD matching between frame : 725 and 735
Fragment 007 / 009 :: RGBD matching between frame : 725 and 740
Fragment 007 / 009 :: RGBD matching between frame : 725 and 745
Fragment 007 / 009 :: RGBD matching between frame : 725 and 750
Fragment 007 / 009 :: RGBD matching between frame : 725 and 755
Fragment 007 / 009 :: RGBD matching between frame : 725 and 760
Fragment 007 / 009 :: RGBD matching between frame : 725 and 765
Fragment 007 / 009 :: RGBD matching between frame : 725 and 770
Fragment 007 / 009 :: RGBD matching between frame : 725 and 775
Fragment 007 / 009 :: RGBD matching between frame : 725 and 780
Fragment 007 / 009 :: RGBD matching between frame : 725 and 785
Fragment 007 / 009 :: RGBD matching between frame : 725 and 790
Fragment 007 / 009 :: RGBD matching between frame : 725 and 795
Fragment 007 / 009 :: RGBD matching between frame : 726 and 727
Fragment 007 / 009 :: RGBD matching between frame : 727 and 728
Fragment 007 / 009 :: RGBD matching between frame : 728 and 729
Fragment 007 / 009 :: RGBD matching between frame : 729 and 730
Fragment 007 / 009 :: RGBD matching between frame : 730 and 731
Fragment 007 / 009 :: RGBD matching between frame : 730 and 735
Fragment 007 / 009 :: RGBD matching between frame : 730 and 740
Fragment 007 / 009 :: RGBD matching between frame : 730 and 745
Fragment 007 / 009 :: RGBD matching between frame : 730 and 750
Fragment 007 / 009 :: RGBD matching between frame : 730 and 755
Fragment 007 / 009 :: RGBD matching between frame : 730 and 760
Fragment 007 / 009 :: RGBD matching between frame : 730 and 765
Fragment 007 / 009 :: RGBD matching between frame : 730 and 770
Fragment 007 / 009 :: RGBD matching between frame : 730 and 775
Fragment 007 / 009 :: RGBD matching between frame : 730 and 780
Fragment 007 / 009 :: RGBD matching between frame : 730 and 785
Fragment 007 / 009 :: RGBD matching between frame : 730 and 790
Fragment 007 / 009 :: RGBD matching between frame : 730 and 795
Fragment 007 / 009 :: RGBD matching between frame : 731 and 732
Fragment 007 / 009 :: RGBD matching between frame : 732 and 733
Fragment 007 / 009 :: RGBD matching between frame : 733 and 734
Fragment 007 / 009 :: RGBD matching between frame : 734 and 735
Fragment 007 / 009 :: RGBD matching between frame : 735 and 736
Fragment 007 / 009 :: RGBD matching between frame : 735 and 740
Fragment 007 / 009 :: RGBD matching between frame : 735 and 745
Fragment 007 / 009 :: RGBD matching between frame : 735 and 750
Fragment 007 / 009 :: RGBD matching between frame : 735 and 755
Fragment 007 / 009 :: RGBD matching between frame : 735 and 760
Fragment 007 / 009 :: RGBD matching between frame : 735 and 765
Fragment 007 / 009 :: RGBD matching between frame : 735 and 770
Fragment 007 / 009 :: RGBD matching between frame : 735 and 775
Fragment 007 / 009 :: RGBD matching between frame : 735 and 780
Fragment 007 / 009 :: RGBD matching between frame : 735 and 785
Fragment 007 / 009 :: RGBD matching between frame : 735 and 790
Fragment 007 / 009 :: RGBD matching between frame : 735 and 795
Fragment 007 / 009 :: RGBD matching between frame : 736 and 737
Fragment 007 / 009 :: RGBD matching between frame : 737 and 738
Fragment 007 / 009 :: RGBD matching between frame : 738 and 739
Fragment 007 / 009 :: RGBD matching between frame : 739 and 740
Fragment 007 / 009 :: RGBD matching between frame : 740 and 741
Fragment 007 / 009 :: RGBD matching between frame : 740 and 745
Fragment 007 / 009 :: RGBD matching between frame : 740 and 750
Fragment 007 / 009 :: RGBD matching between frame : 740 and 755
Fragment 007 / 009 :: RGBD matching between frame : 740 and 760
Fragment 007 / 009 :: RGBD matching between frame : 740 and 765
Fragment 007 / 009 :: RGBD matching between frame : 740 and 770
Fragment 007 / 009 :: RGBD matching between frame : 740 and 775
Fragment 007 / 009 :: RGBD matching between frame : 740 and 780
Fragment 007 / 009 :: RGBD matching between frame : 740 and 785
Fragment 007 / 009 :: RGBD matching between frame : 740 and 790
Fragment 007 / 009 :: RGBD matching between frame : 740 and 795
Fragment 007 / 009 :: RGBD matching between frame : 741 and 742
Fragment 007 / 009 :: RGBD matching between frame : 742 and 743
Fragment 007 / 009 :: RGBD matching between frame : 743 and 744
Fragment 007 / 009 :: RGBD matching between frame : 744 and 745
Fragment 007 / 009 :: RGBD matching between frame : 745 and 746
Fragment 007 / 009 :: RGBD matching between frame : 745 and 750
Fragment 007 / 009 :: RGBD matching between frame : 745 and 755
Fragment 007 / 009 :: RGBD matching between frame : 745 and 760
Fragment 007 / 009 :: RGBD matching between frame : 745 and 765
Fragment 007 / 009 :: RGBD matching between frame : 745 and 770
Fragment 007 / 009 :: RGBD matching between frame : 745 and 775
Fragment 007 / 009 :: RGBD matching between frame : 745 and 780
Fragment 007 / 009 :: RGBD matching between frame : 745 and 785
Fragment 007 / 009 :: RGBD matching between frame : 745 and 790
Fragment 007 / 009 :: RGBD matching between frame : 745 and 795
Fragment 007 / 009 :: RGBD matching between frame : 746 and 747
Fragment 007 / 009 :: RGBD matching between frame : 747 and 748
Fragment 007 / 009 :: RGBD matching between frame : 748 and 749
Fragment 007 / 009 :: RGBD matching between frame : 749 and 750
Fragment 007 / 009 :: RGBD matching between frame : 750 and 751
Fragment 007 / 009 :: RGBD matching between frame : 750 and 755
Fragment 007 / 009 :: RGBD matching between frame : 750 and 760
Fragment 007 / 009 :: RGBD matching between frame : 750 and 765
Fragment 007 / 009 :: RGBD matching between frame : 750 and 770
Fragment 007 / 009 :: RGBD matching between frame : 750 and 775
Fragment 007 / 009 :: RGBD matching between frame : 750 and 780
Fragment 007 / 009 :: RGBD matching between frame : 750 and 785
Fragment 007 / 009 :: RGBD matching between frame : 750 and 790
Fragment 007 / 009 :: RGBD matching between frame : 750 and 795
Fragment 007 / 009 :: RGBD matching between frame : 751 and 752
Fragment 007 / 009 :: RGBD matching between frame : 752 and 753
Fragment 007 / 009 :: RGBD matching between frame : 753 and 754
Fragment 007 / 009 :: RGBD matching between frame : 754 and 755
Fragment 007 / 009 :: RGBD matching between frame : 755 and 756
Fragment 007 / 009 :: RGBD matching between frame : 755 and 760
Fragment 007 / 009 :: RGBD matching between frame : 755 and 765
Fragment 007 / 009 :: RGBD matching between frame : 755 and 770
Fragment 007 / 009 :: RGBD matching between frame : 755 and 775
Fragment 007 / 009 :: RGBD matching between frame : 755 and 780
Fragment 007 / 009 :: RGBD matching between frame : 755 and 785
Fragment 007 / 009 :: RGBD matching between frame : 755 and 790
Fragment 007 / 009 :: RGBD matching between frame : 755 and 795
Fragment 007 / 009 :: RGBD matching between frame : 756 and 757
Fragment 007 / 009 :: RGBD matching between frame : 757 and 758
Fragment 007 / 009 :: RGBD matching between frame : 758 and 759
Fragment 007 / 009 :: RGBD matching between frame : 759 and 760
Fragment 007 / 009 :: RGBD matching between frame : 760 and 761
Fragment 007 / 009 :: RGBD matching between frame : 760 and 765
Fragment 007 / 009 :: RGBD matching between frame : 760 and 770
Fragment 007 / 009 :: RGBD matching between frame : 760 and 775
Fragment 007 / 009 :: RGBD matching between frame : 760 and 780
Fragment 007 / 009 :: RGBD matching between frame : 760 and 785
Fragment 007 / 009 :: RGBD matching between frame : 760 and 790
Fragment 007 / 009 :: RGBD matching between frame : 760 and 795
Fragment 007 / 009 :: RGBD matching between frame : 761 and 762
Fragment 007 / 009 :: RGBD matching between frame : 762 and 763
Fragment 007 / 009 :: RGBD matching between frame : 763 and 764
Fragment 007 / 009 :: RGBD matching between frame : 764 and 765
Fragment 007 / 009 :: RGBD matching between frame : 765 and 766
Fragment 007 / 009 :: RGBD matching between frame : 765 and 770
Fragment 007 / 009 :: RGBD matching between frame : 765 and 775
Fragment 007 / 009 :: RGBD matching between frame : 765 and 780
Fragment 007 / 009 :: RGBD matching between frame : 765 and 785
Fragment 007 / 009 :: RGBD matching between frame : 765 and 790
Fragment 007 / 009 :: RGBD matching between frame : 765 and 795
Fragment 007 / 009 :: RGBD matching between frame : 766 and 767
Fragment 007 / 009 :: RGBD matching between frame : 767 and 768
Fragment 007 / 009 :: RGBD matching between frame : 768 and 769
Fragment 007 / 009 :: RGBD matching between frame : 769 and 770
Fragment 007 / 009 :: RGBD matching between frame : 770 and 771
Fragment 007 / 009 :: RGBD matching between frame : 770 and 775
Fragment 007 / 009 :: RGBD matching between frame : 770 and 780
Fragment 007 / 009 :: RGBD matching between frame : 770 and 785
Fragment 007 / 009 :: RGBD matching between frame : 770 and 790
Fragment 007 / 009 :: RGBD matching between frame : 770 and 795
Fragment 007 / 009 :: RGBD matching between frame : 771 and 772
Fragment 007 / 009 :: RGBD matching between frame : 772 and 773
Fragment 007 / 009 :: RGBD matching between frame : 773 and 774
Fragment 007 / 009 :: RGBD matching between frame : 774 and 775
Fragment 007 / 009 :: RGBD matching between frame : 775 and 776
Fragment 007 / 009 :: RGBD matching between frame : 775 and 780
Fragment 007 / 009 :: RGBD matching between frame : 775 and 785
Fragment 007 / 009 :: RGBD matching between frame : 775 and 790
Fragment 007 / 009 :: RGBD matching between frame : 775 and 795
Fragment 007 / 009 :: RGBD matching between frame : 776 and 777
Fragment 007 / 009 :: RGBD matching between frame : 777 and 778
Fragment 007 / 009 :: RGBD matching between frame : 778 and 779
Fragment 007 / 009 :: RGBD matching between frame : 779 and 780
Fragment 007 / 009 :: RGBD matching between frame : 780 and 781
Fragment 007 / 009 :: RGBD matching between frame : 780 and 785
Fragment 007 / 009 :: RGBD matching between frame : 780 and 790
Fragment 007 / 009 :: RGBD matching between frame : 780 and 795
Fragment 007 / 009 :: RGBD matching between frame : 781 and 782
Fragment 007 / 009 :: RGBD matching between frame : 782 and 783
Fragment 007 / 009 :: RGBD matching between frame : 783 and 784
Fragment 007 / 009 :: RGBD matching between frame : 784 and 785
Fragment 007 / 009 :: RGBD matching between frame : 785 and 786
Fragment 007 / 009 :: RGBD matching between frame : 785 and 790
Fragment 007 / 009 :: RGBD matching between frame : 785 and 795
Fragment 007 / 009 :: RGBD matching between frame : 786 and 787
Fragment 007 / 009 :: RGBD matching between frame : 787 and 788
Fragment 007 / 009 :: RGBD matching between frame : 788 and 789
Fragment 007 / 009 :: RGBD matching between frame : 789 and 790
Fragment 007 / 009 :: RGBD matching between frame : 790 and 791
Fragment 007 / 009 :: RGBD matching between frame : 790 and 795
Fragment 007 / 009 :: RGBD matching between frame : 791 and 792
Fragment 007 / 009 :: RGBD matching between frame : 792 and 793
Fragment 007 / 009 :: RGBD matching between frame : 793 and 794
Fragment 007 / 009 :: RGBD matching between frame : 794 and 795
Fragment 007 / 009 :: RGBD matching between frame : 795 and 796
Fragment 007 / 009 :: RGBD matching between frame : 796 and 797
Fragment 007 / 009 :: RGBD matching between frame : 797 and 798
Fragment 007 / 009 :: RGBD matching between frame : 798 and 799
Fragment 007 / 009 :: integrate rgbd frame 700 (1 of 100).
Fragment 007 / 009 :: integrate rgbd frame 701 (2 of 100).
Fragment 007 / 009 :: integrate rgbd frame 702 (3 of 100).
Fragment 007 / 009 :: integrate rgbd frame 703 (4 of 100).
Fragment 007 / 009 :: integrate rgbd frame 704 (5 of 100).
Fragment 007 / 009 :: integrate rgbd frame 705 (6 of 100).
Fragment 007 / 009 :: integrate rgbd frame 706 (7 of 100).
Fragment 007 / 009 :: integrate rgbd frame 707 (8 of 100).
Fragment 007 / 009 :: integrate rgbd frame 708 (9 of 100).
Fragment 007 / 009 :: integrate rgbd frame 709 (10 of 100).
Fragment 007 / 009 :: integrate rgbd frame 710 (11 of 100).
Fragment 007 / 009 :: integrate rgbd frame 711 (12 of 100).
Fragment 007 / 009 :: integrate rgbd frame 712 (13 of 100).
Fragment 007 / 009 :: integrate rgbd frame 713 (14 of 100).
Fragment 007 / 009 :: integrate rgbd frame 714 (15 of 100).
Fragment 007 / 009 :: integrate rgbd frame 715 (16 of 100).
Fragment 007 / 009 :: integrate rgbd frame 716 (17 of 100).
Fragment 007 / 009 :: integrate rgbd frame 717 (18 of 100).
Fragment 007 / 009 :: integrate rgbd frame 718 (19 of 100).
Fragment 007 / 009 :: integrate rgbd frame 719 (20 of 100).
Fragment 007 / 009 :: integrate rgbd frame 720 (21 of 100).
Fragment 007 / 009 :: integrate rgbd frame 721 (22 of 100).
Fragment 007 / 009 :: integrate rgbd frame 722 (23 of 100).
Fragment 007 / 009 :: integrate rgbd frame 723 (24 of 100).
Fragment 007 / 009 :: integrate rgbd frame 724 (25 of 100).
Fragment 007 / 009 :: integrate rgbd frame 725 (26 of 100).
Fragment 007 / 009 :: integrate rgbd frame 726 (27 of 100).
Fragment 007 / 009 :: integrate rgbd frame 727 (28 of 100).
Fragment 007 / 009 :: integrate rgbd frame 728 (29 of 100).
Fragment 007 / 009 :: integrate rgbd frame 729 (30 of 100).
Fragment 007 / 009 :: integrate rgbd frame 730 (31 of 100).
Fragment 007 / 009 :: integrate rgbd frame 731 (32 of 100).
Fragment 007 / 009 :: integrate rgbd frame 732 (33 of 100).
Fragment 007 / 009 :: integrate rgbd frame 733 (34 of 100).
Fragment 007 / 009 :: integrate rgbd frame 734 (35 of 100).
Fragment 007 / 009 :: integrate rgbd frame 735 (36 of 100).
Fragment 007 / 009 :: integrate rgbd frame 736 (37 of 100).
Fragment 007 / 009 :: integrate rgbd frame 737 (38 of 100).
Fragment 007 / 009 :: integrate rgbd frame 738 (39 of 100).
Fragment 007 / 009 :: integrate rgbd frame 739 (40 of 100).
Fragment 007 / 009 :: integrate rgbd frame 740 (41 of 100).
Fragment 007 / 009 :: integrate rgbd frame 741 (42 of 100).
Fragment 007 / 009 :: integrate rgbd frame 742 (43 of 100).
Fragment 007 / 009 :: integrate rgbd frame 743 (44 of 100).
Fragment 007 / 009 :: integrate rgbd frame 744 (45 of 100).
Fragment 007 / 009 :: integrate rgbd frame 745 (46 of 100).
Fragment 007 / 009 :: integrate rgbd frame 746 (47 of 100).
Fragment 007 / 009 :: integrate rgbd frame 747 (48 of 100).
Fragment 007 / 009 :: integrate rgbd frame 748 (49 of 100).
Fragment 007 / 009 :: integrate rgbd frame 749 (50 of 100).
Fragment 007 / 009 :: integrate rgbd frame 750 (51 of 100).
Fragment 007 / 009 :: integrate rgbd frame 751 (52 of 100).
Fragment 007 / 009 :: integrate rgbd frame 752 (53 of 100).
Fragment 007 / 009 :: integrate rgbd frame 753 (54 of 100).
Fragment 007 / 009 :: integrate rgbd frame 754 (55 of 100).
Fragment 007 / 009 :: integrate rgbd frame 755 (56 of 100).
Fragment 007 / 009 :: integrate rgbd frame 756 (57 of 100).
Fragment 007 / 009 :: integrate rgbd frame 757 (58 of 100).
Fragment 007 / 009 :: integrate rgbd frame 758 (59 of 100).
Fragment 007 / 009 :: integrate rgbd frame 759 (60 of 100).
Fragment 007 / 009 :: integrate rgbd frame 760 (61 of 100).
Fragment 007 / 009 :: integrate rgbd frame 761 (62 of 100).
Fragment 007 / 009 :: integrate rgbd frame 762 (63 of 100).
Fragment 007 / 009 :: integrate rgbd frame 763 (64 of 100).
Fragment 007 / 009 :: integrate rgbd frame 764 (65 of 100).
Fragment 007 / 009 :: integrate rgbd frame 765 (66 of 100).
Fragment 007 / 009 :: integrate rgbd frame 766 (67 of 100).
Fragment 007 / 009 :: integrate rgbd frame 767 (68 of 100).
Fragment 007 / 009 :: integrate rgbd frame 768 (69 of 100).
Fragment 007 / 009 :: integrate rgbd frame 769 (70 of 100).
Fragment 007 / 009 :: integrate rgbd frame 770 (71 of 100).
Fragment 007 / 009 :: integrate rgbd frame 771 (72 of 100).
Fragment 007 / 009 :: integrate rgbd frame 772 (73 of 100).
Fragment 007 / 009 :: integrate rgbd frame 773 (74 of 100).
Fragment 007 / 009 :: integrate rgbd frame 774 (75 of 100).
Fragment 007 / 009 :: integrate rgbd frame 775 (76 of 100).
Fragment 007 / 009 :: integrate rgbd frame 776 (77 of 100).
Fragment 007 / 009 :: integrate rgbd frame 777 (78 of 100).
Fragment 007 / 009 :: integrate rgbd frame 778 (79 of 100).
Fragment 007 / 009 :: integrate rgbd frame 779 (80 of 100).
Fragment 007 / 009 :: integrate rgbd frame 780 (81 of 100).
Fragment 007 / 009 :: integrate rgbd frame 781 (82 of 100).
Fragment 007 / 009 :: integrate rgbd frame 782 (83 of 100).
Fragment 007 / 009 :: integrate rgbd frame 783 (84 of 100).
Fragment 007 / 009 :: integrate rgbd frame 784 (85 of 100).
Fragment 007 / 009 :: integrate rgbd frame 785 (86 of 100).
Fragment 007 / 009 :: integrate rgbd frame 786 (87 of 100).
Fragment 007 / 009 :: integrate rgbd frame 787 (88 of 100).
Fragment 007 / 009 :: integrate rgbd frame 788 (89 of 100).
Fragment 007 / 009 :: integrate rgbd frame 789 (90 of 100).
Fragment 007 / 009 :: integrate rgbd frame 790 (91 of 100).
Fragment 007 / 009 :: integrate rgbd frame 791 (92 of 100).
Fragment 007 / 009 :: integrate rgbd frame 792 (93 of 100).
Fragment 007 / 009 :: integrate rgbd frame 793 (94 of 100).
Fragment 007 / 009 :: integrate rgbd frame 794 (95 of 100).
Fragment 007 / 009 :: integrate rgbd frame 795 (96 of 100).
Fragment 007 / 009 :: integrate rgbd frame 796 (97 of 100).
Fragment 007 / 009 :: integrate rgbd frame 797 (98 of 100).
Fragment 007 / 009 :: integrate rgbd frame 798 (99 of 100).
Fragment 007 / 009 :: integrate rgbd frame 799 (100 of 100).
Fragment 008 / 009 :: RGBD matching between frame : 800 and 801
Fragment 008 / 009 :: RGBD matching between frame : 800 and 805
Fragment 008 / 009 :: RGBD matching between frame : 800 and 810
Fragment 008 / 009 :: RGBD matching between frame : 800 and 815
Fragment 008 / 009 :: RGBD matching between frame : 800 and 820
Fragment 008 / 009 :: RGBD matching between frame : 800 and 825
Fragment 008 / 009 :: RGBD matching between frame : 800 and 830
Fragment 008 / 009 :: RGBD matching between frame : 800 and 835
Fragment 008 / 009 :: RGBD matching between frame : 800 and 840
Fragment 008 / 009 :: RGBD matching between frame : 800 and 845
Fragment 008 / 009 :: RGBD matching between frame : 800 and 850
Fragment 008 / 009 :: RGBD matching between frame : 800 and 855
Fragment 008 / 009 :: RGBD matching between frame : 800 and 860
Fragment 008 / 009 :: RGBD matching between frame : 800 and 865
Fragment 008 / 009 :: RGBD matching between frame : 800 and 870
Fragment 008 / 009 :: RGBD matching between frame : 800 and 875
Fragment 008 / 009 :: RGBD matching between frame : 800 and 880
Fragment 008 / 009 :: RGBD matching between frame : 800 and 885
Fragment 008 / 009 :: RGBD matching between frame : 800 and 890
Fragment 008 / 009 :: RGBD matching between frame : 800 and 895
Fragment 008 / 009 :: RGBD matching between frame : 801 and 802
Fragment 008 / 009 :: RGBD matching between frame : 802 and 803
Fragment 008 / 009 :: RGBD matching between frame : 803 and 804
Fragment 008 / 009 :: RGBD matching between frame : 804 and 805
Fragment 008 / 009 :: RGBD matching between frame : 805 and 806
Fragment 008 / 009 :: RGBD matching between frame : 805 and 810
Fragment 008 / 009 :: RGBD matching between frame : 805 and 815
Fragment 008 / 009 :: RGBD matching between frame : 805 and 820
Fragment 008 / 009 :: RGBD matching between frame : 805 and 825
Fragment 008 / 009 :: RGBD matching between frame : 805 and 830
Fragment 008 / 009 :: RGBD matching between frame : 805 and 835
Fragment 008 / 009 :: RGBD matching between frame : 805 and 840
Fragment 008 / 009 :: RGBD matching between frame : 805 and 845
Fragment 008 / 009 :: RGBD matching between frame : 805 and 850
Fragment 008 / 009 :: RGBD matching between frame : 805 and 855
Fragment 008 / 009 :: RGBD matching between frame : 805 and 860
Fragment 008 / 009 :: RGBD matching between frame : 805 and 865
Fragment 008 / 009 :: RGBD matching between frame : 805 and 870
Fragment 008 / 009 :: RGBD matching between frame : 805 and 875
Fragment 008 / 009 :: RGBD matching between frame : 805 and 880
Fragment 008 / 009 :: RGBD matching between frame : 805 and 885
Fragment 008 / 009 :: RGBD matching between frame : 805 and 890
Fragment 008 / 009 :: RGBD matching between frame : 805 and 895
Fragment 008 / 009 :: RGBD matching between frame : 806 and 807
Fragment 008 / 009 :: RGBD matching between frame : 807 and 808
Fragment 008 / 009 :: RGBD matching between frame : 808 and 809
Fragment 008 / 009 :: RGBD matching between frame : 809 and 810
Fragment 008 / 009 :: RGBD matching between frame : 810 and 811
Fragment 008 / 009 :: RGBD matching between frame : 810 and 815
Fragment 008 / 009 :: RGBD matching between frame : 810 and 820
Fragment 008 / 009 :: RGBD matching between frame : 810 and 825
Fragment 008 / 009 :: RGBD matching between frame : 810 and 830
Fragment 008 / 009 :: RGBD matching between frame : 810 and 835
Fragment 008 / 009 :: RGBD matching between frame : 810 and 840
Fragment 008 / 009 :: RGBD matching between frame : 810 and 845
Fragment 008 / 009 :: RGBD matching between frame : 810 and 850
Fragment 008 / 009 :: RGBD matching between frame : 810 and 855
Fragment 008 / 009 :: RGBD matching between frame : 810 and 860
Fragment 008 / 009 :: RGBD matching between frame : 810 and 865
Fragment 008 / 009 :: RGBD matching between frame : 810 and 870
Fragment 008 / 009 :: RGBD matching between frame : 810 and 875
Fragment 008 / 009 :: RGBD matching between frame : 810 and 880
Fragment 008 / 009 :: RGBD matching between frame : 810 and 885
Fragment 008 / 009 :: RGBD matching between frame : 810 and 890
Fragment 008 / 009 :: RGBD matching between frame : 810 and 895
Fragment 008 / 009 :: RGBD matching between frame : 811 and 812
Fragment 008 / 009 :: RGBD matching between frame : 812 and 813
Fragment 008 / 009 :: RGBD matching between frame : 813 and 814
Fragment 008 / 009 :: RGBD matching between frame : 814 and 815
Fragment 008 / 009 :: RGBD matching between frame : 815 and 816
Fragment 008 / 009 :: RGBD matching between frame : 815 and 820
Fragment 008 / 009 :: RGBD matching between frame : 815 and 825
Fragment 008 / 009 :: RGBD matching between frame : 815 and 830
Fragment 008 / 009 :: RGBD matching between frame : 815 and 835
Fragment 008 / 009 :: RGBD matching between frame : 815 and 840
Fragment 008 / 009 :: RGBD matching between frame : 815 and 845
Fragment 008 / 009 :: RGBD matching between frame : 815 and 850
Fragment 008 / 009 :: RGBD matching between frame : 815 and 855
Fragment 008 / 009 :: RGBD matching between frame : 815 and 860
Fragment 008 / 009 :: RGBD matching between frame : 815 and 865
Fragment 008 / 009 :: RGBD matching between frame : 815 and 870
Fragment 008 / 009 :: RGBD matching between frame : 815 and 875
Fragment 008 / 009 :: RGBD matching between frame : 815 and 880
Fragment 008 / 009 :: RGBD matching between frame : 815 and 885
Fragment 008 / 009 :: RGBD matching between frame : 815 and 890
Fragment 008 / 009 :: RGBD matching between frame : 815 and 895
Fragment 008 / 009 :: RGBD matching between frame : 816 and 817
Fragment 008 / 009 :: RGBD matching between frame : 817 and 818
Fragment 008 / 009 :: RGBD matching between frame : 818 and 819
Fragment 008 / 009 :: RGBD matching between frame : 819 and 820
Fragment 008 / 009 :: RGBD matching between frame : 820 and 821
Fragment 008 / 009 :: RGBD matching between frame : 820 and 825
Fragment 008 / 009 :: RGBD matching between frame : 820 and 830
Fragment 008 / 009 :: RGBD matching between frame : 820 and 835
Fragment 008 / 009 :: RGBD matching between frame : 820 and 840
Fragment 008 / 009 :: RGBD matching between frame : 820 and 845
Fragment 008 / 009 :: RGBD matching between frame : 820 and 850
Fragment 008 / 009 :: RGBD matching between frame : 820 and 855
Fragment 008 / 009 :: RGBD matching between frame : 820 and 860
Fragment 008 / 009 :: RGBD matching between frame : 820 and 865
Fragment 008 / 009 :: RGBD matching between frame : 820 and 870
Fragment 008 / 009 :: RGBD matching between frame : 820 and 875
Fragment 008 / 009 :: RGBD matching between frame : 820 and 880
Fragment 008 / 009 :: RGBD matching between frame : 820 and 885
Fragment 008 / 009 :: RGBD matching between frame : 820 and 890
Fragment 008 / 009 :: RGBD matching between frame : 820 and 895
Fragment 008 / 009 :: RGBD matching between frame : 821 and 822
Fragment 008 / 009 :: RGBD matching between frame : 822 and 823
Fragment 008 / 009 :: RGBD matching between frame : 823 and 824
Fragment 008 / 009 :: RGBD matching between frame : 824 and 825
Fragment 008 / 009 :: RGBD matching between frame : 825 and 826
Fragment 008 / 009 :: RGBD matching between frame : 825 and 830
Fragment 008 / 009 :: RGBD matching between frame : 825 and 835
Fragment 008 / 009 :: RGBD matching between frame : 825 and 840
Fragment 008 / 009 :: RGBD matching between frame : 825 and 845
Fragment 008 / 009 :: RGBD matching between frame : 825 and 850
Fragment 008 / 009 :: RGBD matching between frame : 825 and 855
Fragment 008 / 009 :: RGBD matching between frame : 825 and 860
Fragment 008 / 009 :: RGBD matching between frame : 825 and 865
Fragment 008 / 009 :: RGBD matching between frame : 825 and 870
Fragment 008 / 009 :: RGBD matching between frame : 825 and 875
Fragment 008 / 009 :: RGBD matching between frame : 825 and 880
Fragment 008 / 009 :: RGBD matching between frame : 825 and 885
Fragment 008 / 009 :: RGBD matching between frame : 825 and 890
Fragment 008 / 009 :: RGBD matching between frame : 825 and 895
Fragment 008 / 009 :: RGBD matching between frame : 826 and 827
Fragment 008 / 009 :: RGBD matching between frame : 827 and 828
Fragment 008 / 009 :: RGBD matching between frame : 828 and 829
Fragment 008 / 009 :: RGBD matching between frame : 829 and 830
Fragment 008 / 009 :: RGBD matching between frame : 830 and 831
Fragment 008 / 009 :: RGBD matching between frame : 830 and 835
Fragment 008 / 009 :: RGBD matching between frame : 830 and 840
Fragment 008 / 009 :: RGBD matching between frame : 830 and 845
Fragment 008 / 009 :: RGBD matching between frame : 830 and 850
Fragment 008 / 009 :: RGBD matching between frame : 830 and 855
Fragment 008 / 009 :: RGBD matching between frame : 830 and 860
Fragment 008 / 009 :: RGBD matching between frame : 830 and 865
Fragment 008 / 009 :: RGBD matching between frame : 830 and 870
Fragment 008 / 009 :: RGBD matching between frame : 830 and 875
Fragment 008 / 009 :: RGBD matching between frame : 830 and 880
Fragment 008 / 009 :: RGBD matching between frame : 830 and 885
Fragment 008 / 009 :: RGBD matching between frame : 830 and 890
Fragment 008 / 009 :: RGBD matching between frame : 830 and 895
Fragment 008 / 009 :: RGBD matching between frame : 831 and 832
Fragment 008 / 009 :: RGBD matching between frame : 832 and 833
Fragment 008 / 009 :: RGBD matching between frame : 833 and 834
Fragment 008 / 009 :: RGBD matching between frame : 834 and 835
Fragment 008 / 009 :: RGBD matching between frame : 835 and 836
Fragment 008 / 009 :: RGBD matching between frame : 835 and 840
Fragment 008 / 009 :: RGBD matching between frame : 835 and 845
Fragment 008 / 009 :: RGBD matching between frame : 835 and 850
Fragment 008 / 009 :: RGBD matching between frame : 835 and 855
Fragment 008 / 009 :: RGBD matching between frame : 835 and 860
Fragment 008 / 009 :: RGBD matching between frame : 835 and 865
Fragment 008 / 009 :: RGBD matching between frame : 835 and 870
Fragment 008 / 009 :: RGBD matching between frame : 835 and 875
Fragment 008 / 009 :: RGBD matching between frame : 835 and 880
Fragment 008 / 009 :: RGBD matching between frame : 835 and 885
Fragment 008 / 009 :: RGBD matching between frame : 835 and 890
Fragment 008 / 009 :: RGBD matching between frame : 835 and 895
Fragment 008 / 009 :: RGBD matching between frame : 836 and 837
Fragment 008 / 009 :: RGBD matching between frame : 837 and 838
Fragment 008 / 009 :: RGBD matching between frame : 838 and 839
Fragment 008 / 009 :: RGBD matching between frame : 839 and 840
Fragment 008 / 009 :: RGBD matching between frame : 840 and 841
Fragment 008 / 009 :: RGBD matching between frame : 840 and 845
Fragment 008 / 009 :: RGBD matching between frame : 840 and 850
Fragment 008 / 009 :: RGBD matching between frame : 840 and 855
Fragment 008 / 009 :: RGBD matching between frame : 840 and 860
Fragment 008 / 009 :: RGBD matching between frame : 840 and 865
Fragment 008 / 009 :: RGBD matching between frame : 840 and 870
Fragment 008 / 009 :: RGBD matching between frame : 840 and 875
Fragment 008 / 009 :: RGBD matching between frame : 840 and 880
Fragment 008 / 009 :: RGBD matching between frame : 840 and 885
Fragment 008 / 009 :: RGBD matching between frame : 840 and 890
Fragment 008 / 009 :: RGBD matching between frame : 840 and 895
Fragment 008 / 009 :: RGBD matching between frame : 841 and 842
Fragment 008 / 009 :: RGBD matching between frame : 842 and 843
Fragment 008 / 009 :: RGBD matching between frame : 843 and 844
Fragment 008 / 009 :: RGBD matching between frame : 844 and 845
Fragment 008 / 009 :: RGBD matching between frame : 845 and 846
Fragment 008 / 009 :: RGBD matching between frame : 845 and 850
Fragment 008 / 009 :: RGBD matching between frame : 845 and 855
Fragment 008 / 009 :: RGBD matching between frame : 845 and 860
Fragment 008 / 009 :: RGBD matching between frame : 845 and 865
Fragment 008 / 009 :: RGBD matching between frame : 845 and 870
Fragment 008 / 009 :: RGBD matching between frame : 845 and 875
Fragment 008 / 009 :: RGBD matching between frame : 845 and 880
Fragment 008 / 009 :: RGBD matching between frame : 845 and 885
Fragment 008 / 009 :: RGBD matching between frame : 845 and 890
Fragment 008 / 009 :: RGBD matching between frame : 845 and 895
Fragment 008 / 009 :: RGBD matching between frame : 846 and 847
Fragment 008 / 009 :: RGBD matching between frame : 847 and 848
Fragment 008 / 009 :: RGBD matching between frame : 848 and 849
Fragment 008 / 009 :: RGBD matching between frame : 849 and 850
Fragment 008 / 009 :: RGBD matching between frame : 850 and 851
Fragment 008 / 009 :: RGBD matching between frame : 850 and 855
Fragment 008 / 009 :: RGBD matching between frame : 850 and 860
Fragment 008 / 009 :: RGBD matching between frame : 850 and 865
Fragment 008 / 009 :: RGBD matching between frame : 850 and 870
Fragment 008 / 009 :: RGBD matching between frame : 850 and 875
Fragment 008 / 009 :: RGBD matching between frame : 850 and 880
Fragment 008 / 009 :: RGBD matching between frame : 850 and 885
Fragment 008 / 009 :: RGBD matching between frame : 850 and 890
Fragment 008 / 009 :: RGBD matching between frame : 850 and 895
Fragment 008 / 009 :: RGBD matching between frame : 851 and 852
Fragment 008 / 009 :: RGBD matching between frame : 852 and 853
Fragment 008 / 009 :: RGBD matching between frame : 853 and 854
Fragment 008 / 009 :: RGBD matching between frame : 854 and 855
Fragment 008 / 009 :: RGBD matching between frame : 855 and 856
Fragment 008 / 009 :: RGBD matching between frame : 855 and 860
Fragment 008 / 009 :: RGBD matching between frame : 855 and 865
Fragment 008 / 009 :: RGBD matching between frame : 855 and 870
Fragment 008 / 009 :: RGBD matching between frame : 855 and 875
Fragment 008 / 009 :: RGBD matching between frame : 855 and 880
Fragment 008 / 009 :: RGBD matching between frame : 855 and 885
Fragment 008 / 009 :: RGBD matching between frame : 855 and 890
Fragment 008 / 009 :: RGBD matching between frame : 855 and 895
Fragment 008 / 009 :: RGBD matching between frame : 856 and 857
Fragment 008 / 009 :: RGBD matching between frame : 857 and 858
Fragment 008 / 009 :: RGBD matching between frame : 858 and 859
Fragment 008 / 009 :: RGBD matching between frame : 859 and 860
Fragment 008 / 009 :: RGBD matching between frame : 860 and 861
Fragment 008 / 009 :: RGBD matching between frame : 860 and 865
Fragment 008 / 009 :: RGBD matching between frame : 860 and 870
Fragment 008 / 009 :: RGBD matching between frame : 860 and 875
Fragment 008 / 009 :: RGBD matching between frame : 860 and 880
Fragment 008 / 009 :: RGBD matching between frame : 860 and 885
Fragment 008 / 009 :: RGBD matching between frame : 860 and 890
Fragment 008 / 009 :: RGBD matching between frame : 860 and 895
Fragment 008 / 009 :: RGBD matching between frame : 861 and 862
Fragment 008 / 009 :: RGBD matching between frame : 862 and 863
Fragment 008 / 009 :: RGBD matching between frame : 863 and 864
Fragment 008 / 009 :: RGBD matching between frame : 864 and 865
Fragment 008 / 009 :: RGBD matching between frame : 865 and 866
Fragment 008 / 009 :: RGBD matching between frame : 865 and 870
Fragment 008 / 009 :: RGBD matching between frame : 865 and 875
Fragment 008 / 009 :: RGBD matching between frame : 865 and 880
Fragment 008 / 009 :: RGBD matching between frame : 865 and 885
Fragment 008 / 009 :: RGBD matching between frame : 865 and 890
Fragment 008 / 009 :: RGBD matching between frame : 865 and 895
Fragment 008 / 009 :: RGBD matching between frame : 866 and 867
Fragment 008 / 009 :: RGBD matching between frame : 867 and 868
Fragment 008 / 009 :: RGBD matching between frame : 868 and 869
Fragment 008 / 009 :: RGBD matching between frame : 869 and 870
Fragment 008 / 009 :: RGBD matching between frame : 870 and 871
Fragment 008 / 009 :: RGBD matching between frame : 870 and 875
Fragment 008 / 009 :: RGBD matching between frame : 870 and 880
Fragment 008 / 009 :: RGBD matching between frame : 870 and 885
Fragment 008 / 009 :: RGBD matching between frame : 870 and 890
Fragment 008 / 009 :: RGBD matching between frame : 870 and 895
Fragment 008 / 009 :: RGBD matching between frame : 871 and 872
Fragment 008 / 009 :: RGBD matching between frame : 872 and 873
Fragment 008 / 009 :: RGBD matching between frame : 873 and 874
Fragment 008 / 009 :: RGBD matching between frame : 874 and 875
Fragment 008 / 009 :: RGBD matching between frame : 875 and 876
Fragment 008 / 009 :: RGBD matching between frame : 875 and 880
Fragment 008 / 009 :: RGBD matching between frame : 875 and 885
Fragment 008 / 009 :: RGBD matching between frame : 875 and 890
Fragment 008 / 009 :: RGBD matching between frame : 875 and 895
Fragment 008 / 009 :: RGBD matching between frame : 876 and 877t_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.026 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 259 edges.
[Open3D DEBUG] Line process weight : 70.780375
[Open3D DEBUG] [Initial     ] residual : 2.865817e+02, lambda : 2.775940e+01
[Open3D DEBUG] [Iteration 00] residual : 2.856153e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 2.855477e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 2.855351e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 03] residual : 2.855311e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 04] residual : 2.855297e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] [Iteration 05] residual : 2.855292e+02, valid edges : 160, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.009 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 289 edges.
[Open3D DEBUG] Line process weight : 65.702588
[Open3D DEBUG] [Initial     ] residual : 2.061259e+02, lambda : 2.762859e+01
[Open3D DEBUG] [Iteration 00] residual : 2.351869e+01, valid edges : 190, time : 0.002 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.932616e+01, valid edges : 190, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.932533e+01, valid edges : 190, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.006 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 289 edges.
[Open3D DEBUG] Line process weight : 65.702588
[Open3D DEBUG] [Initial     ] residual : 1.932533e+01, lambda : 2.823950e+01
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.001 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 289 edges.
[Open3D DEBUG] Line process weight : 57.225272
[Open3D DEBUG] [Initial     ] residual : 7.296191e+02, lambda : 2.435130e+01
[Open3D DEBUG] [Iteration 00] residual : 3.473220e+02, valid edges : 185, time : 0.002 sec.
[Open3D DEBUG] [Iteration 01] residual : 3.456611e+02, valid edges : 185, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 3.456437e+02, valid edges : 185, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.005 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 100 nodes and 284 edges.
[Open3D DEBUG] Line process weight : 57.390139
[Open3D DEBUG] [Initial     ] residual : 1.878477e+02, lambda : 2.449058e+01
[Open3D DEBUG] [Iteration 00] residual : 1.848482e+02, valid edges : 185, time : 0.001 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.847259e+02, valid edges : 185, time : 0.001 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.847251e+02, valid edges : 185, time : 0.001 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.005 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 5 nodes and 4 edges.
[Open3D DEBUG] Line process weight : 60.575638
[Open3D DEBUG] [Initial     ] residual : 4.442189e-31, lambda : 2.492250e+00
[Open3D DEBUG] Maximum coefficient of right term < 1.000000e-06
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 5 nodes and 4 edges.
[Open3D DEBUG] Line process weight : 60.575638
[Open3D DEBUG] [Initial     ] residual : 4.442189e-31, lamb
Fragment 008 / 009 :: RGBD matching between frame : 877 and 878
Fragment 008 / 009 :: RGBD matching between frame : 878 and 879
Fragment 008 / 009 :: RGBD matching between frame : 879 and 880
Fragment 008 / 009 :: RGBD matching between frame : 880 and 881
Fragment 008 / 009 :: RGBD matching between frame : 880 and 885
Fragment 008 / 009 :: RGBD matching between frame : 880 and 890
Fragment 008 / 009 :: RGBD matching between frame : 880 and 895
Fragment 008 / 009 :: RGBD matching between frame : 881 and 882
Fragment 008 / 009 :: RGBD matching between frame : 882 and 883
Fragment 008 / 009 :: RGBD matching between frame : 883 and 884
Fragment 008 / 009 :: RGBD matching between frame : 884 and 885
Fragment 008 / 009 :: RGBD matching between frame : 885 and 886
Fragment 008 / 009 :: RGBD matching between frame : 885 and 890
Fragment 008 / 009 :: RGBD matching between frame : 885 and 895
Fragment 008 / 009 :: RGBD matching between frame : 886 and 887
Fragment 008 / 009 :: RGBD matching between frame : 887 and 888
Fragment 008 / 009 :: RGBD matching between frame : 888 and 889
Fragment 008 / 009 :: RGBD matching between frame : 889 and 890
Fragment 008 / 009 :: RGBD matching between frame : 890 and 891
Fragment 008 / 009 :: RGBD matching between frame : 890 and 895
Fragment 008 / 009 :: RGBD matching between frame : 891 and 892
Fragment 008 / 009 :: RGBD matching between frame : 892 and 893
Fragment 008 / 009 :: RGBD matching between frame : 893 and 894
Fragment 008 / 009 :: RGBD matching between frame : 894 and 895
Fragment 008 / 009 :: RGBD matching between frame : 895 and 896
Fragment 008 / 009 :: RGBD matching between frame : 896 and 897
Fragment 008 / 009 :: RGBD matching between frame : 897 and 898
Fragment 008 / 009 :: RGBD matching between frame : 898 and 899
Fragment 008 / 009 :: integrate rgbd frame 800 (1 of 100).
Fragment 008 / 009 :: integrate rgbd frame 801 (2 of 100).
Fragment 008 / 009 :: integrate rgbd frame 802 (3 of 100).
Fragment 008 / 009 :: integrate rgbd frame 803 (4 of 100).
Fragment 008 / 009 :: integrate rgbd frame 804 (5 of 100).
Fragment 008 / 009 :: integrate rgbd frame 805 (6 of 100).
Fragment 008 / 009 :: integrate rgbd frame 806 (7 of 100).
Fragment 008 / 009 :: integrate rgbd frame 807 (8 of 100).
Fragment 008 / 009 :: integrate rgbd frame 808 (9 of 100).
Fragment 008 / 009 :: integrate rgbd frame 809 (10 of 100).
Fragment 008 / 009 :: integrate rgbd frame 810 (11 of 100).
Fragment 008 / 009 :: integrate rgbd frame 811 (12 of 100).
Fragment 008 / 009 :: integrate rgbd frame 812 (13 of 100).
Fragment 008 / 009 :: integrate rgbd frame 813 (14 of 100).
Fragment 008 / 009 :: integrate rgbd frame 814 (15 of 100).
Fragment 008 / 009 :: integrate rgbd frame 815 (16 of 100).
Fragment 008 / 009 :: integrate rgbd frame 816 (17 of 100).
Fragment 008 / 009 :: integrate rgbd frame 817 (18 of 100).
Fragment 008 / 009 :: integrate rgbd frame 818 (19 of 100).
Fragment 008 / 009 :: integrate rgbd frame 819 (20 of 100).
Fragment 008 / 009 :: integrate rgbd frame 820 (21 of 100).
Fragment 008 / 009 :: integrate rgbd frame 821 (22 of 100).
Fragment 008 / 009 :: integrate rgbd frame 822 (23 of 100).
Fragment 008 / 009 :: integrate rgbd frame 823 (24 of 100).
Fragment 008 / 009 :: integrate rgbd frame 824 (25 of 100).
Fragment 008 / 009 :: integrate rgbd frame 825 (26 of 100).
Fragment 008 / 009 :: integrate rgbd frame 826 (27 of 100).
Fragment 008 / 009 :: integrate rgbd frame 827 (28 of 100).
Fragment 008 / 009 :: integrate rgbd frame 828 (29 of 100).
Fragment 008 / 009 :: integrate rgbd frame 829 (30 of 100).
Fragment 008 / 009 :: integrate rgbd frame 830 (31 of 100).
Fragment 008 / 009 :: integrate rgbd frame 831 (32 of 100).
Fragment 008 / 009 :: integrate rgbd frame 832 (33 of 100).
Fragment 008 / 009 :: integrate rgbd frame 833 (34 of 100).
Fragment 008 / 009 :: integrate rgbd frame 834 (35 of 100).
Fragment 008 / 009 :: integrate rgbd frame 835 (36 of 100).
Fragment 008 / 009 :: integrate rgbd frame 836 (37 of 100).
Fragment 008 / 009 :: integrate rgbd frame 837 (38 of 100).
Fragment 008 / 009 :: integrate rgbd frame 838 (39 of 100).
Fragment 008 / 009 :: integrate rgbd frame 839 (40 of 100).
Fragment 008 / 009 :: integrate rgbd frame 840 (41 of 100).
Fragment 008 / 009 :: integrate rgbd frame 841 (42 of 100).
Fragment 008 / 009 :: integrate rgbd frame 842 (43 of 100).
Fragment 008 / 009 :: integrate rgbd frame 843 (44 of 100).
Fragment 008 / 009 :: integrate rgbd frame 844 (45 of 100).
Fragment 008 / 009 :: integrate rgbd frame 845 (46 of 100).
Fragment 008 / 009 :: integrate rgbd frame 846 (47 of 100).
Fragment 008 / 009 :: integrate rgbd frame 847 (48 of 100).
Fragment 008 / 009 :: integrate rgbd frame 848 (49 of 100).
Fragment 008 / 009 :: integrate rgbd frame 849 (50 of 100).
Fragment 008 / 009 :: integrate rgbd frame 850 (51 of 100).
Fragment 008 / 009 :: integrate rgbd frame 851 (52 of 100).
Fragment 008 / 009 :: integrate rgbd frame 852 (53 of 100).
Fragment 008 / 009 :: integrate rgbd frame 853 (54 of 100).
Fragment 008 / 009 :: integrate rgbd frame 854 (55 of 100).
Fragment 008 / 009 :: integrate rgbd frame 855 (56 of 100).
Fragment 008 / 009 :: integrate rgbd frame 856 (57 of 100).
Fragment 008 / 009 :: integrate rgbd frame 857 (58 of 100).
Fragment 008 / 009 :: integrate rgbd frame 858 (59 of 100).
Fragment 008 / 009 :: integrate rgbd frame 859 (60 of 100).
Fragment 008 / 009 :: integrate rgbd frame 860 (61 of 100).
Fragment 008 / 009 :: integrate rgbd frame 861 (62 of 100).
Fragment 008 / 009 :: integrate rgbd frame 862 (63 of 100).
Fragment 008 / 009 :: integrate rgbd frame 863 (64 of 100).
Fragment 008 / 009 :: integrate rgbd frame 864 (65 of 100).
Fragment 008 / 009 :: integrate rgbd frame 865 (66 of 100).
Fragment 008 / 009 :: integrate rgbd frame 866 (67 of 100).
Fragment 008 / 009 :: integrate rgbd frame 867 (68 of 100).
Fragment 008 / 009 :: integrate rgbd frame 868 (69 of 100).
Fragment 008 / 009 :: integrate rgbd frame 869 (70 of 100).
Fragment 008 / 009 :: integrate rgbd frame 870 (71 of 100).
Fragment 008 / 009 :: integrate rgbd frame 871 (72 of 100).
Fragment 008 / 009 :: integrate rgbd frame 872 (73 of 100).
Fragment 008 / 009 :: integrate rgbd frame 873 (74 of 100).
Fragment 008 / 009 :: integrate rgbd frame 874 (75 of 100).
Fragment 008 / 009 :: integrate rgbd frame 875 (76 of 100).
Fragment 008 / 009 :: integrate rgbd frame 876 (77 of 100).
Fragment 008 / 009 :: integrate rgbd frame 877 (78 of 100).
Fragment 008 / 009 :: integrate rgbd frame 878 (79 of 100).
Fragment 008 / 009 :: integrate rgbd frame 879 (80 of 100).
Fragment 008 / 009 :: integrate rgbd frame 880 (81 of 100).
Fragment 008 / 009 :: integrate rgbd frame 881 (82 of 100).
Fragment 008 / 009 :: integrate rgbd frame 882 (83 of 100).
Fragment 008 / 009 :: integrate rgbd frame 883 (84 of 100).
Fragment 008 / 009 :: integrate rgbd frame 884 (85 of 100).
Fragment 008 / 009 :: integrate rgbd frame 885 (86 of 100).
Fragment 008 / 009 :: integrate rgbd frame 886 (87 of 100).
Fragment 008 / 009 :: integrate rgbd frame 887 (88 of 100).
Fragment 008 / 009 :: integrate rgbd frame 888 (89 of 100).
Fragment 008 / 009 :: integrate rgbd frame 889 (90 of 100).
Fragment 008 / 009 :: integrate rgbd frame 890 (91 of 100).
Fragment 008 / 009 :: integrate rgbd frame 891 (92 of 100).
Fragment 008 / 009 :: integrate rgbd frame 892 (93 of 100).
Fragment 008 / 009 :: integrate rgbd frame 893 (94 of 100).
Fragment 008 / 009 :: integrate rgbd frame 894 (95 of 100).
Fragment 008 / 009 :: integrate rgbd frame 895 (96 of 100).
Fragment 008 / 009 :: integrate rgbd frame 896 (97 of 100).
Fragment 008 / 009 :: integrate rgbd frame 897 (98 of 100).
Fragment 008 / 009 :: integrate rgbd frame 898 (99 of 100).
Fragment 008 / 009 :: integrate rgbd frame 899 (100 of 100).
Fragment 009 / 009 :: RGBD matching between frame : 900 and 901
Fragment 009 / 009 :: RGBD matching between frame : 901 and 902
Fragment 009 / 009 :: RGBD matching between frame : 902 and 903
Fragment 009 / 009 :: RGBD matching between frame : 903 and 904
Fragment 009 / 009 :: integrate rgbd frame 900 (1 of 5).
Fragment 009 / 009 :: integrate rgbd frame 901 (2 of 5).
Fragment 009 / 009 :: integrate rgbd frame 902 (3 of 5).da : 2.492250e+00
[Open3D DEBUG] Maximum coefficient of right term < 1.000000e-06
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 366 points to 240 points.
[Open3D DEBUG] Pointcloud down sampled from 396 points to 312 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7000, RMSE 0.0224
[Open3D DEBUG] Residual : 3.03e-04 (# of elements : 168)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6917, RMSE 0.0220
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 3.02e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.6917, RMSE 0.0226
[Open3D DEBUG] Residual : 3.01e-04 (# of elements : 166)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.6917, RMSE 0.0224
[Open3D DEBUG] Residual : 2.78e-04 (# of elements : 166)
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] total_validation : 500
[Open3D DEBUG] RANSAC: Fitness 1.0000, RMSE 0.0201
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] total_validation : 303
[Open3D DEBUG] RANSAC: Fitness 0.8770, RMSE 0.0322
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] total_validation : 218
[Open3D DEBUG] RANSAC: Fitness 0.6776, RMSE 0.0387
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] total_validation : 304
[Open3D DEBUG] RANSAC: Fitness 0.8197, RMSE 0.0396
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] total_validation : 357
[Open3D DEBUG] RANSAC: Fitness 0.8497, RMSE 0.0274
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] total_validation : 500
[Open3D DEBUG] RANSAC: Fitness 0.8060, RMSE 0.0335
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] total_validation : 505
[Open3D DEBUG] RANSAC: Fitness 0.9727, RMSE 0.0319
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 501
[Open3D DEBUG] RANSAC: Fitness 0.8388, RMSE 0.0346
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 396 points to 312 points.
[Open3D DEBUG] Pointcloud down sampled from 684 points to 521 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.9071, RMSE 0.0221
[Open3D DEBUG] Residual : 3.17e-04 (# of elements : 283)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.9071, RMSE 0.0212
[Open3D DEBUG] Residual : 2.44e-04 (# of elements : 283)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.9071, RMSE 0.0210
[Open3D DEBUG] Residual : 2.37e-04 (# of elements : 283)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.9071, RMSE 0.0210
[Open3D DEBUG] Residual : 2.37e-04 (# of elements : 283)
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] total_validation : 339
[Open3D DEBUG] RANSAC: Fitness 0.6894, RMSE 0.0399
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] total_validation : 117
[Open3D DEBUG] RANSAC: Fitness 0.4747, RMSE 0.0384
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] total_validation : 501
[Open3D DEBUG] RANSAC: Fitness 0.8207, RMSE 0.0294
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] total_validation : 500
[Open3D DEBUG] RANSAC: Fitness 0.7273, RMSE 0.0246
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] total_validation : 374
[Open3D DEBUG] RANSAC: Fitness 0.5859, RMSE 0.0325
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] total_validation : 501
[Open3D DEBUG] RANSAC: Fitness 0.6818, RMSE 0.0324
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 244
[Open3D DEBUG] RANSAC: Fitness 0.4495, RMSE 0.0345
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 684 points to 521 points.
[Open3D DEBUG] Pointcloud down sampled from 811 points to 591 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6814, RMSE 0.0251
[Open3D DEBUG] Residual : 5.74e-04 (# of elements : 355)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6775, RMSE 0.0234
[Open3D DEBUG] Residual : 4.48e-04 (# of elements : 353)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6795, RMSE 0.0234
[Open3D DEBUG] Residual : 4.53e-04 (# of elements : 354)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6833, RMSE 0.0236
[Open3D DEBUG] Residual : 4.64e-04 (# of elements : 356)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6852, RMSE 0.0237
[Open3D DEBUG] Residual : 4.69e-04 (# of elements : 357)
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] total_validation : 53
[Open3D DEBUG] RANSAC: Fitness 0.4254, RMSE 0.0414
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] total_validation : 230
[Open3D DEBUG] RANSAC: Fitness 0.6111, RMSE 0.0328
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] total_validation : 501
[Open3D DEBUG] RANSAC: Fitness 0.6944, RMSE 0.0265
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] total_validation : 363
[Open3D DEBUG] RANSAC: Fitness 0.5702, RMSE 0.0322
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] total_validation : 500
[Open3D DEBUG] RANSAC: Fitness 0.7208, RMSE 0.0287
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 204
[Open3D DEBUG] RANSAC: Fitness 0.5044, RMSE 0.0367
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 811 points to 591 points.
[Open3D DEBUG] Pointcloud down sampled from 446 points to 363 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3587, RMSE 0.0241
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3790, RMSE 0.0262
[Open3D DEBUG] Residual : 1.17e-03 (# of elements : 224)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3773, RMSE 0.0271
[Open3D DEBUG] Residual : 1.21e-03 (# of elements : 223)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3824, RMSE 0.0278
[Open3D DEBUG] Residual : 1.23e-03 (# of elements : 226)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3824, RMSE 0.0281
[Open3D DEBUG] Residual : 1.25e-03 (# of elements : 226)
[Open3D DEBUG] ICP Itera
Fragment 009 / 009 :: integrate rgbd frame 903 (4 of 5).
Fragment 009 / 009 :: integrate rgbd frame 904 (5 of 5).
register fragments.
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_001.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.99599279  0.04162536 -0.07915614 -0.04143244]
 [-0.01724005  0.95784417  0.28677051  0.09416674]
 [ 0.08775617 -0.2842567   0.95472351  0.01341244]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_002.ply ...
[[ 0.97374733  0.19491709 -0.11757321 -0.07077194]
 [-0.12698     0.89379855  0.43011654  0.17814606]
 [ 0.18892383 -0.40389539  0.89508452 -0.03137502]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_003.ply ...
[[ 0.85006002  0.49436564 -0.18166062 -0.12809229]
 [-0.49757453  0.86687611  0.03074715  0.04819955]
 [ 0.17267758  0.06425278  0.98288048  0.1318286 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_004.ply ...
[[ 0.91082347  0.39800362  0.10951585  0.05656879]
 [-0.20406206  0.6647416  -0.71866354  0.38328677]
 [-0.35883043  0.63222759  0.68667969  0.17800331]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
[[-0.94222687 -0.14738216 -0.30081062 -0.14741001]
 [ 0.30305547 -0.75763381 -0.5780557  -0.2428505 ]
 [-0.1427092  -0.63582191  0.7585279  -0.61678255]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
[[ 0.89631286  0.42337629 -0.13181721 -0.07985644]
 [-0.40246384  0.90153002  0.15895434  0.11192268]
 [ 0.18613467 -0.08942116  0.9784466   0.09381462]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
[[ 0.99118139  0.13222389 -0.00873513 -0.08083668]
 [-0.13112811  0.98819819  0.07918178  0.0046593 ]
 [ 0.01910177 -0.07733808  0.99682192  0.12802125]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
[[ 0.98986896  0.08787386 -0.11152413 -0.05308486]
 [-0.08409775  0.99572762  0.03813235  0.03394317]
 [ 0.11439849 -0.0283671   0.99302986  0.1334891 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[ 0.99989708 -0.00368839 -0.01386439  0.03667383]
 [ 0.00625862  0.9817256   0.19019904  0.02056876]
 [ 0.0129095  -0.19026624  0.98164765  0.12381184]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_002.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.98980174  0.13376819 -0.04897545 -0.0612769 ]
 [-0.12538882  0.98129085  0.14610243  0.07937003]
 [ 0.06760302 -0.13847146  0.98805642 -0.03235261]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_003.ply ...
[[ 0.98006402 -0.19110666 -0.05433937 -0.27668172]
 [-0.05574654 -0.00199058 -0.99844297  0.59752462]
 [ 0.19070093  0.98156726 -0.01260443  0.64076876]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_004.ply ...
[[-0.97070627  0.24008246  0.00947352  0.28249481]
 [-0.01920893 -0.11684774  0.99296406 -0.86369182]
 [ 0.23950022  0.96369446  0.11803656  0.22606887]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
[[-0.87809332 -0.2324227  -0.41824849  0.10196977]
 [ 0.40781016 -0.82074437 -0.40008693 -0.21595467]
 [-0.25028581 -0.52187965  0.81547449 -0.50994019]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
[[ 0.94359501  0.29831486 -0.1436548  -0.09584755]
 [-0.32081368  0.93105535 -0.17382321  0.03472424]
 [ 0.08189653  0.21010514  0.97424267  0.07600382]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
[[ 0.99638113  0.07777483 -0.03428874 -0.05224443]
 [-0.08466707  0.94371829 -0.31973002 -0.02505184]
 [ 0.00749197  0.32147608  0.94688806  0.09623336]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
[[ 0.99176673  0.11499072 -0.05635492 -0.03568752]
 [-0.12555119  0.95977921 -0.25111901 -0.04728097]
 [ 0.02521192  0.25612691  0.96631432  0.09868603]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[ 0.95674088  0.26078828  0.12898204  0.03242388]
 [-0.24422854  0.96081795 -0.13107742 -0.04837766]
 [-0.15811171  0.09390603  0.98294575  0.10584184]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_003.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.97346079  0.06769904 -0.21861137 -0.06881037]
 [-0.1613904   0.88034297 -0.44603743 -0.11603062]
 [ 0.16225668  0.46948172  0.86790534  0.0810917 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_004.ply ...
[[ 0.94393462  0.06861989 -0.3229222   0.19919621]
 [-0.32279026  0.39698561 -0.85919083  0.1423597 ]
 [ 0.06923788  0.91525611  0.39687829  0.03871485]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
[[-0.91623816 -0.10726072 -0.38600878  0.01861288]
 [ 0.21236754 -0.94702328 -0.24092933 -0.13053961]
 [-0.33971705 -0.30272438  0.89047756 -0.51887752]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
[[ 0.97651961  0.15232877 -0.15233318 -0.03289618]
 [-0.19384073  0.92982982 -0.31279751 -0.07738356]
 [ 0.09399587  0.33498128  0.93752457  0.09352852]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
[[ 9.98507934e-01 -5.10453993e-02  1.93977695e-02  3.10290309e-02]
 [ 5.46038581e-02  9.37042953e-01 -3.44918718e-01 -1.73869002e-01]
 [-5.70029543e-04  3.45463270e-01  9.38432099e-01  8.52318986e-02]
 [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  1.00000000e+00]]
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
[[ 0.99967021 -0.02497237 -0.00598808  0.03127721]
 [ 0.02046032  0.91543166 -0.40195306 -0.15797285]
 [ 0.0155194   0.40169798  0.9156407   0.09344921]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[ 0.96108132 -0.23213234  0.14979075  0.20481148]
 [ 0.26593983  0.92421622 -0.27404449 -0.09922822]
 [-0.07482445  0.30321437  0.94998018  0.10782698]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_004.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.9871912  -0.07389     0.14139943  0.27261398]
 [ 0.15045313  0.72602652 -0.67100622  0.38835793]
 [-0.05307909  0.68368542  0.72784397  0.00466068]
 [ 0.          0.          0.          1.        ]]tion #5: Fitness 0.3841, RMSE 0.0286
[Open3D DEBUG] Residual : 1.28e-03 (# of elements : 227)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3790, RMSE 0.0285
[Open3D DEBUG] Residual : 1.35e-03 (# of elements : 224)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3807, RMSE 0.0291
[Open3D DEBUG] Residual : 1.46e-03 (# of elements : 225)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3739, RMSE 0.0286
[Open3D DEBUG] Residual : 1.44e-03 (# of elements : 221)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3689, RMSE 0.0283
[Open3D DEBUG] Residual : 1.40e-03 (# of elements : 218)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3689, RMSE 0.0285
[Open3D DEBUG] Residual : 1.43e-03 (# of elements : 218)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3672, RMSE 0.0288
[Open3D DEBUG] Residual : 1.47e-03 (# of elements : 217)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3672, RMSE 0.0291
[Open3D DEBUG] Residual : 1.51e-03 (# of elements : 217)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3689, RMSE 0.0295
[Open3D DEBUG] Residual : 1.54e-03 (# of elements : 218)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3638, RMSE 0.0290
[Open3D DEBUG] Residual : 1.52e-03 (# of elements : 215)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3655, RMSE 0.0294
[Open3D DEBUG] Residual : 1.53e-03 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3638, RMSE 0.0292
[Open3D DEBUG] Residual : 1.56e-03 (# of elements : 215)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3621, RMSE 0.0290
[Open3D DEBUG] Residual : 1.54e-03 (# of elements : 214)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3621, RMSE 0.0289
[Open3D DEBUG] Residual : 1.54e-03 (# of elements : 214)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3621, RMSE 0.0289
[Open3D DEBUG] Residual : 1.53e-03 (# of elements : 214)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3621, RMSE 0.0289
[Open3D DEBUG] Residual : 1.53e-03 (# of elements : 214)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3621, RMSE 0.0289
[Open3D DEBUG] Residual : 1.53e-03 (# of elements : 214)
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] total_validation : 96
[Open3D DEBUG] RANSAC: Fitness 0.5302, RMSE 0.0336
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] total_validation : 500
[Open3D DEBUG] RANSAC: Fitness 0.6535, RMSE 0.0338
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] total_validation : 122
[Open3D DEBUG] RANSAC: Fitness 0.5154, RMSE 0.0334
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] total_validation : 320
[Open3D DEBUG] RANSAC: Fitness 0.5919, RMSE 0.0365
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 85
[Open3D DEBUG] RANSAC: Fitness 0.3835, RMSE 0.0331
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] Pointcloud down sampled from 446 points to 363 points.
[Open3D DEBUG] Pointcloud down sampled from 700 points to 531 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2424, RMSE 0.0287
[Open3D DEBUG] Residual : 1.17e-03 (# of elements : 88)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2755, RMSE 0.0287
[Open3D DEBUG] Residual : 1.05e-03 (# of elements : 100)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2893, RMSE 0.0292
[Open3D DEBUG] Residual : 9.06e-04 (# of elements : 105)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3003, RMSE 0.0298
[Open3D DEBUG] Residual : 9.23e-04 (# of elements : 109)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2975, RMSE 0.0302
[Open3D DEBUG] Residual : 8.93e-04 (# of elements : 108)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.2920, RMSE 0.0301
[Open3D DEBUG] Residual : 7.91e-04 (# of elements : 106)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2782, RMSE 0.0296
[Open3D DEBUG] Residual : 7.45e-04 (# of elements : 101)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.2810, RMSE 0.0306
[Open3D DEBUG] Residual : 7.44e-04 (# of elements : 102)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.2810, RMSE 0.0304
[Open3D DEBUG] Residual : 7.37e-04 (# of elements : 102)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.2782, RMSE 0.0303
[Open3D DEBUG] Residual : 7.38e-04 (# of elements : 101)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.2810, RMSE 0.0305
[Open3D DEBUG] Residual : 7.60e-04 (# of elements : 102)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.2810, RMSE 0.0305
[Open3D DEBUG] Residual : 7.53e-04 (# of elements : 102)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.2810, RMSE 0.0303
[Open3D DEBUG] Residual : 7.54e-04 (# of elements : 102)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.2810, RMSE 0.0303
[Open3D DEBUG] Residual : 7.54e-04 (# of elements : 102)
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] total_validation : 125
[Open3D DEBUG] RANSAC: Fitness 0.6547, RMSE 0.0357
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] total_validation : 60
[Open3D DEBUG] RANSAC: Fitness 0.5112, RMSE 0.0433
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] total_validation : 96
[Open3D DEBUG] RANSAC: Fitness 0.6547, RMSE 0.0387
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 41
[Open3D DEBUG] RANSAC: Fitness 0.4552, RMSE 0.0423
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] Pointcloud down sampled from 700 points to 531 points.
[Open3D DEBUG] Pointcloud down sampled from 526 points to 361 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5913, RMSE 0.0272
[Open3D DEBUG] Residual : 6.16e-04 (# of elements : 314)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5989, RMSE 0.0247
[Open3D DEBUG] Residual : 4.59e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5989, RMSE 0.0243
[Open3D DEBUG] Residual : 4.57e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5989, RMSE 0.0243
[Open3D DEBUG] Residual : 4.52e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5989, RMSE 0.0243
[Open3D DEBUG] Residual : 4.52e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5989, RMSE 0.0242
[Open3D DEBUG] Residual : 4.52e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5989, RMSE 0.0242
[Open3D DEBUG] Residual : 4.50e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5989, RMSE 0.0242
[Open3D DEBUG] Residual : 4.47e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5989, RMSE 0.0242
[Open3D DEBUG] Residual : 4.50e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5989, RMSE 0.0242
[Open3D DEBUG] Residual : 4.52e-04 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5989, RMSE 0.0242
[Open3D DEBUG] Residual : 4.52e-04 (# of elements : 318)
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] total_validation : 67
[Open3D DEBUG] RANSAC: Fitness 0.3557, RMSE 0.0430
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] total_validation : 105
[Open3D DEBUG] RANSAC: Fitness 0.4714, RMSE 0.0318
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 24
[Open3D DEBUG] RANSAC: Fitness 0.2900, RMSE 0.0424
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] Pointcloud down sampled from 526 points to 361 points.
[Open3D DEBUG] Pointcloud down sampled from 321 points to 217 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7008, RMSE 0.0255
[Open3D DEBUG] Residual : 4.60e-04 (# of elements : 253)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7230, RMSE 0.0259
[Open3D DEBUG] Residual : 4.73e-04 (# of elements : 261)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7285, RMSE 0.0262
[Open3D DEBUG] Residual : 5.18e-04 (# of elements : 263)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7230, RMSE 0.0260
[Open3D DEBUG] Residual : 5.24e-04 (# of elements : 261)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7230, RMSE 0.0260
[Open3D DEBUG] Residual : 5.18e-04 (# of elements : 261)
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] total_validation : 501
[Open3D DEBUG] RANSAC: Fitness 0.9144, RMSE 0.0334
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 158
[Open3D DEBUG] RANSAC: Fitness 0.5399, RMSE 0.0330
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] Pointcloud down sampled from 321 points to 217 points.
[Open3D DEBUG] Pointcloud down sampled from 437 points to 316 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.9954, RMSE 0.0209
[Open3D DEBUG] Residual : 2.02e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.9954, RMSE 0.0199
[Open3D DEBUG] Residual : 2.03e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.9954, RMSE 0.0198
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.98e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.9954, RMSE 0.0198
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.92e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.9954, RMSE 0.0198
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.9954, RMSE 0.0197
[Open3D DEBUG] Residual : 1.95e-04 (# of elements : 216)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.9954, RMSE 0.0196
[Open3D DEBUG] Residual : 1.94e-04 (# of elements : 216)
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] total_validation : 502
[Open3D DEBUG] RANSAC: Fitness 0.7196, RMSE 0.0337
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] Pointcloud down sampled from 437 points to 316 points.
[Open3D DEBUG] Pointcloud down sampled from 238 points to 168 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6930, RMSE 0.0233
[Open3D DEBUG] Residual : 3.32e-04 (# of elements : 219)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6899, RMSE 0.0230
[Open3D DEBUG] Residual : 3.25e-04 (# of elements : 218)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6930, RMSE 0.0232
[Open3D DEBUG] Residual : 3.25e-04 (# of elements : 219)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6930, RMSE 0.0232
[Open3D DEBUG] Residual : 3.23e-04 (# of elements : 219)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6930, RMSE 0.0232
[Open3D DEBUG] Residual : 3.23e-04 (# of elements : 219)
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 10 nodes and 45 edges.
[Open3D DEBUG] Line process weight : 7.579756
[Open3D DEBUG] [Initial     ] residual : 6.281269e+03, lambda : 1.308528e-02
[Open3D DEBUG] [Iteration 00] residual : 2.059893e+02, valid edges : 8, time : 0.000 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.840840e+02, valid edges : 12, time : 0.000 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.460399e+02, valid edges : 22, time : 0.000 sec.
[Open3D DEBUG] [Iteration 03] residual : 1.198095e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 04] residual : 1.118032e+02, valid edges : 25, time : 0.000 sec.
[Open3D DEBUG] [Iteration 05] residual : 1.052973e+02, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 06] residual : 1.020715e+02, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 07] residual : 1.012418e+02, valid edges : 25, time : 0.000 sec.
[Open3D DEBUG] [Iteration 08] residual : 1.005109e+02, valid edges : 24, time : 0.000 sec.
[Open3D DEBUG] [Iteration 09] residual : 9.946242e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 10] residual : 9.783629e+01, valid edges : 27, time : 0.000 sec.
[Open3D DEBUG] [Iteration 11] residual : 9.557321e+01, valid edges : 27, time : 0.000 sec.
[Open3D DEBUG] [Iteration 12] residual : 9.349238e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 13] residual : 9.258257e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 14] residual : 9.239178e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 15] residual : 9.236183e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 16] residual : 9.235591e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 17] residual : 9.235404e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 18] residual : 9.235325e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 19] residual : 9.235288e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 20] residual : 9.235269e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.003 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 10 nodes and 35 edges.
[Open3D DEBUG] Line process weight : 7.878500
[Open3D DEBUG] [Initial     ] residual : 3.428556e+01, lambda : 2.996407e-02
[Open3D DEBUG] [Iteration 00] residual : 3.217059e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 01] residual : 3.204515e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 02] residual : 3.204092e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 03] residual : 3.204058e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] [Iteration 04] residual : 3.204054e+01, valid edges : 26, time : 0.000 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.001 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7240, RMSE 0.0220
[Open3D DEBUG] Residual : 3.39e-04 (# of elements : 265)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7240, RMSE 0.0219
[Open3D DEBUG] Residual : 3.37e-04 (# of elements : 265)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7240, RMSE 0.0218
[Open3D DEBUG] Residual : 3.38e-04 (# of elements : 265)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7240, RMSE 0.0218
[Open3D DEBUG] Residual : 3.38e-04 (# of elements : 265)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7240, RMSE 0.0218
[Open3D DEBUG] Residual : 3.38e-04 (# of elements : 265)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 1220 points.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 1295 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6656, RMSE 0.0108
[Open3D DEBUG] Residual : 3.29e-04 (# of elements : 812)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6639, RMSE 0.0111
[Open3D DEBUG] Residual : 3.69e-04 (# of elements : 810)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6664, RMSE 0.0112
[Open3D DEBUG] Residual : 3.92e-04 (# of elements : 813)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6664, RMSE 0.0113
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 813)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6680, RMSE 0.0114
[Open3D DEBUG] Residual : 3.80e-04 (# of elements : 815)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6672, RMSE 0.0114
[Open3D DEBUG] Residual : 3.80e-04 (# of elements : 814)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 3921 points.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 4203 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6123, RMSE 0.0065
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 2401)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6200, RMSE 0.0055
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 2431)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6236, RMSE 0.0056
[Open3D DEBUG] Residual : 2.30e-04 (# of elements : 2445)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6218, RMSE 0.0056
[Open3D DEBUG] Residual : 2.32e-04 (# of elements : 2438)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6215, RMSE 0.0056
[Open3D DEBUG] Residual : 2.34e-04 (# of elements : 2437)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6205, RMSE 0.0056
[Open3D DEBUG] Residual : 2.32e-04 (# of elements : 2433)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6208, RMSE 0.0056
[Open3D DEBUG] Residual : 2.31e-04 (# of elements : 2434)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6208, RMSE 0.0056
[Open3D DEBUG] Residual : 2.32e-04 (# of elements : 2434)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6205, RMSE 0.0056
[Open3D DEBUG] Residual : 2.31e-04 (# of elements : 2433)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6208, RMSE 0.0056
[Open3D DEBUG] Residual : 2.32e-04 (# of elements : 2434)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6205, RMSE 0.0056
[Open3D DEBUG] Residual : 2.31e-04 (# of elements : 2433)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6208, RMSE 0.0056
[Open3D DEBUG] Residual : 2.32e-04 (# of elements : 2434)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6205, RMSE 0.0056
[Open3D DEBUG] Residual : 2.31e-04 (# of elements : 2433)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6208, RMSE 0.0056
[Open3D DEBUG] Residual : 2.32e-04 (# of elements : 2434)
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7300, RMSE 0.0241
[Open3D DEBUG] Residual : 5.44e-04 (# of elements : 384)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7281, RMSE 0.0237
[Open3D DEBUG] Residual : 5.39e-04 (# of elements : 383)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7281, RMSE 0.0237
[Open3D DEBUG] Residual : 5.50e-04 (# of elements : 383)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7281, RMSE 0.0237
[Open3D DEBUG] Residual : 5.57e-04 (# of elements : 383)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7281, RMSE 0.0237
[Open3D DEBUG] Residual : 5.54e-04 (# of elements : 383)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.7281, RMSE 0.0237
[Open3D DEBUG] Residual : 5.54e-04 (# of elements : 383)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.7281, RMSE 0.0237
[Open3D DEBUG] Residual : 5.54e-04 (# of elements : 383)
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 1013 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6194, RMSE 0.0120
[Open3D DEBUG] Residual : 3.81e-04 (# of elements : 1149)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6221, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1154)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6248, RMSE 0.0118
[Open3D DEBUG] Residual : 3.20e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6226, RMSE 0.0119
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1155)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6243, RMSE 0.0118
[Open3D DEBUG] Residual : 3.21e-04 (# of elements : 1158)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6226, RMSE 0.0118
[Open3D DEBUG] Residual : 3.05e-04 (# of elements : 1155)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6243, RMSE 0.0118
[Open3D DEBUG] Residual : 3.06e-04 (# of elements : 1158)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 1157)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6248, RMSE 0.0120
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 1159)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6237, RMSE 0.0118
[Open3D DEBUG] Residual : 2.99e-04 (# of elements : 1157)
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 3196 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5547, RMSE 0.0063
[Open3D DEBUG] Residual : 2.90e-04 (# of elements : 3528)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5542, RMSE 0.0063
[Open3D DEBUG] Residual : 2.74e-04 (# of elements : 3525)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5531, RMSE 0.0063
[Open3D DEBUG] Residual : 2.66e-04 (# of elements : 3518)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5544, RMSE 0.0063
[Open3D DEBUG] Residual : 2.71e-04 (# of elements : 3526)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5544, RMSE 0.0063
[Open3D DEBUG] Residual : 2.69e-04 (# of elements : 3526)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5546, RMSE 0.0063
[Open3D DEBUG] Residual : 2.72e-04 (# of elements : 3527)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5546, RMSE 0.0063
[Open3D DEBUG] Residual : 2.70e-04 (# of elements : 3527)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5544, RMSE 0.0063
[Open3D DEBUG] Residual : 2.72e-04 (# of elements : 3526)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5546, RMSE 0.0063
[Open3D DEBUG] Residual : 2.70e-04 (# of elements : 3527)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5544, RMSE 0.0063
[Open3D DEBUG] Residual : 2.72e-04 (# of elements : 3526)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5546, RMSE 0.0063
[Open3D DEBUG] Residual : 2.70e-04 (# of elements : 3527)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5544, RMSE 0.0063
[Open3D DEBUG] Residual : 2.72e-04 (# of elements : 3526)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5546, RMSE 0.0063
[Open3D DEBUG] Residual : 2.70e-04 (# of elements : 3527)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5544, RMSE 0.0063
[Open3D DEBUG] Residual : 2.72e-04 (# of elements : 3526)
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8080, RMSE 0.0284
[Open3D DEBUG] Residual : 9.97e-04 (# of elements : 425)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8099, RMSE 0.0241
[Open3D DEBUG] Residual : 5.22e-04 (# of elements : 426)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8137, RMSE 0.0231
[Open3D DEBUG] Residual : 4.70e-04 (# of elements : 428)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8023, RMSE 0.0224
[Open3D DEBUG] Residual : 4.30e-04 (# of elements : 422)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8023, RMSE 0.0224
[Open3D DEBUG] Residual : 4.28e-04 (# of elements : 422)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.8023, RMSE 0.0224
[Open3D DEBUG] Residual : 4.28e-04 (# of elements : 422)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.8023, RMSE 0.0224
[Open3D DEBUG] Residual : 4.27e-04 (# of elements : 422)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.8023, RMSE 0.0224
[Open3D DEBUG] Residual : 4.27e-04 (# of elements : 422)
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7062, RMSE 0.0119
[Open3D DEBUG] Residual : 3.54e-04 (# of elements : 1310)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7111, RMSE 0.0116
[Open3D DEBUG] Residual : 3.14e-04 (# of elements : 1319)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7111, RMSE 0.0116
[Open3D DEBUG] Residual : 3.20e-04 (# of elements : 1319)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7111, RMSE 0.0116
[Open3D DEBUG] Residual : 3.20e-04 (# of elements : 1319)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7111, RMSE 0.0116
[Open3D DEBUG] Residual : 3.20e-04 (# of elements : 1319)
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6423, RMSE 0.0062
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 4085)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6399, RMSE 0.0060
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 4070)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6368, RMSE 0.0060
[Open3D DEBUG] Residual : 2.55e-04 (# of elements : 4050)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6363, RMSE 0.0060
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 4047)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6371, RMSE 0.0060
[Open3D DEBUG] Residual : 2.45e-04 (# of elements : 4052)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6358, RMSE 0.0060
[Open3D DEBUG] Residual : 2.55e-04 (# of elements : 4044)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6374, RMSE 0.0060
[Open3D DEBUG] Residual : 2.45e-04 (# of elements : 4054)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6365, RMSE 0.0060
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 4048)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6368, RMSE 0.0060
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 4050)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6365, RMSE 0.0060
[Open3D DEBUG] Residual : 2.46e-04 (# of elements : 4048)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6357, RMSE 0.0060
[Open3D DEBUG] Residual : 2.55e-04 (# of elements : 4043)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6371, RMSE 0.0060
[Open3D DEBUG] Residual : 2.46e-04 (# of elements : 4052)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6368, RMSE 0.0060
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 4050)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6371, RMSE 0.0060
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 4052)
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4620, RMSE 0.0255
[Open3D DEBUG] Residual : 7.68e-04 (# of elements : 243)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4772, RMSE 0.0267
[Open3D DEBUG] Residual : 5.51e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.68e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.4772, RMSE 0.0257
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 251)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.4753, RMSE 0.0265
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 250)
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3817, RMSE 0.0132
[Open3D DEBUG] Residual : 3.02e-04 (# of elements : 708)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3774, RMSE 0.0132
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3774, RMSE 0.0132
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3763, RMSE 0.0131
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3768, RMSE 0.0131
[Open3D DEBUG] Residual : 2.86e-04 (# of elements : 699)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.87e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.3774, RMSE 0.0131
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 700)
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2956, RMSE 0.0068
[Open3D DEBUG] Residual : 4.12e-04 (# of elements : 1880)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3003, RMSE 0.0068
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 1910)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3025, RMSE 0.0068
[Open3D DEBUG] Residual : 3.69e-04 (# of elements : 1924)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3027, RMSE 0.0068
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 1925)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3017, RMSE 0.0068
[Open3D DEBUG] Residual : 3.68e-04 (# of elements : 1919)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3024, RMSE 0.0068
[Open3D DEBUG] Residual : 3.68e-04 (# of elements : 1923)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3027, RMSE 0.0068
[Open3D DEBUG] Residual : 3.71e-04 (# of elements : 1925)
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7978, RMSE 0.0236
[Open3D DEBUG] Residual : 5.72e-04 (# of elements : 292)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8033, RMSE 0.0203
[Open3D DEBUG] Residual : 3.68e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8005, RMSE 0.0202
[Open3D DEBUG] Residual : 3.74e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8005, RMSE 0.0202
[Open3D DEBUG] Residual : 3.69e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.69e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.65e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.69e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 293)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.8005, RMSE 0.0203
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 293)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 1220 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8000, RMSE 0.0111
[Open3D DEBUG] Residual : 3.27e-04 (# of elements : 976)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8016, RMSE 0.0106
[Open3D DEBUG] Residual : 3.42e-04 (# of elements : 978)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8016, RMSE 0.0106
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 978)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8016, RMSE 0.0106
[Open3D DEBUG] Residual : 3.44e-04 (# of elements : 978)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8016, RMSE 0.0106
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 978)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.8016, RMSE 0.0106
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 978)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 3921 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7470, RMSE 0.0062
[Open3D DEBUG] Residual : 2.45e-04 (# of elements : 2929)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7465, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2927)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7473, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2930)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7478, RMSE 0.0065
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 2932)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7478, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2932)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.7470, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2929)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.7475, RMSE 0.0065
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 2931)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.7478, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2932)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.7470, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2929)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.7480, RMSE 0.0065
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 2933)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.7478, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2932)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.7470, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2929)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.7478, RMSE 0.0065
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 2932)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.7478, RMSE 0.0065
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 2932)
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7213, RMSE 0.0291
[Open3D DEBUG] Residual : 8.04e-04 (# of elements : 264)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7213, RMSE 0.0209
[Open3D DEBUG] Residual : 3.19e-04 (# of elements : 264)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7131, RMSE 0.0200
[Open3D DEBUG] Residual : 2.91e-04 (# of elements : 261)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7131, RMSE 0.0200
[Open3D DEBUG] Residual : 2.90e-04 (# of elements : 261)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7131, RMSE 0.0200
[Open3D DEBUG] Residual : 2.90e-04 (# of elements : 261)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 1220 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 1013 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6803, RMSE 0.0114
[Open3D DEBUG] Residual : 2.19e-04 (# of elements : 830)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6852, RMSE 0.0114
[Open3D DEBUG] Residual : 2.03e-04 (# of elements : 836)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6836, RMSE 0.0115
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 834)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6828, RMSE 0.0115
[Open3D DEBUG] Residual : 2.00e-04 (# of elements : 833)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6811, RMSE 0.0114
[Open3D DEBUG] Residual : 2.00e-04 (# of elements : 831)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 3921 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 3196 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6162, RMSE 0.0061
[Open3D DEBUG] Residual : 1.78e-04 (# of elements : 2416)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6169, RMSE 0.0059
[Open3D DEBUG] Residual : 1.62e-04 (# of elements : 2419)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.67e-04 (# of elements : 2422)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.66e-04 (# of elements : 2422)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.66e-04 (# of elements : 2422)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.63e-04 (# of elements : 2422)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6182, RMSE 0.0059
[Open3D DEBUG] Residual : 1.67e-04 (# of elements : 2424)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6172, RMSE 0.0059
[Open3D DEBUG] Residual : 1.63e-04 (# of elements : 2420)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.66e-04 (# of elements : 2422)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.63e-04 (# of elements : 2422)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6182, RMSE 0.0059
[Open3D DEBUG] Residual : 1.67e-04 (# of elements : 2424)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6172, RMSE 0.0059
[Open3D DEBUG] Residual : 1.63e-04 (# of elements : 2420)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.66e-04 (# of elements : 2422)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6177, RMSE 0.0059
[Open3D DEBUG] Residual : 1.63e-04 (# of elements : 2422)
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8825, RMSE 0.0279
[Open3D DEBUG] Residual : 6.86e-04 (# of elements : 323)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8743, RMSE 0.0184
[Open3D DEBUG] Residual : 2.56e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8716, RMSE 0.0178
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8716, RMSE 0.0178
[Open3D DEBUG] Residual : 2.19e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8716, RMSE 0.0178
[Open3D DEBUG] Residual : 2.25e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.24e-04 (# of elements : 319)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.8716, RMSE 0.0179
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 319)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 1220 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8738, RMSE 0.0102
[Open3D DEBUG] Residual : 1.83e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.73e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.83e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.8746, RMSE 0.0100
[Open3D DEBUG] Residual : 1.84e-04 (# of elements : 1067)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.8738, RMSE 0.0100
[Open3D DEBUG] Residual : 1.71e-04 (# of elements : 1066)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 3921 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8261, RMSE 0.0055
[Open3D DEBUG] Residual : 1.46e-04 (# of elements : 3239)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8225, RMSE 0.0055
[Open3D DEBUG] Residual : 1.41e-04 (# of elements : 3225)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8215, RMSE 0.0055
[Open3D DEBUG] Residual : 1.41e-04 (# of elements : 3221)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8220, RMSE 0.0055
[Open3D DEBUG] Residual : 1.41e-04 (# of elements : 3223)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8217, RMSE 0.0055
[Open3D DEBUG] Residual : 1.41e-04 (# of elements : 3222)
[Open3D DEBUG] Read geometry::PointCloud: 19002 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 366 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6967, RMSE 0.0267
[Open3D DEBUG] Residual : 7.09e-04 (# of elements : 255)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7678, RMSE 0.0251
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7705, RMSE 0.0252
[Open3D DEBUG] Residual : 4.88e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7705, RMSE 0.0253
[Open3D DEBUG] Residual : 4.86e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7705, RMSE 0.0253
[Open3D DEBUG] Residual : 4.89e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.7705, RMSE 0.0254
[Open3D DEBUG] Residual : 4.91e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.7678, RMSE 0.0252
[Open3D DEBUG] Residual : 4.86e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.84e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.7678, RMSE 0.0253
[Open3D DEBUG] Residual : 4.85e-04 (# of elements : 281)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 1220 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6705, RMSE 0.0124
[Open3D DEBUG] Residual : 2.94e-04 (# of elements : 818)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6770, RMSE 0.0119
[Open3D DEBUG] Residual : 2.94e-04 (# of elements : 826)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.94e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6762, RMSE 0.0119
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 825)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6754, RMSE 0.0119
[Open3D DEBUG] Residual : 2.95e-04 (# of elements : 824)
[Open3D DEBUG] Pointcloud down sampled from 19002 points to 3921 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5728, RMSE 0.0064
[Open3D DEBUG] Residual : 2.67e-04 (# of elements : 2246)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5815, RMSE 0.0061
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 2280)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5830, RMSE 0.0061
[Open3D DEBUG] Residual : 2.54e-04 (# of elements : 2286)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5817, RMSE 0.0061
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 2281)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5815, RMSE 0.0061
[Open3D DEBUG] Residual : 2.41e-04 (# of elements : 2280)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5810, RMSE 0.0060
[Open3D DEBUG] Residual : 2.49e-04 (# of elements : 2278)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5812, RMSE 0.0061
[Open3D DEBUG] Residual : 2.42e-04 (# of elements : 2279)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5812, RMSE 0.0061
[Open3D DEBUG] Residual : 2.49e-04 (# of elements : 2279)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5817, RMSE 0.0061
[Open3D DEBUG] Residual : 2.52e-04 (# of elements : 2281)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5810, RMSE 0.0060
[Open3D DEBUG] Residual : 2.41e-04 (# of elements : 2278)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5815, RMSE 0.0061
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 2280)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5807, RMSE 0.0061
[Open3D DEBUG] Residual : 2.42e-04 (# of elements : 2277)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5812, RMSE 0.0061
[Open3D DEBUG] Residual : 2.49e-04 (# of elements : 2279)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5810, RMSE 0.0061
[Open3D DEBUG] Residual : 2.42e-04 (# of elements : 2278)
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6324, RMSE 0.0282
[Open3D DEBUG] Residual : 7.92e-04 (# of elements : 203)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6604, RMSE 0.0226
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6542, RMSE 0.0219
[Open3D DEBUG] Residual : 4.14e-04 (# of elements : 210)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6542, RMSE 0.0222
[Open3D DEBUG] Residual : 4.12e-04 (# of elements : 210)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6573, RMSE 0.0222
[Open3D DEBUG] Residual : 4.20e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.6604, RMSE 0.0224
[Open3D DEBUG] Residual : 4.18e-04 (# of elements : 212)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.6573, RMSE 0.0224
[Open3D DEBUG] Residual : 4.16e-04 (# of elements : 211)
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 1013 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6051, RMSE 0.0121
[Open3D DEBUG] Residual : 3.39e-04 (# of elements : 613)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5933, RMSE 0.0116
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 601)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 604)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.98e-04 (# of elements : 604)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 604)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 604)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 604)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 604)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 604)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.96e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.5953, RMSE 0.0117
[Open3D DEBUG] Residual : 2.84e-04 (# of elements : 603)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.5962, RMSE 0.0117
[Open3D DEBUG] Residual : 2.97e-04 (# of elements : 604)
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 3196 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5210, RMSE 0.0063
[Open3D DEBUG] Residual : 2.91e-04 (# of elements : 1665)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5278, RMSE 0.0061
[Open3D DEBUG] Residual : 2.72e-04 (# of elements : 1687)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5269, RMSE 0.0062
[Open3D DEBUG] Residual : 2.71e-04 (# of elements : 1684)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5266, RMSE 0.0062
[Open3D DEBUG] Residual : 2.72e-04 (# of elements : 1683)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5269, RMSE 0.0062
[Open3D DEBUG] Residual : 2.72e-04 (# of
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
[[-0.74939248  0.31193991 -0.58404144  0.1008101 ]
 [ 0.20578355 -0.72866192 -0.65322656 -0.12298188]
 [-0.62933619 -0.60970919  0.48186166 -0.59327385]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
[[ 0.99921029 -0.01988376  0.034401    0.03460953]
 [ 0.01844827  0.99896593  0.04155393  0.09522701]
 [-0.03519168 -0.04088647  0.99854386  0.00388203]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
[[ 0.95640976 -0.25711732  0.13845958  0.08096181]
 [ 0.25653779  0.96627633  0.02232517  0.01174372]
 [-0.1395304   0.01416811  0.99011642  0.00691408]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
[[ 0.96116576 -0.24969195  0.1175343   0.06256369]
 [ 0.24505633  0.96808092  0.05259961 -0.04028048]
 [-0.12691641 -0.02175442  0.99167483  0.0078566 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[ 0.90332066 -0.39371335  0.17029851  0.18567828]
 [ 0.35814195  0.91071071  0.20576771 -0.00126718]
 [-0.23610617 -0.12488318  0.96366907 -0.02167187]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.9406858   0.23166201 -0.24787688 -0.16523839]
 [-0.16109479  0.94796652  0.27460509  0.16777769]
 [ 0.29859454 -0.21838543  0.92905818 -0.0011518 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
[[ 0.95048826  0.30878669 -0.03496926 -0.05851273]
 [-0.14474251  0.53947263  0.82946904 -0.26379807]
 [ 0.27499396 -0.78333905  0.55745696  0.31502204]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
[[-0.95388496  0.21648882 -0.20793287  0.30207616]
 [-0.23754774 -0.96790801  0.08200702 -0.33118533]
 [-0.18350628  0.12761925  0.97469932  0.3745237 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
[[ 0.94085781  0.18927849 -0.28099865  0.16179747]
 [ 0.06651776  0.71004955  0.70100287 -0.35765887]
 [ 0.33220773 -0.67823542  0.65546528  0.31913275]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[ 0.84751581  0.32783998 -0.41741813  0.18199164]
 [ 0.17031778  0.57686981  0.79888239 -0.30578951]
 [ 0.5027015  -0.74815919  0.43306931  0.29243652]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_005.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
Using RGBD odometry
voxel_size 0.050000
[[-0.84327223  0.16913044 -0.51018314 -0.20118092]
 [ 0.1655638  -0.82130991 -0.54592917 -0.44187725]
 [-0.51135171 -0.54483477  0.66458596  0.3660831 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_005.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
[[-0.87424425  0.48129918 -0.06362469  0.13534087]
 [-0.33145349 -0.6874779  -0.64615225 -0.63315874]
 [-0.35473311 -0.54380626  0.76055189  0.39250839]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_005.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
[[-0.87251889  0.31604135 -0.37259717  0.00346088]
 [ 0.08059107 -0.65906902 -0.74775203 -0.5445373 ]
 [-0.48188782 -0.68245578  0.54958006  0.29038972]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_005.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[-0.73063259  0.61396615  0.29869982  0.13794764]
 [-0.56242535 -0.29316244 -0.77313227 -0.53823828]
 [-0.38710947 -0.73287198  0.55950417  0.28518714]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_006.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.97635684 -0.20740051  0.06092911  0.05219365]
 [ 0.21134242  0.97507686 -0.06752406 -0.06623933]
 [-0.04540604  0.07880448  0.99585548 -0.00379162]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_006.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
[[ 0.97013811 -0.24252657  0.00359219  0.04175563]
 [ 0.24208449  0.96723716 -0.07646815 -0.07344423]
 [ 0.01507106  0.07505428  0.99706555  0.0076169 ]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_006.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[ 0.91943092 -0.35566507  0.16777707  0.16911166]
 [ 0.35578443  0.93407391  0.03038709 -0.03313997]
 [-0.16752381  0.03175364  0.98535652 -0.00389704]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_007.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.99981197  0.00899813 -0.01717711 -0.00535709]
 [-0.00873224  0.99984186  0.01549179 -0.00783696]
 [ 0.01731379 -0.01533888  0.99973244  0.00183915]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_007.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
[[ 0.99538208 -0.09083455 -0.03104181  0.15749343]
 [ 0.0937338   0.98947321  0.11025763  0.00413429]
 [ 0.02069984 -0.11265813  0.99341817  0.00466657]
 [ 0.          0.          0.          1.        ]]
reading dataset/realsense/fragments/fragment_008.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
Using RGBD odometry
voxel_size 0.050000
[[ 0.97970758 -0.15402418  0.12825603  0.08177017]
 [ 0.13789831  0.98235321  0.12635757  0.00324076]
 [-0.14545484 -0.10610718  0.98365856 -0.0080231 ]
 [ 0.          0.          0.          1.        ]]
refine rough registration of fragments.
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_001.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_006.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_006.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_006.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_000.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_007.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_001.ply ... elements : 1684)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5275, RMSE 0.0062
[Open3D DEBUG] Residual : 2.71e-04 (# of elements : 1686)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5272, RMSE 0.0062
[Open3D DEBUG] Residual : 2.71e-04 (# of elements : 1685)
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.23e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.8889, RMSE 0.0194
[Open3D DEBUG] Residual : 2.22e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.8889, RMSE 0.0191
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 352)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 1295 points.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 2366 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8803, RMSE 0.0111
[Open3D DEBUG] Residual : 2.55e-04 (# of elements : 1140)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8795, RMSE 0.0113
[Open3D DEBUG] Residual : 2.52e-04 (# of elements : 1139)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8772, RMSE 0.0114
[Open3D DEBUG] Residual : 2.50e-04 (# of elements : 1136)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8764, RMSE 0.0114
[Open3D DEBUG] Residual : 2.49e-04 (# of elements : 1135)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8764, RMSE 0.0114
[Open3D DEBUG] Residual : 2.49e-04 (# of elements : 1135)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 4203 points.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 8369 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.8432, RMSE 0.0063
[Open3D DEBUG] Residual : 2.46e-04 (# of elements : 3544)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.8306, RMSE 0.0067
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3491)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.8225, RMSE 0.0066
[Open3D DEBUG] Residual : 2.28e-04 (# of elements : 3457)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.8237, RMSE 0.0066
[Open3D DEBUG] Residual : 2.30e-04 (# of elements : 3462)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.8232, RMSE 0.0066
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3460)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.8244, RMSE 0.0066
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3465)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.8230, RMSE 0.0066
[Open3D DEBUG] Residual : 2.30e-04 (# of elements : 3459)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.8227, RMSE 0.0066
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3458)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.8242, RMSE 0.0066
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3464)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.8230, RMSE 0.0066
[Open3D DEBUG] Residual : 2.30e-04 (# of elements : 3459)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.8227, RMSE 0.0066
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3458)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.8242, RMSE 0.0066
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3464)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.8230, RMSE 0.0066
[Open3D DEBUG] Residual : 2.30e-04 (# of elements : 3459)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.8227, RMSE 0.0066
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 3458)
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.9969, RMSE 0.0182
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.9969, RMSE 0.0172
[Open3D DEBUG] Residual : 1.82e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.9969, RMSE 0.0175
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.9969, RMSE 0.0176
[Open3D DEBUG] Residual : 1.88e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.9969, RMSE 0.0177
[Open3D DEBUG] Residual : 1.90e-04 (# of elements : 320)
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 1013 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.9990, RMSE 0.0104
[Open3D DEBUG] Residual : 1.55e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.9990, RMSE 0.0087
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.17e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.9990, RMSE 0.0091
[Open3D DEBUG] Residual : 1.20e-04 (# of elements : 1012)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.9990, RMSE 0.0090
[Open3D DEBUG] Residual : 1.18e-04 (# of elements : 1012)
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 3196 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.9934, RMSE 0.0052
[Open3D DEBUG] Residual : 1.01e-04 (# of elements : 3175)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.9934, RMSE 0.0051
[Open3D DEBUG] Residual : 1.02e-04 (# of elements : 3175)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.9931, RMSE 0.0051
[Open3D DEBUG] Residual : 1.01e-04 (# of elements : 3174)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.9931, RMSE 0.0051
[Open3D DEBUG] Residual : 1.01e-04 (# of elements : 3174)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.9931, RMSE 0.0051
[Open3D DEBUG] Residual : 1.01e-04 (# of elements : 3174)
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7424, RMSE 0.0246
[Open3D DEBUG] Residual : 4.90e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7500, RMSE 0.0225
[Open3D DEBUG] Residual : 3.72e-04 (# of elements : 297)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7449, RMSE 0.0216
[Open3D DEBUG] Residual : 3.45e-04 (# of elements : 295)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7424, RMSE 0.0214
[Open3D DEBUG] Residual : 3.40e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.41e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.44e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.7424, RMSE 0.0215
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 294)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 1295 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 2207 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7073, RMSE 0.0115
[Open3D DEBUG] Residual : 2.81e-04 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7058, RMSE 0.0112
[Open3D DEBUG] Residual : 2.57e-04 (# of elements : 914)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7073, RMSE 0.0112
[Open3D DEBUG] Residual : 2.56e-04 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7058, RMSE 0.0111
[Open3D DEBUG] Residual : 2.57e-04 (# of elements : 914)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7066, RMSE 0.0111
[Open3D DEBUG] Residual : 2.57e-04 (# of elements : 915)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.7066, RMSE 0.0111
[Open3D DEBUG] Residual : 2.57e-04 (# of elements : 915)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.7066, RMSE 0.0111
[Open3D DEBUG] Residual : 2.57e-04 (# of elements : 915)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.7066, RMSE 0.0111
[Open3D DEBUG] Residual : 2.57e-04 (# of elements : 915)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 4203 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 7191 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6602, RMSE 0.0064
[Open3D DEBUG] Residual : 2.37e-04 (# of elements : 2775)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6586, RMSE 0.0062
[Open3D DEBUG] Residual : 2.21e-04 (# of elements : 2768)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6586, RMSE 0.0061
[Open3D DEBUG] Residual : 2.13e-04 (# of elements : 2768)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6579, RMSE 0.0061
[Open3D DEBUG] Residual : 2.13e-04 (# of elements : 2765)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6579, RMSE 0.0061
[Open3D DEBUG] Residual : 2.12e-04 (# of elements : 2765)
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6944, RMSE 0.0217
[Open3D DEBUG] Residual : 3.43e-04 (# of elements : 275)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6869, RMSE 0.0194
[Open3D DEBUG] Residual : 2.91e-04 (# of elements : 272)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6869, RMSE 0.0195
[Open3D DEBUG] Residual : 2.91e-04 (# of elements : 272)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6869, RMSE 0.0194
[Open3D DEBUG] Residual : 2.91e-04 (# of elements : 272)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6869, RMSE 0.0194
[Open3D DEBUG] Residual : 2.91e-04 (# of elements : 272)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 1295 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6656, RMSE 0.0110
[Open3D DEBUG] Residual : 3.28e-04 (# of elements : 862)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6695, RMSE 0.0115
[Open3D DEBUG] Residual : 3.42e-04 (# of elements : 867)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6695, RMSE 0.0116
[Open3D DEBUG] Residual : 3.39e-04 (# of elements : 867)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6695, RMSE 0.0116
[Open3D DEBUG] Residual : 3.46e-04 (# of elements : 867)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6703, RMSE 0.0117
[Open3D DEBUG] Residual : 3.59e-04 (# of elements : 868)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6710, RMSE 0.0117
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 869)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6718, RMSE 0.0118
[Open3D DEBUG] Residual : 3.58e-04 (# of elements : 870)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6726, RMSE 0.0118
[Open3D DEBUG] Residual : 3.57e-04 (# of elements : 871)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6726, RMSE 0.0118
[Open3D DEBUG] Residual : 3.57e-04 (# of elements : 871)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 4203 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6005, RMSE 0.0067
[Open3D DEBUG] Residual : 2.53e-04 (# of elements : 2524)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5924, RMSE 0.0067
[Open3D DEBUG] Residual : 2.45e-04 (# of elements : 2490)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5884, RMSE 0.0066
[Open3D DEBUG] Residual : 2.50e-04 (# of elements : 2473)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5822, RMSE 0.0065
[Open3D DEBUG] Residual : 2.53e-04 (# of elements : 2447)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5798, RMSE 0.0066
[Open3D DEBUG] Residual : 2.54e-04 (# of elements : 2437)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5810, RMSE 0.0066
[Open3D DEBUG] Residual : 2.56e-04 (# of elements : 2442)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5779, RMSE 0.0066
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 2429)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5767, RMSE 0.0066
[Open3D DEBUG] Residual : 2.60e-04 (# of elements : 2424)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5741, RMSE 0.0066
[Open3D DEBUG] Residual : 2.62e-04 (# of elements : 2413)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5715, RMSE 0.0066
[Open3D DEBUG] Residual : 2.59e-04 (# of elements : 2402)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5724, RMSE 0.0066
[Open3D DEBUG] Residual : 2.61e-04 (# of elements : 2406)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5715, RMSE 0.0066
[Open3D DEBUG] Residual : 2.58e-04 (# of elements : 2402)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5732, RMSE 0.0066
[Open3D DEBUG] Residual : 2.62e-04 (# of elements : 2409)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5724, RMSE 0.0066
[Open3D DEBUG] Residual : 2.62e-04 (# of elements : 2406)
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5177, RMSE 0.0271
[Open3D DEBUG] Residual : 6.97e-04 (# of elements : 205)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5177, RMSE 0.0207
[Open3D DEBUG] Residual : 4.70e-04 (# of elements : 205)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5177, RMSE 0.0203
[Open3D DEBUG] Residual : 4.66e-04 (# of elements : 205)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5177, RMSE 0.0204
[Open3D DEBUG] Residual : 4.60e-04 (# of elements : 205)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5177, RMSE 0.0204
[Open3D DEBUG] Residual : 4.47e-04 (# of elements : 205)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5177, RMSE 0.0203
[Open3D DEBUG] Residual : 4.64e-04 (# of elements : 205)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5177, RMSE 0.0204
[Open3D DEBUG] Residual : 4.48e-04 (# of elements : 205)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 1295 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 1013 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4525, RMSE 0.0121
[Open3D DEBUG] Residual : 3.32e-04 (# of elements : 586)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4548, RMSE 0.0112
[Open3D DEBUG] Residual : 4.00e-04 (# of elements : 589)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4548, RMSE 0.0115
[Open3D DEBUG] Residual : 3.64e-04 (# of elements : 589)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4548, RMSE 0.0115
[Open3D DEBUG] Residual : 3.48e-04 (# of elements : 589)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4548, RMSE 0.0114
[Open3D DEBUG] Residual : 3.38e-04 (# of elements : 589)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4556, RMSE 0.0114
[Open3D DEBUG] Residual : 3.42e-04 (# of elements : 590)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4548, RMSE 0.0114
[Open3D DEBUG] Residual : 3.42e-04 (# of elements : 589)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4556, RMSE 0.0114
[Open3D DEBUG] Residual : 3.42e-04 (# of elements : 590)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 4203 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 3196 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4000, RMSE 0.0068
[Open3D DEBUG] Residual : 2.44e-04 (# of elements : 1681)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4064, RMSE 0.0062
[Open3D DEBUG] Residual : 2.16e-04 (# of elements : 1708)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4052, RMSE 0.0062
[Open3D DEBUG] Residual : 2.18e-04 (# of elements : 1703)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4052, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1703)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4047, RMSE 0.0062
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 1701)
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6010, RMSE 0.0272
[Open3D DEBUG] Residual : 6.26e-04 (# of elements : 238)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6237, RMSE 0.0209
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 247)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6237, RMSE 0.0207
[Open3D DEBUG] Residual : 2.77e-04 (# of elements : 247)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6263, RMSE 0.0209
[Open3D DEBUG] Residual : 2.53e-04 (# of elements : 248)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6263, RMSE 0.0201
[Open3D DEBUG] Residual : 2.64e-04 (# of elements : 248)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6263, RMSE 0.0205
[Open3D DEBUG] Residual : 2.62e-04 (# of elements : 248)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6263, RMSE 0.0204
[Open3D DEBUG] Residual : 2.62e-04 (# of elements : 248)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6263, RMSE 0.0204
[Open3D DEBUG] Residual : 2.62e-04 (# of elements : 248)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 1295 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5745, RMSE 0.0113
[Open3D DEBUG] Residual : 2.33e-04 (# of elements : 744)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5699, RMSE 0.0113
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 738)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.41e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.36e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5714, RMSE 0.0114
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 740)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5699, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 738)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.5699, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 738)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.5699, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 738)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.5699, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 738)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 739)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.5699, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 738)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.5722, RMSE 0.0114
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 741)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.5707, RMSE 0.0113
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 739)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 4203 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5356, RMSE 0.0058
[Open3D DEBUG] Residual : 1.92e-04 (# of elements : 2251)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5403, RMSE 0.0057
[Open3D DEBUG] Residual : 2.05e-04 (# of elements : 2271)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5420, RMSE 0.0058
[Open3D DEBUG] Residual : 2.02e-04 (# of elements : 2278)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5410, RMSE 0.0058
[Open3D DEBUG] Residual : 2.04e-04 (# of elements : 2274)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5408, RMSE 0.0058
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 2273)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5415, RMSE 0.0058
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 2276)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5413, RMSE 0.0058
[Open3D DEBUG] Residual : 2.03e-04 (# of elements : 2275)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5403, RMSE 0.0058
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 2271)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5413, RMSE 0.0058
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 2275)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5415, RMSE 0.0058
[Open3D DEBUG] Residual : 2.00e-04 (# of elements : 2276)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5415, RMSE 0.0058
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 2276)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5413, RMSE 0.0058
[Open3D DEBUG] Residual : 2.02e-04 (# of elements : 2275)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5408, RMSE 0.0058
[Open3D DEBUG] Residual : 2.01e-04 (# of elements : 2273)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5410, RMSE 0.0058
[Open3D DEBUG] Residual : 2.02e-04 (# of elements : 2274)
[Open3D DEBUG] Read geometry::PointCloud: 19128 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 396 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3788, RMSE 0.0275
[Open3D DEBUG] Residual : 5.65e-04 (# of elements : 150)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4040, RMSE 0.0251
[Open3D DEBUG] Residual : 4.54e-04 (# of elements : 160)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3914, RMSE 0.0212
[Open3D DEBUG] Residual : 3.50e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3914, RMSE 0.0209
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3914, RMSE 0.0213
[Open3D DEBUG] Residual : 3.55e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3914, RMSE 0.0209
[Open3D DEBUG] Residual : 3.53e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3914, RMSE 0.0214
[Open3D DEBUG] Residual : 3.59e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3914, RMSE 0.0208
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3914, RMSE 0.0214
[Open3D DEBUG] Residual : 3.60e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3939, RMSE 0.0212
[Open3D DEBUG] Residual : 3.62e-04 (# of elements : 156)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3939, RMSE 0.0218
[Open3D DEBUG] Residual : 3.67e-04 (# of elements : 156)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3914, RMSE 0.0209
[Open3D DEBUG] Residual : 3.28e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.3914, RMSE 0.0207
[Open3D DEBUG] Residual : 3.35e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.3914, RMSE 0.0216
[Open3D DEBUG] Residual : 3.56e-04 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.3914, RMSE 0.0215
[Open3D DEBUG] Residual : 3.30e-04 (# of elements : 155)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 1295 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 3.13e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3336, RMSE 0.0115
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 432)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3336, RMSE 0.0114
[Open3D DEBUG] Residual : 2.51e-04 (# of elements : 432)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3344, RMSE 0.0116
[Open3D DEBUG] Residual : 2.50e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3351, RMSE 0.0117
[Open3D DEBUG] Residual : 2.49e-04 (# of elements : 434)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3336, RMSE 0.0116
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 432)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3344, RMSE 0.0114
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.3344, RMSE 0.0117
[Open3D DEBUG] Residual : 2.38e-04 (# of elements : 433)
[Open3D DEBUG] Pointcloud down sampled from 19128 points to 4203 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2976, RMSE 0.0060
[Open3D DEBUG] Residual : 2.04e-04 (# of elements : 1251)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2991, RMSE 0.0060
[Open3D DEBUG] Residual : 1.98e-04 (# of elements : 1257)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2988, RMSE 0.0062
[Open3D DEBUG] Residual : 1.92e-04 (# of elements : 1256)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3000, RMSE 0.0063
[Open3D DEBUG] Residual : 1.93e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2995, RMSE 0.0062
[Open3D DEBUG] Residual : 1.92e-04 (# of elements : 1259)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3000, RMSE 0.0063
[Open3D DEBUG] Residual : 1.93e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2998, RMSE 0.0062
[Open3D DEBUG] Residual : 1.92e-04 (# of elements : 1260)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3000, RMSE 0.0063
[Open3D DEBUG] Residual : 1.93e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3000, RMSE 0.0062
[Open3D DEBUG] Residual : 1.91e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3000, RMSE 0.0063
[Open3D DEBUG] Residual : 1.93e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3000, RMSE 0.0062
[Open3D DEBUG] Residual : 1.91e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3000, RMSE 0.0063
[Open3D DEBUG] Residual : 1.92e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3000, RMSE 0.0063
[Open3D DEBUG] Residual : 1.93e-04 (# of elements : 1261)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3000, RMSE 0.0062
[Open3D DEBUG] Residual : 1.91e-04 (# of elements : 1261)
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.7061, RMSE 0.0217
[Open3D DEBUG] Residual : 5.88e-04 (# of elements : 483)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.7091, RMSE 0.0217
[Open3D DEBUG] Residual : 6.28e-04 (# of elements : 485)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.7105, RMSE 0.0218
[Open3D DEBUG] Residual : 6.27e-04 (# of elements : 486)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.7105, RMSE 0.0218
[Open3D DEBUG] Residual : 6.26e-04 (# of elements : 486)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.7105, RMSE 0.0218
[Open3D DEBUG] Residual : 6.26e-04 (# of elements : 486)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.7105, RMSE 0.0218
[Open3D DEBUG] Residual : 6.26e-04 (# of elements : 486)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 2366 points.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 2886 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6678, RMSE 0.0122
[Open3D DEBUG] Residual : 5.26e-04 (# of elements : 1580)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6665, RMSE 0.0124
[Open3D DEBUG] Residual : 4.95e-04 (# of elements : 1577)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6644, RMSE 0.0124
[Open3D DEBUG] Residual : 4.90e-04 (# of elements : 1572)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6653, RMSE 0.0125
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1574)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.80e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6657, RMSE 0.0126
[Open3D DEBUG] Residual : 4.80e-04 (# of elements : 1575)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 1576)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6661, RMSE 0.0126
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 1576)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 8369 points.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 9882 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5704, RMSE 0.0075
[Open3D DEBUG] Residual : 4.06e-04 (# of elements : 4774)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5690, RMSE 0.0071
[Open3D DEBUG] Residual : 3.72e-04 (# of elements : 4762)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5678, RMSE 0.0071
[Open3D DEBUG] Residual : 3.70e-04 (# of elements : 4752)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5676, RMSE 0.0072
[Open3D DEBUG] Residual : 3.69e-04 (# of elements : 4750)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5677, RMSE 0.0072
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 4751)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5670, RMSE 0.0072
[Open3D DEBUG] Residual : 3.60e-04 (# of elements : 4745)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5664, RMSE 0.0072
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 4740)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5663, RMSE 0.0072
[Open3D DEBUG] Residual : 3.60e-04 (# of elements : 4739)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5667, RMSE 0.0072
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 4743)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5663, RMSE 0.0072
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 4739)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5663, RMSE 0.0072
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 4739)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5666, RMSE 0.0072
[Open3D DEBUG] Residual : 3.59e-04 (# of elements : 4742)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5661, RMSE 0.0072
[Open3D DEBUG] Residual : 3.60e-04 (# of elements : 4738)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5663, RMSE 0.0072
[Open3D DEBUG] Residual : 3.60e-04 (# of elements : 4739)
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5336, RMSE 0.0269
[Open3D DEBUG] Residual : 8.62e-04 (# of elements : 365)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5673, RMSE 0.0234
[Open3D DEBUG] Residual : 6.35e-04 (# of elements : 388)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5658, RMSE 0.0235
[Open3D DEBUG] Residual : 6.41e-04 (# of elements : 387)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5687, RMSE 0.0240
[Open3D DEBUG] Residual : 6.70e-04 (# of elements : 389)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5673, RMSE 0.0239
[Open3D DEBUG] Residual : 6.61e-04 (# of elements : 388)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5687, RMSE 0.0240
[Open3D DEBUG] Residual : 6.59e-04 (# of elements : 389)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5687, RMSE 0.0240
[Open3D DEBUG] Residual : 6.59e-04 (# of elements : 389)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 2366 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 2207 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4962, RMSE 0.0127
[Open3D DEBUG] Residual : 5.32e-04 (# of elements : 1174)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5042, RMSE 0.0119
[Open3D DEBUG] Residual : 5.71e-04 (# of elements : 1193)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5046, RMSE 0.0119
[Open3D DEBUG] Residual : 5.97e-04 (# of elements : 1194)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5063, RMSE 0.0119
[Open3D DEBUG] Residual : 6.09e-04 (# of elements : 1198)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5059, RMSE 0.0119
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 1197)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5101, RMSE 0.0120
[Open3D DEBUG] Residual : 5.73e-04 (# of elements : 1207)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5097, RMSE 0.0120
[Open3D DEBUG] Residual : 5.75e-04 (# of elements : 1206)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5097, RMSE 0.0120
[Open3D DEBUG] Residual : 5.74e-04 (# of elements : 1206)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5097, RMSE 0.0120
[Open3D DEBUG] Residual : 5.74e-04 (# of elements : 1206)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5101, RMSE 0.0120
[Open3D DEBUG] Residual : 5.74e-04 (# of elements : 1207)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 8369 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 7191 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4545, RMSE 0.0066
[Open3D DEBUG] Residual : 5.26e-04 (# of elements : 3804)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4505, RMSE 0.0065
[Open3D DEBUG] Residual : 4.66e-04 (# of elements : 3770)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4478, RMSE 0.0065
[Open3D DEBUG] Residual : 4.56e-04 (# of elements : 3748)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4478, RMSE 0.0065
[Open3D DEBUG] Residual : 4.52e-04 (# of elements : 3748)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4480, RMSE 0.0065
[Open3D DEBUG] Residual : 4.53e-04 (# of elements : 3749)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4478, RMSE 0.0065
[Open3D DEBUG] Residual : 4.53e-04 (# of elements : 3748)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4476, RMSE 0.0065
[Open3D DEBUG] Residual : 4.53e-04 (# of elements : 3746)
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6535, RMSE 0.0228
[Open3D DEBUG] Residual : 4.35e-04 (# of elements : 447)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6491, RMSE 0.0211
[Open3D DEBUG] Residual : 3.29e-04 (# of elements : 444)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6462, RMSE 0.0209
[Open3D DEBUG] Residual : 3.17e-04 (# of elements : 442)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6447, RMSE 0.0207
[Open3D DEBUG] Residual : 3.15e-04 (# of elements : 441)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.6433, RMSE 0.0206
[Open3D DEBUG] Residual : 3.08e-04 (# of elements : 440)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 2366 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6391, RMSE 0.0112
[Open3D DEBUG] Residual : 2.50e-04 (# of elements : 1512)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6386, RMSE 0.0113
[Open3D DEBUG] Residual : 2.49e-04 (# of elements : 1511)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6386, RMSE 0.0113
[Open3D DEBUG] Residual : 2.45e-04 (# of elements : 1511)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6386, RMSE 0.0113
[Open3D DEBUG] Residual : 2.47e-04 (# of elements : 1511)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6382, RMSE 0.0112
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 1510)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6382, RMSE 0.0112
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 1510)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6382, RMSE 0.0112
[Open3D DEBUG] Residual : 2.48e-04 (# of elements : 1510)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 8369 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6017, RMSE 0.0065
[Open3D DEBUG] Residual : 2.34e-04 (# of elements : 5036)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6001, RMSE 0.0064
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 5022)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5992, RMSE 0.0064
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 5015)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5958, RMSE 0.0064
[Open3D DEBUG] Residual : 2.39e-04 (# of elements : 4986)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5960, RMSE 0.0064
[Open3D DEBUG] Residual : 2.42e-04 (# of elements : 4988)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5964, RMSE 0.0064
[Open3D DEBUG] Residual : 2.42e-04 (# of elements : 4991)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5965, RMSE 0.0064
[Open3D DEBUG] Residual : 2.42e-04 (# of elements : 4992)
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5117, RMSE 0.0273
[Open3D DEBUG] Residual : 7.59e-04 (# of elements : 350)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5190, RMSE 0.0251
[Open3D DEBUG] Residual : 5.64e-04 (# of elements : 355)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5205, RMSE 0.0248
[Open3D DEBUG] Residual : 5.68e-04 (# of elements : 356)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5234, RMSE 0.0251
[Open3D DEBUG] Residual : 5.40e-04 (# of elements : 358)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5205, RMSE 0.0248
[Open3D DEBUG] Residual : 5.12e-04 (# of elements : 356)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5161, RMSE 0.0246
[Open3D DEBUG] Residual : 4.88e-04 (# of elements : 353)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5161, RMSE 0.0246
[Open3D DEBUG] Residual : 4.83e-04 (# of elements : 353)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5161, RMSE 0.0246
[Open3D DEBUG] Residual : 4.88e-04 (# of elements : 353)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5146, RMSE 0.0245
[Open3D DEBUG] Residual : 4.79e-04 (# of elements : 352)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5161, RMSE 0.0246
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 353)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5161, RMSE 0.0246
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 353)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5161, RMSE 0.0246
[Open3D DEBUG] Residual : 4.82e-04 (# of elements : 353)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 2366 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 1013 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4467, RMSE 0.0122
[Open3D DEBUG] Residual : 3.60e-04 (# of elements : 1057)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4476, RMSE 0.0114
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 1059)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4472, RMSE 0.0116
[Open3D DEBUG] Residual : 3.20e-04 (# of elements : 1058)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4467, RMSE 0.0116
[Open3D DEBUG] Residual : 3.16e-04 (# of elements : 1057)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4467, RMSE 0.0117
[Open3D DEBUG] Residual : 3.16e-04 (# of elements : 1057)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4472, RMSE 0.0117
[Open3D DEBUG] Residual : 3.16e-04 (# of elements : 1058)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4472, RMSE 0.0117
[Open3D DEBUG] Residual : 3.16e-04 (# of elements : 1058)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4472, RMSE 0.0117
[Open3D DEBUG] Residual : 3.17e-04 (# of elements : 1058)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 8369 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 3196 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3886, RMSE 0.0067
[Open3D DEBUG] Residual : 2.52e-04 (# of elements : 3252)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3947, RMSE 0.0066
[Open3D DEBUG] Residual : 2.41e-04 (# of elements : 3303)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3960, RMSE 0.0065
[Open3D DEBUG] Residual : 2.41e-04 (# of elements : 3314)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3956, RMSE 0.0065
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 3311)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3956, RMSE 0.0065
[Open3D DEBUG] Residual : 2.41e-04 (# of elements : 3311)
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6491, RMSE 0.0226
[Open3D DEBUG] Residual : 4.71e-04 (# of elements : 444)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6564, RMSE 0.0209
[Open3D DEBUG] Residual : 3.59e-04 (# of elements : 449)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6520, RMSE 0.0204
[Open3D DEBUG] Residual : 3.59e-04 (# of elements : 446)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6535, RMSE 0.0205
[Open3D DEBUG] Residual : 3.63e-04 (# of elements : 447)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6535, RMSE 0.0204
[Open3D DEBUG] Residual : 3.62e-04 (# of elements : 447)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6535, RMSE 0.0204
[Open3D DEBUG] Residual : 3.62e-04 (# of elements : 447)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 2366 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5934, RMSE 0.0118
[Open3D DEBUG] Residual : 2.92e-04 (# of elements : 1404)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5938, RMSE 0.0112
[Open3D DEBUG] Residual : 2.86e-04 (# of elements : 1405)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5934, RMSE 0.0113
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 1404)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5934, RMSE 0.0113
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 1404)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5934, RMSE 0.0113
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 1404)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5934, RMSE 0.0113
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 1404)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5934, RMSE 0.0113
[Open3D DEBUG] Residual : 2.86e-04 (# of elements : 1404)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5934, RMSE 0.0113
[Open3D DEBUG] Residual : 2.86e-04 (# of elements : 1404)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5934, RMSE 0.0113
[Open3D DEBUG] Residual : 2.85e-04 (# of elements : 1404)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 8369 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5419, RMSE 0.0061
[Open3D DEBUG] Residual : 2.40e-04 (# of elements : 4535)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5348, RMSE 0.0062
[Open3D DEBUG] Residual : 2.14e-04 (# of elements : 4476)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5346, RMSE 0.0063
[Open3D DEBUG] Residual : 2.20e-04 (# of elements : 4474)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5328, RMSE 0.0063
[Open3D DEBUG] Residual : 2.18e-04 (# of elements : 4459)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5329, RMSE 0.0063
[Open3D DEBUG] Residual : 2.17e-04 (# of elements : 4460)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5330, RMSE 0.0063
[Open3D DEBUG] Residual : 2.18e-04 (# of elements : 4461)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5329, RMSE 0.0063
[Open3D DEBUG] Residual : 2.19e-04 (# of elements : 4460)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5329, RMSE 0.0063
[Open3D DEBUG] Residual : 2.17e-04 (# of elements : 4460)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5330, RMSE 0.0063
[Open3D DEBUG] Residual : 2.18e-04 (# of elements : 4461)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5329, RMSE 0.0063
[Open3D DEBUG] Residual : 2.19e-04 (# of elements : 4460)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5329, RMSE 0.0063
[Open3D DEBUG] Residual : 2.17e-04 (# of elements : 4460)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5330, RMSE 0.0063
[Open3D DEBUG] Residual : 2.18e-04 (# of elements : 4461)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5329, RMSE 0.0063
[Open3D DEBUG] Residual : 2.19e-04 (# of elements : 4460)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5329, RMSE 0.0063
[Open3D DEBUG] Residual : 2.17e-04 (# of elements : 4460)
[Open3D DEBUG] Read geometry::PointCloud: 40052 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 684 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4269, RMSE 0.0311
[Open3D DEBUG] Residual : 1.19e-03 (# of elements : 292)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4474, RMSE 0.0266
[Open3D DEBUG] Residual : 5.83e-04 (# of elements : 306)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4459, RMSE 0.0261
[Open3D DEBUG] Residual : 5.64e-04 (# of elements : 305)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4503, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4547, RMSE 0.0267
[Open3D DEBUG] Residual : 5.90e-04 (# of elements : 311)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4532, RMSE 0.0268
[Open3D DEBUG] Residual : 5.84e-04 (# of elements : 310)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 309)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.4503, RMSE 0.0266
[Open3D DEBUG] Residual : 5.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.4518, RMSE 0.0267
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 309)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 2366 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3508, RMSE 0.0133
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 830)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3576, RMSE 0.0129
[Open3D DEBUG] Residual : 3.85e-04 (# of elements : 846)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3538, RMSE 0.0128
[Open3D DEBUG] Residual : 4.00e-04 (# of elements : 837)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3546, RMSE 0.0128
[Open3D DEBUG] Residual : 3.97e-04 (# of elements : 839)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3533, RMSE 0.0128
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 836)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3542, RMSE 0.0128
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 838)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3546, RMSE 0.0128
[Open3D DEBUG] Residual : 3.97e-04 (# of elements : 839)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3546, RMSE 0.0128
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 839)
[Open3D DEBUG] Pointcloud down sampled from 40052 points to 8369 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2849, RMSE 0.0068
[Open3D DEBUG] Residual : 3.05e-04 (# of elements : 2384)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2859, RMSE 0.0067
[Open3D DEBUG] Residual : 2.76e-04 (# of elements : 2393)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2847, RMSE 0.0066
[Open3D DEBUG] Residual : 2.76e-04 (# of elements : 2383)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2846, RMSE 0.0066
[Open3D DEBUG] Residual : 2.66e-04 (# of elements : 2382)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2847, RMSE 0.0066
[Open3D DEBUG] Residual : 2.64e-04 (# of elements : 2383)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.2846, RMSE 0.0066
[Open3D DEBUG] Residual : 2.64e-04 (# of elements : 2382)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2847, RMSE 0.0066
[Open3D DEBUG] Residual : 2.63e-04 (# of elements : 2383)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.2851, RMSE 0.0066
[Open3D DEBUG] Residual : 2.63e-04 (# of elements : 2386)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.2851, RMSE 0.0066
[Open3D DEBUG] Residual : 2.64e-04 (# of elements : 2386)
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3921, RMSE 0.0286
[Open3D DEBUG] Residual : 1.47e-03 (# of elements : 318)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3970, RMSE 0.0283
[Open3D DEBUG] Residual : 1.42e-03 (# of elements : 322)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4044, RMSE 0.0284
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 328)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4069, RMSE 0.0284
[Open3D DEBUG] Residual : 1.35e-03 (# of elements : 330)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4069, RMSE 0.0282
[Open3D DEBUG] Residual : 1.30e-03 (# of elements : 330)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4106, RMSE 0.0283
[Open3D DEBUG] Residual : 1.30e-03 (# of elements : 333)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4106, RMSE 0.0283
[Open3D DEBUG] Residual : 1.30e-03 (# of elements : 333)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4106, RMSE 0.0282
[Open3D DEBUG] Residual : 1.29e-03 (# of elements : 333)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4143, RMSE 0.0282
[Open3D DEBUG] Residual : 1.26e-03 (# of elements : 336)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4131, RMSE 0.0277
[Open3D DEBUG] Residual : 1.19e-03 (# of elements : 335)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4081, RMSE 0.0269
[Open3D DEBUG] Residual : 1.19e-03 (# of elements : 331)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4069, RMSE 0.0267
[Open3D DEBUG] Residual : 1.18e-03 (# of elements : 330)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4057, RMSE 0.0264
[Open3D DEBUG] Residual : 1.14e-03 (# of elements : 329)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4057, RMSE 0.0261
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 329)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.4044, RMSE 0.0260
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 328)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.4057, RMSE 0.0262
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 329)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.4057, RMSE 0.0262
[Open3D DEBUG] Residual : 1.14e-03 (# of elements : 329)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.4057, RMSE 0.0260
[Open3D DEBUG] Residual : 1.16e-03 (# of elements : 329)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.4044, RMSE 0.0259
[Open3D DEBUG] Residual : 1.16e-03 (# of elements : 328)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.4057, RMSE 0.0262
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 329)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.4057, RMSE 0.0261
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 329)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 2886 points.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 1410 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3039, RMSE 0.0145
[Open3D DEBUG] Residual : 1.17e-03 (# of elements : 877)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3132, RMSE 0.0144
[Open3D DEBUG] Residual : 1.09e-03 (# of elements : 904)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3146, RMSE 0.0141
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 908)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3177, RMSE 0.0140
[Open3D DEBUG] Residual : 1.07e-03 (# of elements : 917)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3181, RMSE 0.0140
[Open3D DEBUG] Residual : 1.07e-03 (# of elements : 918)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3174, RMSE 0.0139
[Open3D DEBUG] Residual : 1.07e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3164, RMSE 0.0139
[Open3D DEBUG] Residual : 1.07e-03 (# of elements : 913)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3164, RMSE 0.0139
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 913)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3167, RMSE 0.0139
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 914)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3167, RMSE 0.0140
[Open3D DEBUG] Residual : 1.07e-03 (# of elements : 914)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.3174, RMSE 0.0140
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 916)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 9882 points.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 4467 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2190, RMSE 0.0075
[Open3D DEBUG] Residual : 1.22e-03 (# of elements : 2164)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2146, RMSE 0.0073
[Open3D DEBUG] Residual : 1.18e-03 (# of elements : 2121)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2111, RMSE 0.0073
[Open3D DEBUG] Residual : 1.14e-03 (# of elements : 2086)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2194, RMSE 0.0073
[Open3D DEBUG] Residual : 1.03e-03 (# of elements : 2168)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2268, RMSE 0.0073
[Open3D DEBUG] Residual : 9.53e-04 (# of elements : 2241)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.2308, RMSE 0.0073
[Open3D DEBUG] Residual : 9.11e-04 (# of elements : 2281)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2303, RMSE 0.0074
[Open3D DEBUG] Residual : 8.45e-04 (# of elements : 2276)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.2280, RMSE 0.0074
[Open3D DEBUG] Residual : 8.15e-04 (# of elements : 2253)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.2269, RMSE 0.0074
[Open3D DEBUG] Residual : 7.86e-04 (# of elements : 2242)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.2239, RMSE 0.0075
[Open3D DEBUG] Residual : 7.45e-04 (# of elements : 2213)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.2216, RMSE 0.0076
[Open3D DEBUG] Residual : 7.16e-04 (# of elements : 2190)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.2156, RMSE 0.0077
[Open3D DEBUG] Residual : 6.55e-04 (# of elements : 2131)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.2119, RMSE 0.0077
[Open3D DEBUG] Residual : 6.49e-04 (# of elements : 2094)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.2081, RMSE 0.0078
[Open3D DEBUG] Residual : 6.23e-04 (# of elements : 2056)
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4686, RMSE 0.0286
[Open3D DEBUG] Residual : 9.01e-04 (# of elements : 380)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4957, RMSE 0.0247
[Open3D DEBUG] Residual : 6.72e-04 (# of elements : 402)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4908, RMSE 0.0238
[Open3D DEBUG] Residual : 5.85e-04 (# of elements : 398)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4957, RMSE 0.0239
[Open3D DEBUG] Residual : 5.81e-04 (# of elements : 402)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4957, RMSE 0.0238
[Open3D DEBUG] Residual : 5.79e-04 (# of elements : 402)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4957, RMSE 0.0237
[Open3D DEBUG] Residual : 5.84e-04 (# of elements : 402)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4957, RMSE 0.0238
[Open3D DEBUG] Residual : 5.80e-04 (# of elements : 402)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4957, RMSE 0.0237
[Open3D DEBUG] Residual : 5.80e-04 (# of elements : 402)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4957, RMSE 0.0238
[Open3D DEBUG] Residual : 5.78e-04 (# of elements : 402)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4957, RMSE 0.0237
[Open3D DEBUG] Residual : 5.78e-04 (# of elements : 402)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 2886 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 2207 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4536, RMSE 0.0129
[Open3D DEBUG] Residual : 6.15e-04 (# of elements : 1309)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4563, RMSE 0.0122
[Open3D DEBUG] Residual : 6.22e-04 (# of elements : 1317)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4532, RMSE 0.0122
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1308)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4532, RMSE 0.0122
[Open3D DEBUG] Residual : 6.17e-04 (# of elements : 1308)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4518, RMSE 0.0122
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1304)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4515, RMSE 0.0122
[Open3D DEBUG] Residual : 6.35e-04 (# of elements : 1303)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4515, RMSE 0.0122
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1303)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.4515, RMSE 0.0122
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1303)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.4515, RMSE 0.0122
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1303)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.4511, RMSE 0.0121
[Open3D DEBUG] Residual : 6.31e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.4511, RMSE 0.0122
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 1302)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.4515, RMSE 0.0122
[Open3D DEBUG] Residual : 6.30e-04 (# of elements : 1303)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 9882 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 7191 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3974, RMSE 0.0070
[Open3D DEBUG] Residual : 5.92e-04 (# of elements : 3927)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3997, RMSE 0.0070
[Open3D DEBUG] Residual : 5.47e-04 (# of elements : 3950)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4044, RMSE 0.0071
[Open3D DEBUG] Residual : 5.33e-04 (# of elements : 3996)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4028, RMSE 0.0071
[Open3D DEBUG] Residual : 5.24e-04 (# of elements : 3980)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4018, RMSE 0.0071
[Open3D DEBUG] Residual : 5.23e-04 (# of elements : 3971)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4024, RMSE 0.0071
[Open3D DEBUG] Residual : 5.29e-04 (# of elements : 3977)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4022, RMSE 0.0071
[Open3D DEBUG] Residual : 5.29e-04 (# of elements : 3975)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4022, RMSE 0.0071
[Open3D DEBUG] Residual : 5.30e-04 (# of elements : 3975)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4015, RMSE 0.0071
[Open3D DEBUG] Residual : 5.29e-04 (# of elements : 3968)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4019, RMSE 0.0071
[Open3D DEBUG] Residual : 5.30e-04 (# of elements : 3972)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4013, RMSE 0.0071
[Open3D DEBUG] Residual : 5.29e-04 (# of elements : 3966)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4021, RMSE 0.0071
[Open3D DEBUG] Residual : 5.29e-04 (# of elements : 3974)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4020, RMSE 0.0071
[Open3D DEBUG] Residual : 5.30e-04 (# of elements : 3973)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4014, RMSE 0.0071
[Open3D DEBUG] Residual : 5.29e-04 (# of elements : 3967)
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5709, RMSE 0.0288
[Open3D DEBUG] Residual : 9.57e-04 (# of elements : 463)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6030, RMSE 0.0228
[Open3D DEBUG] Residual : 5.09e-04 (# of elements : 489)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5968, RMSE 0.0218
[Open3D DEBUG] Residual : 3.89e-04 (# of elements : 484)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5980, RMSE 0.0219
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 485)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6005, RMSE 0.0221
[Open3D DEBUG] Residual : 3.89e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.71e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6005, RMSE 0.0219
[Open3D DEBUG] Residual : 3.84e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.74e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.82e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.87e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.82e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.87e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.82e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.87e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.82e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.87e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.82e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.87e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.82e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.87e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.83e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.82e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 487)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.6005, RMSE 0.0220
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 487)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 2886 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5582, RMSE 0.0121
[Open3D DEBUG] Residual : 3.39e-04 (# of elements : 1611)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5509, RMSE 0.0119
[Open3D DEBUG] Residual : 3.21e-04 (# of elements : 1590)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5492, RMSE 0.0119
[Open3D DEBUG] Residual : 3.18e-04 (# of elements : 1585)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5492, RMSE 0.0119
[Open3D DEBUG] Residual : 3.19e-04 (# of elements : 1585)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5495, RMSE 0.0119
[Open3D DEBUG] Residual : 3.20e-04 (# of elements : 1586)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5492, RMSE 0.0119
[Open3D DEBUG] Residual : 3.17e-04 (# of elements : 1585)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5492, RMSE 0.0119
[Open3D DEBUG] Residual : 3.16e-04 (# of elements : 1585)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5495, RMSE 0.0119
[Open3D DEBUG] Residual : 3.16e-04 (# of elements : 1586)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5495, RMSE 0.0119
[Open3D DEBUG] Residual : 3.16e-04 (# of elements : 1586)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 9882 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4861, RMSE 0.0069
[Open3D DEBUG] Residual : 2.73e-04 (# of elements : 4804)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4862, RMSE 0.0069
[Open3D DEBUG] Residual : 2.61e-04 (# of elements : 4805)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4857, RMSE 0.0068
[Open3D DEBUG] Residual : 2.56e-04 (# of elements : 4800)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4857, RMSE 0.0068
[Open3D DEBUG] Residual : 2.56e-04 (# of elements : 4800)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4861, RMSE 0.0068
[Open3D DEBUG] Residual : 2.56e-04 (# of elements : 4804)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4859, RMSE 0.0068
[Open3D DEBUG] Residual : 2.55e-04 (# of elements : 4802)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4859, RMSE 0.0068
[Open3D DEBUG] Residual : 2.55e-04 (# of elements : 4802)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4859, RMSE 0.0068
[Open3D DEBUG] Residual : 2.55e-04 (# of elements : 4802)
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 15524 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 321 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4476, RMSE 0.0276
[Open3D DEBUG] Residual : 6.25e-04 (# of elements : 363)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4464, RMSE 0.0236
[Open3D DEBUG] Residual : 4.39e-04 (# of elements : 362)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4427, RMSE 0.0233
[Open3D DEBUG] Residual : 4.42e-04 (# of elements : 359)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4414, RMSE 0.0232
[Open3D DEBUG] Residual : 4.36e-04 (# of elements : 358)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4414, RMSE 0.0231
[Open3D DEBUG] Residual : 4.36e-04 (# of elements : 358)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4414, RMSE 0.0231
[Open3D DEBUG] Residual : 4.36e-04 (# of elements : 358)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 2886 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 1013 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3735, RMSE 0.0131
[Open3D DEBUG] Residual : 4.92e-04 (# of elements : 1078)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3704, RMSE 0.0133
[Open3D DEBUG] Residual : 4.86e-04 (# of elements : 1069)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3683, RMSE 0.0134
[Open3D DEBUG] Residual : 4.65e-04 (# of elements : 1063)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3687, RMSE 0.0135
[Open3D DEBUG] Residual : 4.49e-04 (# of elements : 1064)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3694, RMSE 0.0134
[Open3D DEBUG] Residual : 4.49e-04 (# of elements : 1066)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3680, RMSE 0.0133
[Open3D DEBUG] Residual : 4.37e-04 (# of elements : 1062)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3683, RMSE 0.0133
[Open3D DEBUG] Residual : 4.35e-04 (# of elements : 1063)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3680, RMSE 0.0133
[Open3D DEBUG] Residual : 4.35e-04 (# of elements : 1062)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3680, RMSE 0.0133
[Open3D DEBUG] Residual : 4.35e-04 (# of elements : 1062)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 9882 points.
[Open3D DEBUG] Pointcloud down sampled from 15524 points to 3196 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2896, RMSE 0.0074
[Open3D DEBUG] Residual : 4.30e-04 (# of elements : 2862)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3113, RMSE 0.0070
[Open3D DEBUG] Residual : 3.50e-04 (# of elements : 3076)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3155, RMSE 0.0069
[Open3D DEBUG] Residual : 3.34e-04 (# of elements : 3118)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3148, RMSE 0.0068
[Open3D DEBUG] Residual : 3.26e-04 (# of elements : 3111)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3134, RMSE 0.0068
[Open3D DEBUG] Residual : 3.19e-04 (# of elements : 3097)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3124, RMSE 0.0067
[Open3D DEBUG] Residual : 3.10e-04 (# of elements : 3087)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3124, RMSE 0.0067
[Open3D DEBUG] Residual : 3.09e-04 (# of elements : 3087)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3121, RMSE 0.0067
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 3084)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3125, RMSE 0.0067
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 3088)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3125, RMSE 0.0067
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 3088)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3125, RMSE 0.0067
[Open3D DEBUG] Residual : 3.12e-04 (# of elements : 3088)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3125, RMSE 0.0067
[Open3D DEBUG] Residual : 3.11e-04 (# of elements : 3088)
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5031, RMSE 0.0313
[Open3D DEBUG] Residual : 1.20e-03 (# of elements : 408)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5105, RMSE 0.0234
[Open3D DEBUG] Residual : 5.21e-04 (# of elements : 414)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5092, RMSE 0.0242
[Open3D DEBUG] Residual : 4.67e-04 (# of elements : 413)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5129, RMSE 0.0243
[Open3D DEBUG] Residual : 4.67e-04 (# of elements : 416)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5129, RMSE 0.0243
[Open3D DEBUG] Residual : 4.68e-04 (# of elements : 416)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5129, RMSE 0.0243
[Open3D DEBUG] Residual : 4.68e-04 (# of elements : 416)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 2886 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4245, RMSE 0.0124
[Open3D DEBUG] Residual : 4.00e-04 (# of elements : 1225)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4238, RMSE 0.0123
[Open3D DEBUG] Residual : 3.71e-04 (# of elements : 1223)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4241, RMSE 0.0123
[Open3D DEBUG] Residual : 3.72e-04 (# of elements : 1224)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4245, RMSE 0.0123
[Open3D DEBUG] Residual : 3.85e-04 (# of elements : 1225)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.00e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4258, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1229)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4258, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1229)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4258, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1229)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.01e-04 (# of elements : 1228)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.4255, RMSE 0.0123
[Open3D DEBUG] Residual : 4.04e-04 (# of elements : 1228)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 9882 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3658, RMSE 0.0068
[Open3D DEBUG] Residual : 3.61e-04 (# of elements : 3615)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3642, RMSE 0.0070
[Open3D DEBUG] Residual : 3.71e-04 (# of elements : 3599)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3636, RMSE 0.0071
[Open3D DEBUG] Residual : 3.88e-04 (# of elements : 3593)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3637, RMSE 0.0071
[Open3D DEBUG] Residual : 3.89e-04 (# of elements : 3594)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3642, RMSE 0.0071
[Open3D DEBUG] Residual : 3.86e-04 (# of elements : 3599)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3629, RMSE 0.0071
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 3586)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3623, RMSE 0.0071
[Open3D DEBUG] Residual : 3.78e-04 (# of elements : 3580)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3618, RMSE 0.0072
[Open3D DEBUG] Residual : 3.78e-04 (# of elements : 3575)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3619, RMSE 0.0072
[Open3D DEBUG] Residual : 3.76e-04 (# of elements : 3576)
[Open3D DEBUG] Read geometry::PointCloud: 51696 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 811 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3329, RMSE 0.0270
[Open3D DEBUG] Residual : 1.04e-03 (# of elements : 270)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3292, RMSE 0.0260
[Open3D DEBUG] Residual : 8.46e-04 (# of elements : 267)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3354, RMSE 0.0269
[Open3D DEBUG] Residual : 8.58e-04 (# of elements : 272)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3366, RMSE 0.0270
[Open3D DEBUG] Residual : 8.63e-04 (# of elements : 273)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.60e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.61e-04 (# of elements : 274)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.3379, RMSE 0.0271
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 274)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 2886 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2439, RMSE 0.0142
[Open3D DEBUG] Residual : 7.77e-04 (# of elements : 704)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2415, RMSE 0.0140
[Open3D DEBUG] Residual : 7.79e-04 (# of elements : 697)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2401, RMSE 0.0138
[Open3D DEBUG] Residual : 7.42e-04 (# of elements : 693)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2412, RMSE 0.0136
[Open3D DEBUG] Residual : 7.13e-04 (# of elements : 696)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2426, RMSE 0.0137
[Open3D DEBUG] Residual : 6.91e-04 (# of elements : 700)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.90e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2422, RMSE 0.0137
[Open3D DEBUG] Residual : 6.92e-04 (# of elements : 699)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.91e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.2415, RMSE 0.0136
[Open3D DEBUG] Residual : 6.93e-04 (# of elements : 697)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.90e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.2422, RMSE 0.0137
[Open3D DEBUG] Residual : 6.92e-04 (# of elements : 699)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.91e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.2415, RMSE 0.0136
[Open3D DEBUG] Residual : 6.93e-04 (# of elements : 697)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.90e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.2422, RMSE 0.0137
[Open3D DEBUG] Residual : 6.92e-04 (# of elements : 699)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.91e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.2415, RMSE 0.0136
[Open3D DEBUG] Residual : 6.93e-04 (# of elements : 697)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.90e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.2422, RMSE 0.0137
[Open3D DEBUG] Residual : 6.92e-04 (# of elements : 699)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.91e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.2415, RMSE 0.0136
[Open3D DEBUG] Residual : 6.93e-04 (# of elements : 697)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.90e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.2422, RMSE 0.0137
[Open3D DEBUG] Residual : 6.92e-04 (# of elements : 699)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.91e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.2415, RMSE 0.0136
[Open3D DEBUG] Residual : 6.93e-04 (# of elements : 697)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.90e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.2422, RMSE 0.0137
[Open3D DEBUG] Residual : 6.92e-04 (# of elements : 699)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.91e-04 (# of elements : 698)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.2415, RMSE 0.0136
[Open3D DEBUG] Residual : 6.93e-04 (# of elements : 697)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.2419, RMSE 0.0136
[Open3D DEBUG] Residual : 6.90e-04 (# of elements : 698)
[Open3D DEBUG] Pointcloud down sampled from 51696 points to 9882 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.1728, RMSE 0.0074
[Open3D DEBUG] Residual : 7.18e-04 (# of elements : 1708)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.1748, RMSE 0.0074
[Open3D DEBUG] Residual : 6.48e-04 (# of elements : 1727)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.1726, RMSE 0.0075
[Open3D DEBUG] Residual : 6.33e-04 (# of elements : 1706)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.1721, RMSE 0.0075
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 1701)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.1712, RMSE 0.0076
[Open3D DEBUG] Residual : 5.82e-04 (# of elements : 1692)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.1705, RMSE 0.0076
[Open3D DEBUG] Residual : 5.96e-04 (# of elements : 1685)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.1701, RMSE 0.0077
[Open3D DEBUG] Residual : 5.94e-04 (# of elements : 1681)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.1700, RMSE 0.0077
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 1680)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.1715, RMSE 0.0077
[Open3D DEBUG] Residual : 5.98e-04 (# of elements : 1695)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.1708, RMSE 0.0077
[Open3D DEBUG] Residual : 5.87e-04 (# of elements : 1688)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.1703, RMSE 0.0076
[Open3D DEBUG] Residual : 5.62e-04 (# of elements : 1683)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.1684, RMSE 0.0077
[Open3D DEBUG] Residual : 5.70e-04 (# of elements : 1664)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.1690, RMSE 0.0077
[Open3D DEBUG] Residual : 5.99e-04 (# of elements : 1670)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.1708, RMSE 0.0077
[Open3D DEBUG] Residual : 5.66e-04 (# of elements : 1688)
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2646, RMSE 0.0298
[Open3D DEBUG] Residual : 7.73e-04 (# of elements : 118)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2556, RMSE 0.0294
[Open3D DEBUG] Residual : 7.85e-04 (# of elements : 114)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2646, RMSE 0.0298
[Open3D DEBUG] Residual : 7.85e-04 (# of elements : 118)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2668, RMSE 0.0297
[Open3D DEBUG] Residual : 8.06e-04 (# of elements : 119)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2668, RMSE 0.0294
[Open3D DEBUG] Residual : 8.21e-04 (# of elements : 119)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.2780, RMSE 0.0297
[Open3D DEBUG] Residual : 8.05e-04 (# of elements : 124)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2915, RMSE 0.0305
[Open3D DEBUG] Residual : 8.76e-04 (# of elements : 130)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.2937, RMSE 0.0307
[Open3D DEBUG] Residual : 8.94e-04 (# of elements : 131)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.2915, RMSE 0.0305
[Open3D DEBUG] Residual : 8.99e-04 (# of elements : 130)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.2915, RMSE 0.0304
[Open3D DEBUG] Residual : 9.05e-04 (# of elements : 130)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.2937, RMSE 0.0306
[Open3D DEBUG] Residual : 9.10e-04 (# of elements : 131)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.2937, RMSE 0.0306
[Open3D DEBUG] Residual : 9.14e-04 (# of elements : 131)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.2915, RMSE 0.0305
[Open3D DEBUG] Residual : 9.17e-04 (# of elements : 130)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.2892, RMSE 0.0302
[Open3D DEBUG] Residual : 8.95e-04 (# of elements : 129)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.2892, RMSE 0.0301
[Open3D DEBUG] Residual : 8.91e-04 (# of elements : 129)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.2915, RMSE 0.0303
[Open3D DEBUG] Residual : 8.90e-04 (# of elements : 130)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.2915, RMSE 0.0303
[Open3D DEBUG] Residual : 8.98e-04 (# of elements : 130)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.2915, RMSE 0.0303
[Open3D DEBUG] Residual : 8.90e-04 (# of elements : 130)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.2937, RMSE 0.0305
[Open3D DEBUG] Residual : 8.91e-04 (# of elements : 131)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.2937, RMSE 0.0303
[Open3D DEBUG] Residual : 8.90e-04 (# of elements : 131)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.2937, RMSE 0.0303
[Open3D DEBUG] Residual : 8.90e-04 (# of elements : 131)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 1410 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 2207 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2184, RMSE 0.0164
[Open3D DEBUG] Residual : 7.86e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2177, RMSE 0.0154
[Open3D DEBUG] Residual : 6.46e-04 (# of elements : 307)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2184, RMSE 0.0155
[Open3D DEBUG] Residual : 6.05e-04 (# of elements : 308)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2156, RMSE 0.0156
[Open3D DEBUG] Residual : 6.08e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2064, RMSE 0.0153
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 291)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.1979, RMSE 0.0151
[Open3D DEBUG] Residual : 6.03e-04 (# of elements : 279)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.1965, RMSE 0.0154
[Open3D DEBUG] Residual : 5.71e-04 (# of elements : 277)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.1957, RMSE 0.0154
[Open3D DEBUG] Residual : 5.88e-04 (# of elements : 276)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.1936, RMSE 0.0154
[Open3D DEBUG] Residual : 5.96e-04 (# of elements : 273)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.1908, RMSE 0.0151
[Open3D DEBUG] Residual : 5.82e-04 (# of elements : 269)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.1887, RMSE 0.0148
[Open3D DEBUG] Residual : 5.92e-04 (# of elements : 266)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.1929, RMSE 0.0149
[Open3D DEBUG] Residual : 6.05e-04 (# of elements : 272)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.1957, RMSE 0.0150
[Open3D DEBUG] Residual : 6.03e-04 (# of elements : 276)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.1972, RMSE 0.0149
[Open3D DEBUG] Residual : 6.16e-04 (# of elements : 278)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.1972, RMSE 0.0149
[Open3D DEBUG] Residual : 6.04e-04 (# of elements : 278)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.1993, RMSE 0.0149
[Open3D DEBUG] Residual : 6.04e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.1986, RMSE 0.0147
[Open3D DEBUG] Residual : 6.05e-04 (# of elements : 280)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.2007, RMSE 0.0149
[Open3D DEBUG] Residual : 6.22e-04 (# of elements : 283)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.2000, RMSE 0.0149
[Open3D DEBUG] Residual : 6.22e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.2014, RMSE 0.0151
[Open3D DEBUG] Residual : 6.34e-04 (# of elements : 284)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.2014, RMSE 0.0152
[Open3D DEBUG] Residual : 6.41e-04 (# of elements : 284)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.2000, RMSE 0.0152
[Open3D DEBUG] Residual : 6.48e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.1993, RMSE 0.0151
[Open3D DEBUG] Residual : 6.38e-04 (# of elements : 281)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.2000, RMSE 0.0152
[Open3D DEBUG] Residual : 6.35e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.2007, RMSE 0.0152
[Open3D DEBUG] Residual : 6.46e-04 (# of elements : 283)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.1979, RMSE 0.0150
[Open3D DEBUG] Residual : 6.35e-04 (# of elements : 279)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.2000, RMSE 0.0152
[Open3D DEBUG] Residual : 6.38e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.2000, RMSE 0.0151
[Open3D DEBUG] Residual : 6.38e-04 (# of elements : 282)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.2000, RMSE 0.0151
[Open3D DEBUG] Residual : 6.38e-04 (# of elements : 282)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 4467 points.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 7191 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.1466, RMSE 0.0079
[Open3D DEBUG] Residual : 5.21e-04 (# of elements : 655)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.1518, RMSE 0.0076
[Open3D DEBUG] Residual : 5.01e-04 (# of elements : 678)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.1520, RMSE 0.0076
[Open3D DEBUG] Residual : 5.03e-04 (# of elements : 679)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.1509, RMSE 0.0077
[Open3D DEBUG] Residual : 4.92e-04 (# of elements : 674)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.1495, RMSE 0.0077
[Open3D DEBUG] Residual : 5.08e-04 (# of elements : 668)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.1478, RMSE 0.0077
[Open3D DEBUG] Residual : 5.07e-04 (# of elements : 660)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.1460, RMSE 0.0076
[Open3D DEBUG] Residual : 5.14e-04 (# of elements : 652)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.1462, RMSE 0.0077
[Open3D DEBUG] Residual : 5.20e-04 (# of elements : 653)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.1455, RMSE 0.0077
[Open3D DEBUG] Residual : 5.23e-04 (# of elements : 650)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.1435, RMSE 0.0077
[Open3D DEBUG] Residual : 5.13e-04 (# of elements : 641)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.1428, RMSE 0.0077
[Open3D DEBUG] Residual : 5.16e-04 (# of elements : 638)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.1426, RMSE 0.0077
[Open3D DEBUG] Residual : 5.13e-04 (# of elements : 637)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.1424, RMSE 0.0077
[Open3D DEBUG] Residual : 5.06e-04 (# of elements : 636)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.1422, RMSE 0.0077
[Open3D DEBUG] Residual : 5.06e-04 (# of elements : 635)
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5583, RMSE 0.0298
[Open3D DEBUG] Residual : 2.19e-03 (# of elements : 249)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5605, RMSE 0.0287
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 250)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5695, RMSE 0.0289
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 254)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5561, RMSE 0.0281
[Open3D DEBUG] Residual : 1.93e-03 (# of elements : 248)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5561, RMSE 0.0283
[Open3D DEBUG] Residual : 1.89e-03 (# of elements : 248)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5538, RMSE 0.0285
[Open3D DEBUG] Residual : 1.80e-03 (# of elements : 247)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5471, RMSE 0.0280
[Open3D DEBUG] Residual : 1.76e-03 (# of elements : 244)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5448, RMSE 0.0281
[Open3D DEBUG] Residual : 1.80e-03 (# of elements : 243)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5404, RMSE 0.0284
[Open3D DEBUG] Residual : 1.76e-03 (# of elements : 241)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5404, RMSE 0.0288
[Open3D DEBUG] Residual : 1.71e-03 (# of elements : 241)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5404, RMSE 0.0292
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 241)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5426, RMSE 0.0294
[Open3D DEBUG] Residual : 1.71e-03 (# of elements : 242)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5493, RMSE 0.0297
[Open3D DEBUG] Residual : 1.68e-03 (# of elements : 245)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5538, RMSE 0.0298
[Open3D DEBUG] Residual : 1.69e-03 (# of elements : 247)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.5516, RMSE 0.0296
[Open3D DEBUG] Residual : 1.67e-03 (# of elements : 246)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.5471, RMSE 0.0294
[Open3D DEBUG] Residual : 1.67e-03 (# of elements : 244)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.5471, RMSE 0.0294
[Open3D DEBUG] Residual : 1.66e-03 (# of elements : 244)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.5448, RMSE 0.0293
[Open3D DEBUG] Residual : 1.69e-03 (# of elements : 243)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.5448, RMSE 0.0292
[Open3D DEBUG] Residual : 1.68e-03 (# of elements : 243)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.5471, RMSE 0.0293
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 244)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.5471, RMSE 0.0292
[Open3D DEBUG] Residual : 1.71e-03 (# of elements : 244)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.5448, RMSE 0.0291
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 243)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.5448, RMSE 0.0291
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 243)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.5471, RMSE 0.0292
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 244)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.5471, RMSE 0.0292
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 244)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 1410 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4397, RMSE 0.0157
[Open3D DEBUG] Residual : 1.87e-03 (# of elements : 620)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4206, RMSE 0.0152
[Open3D DEBUG] Residual : 1.78e-03 (# of elements : 593)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4000, RMSE 0.0149
[Open3D DEBUG] Residual : 1.68e-03 (# of elements : 564)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3837, RMSE 0.0147
[Open3D DEBUG] Residual : 1.61e-03 (# of elements : 541)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3759, RMSE 0.0148
[Open3D DEBUG] Residual : 1.67e-03 (# of elements : 530)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3681, RMSE 0.0147
[Open3D DEBUG] Residual : 1.63e-03 (# of elements : 519)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3631, RMSE 0.0147
[Open3D DEBUG] Residual : 1.58e-03 (# of elements : 512)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3518, RMSE 0.0144
[Open3D DEBUG] Residual : 1.53e-03 (# of elements : 496)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3511, RMSE 0.0146
[Open3D DEBUG] Residual : 1.54e-03 (# of elements : 495)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3397, RMSE 0.0152
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 479)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3270, RMSE 0.0151
[Open3D DEBUG] Residual : 1.39e-03 (# of elements : 461)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3227, RMSE 0.0149
[Open3D DEBUG] Residual : 1.32e-03 (# of elements : 455)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3121, RMSE 0.0148
[Open3D DEBUG] Residual : 1.21e-03 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.2993, RMSE 0.0146
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 422)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.2943, RMSE 0.0147
[Open3D DEBUG] Residual : 1.20e-03 (# of elements : 415)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.2943, RMSE 0.0148
[Open3D DEBUG] Residual : 1.24e-03 (# of elements : 415)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.2950, RMSE 0.0148
[Open3D DEBUG] Residual : 1.24e-03 (# of elements : 416)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.2957, RMSE 0.0149
[Open3D DEBUG] Residual : 1.24e-03 (# of elements : 417)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.2936, RMSE 0.0148
[Open3D DEBUG] Residual : 1.23e-03 (# of elements : 414)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.2929, RMSE 0.0147
[Open3D DEBUG] Residual : 1.23e-03 (# of elements : 413)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.2844, RMSE 0.0142
[Open3D DEBUG] Residual : 1.22e-03 (# of elements : 401)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.2872, RMSE 0.0142
[Open3D DEBUG] Residual : 1.22e-03 (# of elements : 405)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.2887, RMSE 0.0143
[Open3D DEBUG] Residual : 1.20e-03 (# of elements : 407)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.2901, RMSE 0.0144
[Open3D DEBUG] Residual : 1.19e-03 (# of elements : 409)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.2915, RMSE 0.0145
[Open3D DEBUG] Residual : 1.20e-03 (# of elements : 411)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.2929, RMSE 0.0145
[Open3D DEBUG] Residual : 1.20e-03 (# of elements : 413)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.2922, RMSE 0.0145
[Open3D DEBUG] Residual : 1.21e-03 (# of elements : 412)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.2929, RMSE 0.0145
[Open3D DEBUG] Residual : 1.22e-03 (# of elements : 413)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.2950, RMSE 0.0146
[Open3D DEBUG] Residual : 1.23e-03 (# of elements : 416)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.2965, RMSE 0.0146
[Open3D DEBUG] Residual : 1.24e-03 (# of elements : 418)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 4467 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2180, RMSE 0.0078
[Open3D DEBUG] Residual : 1.21e-03 (# of elements : 974)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2131, RMSE 0.0079
[Open3D DEBUG] Residual : 1.18e-03 (# of elements : 952)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2046, RMSE 0.0079
[Open3D DEBUG] Residual : 1.15e-03 (# of elements : 914)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2039, RMSE 0.0079
[Open3D DEBUG] Residual : 1.13e-03 (# of elements : 911)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2006, RMSE 0.0079
[Open3D DEBUG] Residual : 1.13e-03 (# of elements : 896)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.1963, RMSE 0.0079
[Open3D DEBUG] Residual : 1.14e-03 (# of elements : 877)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.1930, RMSE 0.0080
[Open3D DEBUG] Residual : 1.13e-03 (# of elements : 862)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.1880, RMSE 0.0079
[Open3D DEBUG] Residual : 1.13e-03 (# of elements : 840)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.1860, RMSE 0.0080
[Open3D DEBUG] Residual : 1.18e-03 (# of elements : 831)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.1854, RMSE 0.0080
[Open3D DEBUG] Residual : 1.17e-03 (# of elements : 828)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.1842, RMSE 0.0080
[Open3D DEBUG] Residual : 1.21e-03 (# of elements : 823)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.1863, RMSE 0.0081
[Open3D DEBUG] Residual : 1.25e-03 (# of elements : 832)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.1865, RMSE 0.0082
[Open3D DEBUG] Residual : 1.26e-03 (# of elements : 833)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.1827, RMSE 0.0081
[Open3D DEBUG] Residual : 1.30e-03 (# of elements : 816)
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5045, RMSE 0.0294
[Open3D DEBUG] Residual : 2.29e-03 (# of elements : 225)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5224, RMSE 0.0298
[Open3D DEBUG] Residual : 2.24e-03 (# of elements : 233)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5336, RMSE 0.0296
[Open3D DEBUG] Residual : 2.23e-03 (# of elements : 238)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5426, RMSE 0.0305
[Open3D DEBUG] Residual : 2.18e-03 (# of elements : 242)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5247, RMSE 0.0298
[Open3D DEBUG] Residual : 2.21e-03 (# of elements : 234)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5179, RMSE 0.0293
[Open3D DEBUG] Residual : 2.17e-03 (# of elements : 231)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5090, RMSE 0.0290
[Open3D DEBUG] Residual : 2.13e-03 (# of elements : 227)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5090, RMSE 0.0292
[Open3D DEBUG] Residual : 2.15e-03 (# of elements : 227)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5067, RMSE 0.0293
[Open3D DEBUG] Residual : 2.14e-03 (# of elements : 226)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5045, RMSE 0.0294
[Open3D DEBUG] Residual : 2.05e-03 (# of elements : 225)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4955, RMSE 0.0291
[Open3D DEBUG] Residual : 2.06e-03 (# of elements : 221)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4865, RMSE 0.0293
[Open3D DEBUG] Residual : 1.98e-03 (# of elements : 217)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4798, RMSE 0.0289
[Open3D DEBUG] Residual : 1.96e-03 (# of elements : 214)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4933, RMSE 0.0293
[Open3D DEBUG] Residual : 2.03e-03 (# of elements : 220)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.4955, RMSE 0.0292
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 221)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.4933, RMSE 0.0290
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 220)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.4955, RMSE 0.0287
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 221)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.5022, RMSE 0.0287
[Open3D DEBUG] Residual : 2.02e-03 (# of elements : 224)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.5067, RMSE 0.0287
[Open3D DEBUG] Residual : 2.06e-03 (# of elements : 226)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.5179, RMSE 0.0286
[Open3D DEBUG] Residual : 2.03e-03 (# of elements : 231)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 1.99e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.5179, RMSE 0.0282
[Open3D DEBUG] Residual : 1.99e-03 (# of elements : 231)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.5179, RMSE 0.0281
[Open3D DEBUG] Residual : 2.03e-03 (# of elements : 231)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.5202, RMSE 0.0282
[Open3D DEBUG] Residual : 2.04e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.5179, RMSE 0.0281
[Open3D DEBUG] Residual : 2.04e-03 (# of elements : 231)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.5157, RMSE 0.0280
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 230)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.5179, RMSE 0.0282
[Open3D DEBUG] Residual : 2.03e-03 (# of elements : 231)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.5179, RMSE 0.0282
[Open3D DEBUG] Residual : 1.98e-03 (# of elements : 231)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.5157, RMSE 0.0280
[Open3D DEBUG] Residual : 1.98e-03 (# of elements : 230)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 1.99e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.5247, RMSE 0.0286
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 234)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.5224, RMSE 0.0285
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 233)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.5224, RMSE 0.0285
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 233)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 1.99e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.5202, RMSE 0.0284
[Open3D DEBUG] Residual : 2.01e-03 (# of elements : 232)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.5202, RMSE 0.0283
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 232)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 1410 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3837, RMSE 0.0161
[Open3D DEBUG] Residual : 2.72e-03 (# of elements : 541)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3809, RMSE 0.0162
[Open3D DEBUG] Residual : 2.10e-03 (# of elements : 537)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3681, RMSE 0.0155
[Open3D DEBUG] Residual : 1.91e-03 (# of elements : 519)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3624, RMSE 0.0157
[Open3D DEBUG] Residual : 1.86e-03 (# of elements : 511)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3553, RMSE 0.0158
[Open3D DEBUG] Residual : 1.80e-03 (# of elements : 501)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3461, RMSE 0.0158
[Open3D DEBUG] Residual : 1.81e-03 (# of elements : 488)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3475, RMSE 0.0160
[Open3D DEBUG] Residual : 1.82e-03 (# of elements : 490)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3411, RMSE 0.0160
[Open3D DEBUG] Residual : 1.85e-03 (# of elements : 481)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3270, RMSE 0.0156
[Open3D DEBUG] Residual : 1.81e-03 (# of elements : 461)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3255, RMSE 0.0155
[Open3D DEBUG] Residual : 1.98e-03 (# of elements : 459)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3213, RMSE 0.0154
[Open3D DEBUG] Residual : 2.06e-03 (# of elements : 453)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3142, RMSE 0.0156
[Open3D DEBUG] Residual : 1.99e-03 (# of elements : 443)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3071, RMSE 0.0156
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3043, RMSE 0.0156
[Open3D DEBUG] Residual : 1.99e-03 (# of elements : 429)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3078, RMSE 0.0157
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 434)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3071, RMSE 0.0157
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3085, RMSE 0.0157
[Open3D DEBUG] Residual : 1.95e-03 (# of elements : 435)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3078, RMSE 0.0157
[Open3D DEBUG] Residual : 1.95e-03 (# of elements : 434)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3121, RMSE 0.0158
[Open3D DEBUG] Residual : 1.95e-03 (# of elements : 440)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3113, RMSE 0.0157
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 439)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3092, RMSE 0.0157
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 436)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3113, RMSE 0.0157
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 439)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3092, RMSE 0.0156
[Open3D DEBUG] Residual : 1.96e-03 (# of elements : 436)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3071, RMSE 0.0156
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3071, RMSE 0.0156
[Open3D DEBUG] Residual : 1.99e-03 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3071, RMSE 0.0156
[Open3D DEBUG] Residual : 1.96e-03 (# of elements : 433)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3099, RMSE 0.0157
[Open3D DEBUG] Residual : 1.94e-03 (# of elements : 437)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3092, RMSE 0.0157
[Open3D DEBUG] Residual : 1.96e-03 (# of elements : 436)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3092, RMSE 0.0157
[Open3D DEBUG] Residual : 2.00e-03 (# of elements : 436)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.3085, RMSE 0.0157
[Open3D DEBUG] Residual : 1.98e-03 (# of elements : 435)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 4467 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.1726, RMSE 0.0084
[Open3D DEBUG] Residual : 1.80e-03 (# of elements : 771)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.1739, RMSE 0.0083
[Open3D DEBUG] Residual : 1.81e-03 (# of elements : 777)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.1751, RMSE 0.0082
[Open3D DEBUG] Residual : 1.84e-03 (# of elements : 782)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.1737, RMSE 0.0081
[Open3D DEBUG] Residual : 1.78e-03 (# of elements : 776)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.1773, RMSE 0.0081
[Open3D DEBUG] Residual : 1.71e-03 (# of elements : 792)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.1798, RMSE 0.0082
[Open3D DEBUG] Residual : 1.68e-03 (# of elements : 803)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.1791, RMSE 0.0082
[Open3D DEBUG] Residual : 1.69e-03 (# of elements : 800)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.1780, RMSE 0.0082
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 795)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.1755, RMSE 0.0082
[Open3D DEBUG] Residual : 1.74e-03 (# of elements : 784)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.1708, RMSE 0.0082
[Open3D DEBUG] Residual : 1.73e-03 (# of elements : 763)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.1733, RMSE 0.0083
[Open3D DEBUG] Residual : 1.77e-03 (# of elements : 774)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.1757, RMSE 0.0085
[Open3D DEBUG] Residual : 1.87e-03 (# of elements : 785)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.1748, RMSE 0.0084
[Open3D DEBUG] Residual : 1.90e-03 (# of elements : 781)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.1699, RMSE 0.0085
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 759)
[Open3D DEBUG] Read geometry::PointCloud: 20665 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 446 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.3206, RMSE 0.0321
[Open3D DEBUG] Residual : 2.78e-03 (# of elements : 143)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.3341, RMSE 0.0309
[Open3D DEBUG] Residual : 2.27e-03 (# of elements : 149)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.3498, RMSE 0.0315
[Open3D DEBUG] Residual : 2.10e-03 (# of elements : 156)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.3543, RMSE 0.0308
[Open3D DEBUG] Residual : 1.97e-03 (# of elements : 158)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.3408, RMSE 0.0297
[Open3D DEBUG] Residual : 1.95e-03 (# of elements : 152)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.3318, RMSE 0.0289
[Open3D DEBUG] Residual : 1.89e-03 (# of elements : 148)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.3341, RMSE 0.0291
[Open3D DEBUG] Residual : 1.81e-03 (# of elements : 149)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.3363, RMSE 0.0293
[Open3D DEBUG] Residual : 1.83e-03 (# of elements : 150)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.3274, RMSE 0.0285
[Open3D DEBUG] Residual : 1.78e-03 (# of elements : 146)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.3386, RMSE 0.0294
[Open3D DEBUG] Residual : 1.72e-03 (# of elements : 151)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.3386, RMSE 0.0295
[Open3D DEBUG] Residual : 1.75e-03 (# of elements : 151)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.3430, RMSE 0.0300
[Open3D DEBUG] Residual : 1.69e-03 (# of elements : 153)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3475, RMSE 0.0303
[Open3D DEBUG] Residual : 1.73e-03 (# of elements : 155)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3498, RMSE 0.0299
[Open3D DEBUG] Residual : 1.98e-03 (# of elements : 156)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3767, RMSE 0.0305
[Open3D DEBUG] Residual : 1.62e-03 (# of elements : 168)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3767, RMSE 0.0303
[Open3D DEBUG] Residual : 1.50e-03 (# of elements : 168)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3744, RMSE 0.0301
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 167)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3834, RMSE 0.0307
[Open3D DEBUG] Residual : 1.44e-03 (# of elements : 171)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3834, RMSE 0.0306
[Open3D DEBUG] Residual : 1.46e-03 (# of elements : 171)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3857, RMSE 0.0307
[Open3D DEBUG] Residual : 1.47e-03 (# of elements : 172)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3901, RMSE 0.0310
[Open3D DEBUG] Residual : 1.46e-03 (# of elements : 174)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3879, RMSE 0.0308
[Open3D DEBUG] Residual : 1.41e-03 (# of elements : 173)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3879, RMSE 0.0308
[Open3D DEBUG] Residual : 1.43e-03 (# of elements : 173)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3834, RMSE 0.0305
[Open3D DEBUG] Residual : 1.41e-03 (# of elements : 171)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3789, RMSE 0.0302
[Open3D DEBUG] Residual : 1.40e-03 (# of elements : 169)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3789, RMSE 0.0301
[Open3D DEBUG] Residual : 1.40e-03 (# of elements : 169)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3789, RMSE 0.0302
[Open3D DEBUG] Residual : 1.40e-03 (# of elements : 169)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3789, RMSE 0.0302
[Open3D DEBUG] Residual : 1.40e-03 (# of elements : 169)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3789, RMSE 0.0302
[Open3D DEBUG] Residual : 1.40e-03 (# of elements : 169)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 1410 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.2525, RMSE 0.0160
[Open3D DEBUG] Residual : 1.39e-03 (# of elements : 356)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2567, RMSE 0.0160
[Open3D DEBUG] Residual : 1.30e-03 (# of elements : 362)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2582, RMSE 0.0160
[Open3D DEBUG] Residual : 1.23e-03 (# of elements : 364)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2518, RMSE 0.0160
[Open3D DEBUG] Residual : 1.22e-03 (# of elements : 355)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2539, RMSE 0.0160
[Open3D DEBUG] Residual : 1.26e-03 (# of elements : 358)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.2546, RMSE 0.0159
[Open3D DEBUG] Residual : 1.14e-03 (# of elements : 359)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2546, RMSE 0.0157
[Open3D DEBUG] Residual : 1.10e-03 (# of elements : 359)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.2603, RMSE 0.0159
[Open3D DEBUG] Residual : 1.14e-03 (# of elements : 367)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.2674, RMSE 0.0157
[Open3D DEBUG] Residual : 1.14e-03 (# of elements : 377)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.2624, RMSE 0.0156
[Open3D DEBUG] Residual : 1.05e-03 (# of elements : 370)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.2837, RMSE 0.0160
[Open3D DEBUG] Residual : 1.08e-03 (# of elements : 400)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.2979, RMSE 0.0160
[Open3D DEBUG] Residual : 1.21e-03 (# of elements : 420)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.3014, RMSE 0.0154
[Open3D DEBUG] Residual : 1.17e-03 (# of elements : 425)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.3255, RMSE 0.0155
[Open3D DEBUG] Residual : 1.31e-03 (# of elements : 459)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.3340, RMSE 0.0147
[Open3D DEBUG] Residual : 1.25e-03 (# of elements : 471)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.3333, RMSE 0.0141
[Open3D DEBUG] Residual : 1.30e-03 (# of elements : 470)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.3277, RMSE 0.0140
[Open3D DEBUG] Residual : 1.25e-03 (# of elements : 462)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.3213, RMSE 0.0141
[Open3D DEBUG] Residual : 1.30e-03 (# of elements : 453)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.3199, RMSE 0.0145
[Open3D DEBUG] Residual : 1.42e-03 (# of elements : 451)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.3106, RMSE 0.0149
[Open3D DEBUG] Residual : 1.43e-03 (# of elements : 438)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.3128, RMSE 0.0148
[Open3D DEBUG] Residual : 1.46e-03 (# of elements : 441)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.3064, RMSE 0.0151
[Open3D DEBUG] Residual : 1.46e-03 (# of elements : 432)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.3128, RMSE 0.0150
[Open3D DEBUG] Residual : 1.46e-03 (# of elements : 441)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.3057, RMSE 0.0151
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 431)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.3135, RMSE 0.0149
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 442)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.3057, RMSE 0.0151
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 431)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.3128, RMSE 0.0149
[Open3D DEBUG] Residual : 1.47e-03 (# of elements : 441)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.3057, RMSE 0.0151
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 431)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.3128, RMSE 0.0149
[Open3D DEBUG] Residual : 1.46e-03 (# of elements : 441)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.3057, RMSE 0.0151
[Open3D DEBUG] Residual : 1.45e-03 (# of elements : 431)
[Open3D DEBUG] Pointcloud down sampled from 20665 points to 4467 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.1907, RMSE 0.0081
[Open3D DEBUG] Residual : 1.43e-03 (# of elements : 852)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.2042, RMSE 0.0080
[Open3D DEBUG] Residual : 1.07e-03 (# of elements : 912)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.2109, RMSE 0.0079
[Open3D DEBUG] Residual : 8.64e-04 (# of elements : 942)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.2107, RMSE 0.0079
[Open3D DEBUG] Residual : 8.29e-04 (# of elements : 941)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.2151, RMSE 0.0078
[Open3D DEBUG] Residual : 8.62e-04 (# of elements : 961)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.2210, RMSE 0.0078
[Open3D DEBUG] Residual : 8.79e-04 (# of elements : 987)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.2225, RMSE 0.0077
[Open3D DEBUG] Residual : 9.11e-04 (# of elements : 994)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.2214, RMSE 0.0077
[Open3D DEBUG] Residual : 8.98e-04 (# of elements : 989)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.2218, RMSE 0.0076
[Open3D DEBUG] Residual : 9.18e-04 (# of elements : 991)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.2227, RMSE 0.0077
[Open3D DEBUG] Residual : 8.95e-04 (# of elements : 995)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.2201, RMSE 0.0076
[Open3D DEBUG] Residual : 8.93e-04 (# of elements : 983)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.2227, RMSE 0.0077
[Open3D DEBUG] Residual : 9.03e-04 (# of elements : 995)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.2221, RMSE 0.0077
[Open3D DEBUG] Residual : 8.99e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.2201, RMSE 0.0076
[Open3D DEBUG] Residual : 8.94e-04 (# of elements : 983)
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 9945 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 238 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6957, RMSE 0.0217
[Open3D DEBUG] Residual : 4.05e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6979, RMSE 0.0226
[Open3D DEBUG] Residual : 4.08e-04 (# of elements : 305)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6957, RMSE 0.0224
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #30: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #31: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #32: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #33: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #34: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #35: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #36: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #37: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #38: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #39: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #40: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #41: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #42: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #43: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #44: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #45: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #46: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #47: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #48: Fitness 0.6957, RMSE 0.0223
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 304)
[Open3D DEBUG] ICP Iteration #49: Fitness 0.6957, RMSE 0.0222
[Open3D DEBUG] Residual : 3.98e-04 (# of elements : 304)
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 737 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6296, RMSE 0.0124
[Open3D DEBUG] Residual : 3.17e-04 (# of elements : 877)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.82e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.6324, RMSE 0.0118
[Open3D DEBUG] Residual : 2.83e-04 (# of elements : 881)
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] Pointcloud down sampled from 9945 points to 2213 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5488, RMSE 0.0063
[Open3D DEBUG] Residual : 2.44e-04 (# of elements : 2510)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5531, RMSE 0.0061
[Open3D DEBUG] Residual : 2.30e-04 (# of elements : 2530)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5529, RMSE 0.0061
[Open3D DEBUG] Residual : 2.29e-04 (# of elements : 2529)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5529, RMSE 0.0061
[Open3D DEBUG] Residual : 2.30e-04 (# of elements : 2529)
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 32313 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 526 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5886, RMSE 0.0215
[Open3D DEBUG] Residual : 4.81e-04 (# of elements : 412)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5886, RMSE 0.0216
[Open3D DEBUG] Residual : 4.60e-04 (# of elements : 412)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5886, RMSE 0.0216
[Open3D DEBUG] Residual : 4.55e-04 (# of elements : 412)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5886, RMSE 0.0215
[Open3D DEBUG] Residual : 4.56e-04 (# of elements : 412)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5886, RMSE 0.0215
[Open3D DEBUG] Residual : 4.56e-04 (# of elements : 412)
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 2207 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 1855 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.6026, RMSE 0.0120
[Open3D DEBUG] Residual : 4.28e-04 (# of elements : 1330)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.6008, RMSE 0.0120
[Open3D DEBUG] Residual : 4.19e-04 (# of elements : 1326)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.6013, RMSE 0.0120
[Open3D DEBUG] Residual : 4.13e-04 (# of elements : 1327)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.6013, RMSE 0.0121
[Open3D DEBUG] Residual : 4.11e-04 (# of elements : 1327)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.6017, RMSE 0.0121
[Open3D DEBUG] Residual : 4.09e-04 (# of elements : 1328)
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 7191 points.
[Open3D DEBUG] Pointcloud down sampled from 32313 points to 6360 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.5436, RMSE 0.0068
[Open3D DEBUG] Residual : 3.85e-04 (# of elements : 3909)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.5357, RMSE 0.0069
[Open3D DEBUG] Residual : 3.79e-04 (# of elements : 3852)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.5319, RMSE 0.0070
[Open3D DEBUG] Residual : 3.71e-04 (# of elements : 3825)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.5307, RMSE 0.0070
[Open3D DEBUG] Residual : 3.75e-04 (# of elements : 3816)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.5301, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3812)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.5316, RMSE 0.0070
[Open3D DEBUG] Residual : 3.74e-04 (# of elements : 3823)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.5318, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3824)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.5314, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3821)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.5316, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3823)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.5315, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3822)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.5318, RMSE 0.0070
[Open3D DEBUG] Residual : 3.74e-04 (# of elements : 3824)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.5315, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3822)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.5318, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3824)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.5315, RMSE 0.0070
[Open3D DEBUG] Residual : 3.73e-04 (# of elements : 3822)
[Open3D DEBUG] Read geometry::PointCloud: 35667 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Read geometry::PointCloud: 22195 vertices.
[Open3D DEBUG] [RemoveNoneFinitePoints] 0 nan points have been removed.
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 700 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 437 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4257, RMSE 0.0273
[Open3D DEBUG] Residual : 9.79e-04 (# of elements : 298)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4571, RMSE 0.0245
[Open3D DEBUG] Residual : 6.41e-04 (# of elements : 320)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4614, RMSE 0.0239
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 323)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4643, RMSE 0.0239
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 325)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4657, RMSE 0.0239
[Open3D DEBUG] Residual : 6.20e-04 (# of elements : 326)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4671, RMSE 0.0239
[Open3D DEBUG] Residual : 6.24e-04 (# of elements : 327)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4671, RMSE 0.0239
[Open3D DEBUG] Residual : 6.24e-04 (# of elements : 327)
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 2207 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 1393 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4431, RMSE 0.0123
[Open3D DEBUG] Residual : 6.52e-04 (# of elements : 978)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4463, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 985)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.20e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.15e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.25e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.24e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4499, RMSE 0.0122
[Open3D DEBUG] Residual : 6.23e-04 (# of elements : 993)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.32e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #14: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #15: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #16: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #17: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #18: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #19: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #20: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #21: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #22: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #23: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #24: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #25: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #26: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #27: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] ICP Iteration #28: Fitness 0.4486, RMSE 0.0121
[Open3D DEBUG] Residual : 6.18e-04 (# of elements : 990)
[Open3D DEBUG] ICP Iteration #29: Fitness 0.4495, RMSE 0.0121
[Open3D DEBUG] Residual : 6.12e-04 (# of elements : 992)
[Open3D DEBUG] Pointcloud down sampled from 35667 points to 7191 points.
[Open3D DEBUG] Pointcloud down sampled from 22195 points to 4574 points.
[Open3D DEBUG] InitializePointCloudForColoredICP
[Open3D DEBUG] ICP Iteration #0: Fitness 0.4101, RMSE 0.0065
[Open3D DEBUG] Residual : 5.45e-04 (# of elements : 2949)
[Open3D DEBUG] ICP Iteration #1: Fitness 0.4155, RMSE 0.0066
[Open3D DEBUG] Residual : 5.16e-04 (# of elements : 2988)
[Open3D DEBUG] ICP Iteration #2: Fitness 0.4158, RMSE 0.0066
[Open3D DEBUG] Residual : 5.19e-04 (# of elements : 2990)
[Open3D DEBUG] ICP Iteration #3: Fitness 0.4162, RMSE 0.0066
[Open3D DEBUG] Residual : 5.16e-04 (# of elements : 2993)
[Open3D DEBUG] ICP Iteration #4: Fitness 0.4164, RMSE 0.0066
[Open3D DEBUG] Residual : 5.16e-04 (# of elements : 2994)
[Open3D DEBUG] ICP Iteration #5: Fitness 0.4166, RMSE 0.0066
[Open3D DEBUG] Residual : 5.17e-04 (# of elements : 2996)
[Open3D DEBUG] ICP Iteration #6: Fitness 0.4166, RMSE 0.0066
[Open3D DEBUG] Residual : 5.17e-04 (# of elements : 2996)
[Open3D DEBUG] ICP Iteration #7: Fitness 0.4165, RMSE 0.0066
[Open3D DEBUG] Residual : 5.18e-04 (# of elements : 2995)
[Open3D DEBUG] ICP Iteration #8: Fitness 0.4166, RMSE 0.0066
[Open3D DEBUG] Residual : 5.17e-04 (# of elements : 2996)
[Open3D DEBUG] ICP Iteration #9: Fitness 0.4166, RMSE 0.0066
[Open3D DEBUG] Residual : 5.16e-04 (# of elements : 2996)
[Open3D DEBUG] ICP Iteration #10: Fitness 0.4168, RMSE 0.0066
[Open3D DEBUG] Residual : 5.18e-04 (# of elements : 2997)
[Open3D DEBUG] ICP Iteration #11: Fitness 0.4164, RMSE 0.0066
[Open3D DEBUG] Residual : 5.17e-04 (# of elements : 2994)
[Open3D DEBUG] ICP Iteration #12: Fitness 0.4166, RMSE 0.0066
[Open3D DEBUG] Residual : 5.18e-04 (# of elements : 2996)
[Open3D DEBUG] ICP Iteration #13: Fitness 0.4165, RMSE 0.0066
[Open3D DEBUG] Residual : 5.17e-04 (# of elements : 2995)
[Open3D DEBUG] Validating PoseGraph - finished.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 10 nodes and 35 edges.
[Open3D DEBUG] Line process weight : 74.734800
[Open3D DEBUG] [Initial     ] residual : 3.763148e+04, lambda : 9.008583e-02
[Open3D DEBUG] [Iteration 00] residual : 2.633536e+03, valid edges : 5, time : 0.000 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.212536e+03, valid edges : 19, time : 0.000 sec.
[Open3D DEBUG] [Iteration 02] residual : 6.503863e+02, valid edges : 20, time : 0.000 sec.
[Open3D DEBUG] [Iteration 03] residual : 4.958651e+02, valid edges : 24, time : 0.000 sec.
[Open3D DEBUG] [Iteration 04] residual : 3.866140e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 05] residual : 3.698281e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 06] residual : 3.661318e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 07] residual : 3.650482e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 08] residual : 3.647596e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 09] residual : 3.646878e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 10] residual : 3.646694e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 11] residual : 3.646643e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 12] residual : 3.646627e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 13] residual : 3.646621e+02, valid edges :
reading dataset/realsense/fragments/fragment_002.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_007.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_001.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_003.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_002.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_004.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_007.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_003.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_005.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_004.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_008.ply ...
reading dataset/realsense/fragments/fragment_009.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_005.ply ...
reading dataset/realsense/fragments/fragment_006.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
reading dataset/realsense/fragments/fragment_005.ply ...
reading dataset/realsense/fragments/fragment_008.ply ...
voxel_size 0.050000
voxel_size 0.025000
voxel_size 0.012500
registration::PoseGraph with 10 nodes and 35 edges.
integrate the whole RGBD sequence using estimated camera pose.
Fragment 000 / 009 :: integrate rgbd frame 0 (1 of 100).
Fragment 000 / 009 :: integrate rgbd frame 1 (2 of 100).
Fragment 000 / 009 :: integrate rgbd frame 2 (3 of 100).
Fragment 000 / 009 :: integrate rgbd frame 3 (4 of 100).
Fragment 000 / 009 :: integrate rgbd frame 4 (5 of 100).
Fragment 000 / 009 :: integrate rgbd frame 5 (6 of 100).
Fragment 000 / 009 :: integrate rgbd frame 6 (7 of 100).
Fragment 000 / 009 :: integrate rgbd frame 7 (8 of 100).
Fragment 000 / 009 :: integrate rgbd frame 8 (9 of 100).
Fragment 000 / 009 :: integrate rgbd frame 9 (10 of 100).
Fragment 000 / 009 :: integrate rgbd frame 10 (11 of 100).
Fragment 000 / 009 :: integrate rgbd frame 11 (12 of 100).
Fragment 000 / 009 :: integrate rgbd frame 12 (13 of 100).
Fragment 000 / 009 :: integrate rgbd frame 13 (14 of 100).
Fragment 000 / 009 :: integrate rgbd frame 14 (15 of 100).
Fragment 000 / 009 :: integrate rgbd frame 15 (16 of 100).
Fragment 000 / 009 :: integrate rgbd frame 16 (17 of 100).
Fragment 000 / 009 :: integrate rgbd frame 17 (18 of 100).
Fragment 000 / 009 :: integrate rgbd frame 18 (19 of 100).
Fragment 000 / 009 :: integrate rgbd frame 19 (20 of 100).
Fragment 000 / 009 :: integrate rgbd frame 20 (21 of 100).
Fragment 000 / 009 :: integrate rgbd frame 21 (22 of 100).
Fragment 000 / 009 :: integrate rgbd frame 22 (23 of 100).
Fragment 000 / 009 :: integrate rgbd frame 23 (24 of 100).
Fragment 000 / 009 :: integrate rgbd frame 24 (25 of 100).
Fragment 000 / 009 :: integrate rgbd frame 25 (26 of 100).
Fragment 000 / 009 :: integrate rgbd frame 26 (27 of 100).
Fragment 000 / 009 :: integrate rgbd frame 27 (28 of 100).
Fragment 000 / 009 :: integrate rgbd frame 28 (29 of 100).
Fragment 000 / 009 :: integrate rgbd frame 29 (30 of 100).
Fragment 000 / 009 :: integrate rgbd frame 30 (31 of 100).
Fragment 000 / 009 :: integrate rgbd frame 31 (32 of 100).
Fragment 000 / 009 :: integrate rgbd frame 32 (33 of 100).
Fragment 000 / 009 :: integrate rgbd frame 33 (34 of 100).
Fragment 000 / 009 :: integrate rgbd frame 34 (35 of 100).
Fragment 000 / 009 :: integrate rgbd frame 35 (36 of 100).
Fragment 000 / 009 :: integrate rgbd frame 36 (37 of 100).
Fragment 000 / 009 :: integrate rgbd frame 37 (38 of 100).
Fragment 000 / 009 :: integrate rgbd frame 38 (39 of 100).
Fragment 000 / 009 :: integrate rgbd frame 39 (40 of 100).
Fragment 000 / 009 :: integrate rgbd frame 40 (41 of 100).
Fragment 000 / 009 :: integrate rgbd frame 41 (42 of 100).
Fragment 000 / 009 :: integrate rgbd frame 42 (43 of 100).
Fragment 000 / 009 :: integrate rgbd frame 43 (44 of 100).
Fragment 000 / 009 :: integrate rgbd frame 44 (45 of 100).
Fragment 000 / 009 :: integrate rgbd frame 45 (46 of 100).
Fragment 000 / 009 :: integrate rgbd frame 46 (47 of 100).
Fragment 000 / 009 :: integrate rgbd frame 47 (48 of 100).
Fragment 000 / 009 :: integrate rgbd frame 48 (49 of 100).
Fragment 000 / 009 :: integrate rgbd frame 49 (50 of 100).
Fragment 000 / 009 :: integrate rgbd frame 50 (51 of 100).
Fragment 000 / 009 :: integrate rgbd frame 51 (52 of 100).
Fragment 000 / 009 :: integrate rgbd frame 52 (53 of 100).
Fragment 000 / 009 :: integrate rgbd frame 53 (54 of 100).
Fragment 000 / 009 :: integrate rgbd frame 54 (55 of 100).
Fragment 000 / 009 :: integrate rgbd frame 55 (56 of 100).
Fragment 000 / 009 :: integrate rgbd frame 56 (57 of 100).
Fragment 000 / 009 :: integrate rgbd frame 57 (58 of 100).
Fragment 000 / 009 :: integrate rgbd frame 58 (59 of 100).
Fragment 000 / 009 :: integrate rgbd frame 59 (60 of 100).
Fragment 000 / 009 :: integrate rgbd frame 60 (61 of 100).
Fragment 000 / 009 :: integrate rgbd frame 61 (62 of 100).
Fragment 000 / 009 :: integrate rgbd frame 62 (63 of 100).
Fragment 000 / 009 :: integrate rgbd frame 63 (64 of 100).
Fragment 000 / 009 :: integrate rgbd frame 64 (65 of 100).
Fragment 000 / 009 :: integrate rgbd frame 65 (66 of 100).
Fragment 000 / 009 :: integrate rgbd frame 66 (67 of 100).
Fragment 000 / 009 :: integrate rgbd frame 67 (68 of 100).
Fragment 000 / 009 :: integrate rgbd frame 68 (69 of 100).
Fragment 000 / 009 :: integrate rgbd frame 69 (70 of 100).
Fragment 000 / 009 :: integrate rgbd frame 70 (71 of 100).
Fragment 000 / 009 :: integrate rgbd frame 71 (72 of 100).
Fragment 000 / 009 :: integrate rgbd frame 72 (73 of 100).
Fragment 000 / 009 :: integrate rgbd frame 73 (74 of 100).
Fragment 000 / 009 :: integrate rgbd frame 74 (75 of 100).
Fragment 000 / 009 :: integrate rgbd frame 75 (76 of 100).
Fragment 000 / 009 :: integrate rgbd frame 76 (77 of 100).
Fragment 000 / 009 :: integrate rgbd frame 77 (78 of 100).
Fragment 000 / 009 :: integrate rgbd frame 78 (79 of 100).
Fragment 000 / 009 :: integrate rgbd frame 79 (80 of 100).
Fragment 000 / 009 :: integrate rgbd frame 80 (81 of 100).
Fragment 000 / 009 :: integrate rgbd frame 81 (82 of 100).
Fragment 000 / 009 :: integrate rgbd frame 82 (83 of 100).
Fragment 000 / 009 :: integrate rgbd frame 83 (84 of 100).
Fragment 000 / 009 :: integrate rgbd frame 84 (85 of 100).
Fragment 000 / 009 :: integrate rgbd frame 85 (86 of 100).
Fragment 000 / 009 :: integrate rgbd frame 86 (87 of 100).
Fragment 000 / 009 :: integrate rgbd frame 87 (88 of 100).
Fragment 000 / 009 :: integrate rgbd frame 88 (89 of 100).
Fragment 000 / 009 :: integrate rgbd frame 89 (90 of 100).
Fragment 000 / 009 :: integrate rgbd frame 90 (91 of 100).
Fragment 000 / 009 :: integrate rgbd frame 91 (92 of 100).
Fragment 000 / 009 :: integrate rgbd frame 92 (93 of 100).
Fragment 000 / 009 :: integrate rgbd frame 93 (94 of 100).
Fragment 000 / 009 :: integrate rgbd frame 94 (95 of 100).
Fragment 000 / 009 :: integrate rgbd frame 95 (96 of 100).
Fragment 000 / 009 :: integrate rgbd frame 96 (97 of 100).
Fragment 000 / 009 :: integrate rgbd frame 97 (98 of 100).
Fragment 000 / 009 :: integrate rgbd frame 98 (99 of 100).
Fragment 000 / 009 :: integrate rgbd frame 99 (100 of 100).
Fragment 001 / 009 :: integrate rgbd frame 100 (1 of 100).
Fragment 001 / 009 :: integrate rgbd frame 101 (2 of 100).
Fragment 001 / 009 :: integrate rgbd frame 102 (3 of 100).
Fragment 001 / 009 :: integrate rgbd frame 103 (4 of 100).
Fragment 001 / 009 :: integrate rgbd frame 104 (5 of 100).
Fragment 001 / 009 :: integrate rgbd frame 105 (6 of 100).
Fragment 001 / 009 :: integrate rgbd frame 106 (7 of 100).
Fragment 001 / 009 :: integrate rgbd frame 107 (8 of 100).
Fragment 001 / 009 :: integrate rgbd frame 108 (9 of 100).
Fragment 001 / 009 :: integrate rgbd frame 109 (10 of 100).
Fragment 001 / 009 :: integrate rgbd frame 110 (11 of 100).
Fragment 001 / 009 :: integrate rgbd frame 111 (12 of 100).
Fragment 001 / 009 :: integrate rgbd frame 112 (13 of 100).
Fragment 001 / 009 :: integrate rgbd frame 113 (14 of 100).
Fragment 001 / 009 :: integrate rgbd frame 114 (15 of 100).
Fragment 001 / 009 :: integrate rgbd frame 115 (16 of 100).
Fragment 001 / 009 :: integrate rgbd frame 116 (17 of 100).
Fragment 001 / 009 :: integrate rgbd frame 117 (18 of 100).
Fragment 001 / 009 :: integrate rgbd frame 118 (19 of 100).
Fragment 001 / 009 :: integrate rgbd frame 119 (20 of 100).
Fragment 001 / 009 :: integrate rgbd frame 120 (21 of 100).
Fragment 001 / 009 :: integrate rgbd frame 121 (22 of 100).
Fragment 001 / 009 :: integrate rgbd frame 122 (23 of 100).
Fragment 001 / 009 :: integrate rgbd frame 123 (24 of 100).
Fragment 001 / 009 :: integrate rgbd frame 124 (25 of 100).
Fragment 001 / 009 :: integrate rgbd frame 125 (26 of 100).
Fragment 001 / 009 :: integrate rgbd frame 126 (27 of 100).
Fragment 001 / 009 :: integrate rgbd frame 127 (28 of 100).
Fragment 001 / 009 :: integrate rgbd frame 128 (29 of 100).
Fragment 001 / 009 :: integrate rgbd frame 129 (30 of 100).
Fragment 001 / 009 :: integrate rgbd frame 130 (31 of 100).
Fragment 001 / 009 :: integrate rgbd frame 131 (32 of 100).
Fragment 001 / 009 :: integrate rgbd frame 132 (33 of 100).
Fragment 001 / 009 :: integrate rgbd frame 133 (34 of 100).
Fragment 001 / 009 :: integrate rgbd frame 134 (35 of 100).
Fragment 001 / 009 :: integrate rgbd frame 135 (36 of 100).
Fragment 001 / 009 :: integrate rgbd frame 136 (37 of 100).
Fragment 001 / 009 :: integrate rgbd frame 137 (38 of 100).
Fragment 001 / 009 :: integrate rgbd frame 138 (39 of 100).
Fragment 001 / 009 :: integrate rgbd frame 139 (40 of 100).
Fragment 001 / 009 :: integrate rgbd frame 140 (41 of 100).
Fragment 001 / 009 :: integrate rgbd frame 141 (42 of 100).
Fragment 001 / 009 :: integrate rgbd frame 142 (43 of 100).
Fragment 001 / 009 :: integrate rgbd frame 143 (44 of 100).
Fragment 001 / 009 :: integrate rgbd frame 144 (45 of 100).
Fragment 001 / 009 :: integrate rgbd frame 145 (46 of 100).
Fragment 001 / 009 :: integrate rgbd frame 146 (47 of 100).
Fragment 001 / 009 :: integrate rgbd frame 147 (48 of 100).
Fragment 001 / 009 :: integrate rgbd frame 148 (49 of 100).
Fragment 001 / 009 :: integrate rgbd frame 149 (50 of 100).
Fragment 001 / 009 :: integrate rgbd frame 150 (51 of 100).
Fragment 001 / 009 :: integrate rgbd frame 151 (52 of 100).
Fragment 001 / 009 :: integrate rgbd frame 152 (53 of 100).
Fragment 001 / 009 :: integrate rgbd frame 153 (54 of 100).
Fragment 001 / 009 :: integrate rgbd frame 154 (55 of 100).
Fragment 001 / 009 :: integrate rgbd frame 155 (56 of 100).
Fragment 001 / 009 :: integrate rgbd frame 156 (57 of 100).
Fragment 001 / 009 :: integrate rgbd frame 157 (58 of 100).
Fragment 001 / 009 :: integrate rgbd frame 158 (59 of 100).
Fragment 001 / 009 :: integrate rgbd frame 159 (60 of 100).
Fragment 001 / 009 :: integrate rgbd frame 160 (61 of 100).
Fragment 001 / 009 :: integrate rgbd frame 161 (62 of 100).
Fragment 001 / 009 :: integrate rgbd frame 162 (63 of 100).
Fragment 001 / 009 :: integrate rgbd frame 163 (64 of 100).
Fragment 001 / 009 :: integrate rgbd frame 164 (65 of 100).
Fragment 001 / 009 :: integrate rgbd frame 165 (66 of 100).
Fragment 001 / 009 :: integrate rgbd frame 166 (67 of 100).
Fragment 001 / 009 :: integrate rgbd frame 167 (68 of 100).
Fragment 001 / 009 :: integrate rgbd frame 168 (69 of 100).
Fragment 001 / 009 :: integrate rgbd frame 169 (70 of 100).
Fragment 001 / 009 :: integrate rgbd frame 170 (71 of 100).
Fragment 001 / 009 :: integrate rgbd frame 171 (72 of 100).
Fragment 001 / 009 :: integrate rgbd frame 172 (73 of 100).
Fragment 001 / 009 :: integrate rgbd frame 173 (74 of 100).
Fragment 001 / 009 :: integrate rgbd frame 174 (75 of 100).
Fragment 001 / 009 :: integrate rgbd frame 175 (76 of 100).
Fragment 001 / 009 :: integrate rgbd frame 176 (77 of 100).
Fragment 001 / 009 :: integrate rgbd frame 177 (78 of 100).
Fragment 001 / 009 :: integrate rgbd frame 178 (79 of 100).
Fragment 001 / 009 :: integrate rgbd frame 179 (80 of 100).
Fragment 001 / 009 :: integrate rgbd frame 180 (81 of 100).
Fragment 001 / 009 :: integrate rgbd frame 181 (82 of 100).
Fragment 001 / 009 :: integrate rgbd frame 182 (83 of 100).
Fragment 001 / 009 :: integrate rgbd frame 183 (84 of 100).
Fragment 001 / 009 :: integrate rgbd frame 184 (85 of 100).
Fragment 001 / 009 :: integrate rgbd frame 185 (86 of 100).
Fragment 001 / 009 :: integrate rgbd frame 186 (87 of 100).
Fragment 001 / 009 :: integrate rgbd frame 187 (88 of 100).
Fragment 001 / 009 :: integrate rgbd frame 188 (89 of 100).
Fragment 001 / 009 :: integrate rgbd frame 189 (90 of 100).
Fragment 001 / 009 :: integrate rgbd frame 190 (91 of 100).
Fragment 001 / 009 :: integrate rgbd frame 191 (92 of 100).
Fragment 001 / 009 :: integrate rgbd frame 192 (93 of 100).
Fragment 001 / 009 :: integrate rgbd frame 193 (94 of 100).
Fragment 001 / 009 :: integrate rgbd frame 194 (95 of 100).
Fragment 001 / 009 :: integrate rgbd frame 195 (96 of 100).
Fragment 001 / 009 :: integrate rgbd frame 196 (97 of 100).
Fragment 001 / 009 :: integrate rgbd frame 197 (98 of 100).
Fragment 001 / 009 :: integrate rgbd frame 198 (99 of 100).
Fragment 001 / 009 :: integrate rgbd frame 199 (100 of 100).
Fragment 002 / 009 :: integrate rgbd frame 200 (1 of 100).
Fragment 002 / 009 :: integrate rgbd frame 201 (2 of 100).
Fragment 002 / 009 :: integrate rgbd frame 202 (3 of 100).
Fragment 002 / 009 :: integrate rgbd frame 203 (4 of 100).
Fragment 002 / 009 :: integrate rgbd frame 204 (5 of 100).
Fragment 002 / 009 :: integrate rgbd frame 205 (6 of 100).
Fragment 002 / 009 :: integrate rgbd frame 206 (7 of 100).
Fragment 002 / 009 :: integrate rgbd frame 207 (8 of 100).
Fragment 002 / 009 :: integrate rgbd frame 208 (9 of 100).
Fragment 002 / 009 :: integrate rgbd frame 209 (10 of 100).
Fragment 002 / 009 :: integrate rgbd frame 210 (11 of 100).
Fragment 002 / 009 :: integrate rgbd frame 211 (12 of 100).
Fragment 002 / 009 :: integrate rgbd frame 212 (13 of 100).
Fragment 002 / 009 :: integrate rgbd frame 213 (14 of 100).
Fragment 002 / 009 :: integrate rgbd frame 214 (15 of 100).
Fragment 002 / 009 :: integrate rgbd frame 215 (16 of 100).
Fragment 002 / 009 :: integrate rgbd frame 216 (17 of 100).
Fragment 002 / 009 :: integrate rgbd frame 217 (18 of 100).
Fragment 002 / 009 :: integrate rgbd frame 218 (19 of 100).
Fragment 002 / 009 :: integrate rgbd frame 219 (20 of 100).
Fragment 002 / 009 :: integrate rgbd frame 220 (21 of 100).
Fragment 002 / 009 :: integrate rgbd frame 221 (22 of 100).
Fragment 002 / 009 :: integrate rgbd frame 222 (23 of 100).
Fragment 002 / 009 :: integrate rgbd frame 223 (24 of 100).
Fragment 002 / 009 :: integrate rgbd frame 224 (25 of 100).
Fragment 002 / 009 :: integrate rgbd frame 225 (26 of 100).
Fragment 002 / 009 :: integrate rgbd frame 226 (27 of 100).
Fragment 002 / 009 :: integrate rgbd frame 227 (28 of 100).
Fragment 002 / 009 :: integrate rgbd frame 228 (29 of 100).
Fragment 002 / 009 :: integrate rgbd frame 229 (30 of 100).
Fragment 002 / 009 :: integrate rgbd frame 230 (31 of 100).
Fragment 002 / 009 :: integrate rgbd frame 231 (32 of 100).
Fragment 002 / 009 :: integrate rgbd frame 232 (33 of 100).
Fragment 002 / 009 :: integrate rgbd frame 233 (34 of 100).
Fragment 002 / 009 :: integrate rgbd frame 234 (35 of 100).
Fragment 002 / 009 :: integrate rgbd frame 235 (36 of 100).
Fragment 002 / 009 :: integrate rgbd frame 236 (37 of 100).
Fragment 002 / 009 :: integrate rgbd frame 237 (38 of 100).
Fragment 002 / 009 :: integrate rgbd frame 238 (39 of 100).
Fragment 002 / 009 :: integrate rgbd frame 239 (40 of 100).
Fragment 002 / 009 :: integrate rgbd frame 240 (41 of 100).
Fragment 002 / 009 :: integrate rgbd frame 241 (42 of 100).
Fragment 002 / 009 :: integrate rgbd frame 242 (43 of 100).
Fragment 002 / 009 :: integrate rgbd frame 243 (44 of 100).
Fragment 002 / 009 :: integrate rgbd frame 244 (45 of 100).
Fragment 002 / 009 :: integrate rgbd frame 245 (46 of 100).
Fragment 002 / 009 :: integrate rgbd frame 246 (47 of 100).
Fragment 002 / 009 :: integrate rgbd frame 247 (48 of 100).
Fragment 002 / 009 :: integrate rgbd frame 248 (49 of 100).
Fragment 002 / 009 :: integrate rgbd frame 249 (50 of 100).
Fragment 002 / 009 :: integrate rgbd frame 250 (51 of 100).
Fragment 002 / 009 :: integrate rgbd frame 251 (52 of 100).
Fragment 002 / 009 :: integrate rgbd frame 252 (53 of 100).
Fragment 002 / 009 :: integrate rgbd frame 253 (54 of 100).
Fragment 002 / 009 :: integrate rgbd frame 254 (55 of 100).
Fragment 002 / 009 :: integrate rgbd frame 255 (56 of 100).
Fragment 002 / 009 :: integrate rgbd frame 256 (57 of 100).
Fragment 002 / 009 :: integrate rgbd frame 257 (58 of 100).
Fragment 002 / 009 :: integrate rgbd frame 258 (59 of 100).
Fragment 002 / 009 :: integrate rgbd frame 259 (60 of 100).
Fragment 002 / 009 :: integrate rgbd frame 260 (61 of 100).
Fragment 002 / 009 :: integrate rgbd frame 261 (62 of 100).
Fragment 002 / 009 :: integrate rgbd frame 262 (63 of 100).
Fragment 002 / 009 :: integrate rgbd frame 263 (64 of 100).
Fragment 002 / 009 :: integrate rgbd frame 264 (65 of 100).
Fragment 002 / 009 :: integrate rgbd frame 265 (66 of 100).
Fragment 002 / 009 :: integrate rgbd frame 266 (67 of 100).
Fragment 002 / 009 :: integrate rgbd frame 267 (68 of 100).
Fragment 002 / 009 :: integrate rgbd frame 268 (69 of 100).
Fragment 002 / 009 :: integrate rgbd frame 269 (70 of 100).
Fragment 002 / 009 :: integrate rgbd frame 270 (71 of 100).
Fragment 002 / 009 :: integrate rgbd frame 271 (72 of 100).
Fragment 002 / 009 :: integrate rgbd frame 272 (73 of 100).
Fragment 002 / 009 :: integrate rgbd frame 273 (74 of 100).
Fragment 002 / 009 :: integrate rgbd frame 274 (75 of 100).
Fragment 002 / 009 :: integrate rgbd frame 275 (76 of 100).
Fragment 002 / 009 :: integrate rgbd frame 276 (77 of 100).
Fragment 002 / 009 :: integrate rgbd frame 277 (78 of 100).
Fragment 002 / 009 :: integrate rgbd frame 278 (79 of 100).
Fragment 002 / 009 :: integrate rgbd frame 279 (80 of 100).
Fragment 002 / 009 :: integrate rgbd frame 280 (81 of 100).
Fragment 002 / 009 :: integrate rgbd frame 281 (82 of 100).
Fragment 002 / 009 :: integrate rgbd frame 282 (83 of 100).
Fragment 002 / 009 :: integrate rgbd frame 283 (84 of 100).
Fragment 002 / 009 :: integrate rgbd frame 284 (85 of 100).
Fragment 002 / 009 :: integrate rgbd frame 285 (86 of 100).
Fragment 002 / 009 :: integrate rgbd frame 286 (87 of 100).
Fragment 002 / 009 :: integrate rgbd frame 287 (88 of 100).
Fragment 002 / 009 :: integrate rgbd frame 288 (89 of 100).
Fragment 002 / 009 :: integrate rgbd frame 289 (90 of 100).
Fragment 002 / 009 :: integrate rgbd frame 290 (91 of 100).
Fragment 002 / 009 :: integrate rgbd frame 291 (92 of 100).
Fragment 002 / 009 :: integrate rgbd frame 292 (93 of 100).
Fragment 002 / 009 :: integrate rgbd frame 293 (94 of 100).
Fragment 002 / 009 :: integrate rgbd frame 294 (95 of 100).
Fragment 002 / 009 :: integrate rgbd frame 295 (96 of 100).
Fragment 002 / 009 :: integrate rgbd frame 296 (97 of 100).
Fragment 002 / 009 :: integrate rgbd frame 297 (98 of 100).
Fragment 002 / 009 :: integrate rgbd frame 298 (99 of 100).
Fragment 002 / 009 :: integrate rgbd frame 299 (100 of 100).
Fragment 003 / 009 :: integrate rgbd frame 300 (1 of 100).
Fragment 003 / 009 :: integrate rgbd frame 301 (2 of 100).
Fragment 003 / 009 :: integrate rgbd frame 302 (3 of 100).
Fragment 003 / 009 :: integrate rgbd frame 303 (4 of 100).
Fragment 003 / 009 :: integrate rgbd frame 304 (5 of 100).
Fragment 003 / 009 :: integrate rgbd frame 305 (6 of 100).
Fragment 003 / 009 :: integrate rgbd frame 306 (7 of 100).
Fragment 003 / 009 :: integrate rgbd frame 307 (8 of 100).
Fragment 003 / 009 :: integrate rgbd frame 308 (9 of 100).
Fragment 003 / 009 :: integrate rgbd frame 309 (10 of 100).
Fragment 003 / 009 :: integrate rgbd frame 310 (11 of 100).
Fragment 003 / 009 :: integrate rgbd frame 311 (12 of 100).
Fragment 003 / 009 :: integrate rgbd frame 312 (13 of 100).
Fragment 003 / 009 :: integrate rgbd frame 313 (14 of 100).
Fragment 003 / 009 :: integrate rgbd frame 314 (15 of 100).
Fragment 003 / 009 :: integrate rgbd frame 315 (16 of 100).
Fragment 003 / 009 :: integrate rgbd frame 316 (17 of 100).
Fragment 003 / 009 :: integrate rgbd frame 317 (18 of 100).
Fragment 003 / 009 :: integrate rgbd frame 318 (19 of 100).
Fragment 003 / 009 :: integrate rgbd frame 319 (20 of 100).
Fragment 003 / 009 :: integrate rgbd frame 320 (21 of 100).
Fragment 003 / 009 :: integrate rgbd frame 321 (22 of 100).
Fragment 003 / 009 :: integrate rgbd frame 322 (23 of 100).
Fragment 003 / 009 :: integrate rgbd frame 323 (24 of 100).
Fragment 003 / 009 :: integrate rgbd frame 324 (25 of 100).
Fragment 003 / 009 :: integrate rgbd frame 325 (26 of 100).
Fragment 003 / 009 :: integrate rgbd frame 326 (27 of 100).
Fragment 003 / 009 :: integrate rgbd frame 327 (28 of 100).
Fragment 003 / 009 :: integrate rgbd frame 328 (29 of 100).
Fragment 003 / 009 :: integrate rgbd frame 329 (30 of 100).
Fragment 003 / 009 :: integrate rgbd frame 330 (31 of 100).
Fragment 003 / 009 :: integrate rgbd frame 331 (32 of 100).
Fragment 003 / 009 :: integrate rgbd frame 332 (33 of 100).
Fragment 003 / 009 :: integrate rgbd frame 333 (34 of 100).
Fragment 003 / 009 :: integrate rgbd frame 334 (35 of 100).
Fragment 003 / 009 :: integrate rgbd frame 335 (36 of 100).
Fragment 003 / 009 :: integrate rgbd frame 336 (37 of 100).
Fragment 003 / 009 :: integrate rgbd frame 337 (38 of 100).
Fragment 003 / 009 :: integrate rgbd frame 338 (39 of 100).
Fragment 003 / 009 :: integrate rgbd frame 339 (40 of 100).
Fragment 003 / 009 :: integrate rgbd frame 340 (41 of 100).
Fragment 003 / 009 :: integrate rgbd frame 341 (42 of 100).
Fragment 003 / 009 :: integrate rgbd frame 342 (43 of 100).
Fragment 003 / 009 :: integrate rgbd frame 343 (44 of 100).
Fragment 003 / 009 :: integrate rgbd frame 344 (45 of 100).
Fragment 003 / 009 :: integrate rgbd frame 345 (46 of 100).
Fragment 003 / 009 :: integrate rgbd frame 346 (47 of 100).
Fragment 003 / 009 :: integrate rgbd frame 347 (48 of 100).
Fragment 003 / 009 :: integrate rgbd frame 348 (49 of 100).
Fragment 003 / 009 :: integrate rgbd frame 349 (50 of 100).
Fragment 003 / 009 :: integrate rgbd frame 350 (51 of 100).
Fragment 003 / 009 :: integrate rgbd frame 351 (52 of 100).
Fragment 003 / 009 :: integrate rgbd frame 352 (53 of 100).
Fragment 003 / 009 :: integrate rgbd frame 353 (54 of 100).
Fragment 003 / 009 :: integrate rgbd frame 354 (55 of 100).
Fragment 003 / 009 :: integrate rgbd frame 355 (56 of 100).
Fragment 003 / 009 :: integrate rgbd frame 356 (57 of 100).
Fragment 003 / 009 :: integrate rgbd frame 357 (58 of 100).
Fragment 003 / 009 :: integrate rgbd frame 358 (59 of 100).
Fragment 003 / 009 :: integrate rgbd frame 359 (60 of 100).
Fragment 003 / 009 :: integrate rgbd frame 360 (61 of 100).
Fragment 003 / 009 :: integrate rgbd frame 361 (62 of 100).
Fragment 003 / 009 :: integrate rgbd frame 362 (63 of 100).
Fragment 003 / 009 :: integrate rgbd frame 363 (64 of 100).
Fragment 003 / 009 :: integrate rgbd frame 364 (65 of 100).
Fragment 003 / 009 :: integrate rgbd frame 365 (66 of 100).
Fragment 003 / 009 :: integrate rgbd frame 366 (67 of 100).
Fragment 003 / 009 :: integrate rgbd frame 367 (68 of 100).
Fragment 003 / 009 :: integrate rgbd frame 368 (69 of 100).
Fragment 003 / 009 :: integrate rgbd frame 369 (70 of 100).
Fragment 003 / 009 :: integrate rgbd frame 370 (71 of 100).
Fragment 003 / 009 :: integrate rgbd frame 371 (72 of 100).
Fragment 003 / 009 :: integrate rgbd frame 372 (73 of 100).
Fragment 003 / 009 :: integrate rgbd frame 373 (74 of 100).
Fragment 003 / 009 :: integrate rgbd frame 374 (75 of 100).
Fragment 003 / 009 :: integrate rgbd frame 375 (76 of 100).
Fragment 003 / 009 :: integrate rgbd frame 376 (77 of 100).
Fragment 003 / 009 :: integrate rgbd frame 377 (78 of 100).
Fragment 003 / 009 :: integrate rgbd frame 378 (79 of 100).
Fragment 003 / 009 :: integrate rgbd frame 379 (80 of 100).
Fragment 003 / 009 :: integrate rgbd frame 380 (81 of 100).
Fragment 003 / 009 :: integrate rgbd frame 381 (82 of 100).
Fragment 003 / 009 :: integrate rgbd frame 382 (83 of 100).
Fragment 003 / 009 :: integrate rgbd frame 383 (84 of 100).
Fragment 003 / 009 :: integrate rgbd frame 384 (85 of 100).
Fragment 003 / 009 :: integrate rgbd frame 385 (86 of 100).
Fragment 003 / 009 :: integrate rgbd frame 386 (87 of 100).
Fragment 003 / 009 :: integrate rgbd frame 387 (88 of 100).
Fragment 003 / 009 :: integrate rgbd frame 388 (89 of 100).
Fragment 003 / 009 :: integrate rgbd frame 389 (90 of 100).
Fragment 003 / 009 :: integrate rgbd frame 390 (91 of 100).
Fragment 003 / 009 :: integrate rgbd frame 391 (92 of 100).
Fragment 003 / 009 :: integrate rgbd frame 392 (93 of 100).
Fragment 003 / 009 :: integrate rgbd frame 393 (94 of 100).
Fragment 003 / 009 :: integrate rgbd frame 394 (95 of 100).
Fragment 003 / 009 :: integrate rgbd frame 395 (96 of 100).
Fragment 003 / 009 :: integrate rgbd frame 396 (97 of 100).
Fragment 003 / 009 :: integrate rgbd frame 397 (98 of 100).
Fragment 003 / 009 :: integrate rgbd frame 398 (99 of 100).
Fragment 003 / 009 :: integrate rgbd frame 399 (100 of 100).
Fragment 004 / 009 :: integrate rgbd frame 400 (1 of 100).
Fragment 004 / 009 :: integrate rgbd frame 401 (2 of 100).
Fragment 004 / 009 :: integrate rgbd frame 402 (3 of 100).
Fragment 004 / 009 :: integrate rgbd frame 403 (4 of 100).
Fragment 004 / 009 :: integrate rgbd frame 404 (5 of 100).
Fragment 004 / 009 :: integrate rgbd frame 405 (6 of 100).
Fragment 004 / 009 :: integrate rgbd frame 406 (7 of 100).
Fragment 004 / 009 :: integrate rgbd frame 407 (8 of 100).
Fragment 004 / 009 :: integrate rgbd frame 408 (9 of 100).
Fragment 004 / 009 :: integrate rgbd frame 409 (10 of 100).
Fragment 004 / 009 :: integrate rgbd frame 410 (11 of 100).
Fragment 004 / 009 :: integrate rgbd frame 411 (12 of 100).
Fragment 004 / 009 :: integrate rgbd frame 412 (13 of 100).
Fragment 004 / 009 :: integrate rgbd frame 413 (14 of 100).
Fragment 004 / 009 :: integrate rgbd frame 414 (15 of 100).
Fragment 004 / 009 :: integrate rgbd frame 415 (16 of 100).
Fragment 004 / 009 :: integrate rgbd frame 416 (17 of 100).
Fragment 004 / 009 :: integrate rgbd frame 417 (18 of 100).
Fragment 004 / 009 :: integrate rgbd frame 418 (19 of 100).
Fragment 004 / 009 :: integrate rgbd frame 419 (20 of 100).
Fragment 004 / 009 :: integrate rgbd frame 420 (21 of 100).
Fragment 004 / 009 :: integrate rgbd frame 421 (22 of 100).
Fragment 004 / 009 :: integrate rgbd frame 422 (23 of 100).
Fragment 004 / 009 :: integrate rgbd frame 423 (24 of 100).
Fragment 004 / 009 :: integrate rgbd frame 424 (25 of 100).
Fragment 004 / 009 :: integrate rgbd frame 425 (26 of 100).
Fragment 004 / 009 :: integrate rgbd frame 426 (27 of 100).
Fragment 004 / 009 :: integrate rgbd frame 427 (28 of 100).
Fragment 004 / 009 :: integrate rgbd frame 428 (29 of 100).
Fragment 004 / 009 :: integrate rgbd frame 429 (30 of 100).
Fragment 004 / 009 :: integrate rgbd frame 430 (31 of 100).
Fragment 004 / 009 :: integrate rgbd frame 431 (32 of 100).
Fragment 004 / 009 :: integrate rgbd frame 432 (33 of 100).
Fragment 004 / 009 :: integrate rgbd frame 433 (34 of 100).
Fragment 004 / 009 :: integrate rgbd frame 434 (35 of 100).
Fragment 004 / 009 :: integrate rgbd frame 435 (36 of 100).
Fragment 004 / 009 :: integrate rgbd frame 436 (37 of 100).
Fragment 004 / 009 :: integrate rgbd frame 437 (38 of 100).
Fragment 004 / 009 :: integrate rgbd frame 438 (39 of 100).
Fragment 004 / 009 :: integrate rgbd frame 439 (40 of 100).
Fragment 004 / 009 :: integrate rgbd frame 440 (41 of 100).
Fragment 004 / 009 :: integrate rgbd frame 441 (42 of 100).
Fragment 004 / 009 :: integrate rgbd frame 442 (43 of 100).
Fragment 004 / 009 :: integrate rgbd frame 443 (44 of 100).
Fragment 004 / 009 :: integrate rgbd frame 444 (45 of 100).
Fragment 004 / 009 :: integrate rgbd frame 445 (46 of 100).
Fragment 004 / 009 :: integrate rgbd frame 446 (47 of 100).
Fragment 004 / 009 :: integrate rgbd frame 447 (48 of 100).
Fragment 004 / 009 :: integrate rgbd frame 448 (49 of 100).
Fragment 004 / 009 :: integrate rgbd frame 449 (50 of 100).
Fragment 004 / 009 :: integrate rgbd frame 450 (51 of 100).
Fragment 004 / 009 :: integrate rgbd frame 451 (52 of 100).
Fragment 004 / 009 :: integrate rgbd frame 452 (53 of 100).
Fragment 004 / 009 :: integrate rgbd frame 453 (54 of 100).
Fragment 004 / 009 :: integrate rgbd frame 454 (55 of 100).
Fragment 004 / 009 :: integrate rgbd frame 455 (56 of 100).
Fragment 004 / 009 :: integrate rgbd frame 456 (57 of 100).
Fragment 004 / 009 :: integrate rgbd frame 457 (58 of 100).
Fragment 004 / 009 :: integrate rgbd frame 458 (59 of 100).
Fragment 004 / 009 :: integrate rgbd frame 459 (60 of 100).
Fragment 004 / 009 :: integrate rgbd frame 460 (61 of 100).
Fragment 004 / 009 :: integrate rgbd frame 461 (62 of 100).
Fragment 004 / 009 :: integrate rgbd frame 462 (63 of 100).
Fragment 004 / 009 :: integrate rgbd frame 463 (64 of 100).
Fragment 004 / 009 :: integrate rgbd frame 464 (65 of 100).
Fragment 004 / 009 :: integrate rgbd frame 465 (66 of 100).
Fragment 004 / 009 :: integrate rgbd frame 466 (67 of 100).
Fragment 004 / 009 :: integrate rgbd frame 467 (68 of 100).
Fragment 004 / 009 :: integrate rgbd frame 468 (69 of 100).
Fragment 004 / 009 :: integrate rgbd frame 469 (70 of 100).
Fragment 004 / 009 :: integrate rgbd frame 470 (71 of 100).
Fragment 004 / 009 :: integrate rgbd frame 471 (72 of 100).
Fragment 004 / 009 :: integrate rgbd frame 472 (73 of 100).
Fragment 004 / 009 :: integrate rgbd frame 473 (74 of 100).
Fragment 004 / 009 :: integrate rgbd frame 474 (75 of 100).
Fragment 004 / 009 :: integrate rgbd frame 475 (76 of 100).
Fragment 004 / 009 :: integrate rgbd frame 476 (77 of 100).
Fragment 004 / 009 :: integrate rgbd frame 477 (78 of 100).
Fragment 004 / 009 :: integrate rgbd frame 478 (79 of 100).
Fragment 004 / 009 :: integrate rgbd frame 479 (80 of 100).
Fragment 004 / 009 :: integrate rgbd frame 480 (81 of 100).
Fragment 004 / 009 :: integrate rgbd frame 481 (82 of 100).
Fragment 004 / 009 :: integrate rgbd frame 482 (83 of 100).
Fragment 004 / 009 :: integrate rgbd frame 483 (84 of 100).
Fragment 004 / 009 :: integrate rgbd frame 484 (85 of 100).
Fragment 004 / 009 :: integrate rgbd frame 485 (86 of 100).
Fragment 004 / 009 :: integrate rgbd frame 486 (87 of 100).
Fragment 004 / 009 :: integrate rgbd frame 487 (88 of 100).
Fragment 004 / 009 :: integrate rgbd frame 488 (89 of 100).
Fragment 004 / 009 :: integrate rgbd frame 489 (90 of 100).
Fragment 004 / 009 :: integrate rgbd frame 490 (91 of 100).
Fragment 004 / 009 :: integrate rgbd frame 491 (92 of 100).
Fragment 004 / 009 :: integrate rgbd frame 492 (93 of 100).
Fragment 004 / 009 :: integrate rgbd frame 493 (94 of 100).
Fragment 004 / 009 :: integrate rgbd frame 494 (95 of 100).
Fragment 004 / 009 :: integrate rgbd frame 495 (96 of 100).
Fragment 004 / 009 :: integrate rgbd frame 496 (97 of 100).
Fragment 004 / 009 :: integrate rgbd frame 497 (98 of 100).
Fragment 004 / 009 :: integrate rgbd frame 498 (99 of 100).
Fragment 004 / 009 :: integrate rgbd frame 499 (100 of 100).
Fragment 005 / 009 :: integrate rgbd frame 500 (1 of 100).
Fragment 005 / 009 :: integrate rgbd frame 501 (2 of 100).
Fragment 005 / 009 :: integrate rgbd frame 502 (3 of 100).
Fragment 005 / 009 :: integrate rgbd frame 503 (4 of 100).
Fragment 005 / 009 :: integrate rgbd frame 504 (5 of 100).
Fragment 005 / 009 :: integrate rgbd frame 505 (6 of 100).
Fragment 005 / 009 :: integrate rgbd frame 506 (7 of 100).
Fragment 005 / 009 :: integrate rgbd frame 507 (8 of 100).
Fragment 005 / 009 :: integrate rgbd frame 508 (9 of 100).
Fragment 005 / 009 :: integrate rgbd frame 509 (10 of 100).
Fragment 005 / 009 :: integrate rgbd frame 510 (11 of 100).
Fragment 005 / 009 :: integrate rgbd frame 511 (12 of 100).
Fragment 005 / 009 :: integrate rgbd frame 512 (13 of 100).
Fragment 005 / 009 :: integrate rgbd frame 513 (14 of 100).
Fragment 005 / 009 :: integrate rgbd frame 514 (15 of 100).
Fragment 005 / 009 :: integrate rgbd frame 515 (16 of 100).
Fragment 005 / 009 :: integrate rgbd frame 516 (17 of 100).
Fragment 005 / 009 :: integrate rgbd frame 517 (18 of 100).
Fragment 005 / 009 :: integrate rgbd frame 518 (19 of 100).
Fragment 005 / 009 :: integrate rgbd frame 519 (20 of 100).
Fragment 005 / 009 :: integrate rgbd frame 520 (21 of 100).
Fragment 005 / 009 :: integrate rgbd frame 521 (22 of 100).
Fragment 005 / 009 :: integrate rgbd frame 522 (23 of 100).
Fragment 005 / 009 :: integrate rgbd frame 523 (24 of 100).
Fragment 005 / 009 :: integrate rgbd frame 524 (25 of 100).
Fragment 005 / 009 :: integrate rgbd frame 525 (26 of 100).
Fragment 005 / 009 :: integrate rgbd frame 526 (27 of 100).
Fragment 005 / 009 :: integrate rgbd frame 527 (28 of 100).
Fragment 005 / 009 :: integrate rgbd frame 528 (29 of 100).
Fragment 005 / 009 :: integrate rgbd frame 529 (30 of 100).
Fragment 005 / 009 :: integrate rgbd frame 530 (31 of 100).
Fragment 005 / 009 :: integrate rgbd frame 531 (32 of 100).
Fragment 005 / 009 :: integrate rgbd frame 532 (33 of 100).
Fragment 005 / 009 :: integrate rgbd frame 533 (34 of 100).
Fragment 005 / 009 :: integrate rgbd frame 534 (35 of 100).
Fragment 005 / 009 :: integrate rgbd frame 535 (36 of 100).
Fragment 005 / 009 :: integrate rgbd frame 536 (37 of 100).
Fragment 005 / 009 :: integrate rgbd frame 537 (38 of 100).
Fragment 005 / 009 :: integrate rgbd frame 538 (39 of 100).
Fragment 005 / 009 :: integrate rgbd frame 539 (40 of 100).
Fragment 005 / 009 :: integrate rgbd frame 540 (41 of 100).
Fragment 005 / 009 :: integrate rgbd frame 541 (42 of 100).
Fragment 005 / 009 :: integrate rgbd frame 542 (43 of 100).
Fragment 005 / 009 :: integrate rgbd frame 543 (44 of 100).
Fragment 005 / 009 :: integrate rgbd frame 544 (45 of 100).
Fragment 005 / 009 :: integrate rgbd frame 545 (46 of 100).
Fragment 005 / 009 :: integrate rgbd frame 546 (47 of 100).
Fragment 005 / 009 :: integrate rgbd frame 547 (48 of 100).
Fragment 005 / 009 :: integrate rgbd frame 548 (49 of 100).
Fragment 005 / 009 :: integrate rgbd frame 549 (50 of 100).
Fragment 005 / 009 :: integrate rgbd frame 550 (51 of 100).
Fragment 005 / 009 :: integrate rgbd frame 551 (52 of 100).
Fragment 005 / 009 :: integrate rgbd frame 552 (53 of 100).
Fragment 005 / 009 :: integrate rgbd frame 553 (54 of 100).
Fragment 005 / 009 :: integrate rgbd frame 554 (55 of 100).
Fragment 005 / 009 :: integrate rgbd frame 555 (56 of 100).
Fragment 005 / 009 :: integrate rgbd frame 556 (57 of 100).
Fragment 005 / 009 :: integrate rgbd frame 557 (58 of 100).
Fragment 005 / 009 :: integrate rgbd frame 558 (59 of 100).
Fragment 005 / 009 :: integrate rgbd frame 559 (60 of 100).
Fragment 005 / 009 :: integrate rgbd frame 560 (61 of 100).
Fragment 005 / 009 :: integrate rgbd frame 561 (62 of 100).
Fragment 005 / 009 :: integrate rgbd frame 562 (63 of 100).
Fragment 005 / 009 :: integrate rgbd frame 563 (64 of 100).
Fragment 005 / 009 :: integrate rgbd frame 564 (65 of 100).
Fragment 005 / 009 :: integrate rgbd frame 565 (66 of 100).
Fragment 005 / 009 :: integrate rgbd frame 566 (67 of 100).
Fragment 005 / 009 :: integrate rgbd frame 567 (68 of 100).
Fragment 005 / 009 :: integrate rgbd frame 568 (69 of 100).
Fragment 005 / 009 :: integrate rgbd frame 569 (70 of 100).
Fragment 005 / 009 :: integrate rgbd frame 570 (71 of 100).
Fragment 005 / 009 :: integrate rgbd frame 571 (72 of 100).
Fragment 005 / 009 :: integrate rgbd frame 572 (73 of 100).
Fragment 005 / 009 :: integrate rgbd frame 573 (74 of 100).
Fragment 005 / 009 :: integrate rgbd frame 574 (75 of 100).
Fragment 005 / 009 :: integrate rgbd frame 575 (76 of 100).
Fragment 005 / 009 :: integrate rgbd frame 576 (77 of 100).
Fragment 005 / 009 :: integrate rgbd frame 577 (78 of 100).
Fragment 005 / 009 :: integrate rgbd frame 578 (79 of 100).
Fragment 005 / 009 :: integrate rgbd frame 579 (80 of 100).
Fragment 005 / 009 :: integrate rgbd frame 580 (81 of 100).
Fragment 005 / 009 :: integrate rgbd frame 581 (82 of 100).
Fragment 005 / 009 :: integrate rgbd frame 582 (83 of 100).
Fragment 005 / 009 :: integrate rgbd frame 583 (84 of 100).
Fragment 005 / 009 :: integrate rgbd frame 584 (85 of 100).
Fragment 005 / 009 :: integrate rgbd frame 585 (86 of 100).
Fragment 005 / 009 :: integrate rgbd frame 586 (87 of 100).
Fragment 005 / 009 :: integrate rgbd frame 587 (88 of 100).
Fragment 005 / 009 :: integrate rgbd frame 588 (89 of 100).
Fragment 005 / 009 :: integrate rgbd frame 589 (90 of 100).
Fragment 005 / 009 :: integrate rgbd frame 590 (91 of 100).
Fragment 005 / 009 :: integrate rgbd frame 591 (92 of 100).
Fragment 005 / 009 :: integrate rgbd frame 592 (93 of 100).
Fragment 005 / 009 :: integrate rgbd frame 593 (94 of 100).
Fragment 005 / 009 :: integrate rgbd frame 594 (95 of 100).
Fragment 005 / 009 :: integrate rgbd frame 595 (96 of 100).
Fragment 005 / 009 :: integrate rgbd frame 596 (97 of 100).
Fragment 005 / 009 :: integrate rgbd frame 597 (98 of 100).
Fragment 005 / 009 :: integrate rgbd frame 598 (99 of 100).
Fragment 005 / 009 :: integrate rgbd frame 599 (100 of 100).
Fragment 006 / 009 :: integrate rgbd frame 600 (1 of 100).
Fragment 006 / 009 :: integrate rgbd frame 601 (2 of 100).
Fragment 006 / 009 :: integrate rgbd frame 602 (3 of 100).
Fragment 006 / 009 :: integrate rgbd frame 603 (4 of 100).
Fragment 006 / 009 :: integrate rgbd frame 604 (5 of 100).
Fragment 006 / 009 :: integrate rgbd frame 605 (6 of 100).
Fragment 006 / 009 :: integrate rgbd frame 606 (7 of 100).
Fragment 006 / 009 :: integrate rgbd frame 607 (8 of 100).
Fragment 006 / 009 :: integrate rgbd frame 608 (9 of 100).
Fragment 006 / 009 :: integrate rgbd frame 609 (10 of 100).
Fragment 006 / 009 :: integrate rgbd frame 610 (11 of 100).
Fragment 006 / 009 :: integrate rgbd frame 611 (12 of 100).
Fragment 006 / 009 :: integrate rgbd frame 612 (13 of 100).
Fragment 006 / 009 :: integrate rgbd frame 613 (14 of 100).
Fragment 006 / 009 :: integrate rgbd frame 614 (15 of 100).
Fragment 006 / 009 :: integrate rgbd frame 615 (16 of 100).
Fragment 006 / 009 :: integrate rgbd frame 616 (17 of 100).
Fragment 006 / 009 :: integrate rgbd frame 617 (18 of 100).
Fragment 006 / 009 :: integrate rgbd frame 618 (19 of 100).
Fragment 006 / 009 :: integrate rgbd frame 619 (20 of 100).
Fragment 006 / 009 :: integrate rgbd frame 620 (21 of 100).
Fragment 006 / 009 :: integrate rgbd frame 621 (22 of 100).
Fragment 006 / 009 :: integrate rgbd frame 622 (23 of 100).
Fragment 006 / 009 :: integrate rgbd frame 623 (24 of 100).
Fragment 006 / 009 :: integrate rgbd frame 624 (25 of 100).
Fragment 006 / 009 :: integrate rgbd frame 625 (26 of 100).
Fragment 006 / 009 :: integrate rgbd frame 626 (27 of 100).
Fragment 006 / 009 :: integrate rgbd frame 627 (28 of 100).
Fragment 006 / 009 :: integrate rgbd frame 628 (29 of 100).
Fragment 006 / 009 :: integrate rgbd frame 629 (30 of 100).
Fragment 006 / 009 :: integrate rgbd frame 630 (31 of 100).
Fragment 006 / 009 :: integrate rgbd frame 631 (32 of 100).
Fragment 006 / 009 :: integrate rgbd frame 632 (33 of 100).
Fragment 006 / 009 :: integrate rgbd frame 633 (34 of 100).
Fragment 006 / 009 :: integrate rgbd frame 634 (35 of 100).
Fragment 006 / 009 :: integrate rgbd frame 635 (36 of 100).
Fragment 006 / 009 :: integrate rgbd frame 636 (37 of 100).
Fragment 006 / 009 :: integrate rgbd frame 637 (38 of 100).
Fragment 006 / 009 :: integrate rgbd frame 638 (39 of 100).
Fragment 006 / 009 :: integrate rgbd frame 639 (40 of 100).
Fragment 006 / 009 :: integrate rgbd frame 640 (41 of 100).
Fragment 006 / 009 :: integrate rgbd frame 641 (42 of 100).
Fragment 006 / 009 :: integrate rgbd frame 642 (43 of 100).
Fragment 006 / 009 :: integrate rgbd frame 643 (44 of 100).
Fragment 006 / 009 :: integrate rgbd frame 644 (45 of 100).
Fragment 006 / 009 :: integrate rgbd frame 645 (46 of 100).
Fragment 006 / 009 :: integrate rgbd frame 646 (47 of 100).
Fragment 006 / 009 :: integrate rgbd frame 647 (48 of 100).
Fragment 006 / 009 :: integrate rgbd frame 648 (49 of 100).
Fragment 006 / 009 :: integrate rgbd frame 649 (50 of 100).
Fragment 006 / 009 :: integrate rgbd frame 650 (51 of 100).
Fragment 006 / 009 :: integrate rgbd frame 651 (52 of 100).
Fragment 006 / 009 :: integrate rgbd frame 652 (53 of 100).
Fragment 006 / 009 :: integrate rgbd frame 653 (54 of 100).
Fragment 006 / 009 :: integrate rgbd frame 654 (55 of 100).
Fragment 006 / 009 :: integrate rgbd frame 655 (56 of 100).
Fragment 006 / 009 :: integrate rgbd frame 656 (57 of 100).
Fragment 006 / 009 :: integrate rgbd frame 657 (58 of 100).
Fragment 006 / 009 :: integrate rgbd frame 658 (59 of 100).
Fragment 006 / 009 :: integrate rgbd frame 659 (60 of 100).
Fragment 006 / 009 :: integrate rgbd frame 660 (61 of 100).
Fragment 006 / 009 :: integrate rgbd frame 661 (62 of 100).
Fragment 006 / 009 :: integrate rgbd frame 662 (63 of 100).
Fragment 006 / 009 :: integrate rgbd frame 663 (64 of 100).
Fragment 006 / 009 :: integrate rgbd frame 664 (65 of 100).
Fragment 006 / 009 :: integrate rgbd frame 665 (66 of 100).
Fragment 006 / 009 :: integrate rgbd frame 666 (67 of 100).
Fragment 006 / 009 :: integrate rgbd frame 667 (68 of 100).
Fragment 006 / 009 :: integrate rgbd frame 668 (69 of 100).
Fragment 006 / 009 :: integrate rgbd frame 669 (70 of 100).
Fragment 006 / 009 :: integrate rgbd frame 670 (71 of 100).
Fragment 006 / 009 :: integrate rgbd frame 671 (72 of 100).
Fragment 006 / 009 :: integrate rgbd frame 672 (73 of 100).
Fragment 006 / 009 :: integrate rgbd frame 673 (74 of 100).
Fragment 006 / 009 :: integrate rgbd frame 674 (75 of 100).
Fragment 006 / 009 :: integrate rgbd frame 675 (76 of 100).
Fragment 006 / 009 :: integrate rgbd frame 676 (77 of 100).
Fragment 006 / 009 :: integrate rgbd frame 677 (78 of 100).
Fragment 006 / 009 :: integrate rgbd frame 678 (79 of 100).
Fragment 006 / 009 :: integrate rgbd frame 679 (80 of 100).
Fragment 006 / 009 :: integrate rgbd frame 680 (81 of 100).
Fragment 006 / 009 :: integrate rgbd frame 681 (82 of 100).
Fragment 006 / 009 :: integrate rgbd frame 682 (83 of 100).
Fragment 006 / 009 :: integrate rgbd frame 683 (84 of 100).
Fragment 006 / 009 :: integrate rgbd frame 684 (85 of 100).
Fragment 006 / 009 :: integrate rgbd frame 685 (86 of 100).
Fragment 006 / 009 :: integrate rgbd frame 686 (87 of 100).
Fragment 006 / 009 :: integrate rgbd frame 687 (88 of 100).
Fragment 006 / 009 :: integrate rgbd frame 688 (89 of 100).
Fragment 006 / 009 :: integrate rgbd frame 689 (90 of 100).
Fragment 006 / 009 :: integrate rgbd frame 690 (91 of 100).
Fragment 006 / 009 :: integrate rgbd frame 691 (92 of 100).
Fragment 006 / 009 :: integrate rgbd frame 692 (93 of 100).
Fragment 006 / 009 :: integrate rgbd frame 693 (94 of 100).
Fragment 006 / 009 :: integrate rgbd frame 694 (95 of 100).
Fragment 006 / 009 :: integrate rgbd frame 695 (96 of 100).
Fragment 006 / 009 :: integrate rgbd frame 696 (97 of 100).
Fragment 006 / 009 :: integrate rgbd frame 697 (98 of 100).
Fragment 006 / 009 :: integrate rgbd frame 698 (99 of 100).
Fragment 006 / 009 :: integrate rgbd frame 699 (100 of 100).
Fragment 007 / 009 :: integrate rgbd frame 700 (1 of 100).
Fragment 007 / 009 :: integrate rgbd frame 701 (2 of 100).
Fragment 007 / 009 :: integrate rgbd frame 702 (3 of 100).
Fragment 007 / 009 :: integrate rgbd frame 703 (4 of 100).
Fragment 007 / 009 :: integrate rgbd frame 704 (5 of 100).
Fragment 007 / 009 :: integrate rgbd frame 705 (6 of 100).
Fragment 007 / 009 :: integrate rgbd frame 706 (7 of 100).
Fragment 007 / 009 :: integrate rgbd frame 707 (8 of 100).
Fragment 007 / 009 :: integrate rgbd frame 708 (9 of 100).
Fragment 007 / 009 :: integrate rgbd frame 709 (10 of 100).
Fragment 007 / 009 :: integrate rgbd frame 710 (11 of 100).
Fragment 007 / 009 :: integrate rgbd frame 711 (12 of 100).
Fragment 007 / 009 :: integrate rgbd frame 712 (13 of 100).
Fragment 007 / 009 :: integrate rgbd frame 713 (14 of 100).
Fragment 007 / 009 :: integrate rgbd frame 714 (15 of 100).
Fragment 007 / 009 :: integrate rgbd frame 715 (16 of 100).
Fragment 007 / 009 :: integrate rgbd frame 716 (17 of 100).
Fragment 007 / 009 :: integrate rgbd frame 717 (18 of 100).
Fragment 007 / 009 :: integrate rgbd frame 718 (19 of 100).
Fragment 007 / 009 :: integrate rgbd frame 719 (20 of 100).
Fragment 007 / 009 :: integrate rgbd frame 720 (21 of 100).
Fragment 007 / 009 :: integrate rgbd frame 721 (22 of 100).
Fragment 007 / 009 :: integrate rgbd frame 722 (23 of 100).
Fragment 007 / 009 :: integrate rgbd frame 723 (24 of 100).
Fragment 007 / 009 :: integrate rgbd frame 724 (25 of 100).
Fragment 007 / 009 :: integrate rgbd frame 725 (26 of 100).
Fragment 007 / 009 :: integrate rgbd frame 726 (27 of 100).
Fragment 007 / 009 :: integrate rgbd frame 727 (28 of 100).
Fragment 007 / 009 :: integrate rgbd frame 728 (29 of 100).
Fragment 007 / 009 :: integrate rgbd frame 729 (30 of 100).
Fragment 007 / 009 :: integrate rgbd frame 730 (31 of 100).
Fragment 007 / 009 :: integrate rgbd frame 731 (32 of 100).
Fragment 007 / 009 :: integrate rgbd frame 732 (33 of 100).
Fragment 007 / 009 :: integrate rgbd frame 733 (34 of 100).
Fragment 007 / 009 :: integrate rgbd frame 734 (35 of 100).
Fragment 007 / 009 :: integrate rgbd frame 735 (36 of 100).
Fragment 007 / 009 :: integrate rgbd frame 736 (37 of 100).
Fragment 007 / 009 :: integrate rgbd frame 737 (38 of 100).
Fragment 007 / 009 :: integrate rgbd frame 738 (39 of 100).
Fragment 007 / 009 :: integrate rgbd frame 739 (40 of 100).
Fragment 007 / 009 :: integrate rgbd frame 740 (41 of 100).
Fragment 007 / 009 :: integrate rgbd frame 741 (42 of 100).
Fragment 007 / 009 :: integrate rgbd frame 742 (43 of 100).
Fragment 007 / 009 :: integrate rgbd frame 743 (44 of 100).
Fragment 007 / 009 :: integrate rgbd frame 744 (45 of 100).
Fragment 007 / 009 :: integrate rgbd frame 745 (46 of 100).
Fragment 007 / 009 :: integrate rgbd frame 746 (47 of 100).
Fragment 007 / 009 :: integrate rgbd frame 747 (48 of 100).
Fragment 007 / 009 :: integrate rgbd frame 748 (49 of 100).
Fragment 007 / 009 :: integrate rgbd frame 749 (50 of 100).
Fragment 007 / 009 :: integrate rgbd frame 750 (51 of 100).
Fragment 007 / 009 :: integrate rgbd frame 751 (52 of 100).
Fragment 007 / 009 :: integrate rgbd frame 752 (53 of 100).
Fragment 007 / 009 :: integrate rgbd frame 753 (54 of 100).
Fragment 007 / 009 :: integrate rgbd frame 754 (55 of 100).
Fragment 007 / 009 :: integrate rgbd frame 755 (56 of 100).
Fragment 007 / 009 :: integrate rgbd frame 756 (57 of 100).
Fragment 007 / 009 :: integrate rgbd frame 757 (58 of 100).
Fragment 007 / 009 :: integrate rgbd frame 758 (59 of 100).
Fragment 007 / 009 :: integrate rgbd frame 759 (60 of 100).
Fragment 007 / 009 :: integrate rgbd frame 760 (61 of 100).
Fragment 007 / 009 :: integrate rgbd frame 761 (62 of 100).
Fragment 007 / 009 :: integrate rgbd frame 762 (63 of 100).
Fragment 007 / 009 :: integrate rgbd frame 763 (64 of 100).
Fragment 007 / 009 :: integrate rgbd frame 764 (65 of 100).
Fragment 007 / 009 :: integrate rgbd frame 765 (66 of 100).
Fragment 007 / 009 :: integrate rgbd frame 766 (67 of 100).
Fragment 007 / 009 :: integrate rgbd frame 767 (68 of 100).
Fragment 007 / 009 :: integrate rgbd frame 768 (69 of 100).
Fragment 007 / 009 :: integrate rgbd frame 769 (70 of 100).
Fragment 007 / 009 :: integrate rgbd frame 770 (71 of 100).
Fragment 007 / 009 :: integrate rgbd frame 771 (72 of 100).
Fragment 007 / 009 :: integrate rgbd frame 772 (73 of 100).
Fragment 007 / 009 :: integrate rgbd frame 773 (74 of 100).
Fragment 007 / 009 :: integrate rgbd frame 774 (75 of 100).
Fragment 007 / 009 :: integrate rgbd frame 775 (76 of 100).
Fragment 007 / 009 :: integrate rgbd frame 776 (77 of 100).
Fragment 007 / 009 :: integrate rgbd frame 777 (78 of 100).
Fragment 007 / 009 :: integrate rgbd frame 778 (79 of 100).
Fragment 007 / 009 :: integrate rgbd frame 779 (80 of 100).
Fragment 007 / 009 :: integrate rgbd frame 780 (81 of 100).
Fragment 007 / 009 :: integrate rgbd frame 781 (82 of 100).
Fragment 007 / 009 :: integrate rgbd frame 782 (83 of 100).
Fragment 007 / 009 :: integrate rgbd frame 783 (84 of 100).
Fragment 007 / 009 :: integrate rgbd frame 784 (85 of 100).
Fragment 007 / 009 :: integrate rgbd frame 785 (86 of 100).
Fragment 007 / 009 :: integrate rgbd frame 786 (87 of 100).
Fragment 007 / 009 :: integrate rgbd frame 787 (88 of 100).
Fragment 007 / 009 :: integrate rgbd frame 788 (89 of 100).
Fragment 007 / 009 :: integrate rgbd frame 789 (90 of 100).
Fragment 007 / 009 :: integrate rgbd frame 790 (91 of 100).
Fragment 007 / 009 :: integrate rgbd frame 791 (92 of 100).
Fragment 007 / 009 :: integrate rgbd frame 792 (93 of 100).
Fragment 007 / 009 :: integrate rgbd frame 793 (94 of 100).
Fragment 007 / 009 :: integrate rgbd frame 794 (95 of 100).
Fragment 007 / 009 :: integrate rgbd frame 795 (96 of 100).
Fragment 007 / 009 :: integrate rgbd frame 796 (97 of 100).
Fragment 007 / 009 :: integrate rgbd frame 797 (98 of 100).
Fragment 007 / 009 :: integrate rgbd frame 798 (99 of 100).
Fragment 007 / 009 :: integrate rgbd frame 799 (100 of 100).
Fragment 008 / 009 :: integrate rgbd frame 800 (1 of 100).
Fragment 008 / 009 :: integrate rgbd frame 801 (2 of 100).
Fragment 008 / 009 :: integrate rgbd frame 802 (3 of 100).
Fragment 008 / 009 :: integrate rgbd frame 803 (4 of 100).
Fragment 008 / 009 :: integrate rgbd frame 804 (5 of 100).
Fragment 008 / 009 :: integrate rgbd frame 805 (6 of 100).
Fragment 008 / 009 :: integrate rgbd frame 806 (7 of 100).
Fragment 008 / 009 :: integrate rgbd frame 807 (8 of 100).
Fragment 008 / 009 :: integrate rgbd frame 808 (9 of 100).
Fragment 008 / 009 :: integrate rgbd frame 809 (10 of 100).
Fragment 008 / 009 :: integrate rgbd frame 810 (11 of 100).
Fragment 008 / 009 :: integrate rgbd frame 811 (12 of 100).
Fragment 008 / 009 :: integrate rgbd frame 812 (13 of 100).
Fragment 008 / 009 :: integrate rgbd frame 813 (14 of 100).
Fragment 008 / 009 :: integrate rgbd frame 814 (15 of 100).
Fragment 008 / 009 :: integrate rgbd frame 815 (16 of 100).
Fragment 008 / 009 :: integrate rgbd frame 816 (17 of 100).
Fragment 008 / 009 :: integrate rgbd frame 817 (18 of 100).
Fragment 008 / 009 :: integrate rgbd frame 818 (19 of 100).
Fragment 008 / 009 :: integrate rgbd frame 819 (20 of 100).
Fragment 008 / 009 :: integrate rgbd frame 820 (21 of 100).
Fragment 008 / 009 :: integrate rgbd frame 821 (22 of 100).
Fragment 008 / 009 :: integrate rgbd frame 822 (23 of 100).
Fragment 008 / 009 :: integrate rgbd frame 823 (24 of 100).
Fragment 008 / 009 :: integrate rgbd frame 824 (25 of 100).
Fragment 008 / 009 :: integrate rgbd frame 825 (26 of 100).
Fragment 008 / 009 :: integrate rgbd frame 826 (27 of 100).
Fragment 008 / 009 :: integrate rgbd frame 827 (28 of 100).
Fragment 008 / 009 :: integrate rgbd frame 828 (29 of 100).
Fragment 008 / 009 :: integrate rgbd frame 829 (30 of 100).
Fragment 008 / 009 :: integrate rgbd frame 830 (31 of 100).
Fragment 008 / 009 :: integrate rgbd frame 831 (32 of 100).
Fragment 008 / 009 :: integrate rgbd frame 832 (33 of 100).
Fragment 008 / 009 :: integrate rgbd frame 833 (34 of 100).
Fragment 008 / 009 :: integrate rgbd frame 834 (35 of 100).
Fragment 008 / 009 :: integrate rgbd frame 835 (36 of 100).
Fragment 008 / 009 :: integrate rgbd frame 836 (37 of 100).
Fragment 008 / 009 :: integrate rgbd frame 837 (38 of 100).
Fragment 008 / 009 :: integrate rgbd frame 838 (39 of 100).
Fragment 008 / 009 :: integrate rgbd frame 839 (40 of 100).
Fragment 008 / 009 :: integrate rgbd frame 840 (41 of 100).
Fragment 008 / 009 :: integrate rgbd frame 841 (42 of 100).
Fragment 008 / 009 :: integrate rgbd frame 842 (43 of 100).
Fragment 008 / 009 :: integrate rgbd frame 843 (44 of 100).
Fragment 008 / 009 :: integrate rgbd frame 844 (45 of 100).
Fragment 008 / 009 :: integrate rgbd frame 845 (46 of 100).
Fragment 008 / 009 :: integrate rgbd frame 846 (47 of 100).
Fragment 008 / 009 :: integrate rgbd frame 847 (48 of 100).
Fragment 008 / 009 :: integrate rgbd frame 848 (49 of 100).
Fragment 008 / 009 :: integrate rgbd frame 849 (50 of 100).
Fragment 008 / 009 :: integrate rgbd frame 850 (51 of 100).
Fragment 008 / 009 :: integrate rgbd frame 851 (52 of 100).
Fragment 008 / 009 :: integrate rgbd frame 852 (53 of 100).
Fragment 008 / 009 :: integrate rgbd frame 853 (54 of 100).
Fragment 008 / 009 :: integrate rgbd frame 854 (55 of 100).
Fragment 008 / 009 :: integrate rgbd frame 855 (56 of 100).
Fragment 008 / 009 :: integrate rgbd frame 856 (57 of 100).
Fragment 008 / 009 :: integrate rgbd frame 857 (58 of 100).
Fragment 008 / 009 :: integrate rgbd frame 858 (59 of 100).
Fragment 008 / 009 :: integrate rgbd frame 859 (60 of 100).
Fragment 008 / 009 :: integrate rgbd frame 860 (61 of 100).
Fragment 008 / 009 :: integrate rgbd frame 861 (62 of 100).
Fragment 008 / 009 :: integrate rgbd frame 862 (63 of 100).
Fragment 008 / 009 :: integrate rgbd frame 863 (64 of 100).
Fragment 008 / 009 :: integrate rgbd frame 864 (65 of 100).
Fragment 008 / 009 :: integrate rgbd frame 865 (66 of 100).
Fragment 008 / 009 :: integrate rgbd frame 866 (67 of 100).
Fragment 008 / 009 :: integrate rgbd frame 867 (68 of 100).
Fragment 008 / 009 :: integrate rgbd frame 868 (69 of 100).
Fragment 008 / 009 :: integrate rgbd frame 869 (70 of 100).
Fragment 008 / 009 :: integrate rgbd frame 870 (71 of 100).
Fragment 008 / 009 :: integrate rgbd frame 871 (72 of 100).
Fragment 008 / 009 :: integrate rgbd frame 872 (73 of 100).
Fragment 008 / 009 :: integrate rgbd frame 873 (74 of 100).
Fragment 008 / 009 :: integrate rgbd frame 874 (75 of 100).
Fragment 008 / 009 :: integrate rgbd frame 875 (76 of 100).
Fragment 008 / 009 :: integrate rgbd frame 876 (77 of 100).
Fragment 008 / 009 :: integrate rgbd frame 877 (78 of 100).
Fragment 008 / 009 :: integrate rgbd frame 878 (79 of 100).
Fragment 008 / 009 :: integrate rgbd frame 879 (80 of 100).
Fragment 008 / 009 :: integrate rgbd frame 880 (81 of 100).
Fragment 008 / 009 :: integrate rgbd frame 881 (82 of 100).
Fragment 008 / 009 :: integrate rgbd frame 882 (83 of 100).
Fragment 008 / 009 :: integrate rgbd frame 883 (84 of 100).
Fragment 008 / 009 :: integrate rgbd frame 884 (85 of 100).
Fragment 008 / 009 :: integrate rgbd frame 885 (86 of 100).
Fragment 008 / 009 :: integrate rgbd frame 886 (87 of 100).
Fragment 008 / 009 :: integrate rgbd frame 887 (88 of 100).
Fragment 008 / 009 :: integrate rgbd frame 888 (89 of 100).
Fragment 008 / 009 :: integrate rgbd frame 889 (90 of 100).
Fragment 008 / 009 :: integrate rgbd frame 890 (91 of 100).
Fragment 008 / 009 :: integrate rgbd frame 891 (92 of 100).
Fragment 008 / 009 :: integrate rgbd frame 892 (93 of 100).
Fragment 008 / 009 :: integrate rgbd frame 893 (94 of 100).
Fragment 008 / 009 :: integrate rgbd frame 894 (95 of 100).
Fragment 008 / 009 :: integrate rgbd frame 895 (96 of 100).
Fragment 008 / 009 :: integrate rgbd frame 896 (97 of 100).
Fragment 008 / 009 :: integrate rgbd frame 897 (98 of 100).
Fragment 008 / 009 :: integrate rgbd frame 898 (99 of 100).
Fragment 008 / 009 :: integrate rgbd frame 899 (100 of 100).
Fragment 009 / 009 :: integrate rgbd frame 900 (1 of 5).
Fragment 009 / 009 :: integrate rgbd frame 901 (2 of 5).
Fragment 009 / 009 :: integrate rgbd frame 902 (3 of 5).
Fragment 009 / 009 :: integrate rgbd frame 903 (4 of 5).
Fragment 009 / 009 :: integrate rgbd frame 904 (5 of 5).
====================================
Elapsed time (in h:m:s)
====================================
- Making fragments    0:18:39.593087
- Register fragments  0:00:49.357369
- Refine registration 0:00:02.105286
- Integrate frames    0:00:57.097497
- Total               0:20:28.153239
 23, time : 0.000 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.002 sec.
[Open3D DEBUG] [GlobalOptimizationLM] Optimizing PoseGraph having 10 nodes and 32 edges.
[Open3D DEBUG] Line process weight : 78.138922
[Open3D DEBUG] [Initial     ] residual : 1.897088e+02, lambda : 2.949502e-01
[Open3D DEBUG] [Iteration 00] residual : 1.854947e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 01] residual : 1.851665e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 02] residual : 1.851429e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 03] residual : 1.851405e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] [Iteration 04] residual : 1.851403e+02, valid edges : 23, time : 0.000 sec.
[Open3D DEBUG] Current_residual - new_residual < 1.000000e-06 * current_residual
[Open3D DEBUG] [GlobalOptimizationLM] total time : 0.001 sec.
[Open3D DEBUG] CompensateReferencePoseGraphNode : reference : 0
