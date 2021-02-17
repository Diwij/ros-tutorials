#!/usr/bin/env python
import rospy
from ros_essentials_cpp.msg import CustomMsg
import random

pub = rospy.Publisher('Custom_msgs', CustomMsg, queue_size=10)
rospy.init_node('Custom_publisher_node', anonymous=True)
rate = rospy.Rate(0.2)

i = 0
while not rospy.is_shutdown():
    Custom = CustomMsg()
    Custom.name = "Diwij"
    Custom.age= 19

    Custom.gender = "Male"
    Custom.marks = 75 + (random.random()*25)
    rospy.loginfo("I publish:")
    rospy.loginfo(Custom)
    pub.publish(Custom)
    rate.sleep()
    i=i+1

