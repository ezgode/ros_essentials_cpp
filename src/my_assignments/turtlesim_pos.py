#!/usr/bin/env python
# license removed for brevity
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
    #rospy.loginfo("I heard %s", message.data)

def control():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    rospy.init_node('turtle_controller', anonymous=True)
    rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
    rate = rospy.Rate(1) # 1hz

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
