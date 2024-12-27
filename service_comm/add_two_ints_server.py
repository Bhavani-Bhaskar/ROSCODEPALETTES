#!/usr/bin/env python3
import rospy
from <package_name>.srv import AddTwoInts, AddTwoIntsResponse
def handle_add_two_ints(req):
    result = req.a + req.b
    rospy.loginfo(f"Summing: {req.a} + {req.b} = {result}")
    return AddTwoIntsResponse(result)
rospy.init_node('add_two_ints_server')
service = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
rospy.loginfo("Service ready to add two integers.")
rospy.spin()
