#!/usr/bin/env python
# license removed for brevity
# chmod +x
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(message):
    print(message)
    #rospy.loginfo("I heard %s", message.data)

def control():
    #create a new publisher. we specify the topic name, then type of message then the queue size
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

    #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('turtle_controller', anonymous=True)
    #set the loop rate
    rate = rospy.Rate(1) # 1hz
    #rospy.spin()
    #keep publishing until a Ctrl-C is pressed
    i = 0
    command = Twist()
    while not rospy.is_shutdown():
        
        command.linear.x=1
        command.angular.z=1+i%3
        
        #rospy.loginfo(hello_str)
        pub.publish(command)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass
