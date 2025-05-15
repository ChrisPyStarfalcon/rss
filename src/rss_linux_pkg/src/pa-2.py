#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class MoveTurtleBot():

    def __init__(self):
        self.turtlebot_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)

    def publish_once_in_cmd_vel(self):
        while not self.ctrl_c:
            connections = self.turtlebot_vel_publisher.get_num_connections()
            if connections > 0:
                self.turtlebot_vel_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.stop_turtlebot()
        self.ctrl_c = True

    def stop_turtlebot(self):
        rospy.loginfo("shutdown time! Stop the robot")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()

    def move_for_time(self, moving_time, linear_speed):
        self.cmd.linear.x = -linear_speed
        self.cmd.angular.z = 0
        rospy.loginfo("forward " + str(moving_time))        
        self.publish_for_time(moving_time)
        self.stop_turtlebot()
    
    def spot_turn_for_rads(self, moving_time, radians):
        self.cmd.linear.x = 0
        self.cmd.angular.z = radians
        rospy.loginfo("spot turn "+ str(radians) + " for " + str(moving_time) + "s")
        self.publish_for_time(moving_time)
        self.stop_turtlebot()
    
    def publish_for_time(self, moving_time):
        i = 0
        while not self.ctrl_c and i <= moving_time:
            self.publish_once_in_cmd_vel()
            i = i+1
            self.rate.sleep()


if __name__ == '__main__':
    rospy.init_node('move_turtlebot_test', anonymous=True)
    moveturtlebot_object = MoveTurtleBot()
    try:
        i = 0
        while i < 4:
            moveturtlebot_object.move_for_time(5, 0.2)
            moveturtlebot_object.spot_turn_for_rads(0.75, 1.57)
            i = i + 1
    except rospy.ROSInterruptException:
        pass
