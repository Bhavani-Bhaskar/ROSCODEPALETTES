#!/usr/bin/env python3

import rospy
from pack3cm.msg import Mycmessage  # Replace with your package name

def callback(message):
    rospy.loginfo(f"Received message: id={message.id}, name={message.name}, value={message.value}")

def subscriber_node():
    rospy.init_node('custom_message_subscriber', anonymous=True)
    rospy.Subscriber('custom_topic', Mycmessage, callback)
    rospy.loginfo("Subscriber node is now listening to 'custom_topic'...")
    rospy.spin()  # Keep the node alive to listen for messages

if _name_ == "_main_":
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass