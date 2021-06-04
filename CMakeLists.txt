cmake_minimum_required(VERSION 3.0.2)
project(deep_mpc)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  tf
  laser_geometry
  sensor_msgs
  message_filters
)

catkin_package(
 INCLUDE_DIRS include
 LIBRARIES
 CATKIN_DEPENDS roscpp rospy
 DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)



add_executable(sphere src/sphere.cpp)
target_link_libraries(sphere ${catkin_LIBRARIES})
add_dependencies(sphere ${catkin_EXPORTED_TARGETS})