cmake_minimum_required(VERSION 3.0.2)
project(rss_linux_pkg)

## Find catkin and required packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

## Declare the ROS messages/services
add_service_files(
  FILES
  turtlebot_move_square.srv
)

## Generate the service message headers
generate_messages(
  DEPENDENCIES
  std_msgs
)

## Declare the catkin package
catkin_package(
  CATKIN_DEPENDS rospy std_msgs message_runtime
)

## Install Python scripts
catkin_install_python(PROGRAMS
  scripts/move_square_server.py
  scripts/move_square_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Include directories
include_directories(
  ${catkin_INCLUDE_DIRS}
)
