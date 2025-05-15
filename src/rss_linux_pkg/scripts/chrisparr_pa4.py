#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import math

class MoveDistance:
    def __init__(self, target):
        rospy.init_node('move_until_distance', anonymous=True)

        # publisher
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # subscriber
        rospy.Subscriber('/odom', Odometry, self.odom_callback)

        # Store initial position
        self.initial_x = None
        self.initial_y = None
        self.target = target

        # Velocity command
        self.cmd = Twist()

    def odom_callback(self, pos):
        """ Process odometry and stop the robot when distance is reached """
        x = pos.pose.pose.position.x
        y = pos.pose.pose.position.y

        if self.initial_x is None or self.initial_y is None:
            self.initial_x = x
            self.initial_y = y
            return

        # Calculate traveled distance using pythagoras
        distance = math.sqrt((x - self.initial_x) ** 2 + (y - self.initial_y) ** 2)
        rospy.loginfo(f"Distance traveled: {distance:.2f}m")

        if distance < self.target:
            self.cmd.linear.x = 0.2
        else:
            self.cmd.linear.x = 0.0
            rospy.loginfo("Target distance reached! Stopping.")

        self.cmd_pub.publish(self.cmd)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        node = MoveDistance(target=2.0)
        node.run()
    except rospy.ROSInterruptException:
        pass
