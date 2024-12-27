#!/usr/bin/env python3
import rospy
from <package_name>.srv import AddTwoInts
rospy.init_node('add_two_ints_client')
rospy.wait_for_service('add_two_ints')
add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
result = add_two_ints(5, 10)
rospy.loginfo(f"Sum: {result.sum}")
