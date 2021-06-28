#!/usr/bin/env python 
import rospy
from ros_tasks.msg import custom

def sender(val1, val2):
    rospy.init_node('publisher')
    pub = rospy.Publisher('value', custom, queue_size = 10)
    #val2 = int(input("Enter another integer: ")
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(val1,val2) 
        rate.sleep()
def values():
    a = int(input("Enter 1st value:  "))
    b = int(input("Enter 2 value: "))
    return a, b

if __name__ == '__main__':
    try:
        x, y = values()
        sender(x, y)
    except rospy.ROSInterruptException:
            pass

