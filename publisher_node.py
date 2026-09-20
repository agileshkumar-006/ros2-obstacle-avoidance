import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelocityPublisher(Node):

    def __init__(self):
        super().__init__("velocity_publisher")

        # Create a publisher for the /cmd_vel topic
        self.publisher_ = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        # Publish every 0.5 seconds
        self.timer = self.create_timer(
            0.5,
            self.publish_velocity
        )

        self.get_logger().info("Velocity Publisher Started")

    def publish_velocity(self):

        msg = Twist()

        # Move forward
        msg.linear.x = 0.20

        # No sideways movement
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        # No rotation
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)

        self.get_logger().info("Publishing Forward Velocity")


def main(args=None):

    rclpy.init(args=args)

    node = VelocityPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()