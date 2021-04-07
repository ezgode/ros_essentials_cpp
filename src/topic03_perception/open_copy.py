#!/usr/bin/env python

#import numpy: the data structure that will handle an image
import numpy as np

#import openCV
import cv2
 

image_name = "flower"

print ('read an image from file')
img = cv2.imread("/home/ezequiel/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/images/"+image_name+".jpg")

print ('create a window holder for the image')
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

print ('display the image')
cv2.imshow("Image",img)

print ('press a key inside the image to make a copy')
cv2.waitKey(0)

print ('image copied to folder /home/ezequiel/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/images/copy/')
cv2.imwrite("/home/ezequiel/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/images/copy/"+image_name+"-copy.jpg",img)
