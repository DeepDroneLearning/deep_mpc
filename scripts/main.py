#! /home/michael/.local/share/virtualenvs/DeepLearningProject-WE2UAgWf/bin/python

import rospy
import numpy as numpy
from geometry_msgs.msg import Twist

# import tensorflow as tf


def move(lin_vel, ang_vel):

    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)

    vel = Twist()
    while not rospy.is_shutdown():

        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = lin_vel

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel

        pub.publish(vel)
        rate.sleep()


if __name__ == "__main__":
    rospy.init_node("controller")

    try:
        node = move(10, 0)

    except rospy.ROSInterruptException:
        print("Caught Error")

    print("Exit")
