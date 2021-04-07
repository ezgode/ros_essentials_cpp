#!/usr/bin/env python 
import numpy as np
import cv2


def filter_color(rgb_image, lower_bound_color, upper_bound_color):
    #convert the image into the HSV color space
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv image",hsv_image)

    #find the upper and lower bounds of the yellow color (tennis ball)


    #define a mask using the lower and upper bounds of the yellow color 
    mask = cv2.inRange(hsv_image, lower_bound_color, upper_bound_color)
    return mask, hsv_image

def getContours(binary_image):      
    #_, contours, hierarchy = cv2.findContours(binary_image, 
    #                                          cv2.RETR_TREE, 
    #                                           cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(binary_image.copy(), 
                                            cv2.RETR_EXTERNAL,
	                                        cv2.CHAIN_APPROX_SIMPLE)
    return contours


def draw_contours_on_image(img, contours):
    for c in contours:
        area = cv2.contourArea(c)
        perimeter= cv2.arcLength(c, True)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if (area>100):
            cv2.drawContours(img, [c], -1, (150,250,150), 3)
            cx, cy = get_contour_center(c)
            cv2.circle(img, (cx,cy),(int)(radius),(0,0,255),3)
    return img

def draw_ball_contour(binary_image, rgb_image, contours):
    black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3],'uint8')
    rgb_image = draw_contours_on_image(rgb_image, contours)
    black_image = draw_contours_on_image(black_image, contours)
    return rgb_image, black_image

def get_contour_center(contour):
    M = cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx= int(M['m10']/M['m00'])
        cy= int(M['m01']/M['m00'])
    return cx, cy

def find_ball(frame):
	# FILTER COLOR
	yellowLower =(20, 100, 100)
	yellowUpper = (80, 255, 255)
	binary_image_mask, hsv_image = filter_color(frame, yellowLower, yellowUpper)

	black_image = frame[:]*0

	# CONTOUR
	contours = getContours(binary_image_mask)

	draw_contours_on_image(black_image, contours)
	draw_contours_on_image(frame, contours)
	draw_contours_on_image(hsv_image, contours)

	return np.concatenate((frame, hsv_image, black_image), axis=1)	

if __name__ == '__main__':
	video_capture = cv2.VideoCapture('/home/ezequiel/catkin_ws/src/ros_essentials_cpp/src/topic03_perception/video/tennis-ball-video.mp4')
	while(True):
		# read the new frame
		ret, frame = video_capture.read()
		frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
		frame_ = find_ball(frame)
		cv2.imshow("Frame",frame_)
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break

	video_capture.release()
	cv2.destroyAllWindows()