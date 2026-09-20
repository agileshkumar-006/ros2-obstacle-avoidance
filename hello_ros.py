import rclpy
from rclpy.node import Node


class HelloROS(Node):

    def __init__(self):
        super().__init__("hello_ros_node")

        self.get_logger().info("Hello! Welcome to ROS 2 Jazzy.")


def main(args=None):

    rclpy.init(args=args)

    node = HelloROS()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()