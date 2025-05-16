#!/usr/bin/env python3
import rospy
from rss_linux_pkg.srv import turtlebot_move_square

rospy.init_node('move_square_client')
rospy.wait_for_service('turtlebot_move_square')
service_proxy = rospy.ServiceProxy('turtlebot_move_square', turtlebot_move_square)

side_length = 1.0  # Example side length in meters
repetitions = 3    # Example number of times to repeat

response = service_proxy(side_length, repetitions)
if response.success:
    rospy.loginfo("Successfully completed the square movement!")
else:
    rospy.logwarn("Failed to complete the movement.")