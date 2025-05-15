#!/usr/bin/env python3

import rospy
from rss2_msgsrv_pkg.msg import date_cmd_vel
from geometry_msgs.msg import Twist

from datetime import datetime

rospy.init_node('msg_pub')
now = datetime.now ()
date_str = now.strftime("%m/%d/%y, %H:%M:%S")

pw_cmd_vel = date_cmd_vel ()
pw_cmd_vel.pw_date = date_str
pw_cmd_vel.pw_cmd_vel.linear.x = 0.5
pw_cmd_vel.pw_cmd_vel.angular.z = 0.1

pub = rospy.Publisher('/pw_topic', date_cmd_vel, queue_size = 1)
rate = rospy.Rate (1)

while not rospy.is_shutdown():
    pub.publish(pw_cmd_vel)
    rate.sleep()