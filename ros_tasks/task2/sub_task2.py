#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('final_eligibility_status')

def callback(msg):
    st = msg.data
    if st == "True":
        print("Candidate is eligible to vote!")
    else:
        print("Candidate is inelidible to vote ")
def main():
    sub = rospy.Subscriber('eligibility', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except ROSInterruptException:
        pass
