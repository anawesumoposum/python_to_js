#!/usr/bin/env python3

import random, time, json
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

def callback0(data):
    stuff = {'angular': {'x': data.angular.x, 'y': data.angular.y, 'z': data.angular.z},
            'linear': {'x': data.linear.x, 'y': data.linear.y, 'z': data.linear.z}}
    jsonstuff = json.dumps(stuff)
    print(jsonstuff, flush=True, end=' ')


def callback1(data):
    jsonstuff = json.dumps(data.data)
    print(jsonstuff, flush=True, end = ' ')

def listener():
    rospy.init_node('upstream_listener', anonymous=True)
    #rospy.Subscriber('/upstream_data', Twist, callback0)
    rospy.Subscriber('/surface_depth', Float32, callback1)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass