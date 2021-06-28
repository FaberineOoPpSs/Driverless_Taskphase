#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ros_tasks.msg import rec

rospy.init_node('doubler_data')

global st

def callback(data):
    #global st
    if data.age >= 18:
        st = "True"
        #print(st)
    else:
        st = "False"
    pub = rospy.Publisher('eligibility', String, queue_size = 30)
    pub.publish(st)
def main():
    #global st
    sub = rospy.Subscriber('datas', rec, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy. ROSInterruptException:
        pass
