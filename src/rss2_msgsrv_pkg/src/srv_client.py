#! / usr / bin / env python3

from __future__ import print_function
import sys
import rospy
from std_srvs.srv import SetBool, SetBoolRequest

rospy.init_node('pw_srv_client ')
rospy.wait_for_service('/setBool_service')
try :
    get_setBool_service = rospy.ServiceProxy('/ setBool_service ', SetBool)
    get_setBool_object = SetBoolRequest()
    get_setBool_object.data = False
    result = get_setBool_service(get_setBool_object)
    if result.success == True :
        rospy.loginfo('Service called successful !')
        rospy.loginfo(result.message)
    else:
        rospy.loginfo('Service called not successful ! ')
        rospy.loginfo(result.message)
        rospy.loginfo('End of service call')
except rospy.ServiceException as e:
    print ("Service did not process request : " + str(e))