#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def callback(data):
    rospy.loginfo(f"Subscriber received: {data.data}")
def subscriber():
    rospy.init_node('greetings_subscriber', anonymous=True)
    rospy.Subscriber('/greetings', String, callback)
    rospy.spin()  # Keep the node running to process incoming messages

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass


