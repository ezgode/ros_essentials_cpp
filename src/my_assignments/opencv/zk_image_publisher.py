#!/usr/bin/env python 
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

if __name__ == '__main__':
  rospy.init_node('image_publisher', anonymous=True)
  video_capture = cv2.VideoCapture('/home/ezequiel/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/video/tennis-ball-video.mp4')
  pub = rospy.Publisher('/tennis_ball_image', Image, queue_size=10)
  bridge = CvBridge()
  while(True):
    # read the new frame
    ret, frame = video_capture.read()
    frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
    pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
    cv2.waitKey(30)
  video_capture.release()