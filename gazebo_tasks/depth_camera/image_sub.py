#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def callback(data):
    br = CvBridge()
    rospy.loginfo("Video frames is being received")
    fr = br.imgmsg_to_cv2(data)

    cv2.imshow("camera", fr)
    cv2.waitKey(1)


def subscriber():
    rospy.init_node('depth_camera_feed_sub', anonymous = True)
    rospy.Subscriber('camera/depth/image_raw', Image, callback)
    rospy.spin()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    subscriber()
