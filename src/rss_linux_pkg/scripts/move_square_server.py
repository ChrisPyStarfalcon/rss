#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from rss_linux_pkg.srv import turtlebot_move_square, turtlebot_move_squareResponse
import math
from nav_msgs.msg import Odometry


class MoveTurtleBot:
    initial_x = 0
    initial_y = 0
    def __init__(self):
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        rospy.Subscriber('/odom', Odometry, self.odom_callback)

        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)

        # Initialize position tracking attributes
        self.initial_x = None
        self.initial_y = None
        self.distance_traveled = 0.0  # Add this to prevent missing attribute issues

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.stop_turtlebot()
        self.ctrl_c = True

    def odom_callback(self, pos):
        """Track distance traveled"""
        x = pos.pose.pose.position.x
        y = pos.pose.pose.position.y

        if self.initial_x is None or self.initial_y is None:
            self.initial_x = x
            self.initial_y = y
            return

        self.distance_traveled = math.sqrt((x - self.initial_x) ** 2 + (y - self.initial_y) ** 2)

    def stop_turtlebot(self):
        """Stop the robot"""
        rospy.loginfo("Stopping TurtleBot.")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.vel_pub.publish(self.cmd)

    def move_for_distance(self, target_distance, speed):
        """Move forward until the target distance is reached"""
        self.initial_x = None  # Reset initial position
        self.initial_y = None
        self.distance_traveled = 0.0

        self.cmd.linear.x = speed
        while self.distance_traveled < target_distance and not rospy.is_shutdown():
            self.vel_pub.publish(self.cmd)
            self.rate.sleep()

        self.stop_turtlebot()

    def spot_turn(self, radians):
        """Turn in place"""
        self.cmd.linear.x = 0
        self.cmd.angular.z = radians
        rospy.loginfo(f"Turning {radians} radians.")
        
        for _ in range(int(1.5)):  # Adjust duration
            self.vel_pub.publish(self.cmd)
            self.rate.sleep()

        self.stop_turtlebot()


def handle_request(req):
    """Service callback to move the TurtleBot in a square"""
    rospy.loginfo(f"Moving in a square with side length {req.sideLength}, repeating {req.repetitions} times.")
    
    mover = MoveTurtleBot()
    success = True

    try:
        for _ in range(req.repetitions):
            for _ in range(4):  # Four sides of the square
                mover.move_for_distance(req.sideLength, 0.2)  # Move forward for requested side length
                mover.spot_turn(1.57)  # Turn 90 degrees
    except Exception as e:
        rospy.logwarn(f"Movement error: {str(e)}")
        success = False

    return turtlebot_move_squareResponse(success)


if __name__ == '__main__':
    rospy.init_node('move_square_server')  # Initialize the node here
    service = rospy.Service('turtlebot_move_square', turtlebot_move_square, handle_request)
    rospy.loginfo("Ready to move TurtleBot in a square!")
    rospy.spin()
