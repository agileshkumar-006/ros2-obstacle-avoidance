import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import TwistStamped


class ObstacleAvoidance(Node):

    def __init__(self):

        super().__init__("obstacle_avoidance_node")

        # -------------------------
        # ROS2 Parameters
        # -------------------------
        self.declare_parameter("safe_distance", 0.6)
        self.declare_parameter("linear_speed", 0.20)
        self.declare_parameter("angular_speed", 0.80)
        self.declare_parameter("debug", True)

        self.safe_distance = self.get_parameter(
            "safe_distance").value

        self.linear_speed = self.get_parameter(
            "linear_speed").value

        self.angular_speed = self.get_parameter(
            "angular_speed").value

        self.debug = self.get_parameter(
            "debug").value

        # Subscriber
        self.subscription = self.create_subscription(
            LaserScan,
            "/scan",
            self.scan_callback,
            10
        )

        # Publisher
        self.publisher = self.create_publisher(
            TwistStamped,
            "/cmd_vel",
            10
        )

        self.get_logger().info("Obstacle Avoidance Started")

    # -------------------------------------------------------

    def get_min_distance(self, data):

        valid = [
            x for x in data
            if not math.isinf(x)
            and not math.isnan(x)
            and x > 0.12
        ]

        if len(valid) == 0:
            return 10.0

        return min(valid)

    # -------------------------------------------------------

    def scan_callback(self, msg):

        total = len(msg.ranges)

        # Front
        front = list(msg.ranges[:20]) + list(msg.ranges[-20:])

        # Left
        left = msg.ranges[60:120]

        # Right
        right = msg.ranges[240:300]

        front_distance = self.get_min_distance(front)
        left_distance = self.get_min_distance(left)
        right_distance = self.get_min_distance(right)

        if self.debug:
            self.get_logger().info(
                f"Front: {front_distance:.2f} m | "
                f"Left: {left_distance:.2f} m | "
                f"Right: {right_distance:.2f} m"
            )

        cmd = TwistStamped()

        cmd.header.stamp = self.get_clock().now().to_msg()

        # -----------------------------
        # Robot Decision
        # -----------------------------

        if front_distance > self.safe_distance:

            cmd.twist.linear.x = self.linear_speed
            cmd.twist.angular.z = 0.0

            if self.debug:
                self.get_logger().info("Moving Forward")

        else:

            if left_distance > right_distance:

                cmd.twist.linear.x = 0.05
                cmd.twist.angular.z = self.angular_speed

                if self.debug:
                    self.get_logger().warn("Turning Left")

            else:

                cmd.twist.linear.x = 0.05
                cmd.twist.angular.z = -self.angular_speed

                if self.debug:
                    self.get_logger().warn("Turning Right")

        self.publisher.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = ObstacleAvoidance()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()