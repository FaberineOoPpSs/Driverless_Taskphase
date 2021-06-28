#!/usr/bin/env python
import rospy
from ros_tasks.msg import custom

rospy.init_node('final_value_pub')

def callback(msg):
    a = msg.value1
    b = msg.value2
    print(a + b)

def main():
    sub = rospy.Subscriber('value', custom, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
