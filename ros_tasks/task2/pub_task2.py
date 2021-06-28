#!/usr/bin/env python

import rospy
from ros_tasks.msg import rec

global name, age

def data():
    global name, age
    name = input("Enter name in double quotations: ")
    age = int(input("Enter the age: "))

def main():
    global name, age
    rospy.init_node('data_collector')
    pub = rospy.Publisher('datas', rec, queue_size = 30)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(age, name)
        rate.sleep()

if __name__ == '__main__':
    try:
        data()
        main()
    except ROSInterruptException:
        pass
    

