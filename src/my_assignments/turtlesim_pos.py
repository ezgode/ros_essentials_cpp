#!/usr/bin/env python
# rosrun ros_essentials_cpp turtlesim_pos.py
# chmod +x
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def poseCallback(message):
    print(message)
    print("pose callback")
    print(' x=', message.x)
    print(' y=', message.y)
    print(' yaw=', message.theta)

if __name__ == '__main__':
    try:
        rospy.init_node('turtle_controller', anonymous=True)
        rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
        #rate = rospy.Rate(1) # 1hz
        rospy.spin()
        
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
