#!/usr/bin/env python
# rosrun ros_essentials_cpp turtlesim_cleaner.py
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from sensor_msgs.msg import LaserScan

def scan_callback(msg, data):
    delta_ids = int(math.radians(20)//msg.angle_increment)
    sector_data = msg.ranges[-delta_ids:]+msg.ranges[0:delta_ids]
    min_dist_ahead = min(sector_data)
    data['min_dist_ahead'] = min_dist_ahead

def move_foward(speed_cmd, pub, data_dct, rate):
    done = False
    speed_cmd.linear.x = 0.3

    while not done:
        done = data_dct['min_dist_ahead']<0.6
        pub.publish(speed_cmd)
        rate.sleep()
        #print(data_dct['min_dist_ahead'], speed_cmd.linear.x)
    speed_cmd.linear.x = 0
    pub.publish(speed_cmd)

def rotate_until_free(speed_cmd, pub, data_dct, rate):
    done = False
    speed_cmd.angular.z = 0.5

    while not done:
        done = data_dct['min_dist_ahead']>3
        pub.publish(speed_cmd)
        rate.sleep()
        #print(data_dct['min_dist_ahead'], speed_cmd.angular.z)
    speed_cmd.angular.z = 0.0
    pub.publish(speed_cmd)


if __name__ == '__main__':
    rospy.init_node('turtlebot3_move_while_possible')

    # Reset the turtle simulator
    print("Reseting the simulator")
    reset_turtle = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
    reset_turtle()

    # create the command publisher and the pose subscriber
    data_dct = {'min_dist_ahead':100}
    rospy.Subscriber("/scan", LaserScan, scan_callback, data_dct)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Initialize the speed message
    speed_cmd = Twist()
    

    # # Set the frequency at which we wwant to iterate
    rate = rospy.Rate(20) # 1hz

    while True:
        move_foward(speed_cmd, pub, data_dct, rate)
        rotate_until_free(speed_cmd, pub, data_dct, rate)
    