from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import SetRemap
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    rtabmap_lidar3d = os.path.join(
        get_package_share_directory('rtabmap_examples'),
        'launch', 'lidar3d.launch.py'
    )

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rtabmap_lidar3d),
        launch_arguments={
            'lidar_topic': '/robot1/velodyne_points/points',
            'frame_id': 'velodyne_frame',
            'use_sim_time': 'true',
            'voxel_size': '0.15',
            'deskewing': 'true',
        }.items()
    )

    slam_group = GroupAction([
        SetRemap(src="/tf", dst="/robot1/tf"),
        SetRemap(src="/tf_static", dst="/robot1/tf_static"),
        slam,
    ])

    return LaunchDescription([slam_group])
