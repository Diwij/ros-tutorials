#!/usr/bin/env python
import rospy
from ros_essentials_cpp.msg import CustomMsg

def Custom_msg_callback(Custom_msgs):
    rospy.loginfo("new CustomData received: (%s, %d, %s ,%d)", 
        Custom_msgs.name,Custom_msgs.age,
        Custom_msgs.gender,Custom_msgs.marks)

rospy.init_node('Custom_subscriber_node', anonymous=True)

rospy.Subscriber("Custom_msgs", CustomMsg, Custom_msg_callback)

rospy.spin()