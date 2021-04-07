#!/usr/bin/env python
# rosrun ros_essentials_cpp turtlesim_cleaner.py
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from sensor_msgs.msg import LaserScan


def min_dist_in_range(ranges, rg, angle_increment):
    range_init = int(math.radians(rg[0]%360)//angle_increment)
    range_end = int(math.radians(rg[1]%360)//angle_increment)
    if range_end > range_init:
        sector_data = ranges[range_init:range_end]
    else:
        sector_data = ranges[range_init:] + ranges[0:range_end]
    #print(sector_data)
    return min(sector_data)

def scan_callback(msg, data):
    
    data['dist_ahead'] = min_dist_in_range(msg.ranges, [-6, 6], msg.angle_increment)
    data['dist_left'] = min_dist_in_range(msg.ranges, [0, 30], msg.angle_increment)
    data['dist_right'] = min_dist_in_range(msg.ranges, [-30, 0], msg.angle_increment)
    #print(data)

def move_foward(speed_cmd, pub, data_dct, rate):
    done = False
    speed_cmd.linear.x = 0.3

    while not done:
        done = data_dct['dist_ahead']<0.6
        diff = data_dct['dist_left'] - data_dct['dist_right']
        if abs(diff)>.8:
            speed_cmd.angular.z = (diff)*0.3
        else:
            speed_cmd.angular.z = max([0, (1.5-data_dct['dist_ahead'])])*0.8

        speed_cmd.linear.x = 0.3 - max([0, (1.5-data_dct['dist_ahead'])]) * 0.3
        print(data_dct, speed_cmd.angular.z)
        pub.publish(speed_cmd)
        rate.sleep()
        #print(data_dct['dist_ahead'], speed_cmd.linear.x)
    speed_cmd.linear.x = 0
    speed_cmd.angular.z = 0
    pub.publish(speed_cmd)

def rotate_until_free(speed_cmd, pub, data_dct, rate):
    done = False
    speed_cmd.angular.z = 0.5

    while not done:
        done = data_dct['dist_ahead']>3
        pub.publish(speed_cmd)
        rate.sleep()
        #print(data_dct['dist_ahead'], speed_cmd.angular.z)
    speed_cmd.angular.z = 0.0
    pub.publish(speed_cmd)


if __name__ == '__main__':
    rospy.init_node('turtlebot3_move_while_possible')

    # Reset the turtle simulator
    print("Reseting the simulator")
    reset_turtle = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
    reset_turtle()

    # create the command publisher and the pose subscriber
    data_dct = {'dist_ahead':100, 'dist_left':100, 'dist_right':100}
    rospy.Subscriber("/scan", LaserScan, scan_callback, data_dct)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    # Initialize the speed message
    speed_cmd = Twist()
    

    # # Set the frequency at which we wwant to iterate
    rate = rospy.Rate(20) # 1hz

    while True:
        #x = max([0, ])
        move_foward(speed_cmd, pub, data_dct, rate)
        rotate_until_free(speed_cmd, pub, data_dct, rate)
    