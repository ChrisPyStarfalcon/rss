#!/usr/bin/env python3

from __future__ import print_function
import rospy
from std_srvs.srv import SetBool, SetBoolResponse

def pw_callback(request):
    rospy.loginfo("SetBool Server has been called")
    cur_response = SetBoolResponse()
    if request.data:
        cur_response.success = True
        cur_response.message = 'OK'
        return cur_response
    else:
        cur_response.success = False
        cur_response.message = 'failed'
        return cur_response
    
# server node
rospy.init_node('pw_srv_server')

# create service
pw_service = rospy.Service('setBool_service', SetBool, pw_callback)
rospy.loginfo('Service /SetBool_service Ready')

rospy.spin()