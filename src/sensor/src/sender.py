#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

def talker():
    rospy.init_node('test_dummy', anonymous=True)
    pub1 = rospy.Publisher('/upstream_data', Twist, queue_size=10)
    pub2 = rospy.Publisher('/surface_depth', Float32, queue_size=10)
    rate = rospy.Rate(50)

    while not rospy.is_shutdown():
        msg = Twist()
        meh = Float32()
        meh = 12.34
        msg.linear.x = 0
        msg.linear.y = 1
        msg.linear.z = -1
        msg.angular.x = 0
        msg.angular.y = 1
        msg.angular.z = -1
        pub1.publish(msg)
        pub2.publish(meh)
        rospy.loginfo(meh)
        rospy.loginfo(msg)
        rate.sleep()

if __name__ == '__main__':
    talker()