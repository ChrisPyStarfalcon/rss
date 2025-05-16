#!/usr/bin/env python3

import rospy
from rss_linux_pkg.msg import date_cmd_vel
from geometry_msgs.msg import Twist

from datetime import datetime

rospy.init_node('msg_pub')
now = datetime.now ()
date_str = now.strftime("%m/%d/%y, %H:%M:%S")

cp_cmd_vel = date_cmd_vel()
cp_cmd_vel.cp_date = date_str
cp_cmd_vel.cp_cmd_vel.linear.x = 0.5
cp_cmd_vel.cp_cmd_vel.angular.z = 0.1

pub = rospy.Publisher('/cp_topic', date_cmd_vel, queue_size = 1)
rate = rospy.Rate (1)

while not rospy.is_shutdown():
    pub.publish(cp_cmd_vel)
    rate.sleep()