#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def publisher(pub, rate):
    """Function to publish messages."""
    message = "Hello from the publisher!"
    rospy.loginfo(f"Publishing: {message}")
    pub.publish(message)
    rate.sleep()

def callback(data):
    """Callback function for subscriber."""
    rospy.loginfo(f"Subscriber received: {data.data}")

if __name__ == '__main__':
    try:
        # Initialize the node
        rospy.init_node('greetings_pub_sub', anonymous=True)

# Publisher setup
        pub = rospy.Publisher('/greetings', String, queue_size=10)
        rate = rospy.Rate(1)  # 1 message per second

        # Subscriber setup
        rospy.Subscriber('/greetings', String, callback)

        # Run the publisher and subscriber in the same loop
        while not rospy.is_shutdown():
            publisher(pub, rate)
            rospy.spin()  # Process incoming messages
            
    except rospy.ROSInterruptException:
        pass

