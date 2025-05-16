#!/usr/bin/env python3

import rospy
from rss_linux_pkg.msg import date_cmd_vel

def callback(msg):
    rospy.loginfo(msg.cp_date)
    rospy.loginfo(msg.cp_cmd_vel)

rospy.init_node('msg_sub')
sub = rospy.Subscriber('/cp_topic', date_cmd_vel, callback)

rospy.spin()