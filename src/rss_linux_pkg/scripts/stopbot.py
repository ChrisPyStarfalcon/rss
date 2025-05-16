#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def stop_robot():
    rospy.init_node('stop_robot')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    stop_cmd = Twist()
    stop_cmd.linear.x = 0.0
    stop_cmd.linear.y = 0.0
    stop_cmd.linear.z = 0.0
    stop_cmd.angular.x = 0.0
    stop_cmd.angular.y = 0.0
    stop_cmd.angular.z = 0.0
    
    rospy.loginfo("Stopping the robot...")
    pub.publish(stop_cmd)

if __name__ == "__main__":
    stop_robot()
