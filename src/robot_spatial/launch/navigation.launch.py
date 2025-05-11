from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable

import os

def generate_launch_description():
    pkg_dir = get_package_share_directory("robot_spatial")
    world_file = os.path.join(pkg_dir, "worlds", "my_world.world")
    maps_file = os.path.join(pkg_dir, "maps", "map.yaml")

    map_arg = DeclareLaunchArgument(
            name='map', default_value=maps_file)

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

    bringup_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory('nav2_bringup'),'/launch/bringup_launch.py']),
        launch_arguments={
            'use_namespace': 'False',
            'slam': 'False',
            'map': LaunchConfiguration('map'),
            'use_sim_time': 'True',
            'params_file': [get_package_share_directory('robot_spatial'),'/config/navigation.yaml'],
            'autostart': 'True',
            'use_composition': 'True',
            'use_respawn': 'False'
        }.items()
    )


# -----------------------------------------------------

    ld = LaunchDescription()
    # ld.add_action(map_arg)
    ld.add_action(gazebo)
    ld.add_action(load_robot)
    # ld.add_action(bringup_cmd)

    return ld
