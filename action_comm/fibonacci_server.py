#!/usr/bin/env python3
import rospy
import actionlib
from rosrev1.msg import fibonacciAction, fibonacciFeedback, fibonacciResult

class fibonacciActionServer:
    def _init_(self):
        self.server = actionlib.SimpleActionServer(
            'fibonacci', 
            fibonacciAction, 
            self.execute_callback, 
            False
        )
        self.server.start()

    def execute_callback(self, goal):
        feedback = fibonacciFeedback()
        result = fibonacciResult()
        sequence = [0, 1]

        for i in range(2, goal.order):
            if self.server.is_preempt_requested():
                rospy.loginfo('Goal canceled/preempted')
                self.server.set_preempted()
                return
            
            sequence.append(sequence[i-1] + sequence[i-2])
            feedback.partial_sequence = sequence
            self.server.publish_feedback(feedback)
            rospy.sleep(1)  # Simulating a delay

        result.sequence = sequence
        self.server.set_succeeded(result)

if _name_ == '_main_':
    rospy.init_node('fibonacci_server')
    server = fibonacciActionServer()
    rospy.spin()