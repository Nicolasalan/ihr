from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.actions import DeclareLaunchArgument

import os

def generate_launch_description():
    pkg_dir = get_package_share_directory("robot_spatial")
    world_file = os.path.join(pkg_dir, "worlds", "my_world.world")

    load_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('robot_description'),'/launch/robot.launch.py']),
        launch_arguments={
            'rviz_config': [get_package_share_directory('robot_spatial'), '/rviz/navigation.rviz'],
        }.items()

    )
    gazebo_launch_file = os.path.join(
        get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py"
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments={
            "world": world_file,
        }.items(),
    )

# -----------------------------------------------------

    ld = LaunchDescription()
    ld.add_action(gazebo)
    ld.add_action(load_robot)

    return ld
