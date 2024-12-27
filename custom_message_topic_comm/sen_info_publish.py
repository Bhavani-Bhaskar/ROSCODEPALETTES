#!/usr/bin/env python3

import rospy
from pack3cm.msg import Mycmessage  # Replace <package_name> with your package name

def publisher_node():
    rospy.init_node('custom_message_publisher', anonymous=True)
    pub = rospy.Publisher('custom_topic', Mycmessage, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # Create a message instance
        message = Mycmessage()
        message.id = 1
        message.name = "Sample Name"
        message.value = 42.0

        rospy.loginfo(f"Publishing: {message}")
        pub.publish(message)
        rate.sleep()

if _name_ == "_main_":
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass