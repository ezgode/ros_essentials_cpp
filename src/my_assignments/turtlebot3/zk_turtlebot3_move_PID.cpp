#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "laserscan/LaserScanner.h"
#include "geometry_msgs/Twist.h"
#include "std_srvs/Empty.h"
#include "utility_lib.h"
#include <cstdlib>

using namespace std;

int angToIdx(double angle, double angle_inc){
  if (angle<0){
      angle = 360.0 + angle;
  }
  return (int)(angle/radian2degree(angle_inc));
};

void getMinRange(double &res, sensor_msgs::LaserScan & laser_scan_msg, double angle, double delta_ang){
  int index0 {angToIdx(angle-delta_ang, laser_scan_msg.angle_increment)};
  int index1 {angToIdx(angle+delta_ang, laser_scan_msg.angle_increment)};
  if (index1>index0){
    res = LaserScanner::getAverageRange(laser_scan_msg, index0, index1);
  }else{
    double rs1 {0.0}, rs2 {0.0};
    rs1 = LaserScanner::getAverageRange(laser_scan_msg, 0, index1);
    rs2 = LaserScanner::getAverageRange(laser_scan_msg, index0, laser_scan_msg.ranges.size());
    res = (rs1<rs2) ? rs1 : rs2;
  } 

  if(std::isnan(res))
    res = 100;
};

class Listener{
public:
  double dist_ahead {100.0};
  double dist_left {100.0};
  double dist_right {10.0};
public:
  void scanCallback(sensor_msgs::LaserScan scanMessage){
    getMinRange(this->dist_ahead, scanMessage, 0, 45);
    getMinRange(this->dist_left, scanMessage, 45, 20);
    getMinRange(this->dist_right, scanMessage, -45, 20);
  };
};

void resetSpeedCmd(geometry_msgs::Twist &vel_msg){
  vel_msg.linear.x =0.0;
  vel_msg.angular.z =0.0;
};

ros::Subscriber scanSubscriber;
ros::Publisher velocity_publisher;

//void scanCallback (sensor_msgs::LaserScan scanMessage, distances &dist);
int main(int argc, char **argv)
{
  ros::init(argc, argv, "turtlebot3_move_PID");
  ros::NodeHandle n;

  // RESET THE SIMULATION
  ros::ServiceClient client = n.serviceClient<std_srvs::Empty>("/gazebo/reset_simulation");
  std_srvs::Empty req;
  cout << "Reseting the simulator" << endl;
  client.call(req);

  // Subscribe to the scan topic
  Listener listener;
  scanSubscriber = n.subscribe("/scan", 10, &Listener::scanCallback, &listener);
  velocity_publisher = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);

  geometry_msgs::Twist vel_msg;
  ros::Rate loop_rate(100);

  int stop_cnts {0};
  int state_id {0};
  int rot_sign {1};
  const double ahead_th {4}, lat_dist {0.4};
  double t0 = ros::Time::now().toSec();
  double t1 = ros::Time::now().toSec();  
  do{

    vel_msg.linear.x = (listener.dist_ahead > ahead_th) ? 0.4 : 0.4 - (ahead_th-listener.dist_ahead)*0.1;
    double delta_lat_dist {listener.dist_left - listener.dist_right};
    vel_msg.angular.z = (delta_lat_dist <-lat_dist or delta_lat_dist > lat_dist) ? (delta_lat_dist - lat_dist)*0.001 : 0.0;

    //vel_msg.linear.x = (vel_msg.linear.x<.8) ? vel_msg.linear.x : 0.8;  
    vel_msg.angular.z = (vel_msg.angular.z<-.5) ? -.5 : ((vel_msg.angular.z>.5) ? 0.5 : vel_msg.angular.z);  
    velocity_publisher.publish(vel_msg);

    cout << vel_msg.linear.x << " " << vel_msg.angular.z << endl;

    ros::spinOnce();
    loop_rate.sleep();
    t1 = ros::Time::now().toSec();    
  }while((t1-t0)<10);

  resetSpeedCmd(vel_msg);
  velocity_publisher.publish(vel_msg);
  return 0;
}
