#!/usr/bin/env python3

import rospy
from rss_linux_pkg import srv_turtlebot_move, srv_turtlebot_moveResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo('Turtlebot_move_service called')
    vel.linear.x = 0.2
    vel.angular.z = 0.2
    total_time = 0
    while total_time <= request.duration:
        cp_pub.publish(vel)
        rospy.loginfo('time = %d', total_time)
        rate.sleep()
        total_time += 1
    vel.linear.x = 0
    vel.angular.z = 0
    cp_pub.publish(vel)
    rate.sleep()

    return srv_turtlebot_moveResponse(True)

rospy.init_node('turtlebot_move_server')

cp_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
cp_service = rospy.Service('/turtlebot_move_service', srv_turtlebot_move, my_callback)
vel = Twist()

rate = rospy.Rate(1)

rospy.loginfo('Service /turtlebot_move_service is ready')
rospy.spin()