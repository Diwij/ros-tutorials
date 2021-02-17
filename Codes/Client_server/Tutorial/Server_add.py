#!/usr/bin/env python

from ros_essentials_cpp.srv import Add_3_int
from ros_essentials_cpp.srv import Add_3_intRequest
from ros_essentials_cpp.srv import Add_3_intResponse
import rospy

def handle_add_3_int(req):
    print "Returning [%s + %s + %s = %s]"%(req.a, req.b, req.c, (req.a + req.b + req.c))
    return Add_3_intResponse(req.a + req.b + req.c)

def add_3_int_server():
    rospy.init_node('add_3_ints_server')
    Ser = rospy.Service('adding3int', Add_3_int, handle_add_3_int)
    print("Ready to add 3 integers")

    rospy.spin()

if __name__ == "__main__":
    add_3_int_server()