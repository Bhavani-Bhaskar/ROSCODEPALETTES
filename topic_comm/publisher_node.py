#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def publisher():
    rospy.init_node('greetings_publisher', anonymous=True)
    pub = rospy.Publisher('/greetings', String, queue_size=10)
    rate = rospy.Rate(1)  # 1 message per second
    while not rospy.is_shutdown():
        message = "Hello from the publisher!"
        rospy.loginfo(f"Publishing: {message}")
        pub.publish(message)
        rate.sleep()
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

