cmake_minimum_required(VERSION 3.0.2)
project(hrwros_week1_assignment)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  hrwros_msgs
  message_generation
)


add_message_files(DIRECTORY msg
  FILES
  BoxHeightInformation.msg
  ## Add the file name for A1 part 2 here ##

)
generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES hrwros_week1
 CATKIN_DEPENDS rospy std_msgs message_runtime
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/week1_assignment2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)