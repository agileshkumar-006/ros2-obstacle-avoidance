import os

from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    package_share = get_package_share_directory("obstacle_avoidance")

    params = os.path.join(
        package_share,
        "config",
        "params.yaml"
    )

    rviz = os.path.join(
        package_share,
        "config",
        "obstacle.rviz"
    )

    obstacle_node = Node(
        package="obstacle_avoidance",
        executable="obstacle_node",
        output="screen",
        parameters=[params]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["-d", rviz],
        output="screen"
    )

    return LaunchDescription([
        obstacle_node,
        rviz_node,
    ])