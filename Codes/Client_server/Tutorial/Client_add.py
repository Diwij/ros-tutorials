#!/usr/bin/env python

from ros_essentials_cpp.srv import Add_3_int
from ros_essentials_cpp.srv import Add_3_intRequest 
from ros_essentials_cpp.srv import Add_3_intResponse
import rospy    
import sys

def add_3_int_client(x, y, z):
    rospy.wait_for_service('adding3int')
    try:
        add_3_int = rospy.ServiceProxy('adding3int', Add_3_int)
        resp1 = add_3_int(x, y, z)
        return resp1.sum

    except rospy.ServiceException(e):
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y z]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s+%s+%s"%(x, y, z)
    s = add_3_int_client(x, y, z)
    print "%s + %s +%s = %s"%(x, y, z, s)