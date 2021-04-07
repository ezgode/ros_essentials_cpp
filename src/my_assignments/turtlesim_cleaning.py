#!/usr/bin/env python
# rosrun ros_essentials_cpp turtlesim_cleaner.py
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty


def go_to(x, y, pos_dct, speed_cmd, pub, rate):
    done = False
    eps = 0.0005
    while not done:
        dy = y-pos_dct['y']
        dx = x-pos_dct['x']
        # print(dx, dy)
        dist_to_goal = math.sqrt( dx**2 + dy**2 )
        
        target_vector = [dx/dist_to_goal, dy/dist_to_goal]
        head_vector = [math.cos(pos_dct['theta']), math.sin(pos_dct['theta'])]

        # correct angle first if needed
        scalar_prod = target_vector[0] * head_vector[0] + target_vector[1] * head_vector[1]
        # print(scalar_prod)
        if scalar_prod>(1+eps) or scalar_prod<(1-eps):
            speed_cmd.linear.x = 0
            speed_cmd.angular.z = max([1,abs(1-scalar_prod)*2.5])
        else:
            speed_cmd.linear.x = max([1, dist_to_goal-1])*2.3
            speed_cmd.angular.z = 0        
        
        pub.publish(speed_cmd)
        done = dist_to_goal<0.2
        rate.sleep()
    
    # print('Arrived')
    speed_cmd.linear.x = 0
    speed_cmd.angular.z = 0      
    pub.publish(speed_cmd)

def norm_v(vs):
    d = math.sqrt(vs[0]**2+vs[1]**2)

    return [vs[0]/d, vs[1]/d]

def calc_corners(n, r=5, c=[5.,5.], delta_ang=30):
    angs = [ math.radians( i*360/n + delta_ang ) for i in range(n)]
    res = [[math.cos(a)*r + c[0], math.sin(a)*r + c[1]] for a in angs]
    return res

def get_directive_vectors(corners):
    aux_tow = [corners[-1]]+corners[:]
    aux_from = corners[:]+[corners[0]]

    vs_towards_norm = [ norm_v([aux_tow[i+1][0] - aux_tow[i][0] , aux_tow[i+1][1] - aux_tow[i][1] ]) for i in range(len(aux_tow)-1)  ]
    vs_from_norm = [norm_v([ aux_from[i+1][0] - aux_from[i][0], aux_from[i+1][1] - aux_from[i][1] ]) for i in range(len(aux_from)-1)  ]
    vs_aux = [ norm_v([vs_from_norm[i][0]-vs_towards_norm[i][0], vs_from_norm[i][1]-vs_towards_norm[i][1] ])    for i in range(len(vs_towards_norm))]
    return vs_aux

def poseCallback(message, pos_dct):
    pos_dct['x'] = message.x
    pos_dct['y'] = message.y
    pos_dct['theta'] = message.theta

if __name__ == '__main__':
    rospy.init_node('cleaning_turtle', anonymous=True)

    # Reset the turtle simulator
    print("Reseting the turtle simulator")
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()

    # create the command publisher and the pose subscriber
    pos_dct = {'x':0, 'y':0, 'theta':0}
    rospy.Subscriber("/turtle1/pose", Pose, poseCallback, pos_dct)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Initialize the speed message
    speed_cmd = Twist()
    speed_cmd.linear.x = 1

    # Set the frequency at which we wwant to iterate
    rate = rospy.Rate(40) # 1hz

    corners = calc_corners(10)
    vs_aux = get_directive_vectors(corners)

    done = False
    dd = 0.5
    cnt =0    
    while not done:     
        cnt += 1  
        for i, c in enumerate(corners):
            xt = c[0] + vs_aux[i][0] * dd 
            yt = c[1] + vs_aux[i][1] * dd 

            go_to(xt, yt, pos_dct, speed_cmd, pub, rate)
        dd += 0.5
        done = cnt>4
    # Infinite loop
    # while not rospy.is_shutdown():
    #     print(pos_dct)
    #     pub.publish(speed_cmd)
    #     rate.sleep()

    # rospy.spin()*