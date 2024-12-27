#!/usr/bin/env python3
import rospy
import actionlib
from rosrev1.msg import fibonacciAction, fibonacciGoal

def feedback_callback(feedback):
    rospy.loginfo(f"Received feedback: {feedback.partial_sequence}")

if _name_ == '_main_':
    rospy.init_node('fibonacci_client')
    client = actionlib.SimpleActionClient('fibonacci', fibonacciAction)

    rospy.loginfo('Waiting for action server to start...')
    client.wait_for_server()

    goal = fibonacciGoal(order=30)
    rospy.loginfo('Sending goal...')
    client.send_goal(goal, feedback_cb=feedback_callback)

    client.wait_for_result()
    rospy.loginfo(f"Result: {client.get_result().sequence}")