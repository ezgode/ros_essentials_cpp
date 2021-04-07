## Section 1: Introduction
## ####################################

section 1 : What is this course about?
---------------------------------------
Learning path: 
- ROS basics
- Motion With ROS
- Perception I OPEN CV and II LASERSCANNER.
- ROSSERIAL ARDUINO

section 2 : About the Instructor
---------------------------------------

## Section 2: ROS:  How did it revolutionize robotics software deve…Section 2: ROS:  How did it revolutionize robotics software development
## #################################### 

section 3 : About this section (slides attached to resources)
---------------------------------------
section 4 : Introduction
---------------------------------------
section 5 : Why did I decided to use ROS in my work?
---------------------------------------
section 6 : The Robot Life Cycle
---------------------------------------
section 7 : ROS Impact
---------------------------------------
section 8 : Self-Driving Car Use Case
---------------------------------------
section 9 : ROS Evolution
---------------------------------------
section 10 : ROS Distributions (version) over Time
---------------------------------------
section 11 : ROS Architecture
---------------------------------------
Ros architecture composed of nodes (processes running in the system) and they register using the ROS master. Then they will be able to communicate between each other. 
If the ROS master crashes everything goes caput. 

NDOES
////
ROS master
////
Client libraries : 
rospy, and roscpp for interprocess comunication
////
TCPROS/UDPROS
////
UNIX

section 12 : ROS Basic Concepts and Demo
---------------------------------------
To start a ros application we need to star the `roscore`, which is the master
and then we need to start the processes/nodes. 

```
roscore
rosrun 
rosnode list
rostopic list
rostopic echo ...
```

section 13 : ROS Communication Paradigms (Topics/Services/ActionLib)
---------------------------------------

Three main communication approaches
* publisher -> subscriber. We can have several subscribers to the same topic. 
* ROS services -> The subscriver sends a request, and waits until the response arrives.
* ROS ActionLib -> client sends a request, it does not block, and will receive the process of the computation of the data requested and the response. 

section 14 : ROS Path Planning and Navigation
---------------------------------------
Simplifies navigation. 
Global path planner >> local path planner
Ros provides already packages to abstract this task, and algorithms already implemented to do mapping localizatione etc.

Global path planner : Responislbe to have the rough path from origin to destination
Local path planner : to follow the designed path. 

section 15 : Limitation of ROS
---------------------------------------
Designed for the single robot case...
To do multirobot comunication might require designing your own packages. 
**It is not real-time** does not allow to modify prioritu
Need reliable network.
It has the problem of the ros master, the single point if failer, the way yhey call it. 

These limitations lead to ROS 2.0

section 16 : ROS2
---------------------------------------
Getting rid of the ros moster, and using a more standard way of comunicating processses. 
They use now the DDS, Distributed data set protocol. 

So now it looks like...

//////////
Nodes
//////////
Client libraries (rclpy, rclcpp)
Abstract DDS
DDS // Intra-process API
//////////
Linux/Windows/MacOs


It was also targeted to manage swarms of robots. 
They use DDS as middleware and communication between the processes. 

DDS Data Distributed Service. 
* An industr-standard communication system 
* Designed by Ojbect Mangement Group
* Data-Centric Publish Subscribe system
* Real-time machine-to-machine communication
* Uses publish-subscribe pattern
* Used in: financial trading, air-traffic control, smart grid management, big data and IoI applications. 
* Started in 2001 with two vendors: RTI in the US and Thales group in France. 

How does the DDS is structure....
it includes
* Domain : mworld you are talking about. 
* Topic : group of similar things
* Instance : individual (changing) thing
* Sample : Snapshot of an instance at a point in time"
* DataWrite : source of information about part of the world (topic)
* DataRead : observer of part of the world (topic).

The DDS also implements discovery methods, and new messages... 
DDS is no vendor lock... so you can decide which DDS distribution to us. 

section 17 : [OPTIONAL] Some Contributions to ROS
---------------------------------------


## Section 3: [NEW] Setting your environment with ROS Noetic
## #################################### 

section 18 : Install ROS Slides
---------------------------------------

section 19 : Install ROS Noetic on Ubuntu 20.04
---------------------------------------

section 20 : Create your catkin workspace with ROS Noetic
---------------------------------------

section 21 : Clone the right GitHub Repository for the ROS Noetic distribution
---------------------------------------

section 22 : Testing your installation with C++ nodes
---------------------------------------

section 23 : Testing and fixing installation with Python nodes
---------------------------------------

section 24 : [IMPORTANT] BEFORE START WORKING ON THE COURSE
---------------------------------------

## Section 4: [LEGACY] Installation and Environment Setup
## #################################### 



## Section 5: Create a ROS Workspace and a ROS Package
## #################################### 

Ros workspace and packages? 

Roes will be installed in `opt/ros/<version name>`
There we find the ros workspace, or rather the ros installation. 
It represents the working area, and it typically has a special file called `setup.bash`, `setup.sh`, `setup.zsh`.
This file **must** be executed to enable the workspace. 
Hence the workspace is the directory where this file(s) is located.

We run the setup by using `source`. Instead or sourcing every time, we should inculde the sourcing commnd in the `.bashrc` which is executed everytime you open a terminal. 
In that file I had, in this case
```bash
source /opt/ros/noetic/setup.bash
source /home/ezgode/catkin_ws/devel/setup.bash !!!!!!
```
Unless we source those setups, commands like `roscore` or `roscd` won't do anything. 

When woking with ros, it is not convenient to work in the default workspace, the common practice is creating my own ws to put my project. 

To create a worksapce.... we gotta create a folder and follow the instructions in the ROS website. 
http://wiki.ros.org/catkin/Tutorials/create_a_workspace
**catkin** if the compilation framework used by the ROS environment. 

To set up the workspace

```shell
// create directory
mkdir -p ~/catkin_ws/
mkdir -p ~/catkin_ws/src
// go inside
cd ~/catkin_ws
// to compile 
catkin_make
```

A workspace is a complete working environment, and packages are separate projects. 

Upon compilation, we will have a `build` and a `devel` folder inside? 
to make the `roscd` leave us to our project, we need to setup the bash profile in the devel folder. 
```
source ~/catkin_ws/devel/setup.bash
```
If we want to do this permanently, then we do, as well, the source of the workspace...

Now that we created the workspace. 
We can start creating our project. 
These projects are called **packages**, and they have to be created in the workspace...

we need to go to the workspace and creating the package with `catkin_create_pkg`. 
```
cd ~/catkin_ws_name/src
catkin_create_pkg ros_basics_tutorials 
```

The `catkin_create_pkg` command, requires the name of the package, and the ros libraries the project will depend upon... typical libraries are
* `std_msgs`
* `rospy`
* `roscpp`

We don't know a priori all the libraries we need, we can add them later on. 
So the command woul look like... 
```
catkin_create_pkg ros_basics_tutorials std_msgs rospy roscpp
```
But I still need to compile the workspace. To do that, we go to the root of our workspace and run `catkin_make`. 
This will create a folder within the `src` folder with the name of the package. 
inside we will have another `src` folder for the code, and an `include` folder to put the libraries. 

We can now start creating scripts and files within the `workspace/src/package_name/src` folders and files. These are the nodes. 
He created two `cpp` files... and he had to modify the `CMakeLists.txt` file within the package director. 

He put something like...
```
// here we put the path to the src code of the node
add_executable(listener_ros_node src/talker.cpp) 
target_link_libraries (listener_ros_node ${catkin_LIBRARIES})
```

And once all this is done, you go back and `catkin_make` the whole workspace again...

Now to run the program...
he runs the `roscore` and then 
`rosrun ros_basics_tutorials talker_node` 
and
`rosrun ros_basics_tutorials listener_node` 

## Section 6: [NEW] ROS Computation Graph
## #################################### 

section 38 What is a ROS Computation Graph?
---------------------------------------
The nodes can communicate with all notes... the fundamental ways are...
* publisher - subscriber mode
* service - you can implement a server and a client in different nodes, and the client can request information for the server. (synchronos, it blocks!)
* action - It is similar to a server( asynchronous, it does not block and the server sends the state of the requested process)
* We also have a central node, the ros master, that is in the middle of all comunication channels. 

section 39 ROS Computation Graph Life Cycle
---------------------------------------

section 40 Start the ROS Master Node
---------------------------------------
We gotta start always by starting the `roscore` .
We could start the tortoise node, which is a simulater robot...
and we could have another node for the input device. 

We can use `rosnode list` command to find the nodes that ARE RUNNING!!
By default, the only one available is `rosout` that corresponds to the roscore. 

We can find the list of topics by goind...
`rostopic list` which by default returns

```
/rosout
/rosout_agg
```

section 41 How to run a new node (executable) in ROS?
---------------------------------------
section 42 What happens when we start a new ROS node?
---------------------------------------

Then, to run a node we would...
```
rosrun turtlesim turtlesim_node
```
* `rosrun` is the command to run ta node
* `turtlesim` the **package** name!!!
* `turtlesim_node` the **node** of the node that you are going to execute. 


section 43 Adding a teleop node to make the robot move
---------------------------------------
```
rosrun turtlesim turtle_teleop_key
rosnode info /turtlesim
rostopic info /topic/name
```

section 45 The content of the motion message /tutle1/cmd_vel
---------------------------------------
What about the message structures???? 
The teleoperation node is publishing in the topic... Specificall, the `/turtle1/cmd_vel` topic is expecting messages with the following structure

* linear
	float64 x
	float64 y
	float64 z

* angular
	float64 x
	float64 y
	float64 z

section 46 Understand the structure of a ROS message
---------------------------------------
What's the type of the message? 
when we do `rosnode info /turtlesim` we get that 
```
* /turtle1/cmd_vel [geometry_msgs/Twist]
```
This the message type `geometry_msgs/Twist`. 
Typically the messages in ROS are denotes with two name `name1/name2`. 
The first name represents the ros package where the message is defined. 
The second is the tos message name itself. 

We find in 
``` 
/opt/ros/noetic/share/geometry_msgs/msg/Vector3.msg
```
The information about the message...
it says it contains two Vector3.. which can be in turns found in 
``` 
/opt/ros/noetic/share/geometry_msgs/msg/Vector3.msg
```

The twist message is a standard message in ros. 
Ros, nonetheless, allows us to create our custom messages.
 
 section 47 How to show the message structure on ROS
command line?
---------------------------------------
To see the content of messages, we cna do..
```bash
rosmsg show geometry_msgs/Twist
rosmsg show geometry_msgs/Vector3
rosmsg show geometry_msgs/Pose
```

section 48 Publish a message on a topic from a command line
---------------------------------------

We can post in a topic by doing...
```bash
rostopic pub -r 10 
	/turtle1/cmd_vel 
	geometry_msgs/Twist '{linear:{x:0.1, y:0.0, z:0.0}, angular:{x:0.0, y:0.0, z:0.0}}'
```

section 49 Visualize the ROS Computation Graph using ros_rqt_graph
---------------------------------------
```
rosrun rqt_graph rqt_graph
```

section 50 Demo: Starting Turtlesim and checking information
about the nodes and topics
---------------------------------------

section 51 Demo: Showing the content of ROS messages
published
---------------------------------------

section 52 Demo: Understand the pose topic
---------------------------------------

section 53 Demo: What is the benefit of using ROS?
---------------------------------------

section 54 Demo: Publishing a message from a command line
using rostopic pub
---------------------------------------

section 55 Demo: rqt_graph
---------------------------------------

Quiz 1: [Quiz] ROS Computation Graph

Progress cannot be changed for this item
Assignment 1: ROS Filesystem and Ecosystem

section 56 NOTE
---------------------------------------

section 57 [OLD] The ROS Master Node (OPTIONAL - KEPT FOR
STUDENT NOTES)
---------------------------------------

section 58 [OLD] ROS Computation Graph: Nodes, Topics
(OPTIONAL - KEPT FOR STUDENT NOTES)

## Section 7: ROS Topics
## #################################### 

section 59: ROS Topics Overview
---------------------------------------
Reminder: we gotta have a node streaming data into a topic, and any subscriber will have access to that info.

Every node connects first with the master to tell it the communication they required. 

* `roscore`
* `rosrun PACKAGE_NAME NODE_NAME`
* `rolaunch PACKAGE_NAME LAUNC_NAME` (??)

There is a three steps handshake to build the actual communication channel between the three nodes.
They communicate over TCP.

section 60: Question: what happens if ROS Master crashes?
---------------------------------------

Once the communication is built, the rosmaster is not really necessary. 
So if the master crashes, the communication will stay allive. 
The problem is that if the communication dies and it needs to be restarted, that won't happen without the master alive. 

/DEMO/


section 61: Guidelines to Write a Publisher and a Subscriber in ROS
---------------------------------------

Practical tips for the pulisher
* step 1 : Determine a name for the topic to publish
* step 2 : Determine the type of the messages that the topic will publish
* step 3 : Determine the frequency of topic publication
* step 4 : Create a publisher object with parameters chosen
* step 5 : Keep publichins the topic message at the selected frequency. 

Practical tips for the Listener
* step 1 : Identify the name for the topic to listen to
* step 2 : identify the type of the message to be received
* step 3 : Define a callback function that will be automatically executed when a new message is received on the tocpic. 
* step 4 : Start listening for the topic messages
* step 5 : spin to listen for ever (in C++) 

section 62: Overview of the Talker/Listener Application (ROS Hello World Examp…
---------------------------------------
The talker/listener application. 
topic : chatter
message : std_msgs/String
field: data="Hello World %d"

section 62: Overview of the Talker/Listener Application (ROS Hello World Example)
---------------------------------------

section 63: Write a Publisher Node in Python
---------------------------------------
Talker
```python
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True) # Anonymous adds an id for the name to be unique
	rate = rospy.Rate(1) # 1Hz
	# rate = rospy.Rate(10) # 10Hz
	i = 0
	while not rospy.is_shutdown():
		# hello_str = "Hello world {:s}".format(i)
		hello_str = "Hello world %s" % i
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
		i+=1

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
```


section 64: Write a Subscriber Node in Python
---------------------------------------
Listener
```python
import rospy
from std_msgs.msg import String

def chatter_callback(message):
	rospy.loginfo(rospy.get_caller_id() + "I heard {:s}".format(message.data))

def listener():
	rospy.init_node('listener', anonymous=True) # Anonymous adds an id for the name to be unique
	sub = rospy.Subscriber('chatter', String, chatter_callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
```

section 66: Write a Publisher/Subscriber Node in C++
---------------------------------------

```c++
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv){
	ros::init(argc, argv, "talker_node");
	ros::NodeHandle n;
	ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("chatter", 1000);
	ros::Rate loop_rate(0.5);

	int count = 0;
	while(ros::ok()){
		std_msgs::String msg;
		std::stringstream ss;
		ss << "Hello World" << count;
		msg.data = ss.str();
		ROS_INFO("[Talker] I published %s\n", msg.data.c_str());
		chatter_publisher.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();
		count++;
	}
}
```

Listener
```c++
#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String::constPtr& msg)
{
	ROS_INFO("[Talker] I heard %s\n", msg->data.c_str());
}
int main(int argc, char **argv){
	ros::init(arg, argv, "listener_node");
	ros::NodeHandle n;
	// We dont's specify here the type! cuz it is already defined in the definition of the callback class. 
	ros::Subscriber sub = node.subscribe("chatter", 1000, chatterCallback);
	ros::spin();
	return 0;
}
```

However, this time we also need to modify the `CMakeLists.txt` and add
```txt
cmake_mininmum_required(VERSION 2.8.3)
project(ros_essentialts_cpp)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS 
	roscpp
	rospy
	std_msgs
)
```

and adding the dependencies at the end of the cmakelist
```
# talker
add_executable(talker_node src/topic01_basics/talker_listener/talker.cpp)
target_link_libraries(talker_node ${catkin_LIBRARIES})

# listener
add_executable(listener_node src/topic01_basics/talker_listener/listener.cpp)
target_link_libraries(listener_node ${catkin_LIBRARIES})
```

and in the `package.xml`

```xml
<buildtool_depend>catkin</buildtool_depend>
<build_depend>roscpp</build_depend>
<build_depend>rospy</build_depend>
<build_depend>std_msg</build_depend>

<build_export_depend>roscpp</build_export_depend>
<build_export_depend>rospy</build_export_depend>
<build_export_depend>std_msgs</build_export_depend>

<exec_depend>roscpp</exec_depend>
<exec_depend>rospy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

all this information is required by `catkin_make`

section 67: [DEMO] Talker/Listener in C++
---------------------------------------

section 68: Do-It-Yourself Assignment Explanation
---------------------------------------

```
rosrun turtlesim turtlesim_node
```

publish comands to move, and subscribe to the topic with the position of the robot. 

* subscriber for the topic that will show the location of the robot
* publisher to the topic that will make the robot move
* what is the topic of the position ?
* what is the topic that makes the robot move ? 

We can get the scripts 

`rostopic list`
`rostnode list`
`rostopic info /turtle1/cmd_vel` to get the type of the message
`rosmsg show geometry_msgs/Twist`

To define the message...
```
twist = Twist()
twist.linear.x = 1.0
```

Assignment 2: Do-It-Yourself: Write your First ROS Program to Control the Motion of a Robot
---------------------------------------

## Section 8: ROS Messages
## #################################### 

section 71 : Create Custom ROS Messages: Overview
---------------------------------------
How to create custom messages?

**EVERY NAME** MUST BE COMPOSED as `package_name/message_type` for example: `std_msgs/String`, `geometry_msgs/Twist`. 

They might have several fields...
```
type1 field1
type2 field2
```
The types can be custom types as well. 

Let's try to create `IoTSensor` Message with fields: `id`, `name`, `temperature`, `humidity`. 

To do that we will use the director `msg` located in our `<workspace>/src/<package_name>/msg`

There we just need to create a file `mesage_name.msg`, that in our case might look like. 
```
int32 id
string name
float32 temperature
float32 humidity
```
Before being able to use this message we need to modify the CMakeLists.txt. In the CMakeLists.txt we must include the `message_generation` within the packages. 

```
find_package(catkin REQUIRED COMPONENTS
  ...
  message_generation
  ...
)
``` 
and also...
```
catkin_package(
	...
	CATKIN_DEPENDS ... ... ... message_runtime
	...
)
```
and make sure that the generate message dependency is activated. That is that you have...
```
generate_messages(
	DEPENDENCIES
	std_msgs
	acitionlib_msgs
)
```

Then, we must link the file caontaining the message description. we do that by doing
```
add_message_files(
	FILES
	IoTSensor.msg
)
```

Then we must change the `package.xml` and add
```xml
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```

Finally, we `catkin_make`. Then you should see the message showing up when doing 
```
rosmsg show ros_essentials_cpp/IoTSensor
```
To know the types that might be available to us, we could check the info in http://wiki.ros.org/msg.


section 72 : [Demo] Create a Custom ROS Message: Implementation
---------------------------------------

section 73 : [DEMO] IoTSensor Custom Message Publisher/Subscriber Ap…
---------------------------------------

To use the custom message we just need to do the following
```python
# imports
from ros_essentials_cpp.msgs import IoISensor

# Publishers...
pub = rospy.Publisher('', IoTSensor, queue_size=10)

# Then you create the message
iot_sensor = IoTSensor()
iot_sensor.id = 1
iot_sensor.name = 'noname' 
iot_sensor.temperature = 0.0
iot_sensor.humidity = 1.0
pub.publish(iot_sensor)
```

To create a subscriber, the same story...
```python
from ros_essentials_cpp.msg import IoTSensor
rospy.Subscriber("iot_sensor_topic", IoTSensor, iot_sensor_callback)
```

## Section 9: ROS Services
## ####################################

section 74 : What is a ROS Service
---------------------------------------

What is a ROS Service? 
* ROS Server
* ROS Client
* Not like topic, service is one-time communication
	* A client sends a request, then the server sends back a response. 
	* BLOCKING!!!!!!

When to use ROS Service?
* Request the robot to perform a specific action
* Example: find the path from point A to point B, spawn one robot in the simulator, ...

We have here bi-directional communication. 

75
---------------------------------------
Same tha with topics, we have available the commands...
```bash
rosservice list
rosservice info
rosservice call
```
Now the important thing it that we will have a message for the request, and another one for the repsonse. 
The request message will need some arguments. 

Now to see the info of the messages required by the service, we do 
```bash
rossrv show turtlesim/Spawn
```
In our case that shows...
```
float32 x
float32 y
float32 theta
string name
---
string name
```

76
---------------------------------------

77
---------------------------------------
How to create them? 

* Define the service message (servide file)
* Create ROS Server node
* Create ROS Client node
* Execute the service
* Consume the service by the client. 

To create the custom message we need to create a file in the folder ./<worksapce>/src/<work_package>/srv where we will include the service definition. In the example we used...

```python
int64 a
int64b
---
int64 sum
```

Then we need to update the dependencies... I.E in the `CMakeLists.txt` file we have to add
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```

Also, in the `find_ackage` line we gotta have
```
find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	...
	message_generation
	...
)
```
Also... to point to the file we gotta have
```
add_service_files(
	FILES
	AddTwoInts.srv
)
```
Finally, we gotta catkin_make to compile the changes and have the service actually available. 
Then we should see new related files in the <workspace>/devel/include/<package> directory (some header files basically). 

after catkin_make you should be able to see the content of the service with 
```
rossrv show <package>/AddTwoInts
```

78
---------------------------------------

79
---------------------------------------
Python implementation for python

```python
from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

import rospy

def handle_add_two_ints(req):
	res = req.a + req.b
	return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
	ros.init_node('add_two_ints_server')
	s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
	rospy.spin()

if __name__ = "__main__":
	add_two_ints_server()
```

THE CLIENT
```python
from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

import rospy


def add_two_ints_client(x,y):
	# This is waiting for the setvice to start!
	rospy.wait_for_service('add_two_ints') 
	try:
		# Service client, or service proxy. 
		# Here the name must be the same used in the server definition. 
		add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts) 
		resp1 = add_two_ints(x,y)
		return resp1.sum
	except rospy.ServiceException(e):
		print('Srvice call failed: {:s}'.format(e))

if __name__ = "__main__":
	x = 1
	y = 1
	s = add_two_ints_client(x,y)
```

81
---------------------------------------

In cpp!!

SERVER
```cpp
#include "ros/ros.h"
#include "ros_essentials_cpp/AddTwoInts.h"

bool add(ros_essentials_cpp::AddTwoInts::Request &req, ros_essentials_cpp::AddTwoInts::Response &res)
{
	res.sum = req.a + req.b;
	ROS_INFO("Request...");
	return true;
}

int main(int argc, char **argv){
	ros::init(argc, argv, "add_two_ints")
	ros::NodeHandle n;
	ros::ServiceServer service = n.advertiseService("add_two_ints", add);
	ROS_INFO("Ready to add two ints");
	ros::spin();
	return 0
}
```

CLIENT
```cpp
#include "ros/ros.h"
#include "ros_essentials_cpp/AddTwoInts.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_client");
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<ros_essentials_cpp::AddTwoInts>("add_two_ints");
  ros_essentials_cpp::AddTwoInts srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  if (client.call(srv))
  {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }

  return 0
```

Now we need to add the instructions to compile the server and the client in the `CMakeLists`...

```txt
add_executable(add_two_ints_server src/topic01_basics/service/add_two_ints_server.cpp)
target_link_libraries(add_two_ints_server ${catkin_LIBRARIES})
add_dependencies(add_two_ints_server ros_essentials_cpp_gencpp)

add_executable(add_two_ints_client src/topic01_basics/service/add_two_ints_client.cpp)
target_link_libraries(add_two_ints_client ${catkin_LIBRARIES})
add_dependencies(add_two_ints_client ros_essentials_cpp_gencpp)
```

82
---------------------------------------

ASSIGNMENT
---------------------------------------

We first need to go to the workspace src folder, that is

 cd ~/catkin_ws/src 

and then create the package by doing

catkin_create_pkg ros_service_assignment 

```
~/catkin_ws/src/ros_service_assignment/srv
```

## Section 10: [NEW] Motion in ROS (updated with ROS Noetic)
## #################################### 

83
---------------------------------------
84
---------------------------------------
```
/turtl1/cmd_vel
geometry_msgs/Twist
/turtl1/Pose
```
85
---------------------------------------

```
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#include "ros/ros.h" 
#include "geometry_msgs/Twist.h"
#include "turtlesim/Pose.h"
```
86
---------------------------------------
87
---------------------------------------
88
---------------------------------------
89
---------------------------------------
90
---------------------------------------
90
---------------------------------------
91
---------------------------------------
92
---------------------------------------
93
---------------------------------------
94
---------------------------------------
95
---------------------------------------
96
---------------------------------------
97
---------------------------------------
98
---------------------------------------
Running several nodes at once...
Using laun files
```xml
<launch>
	<node name="turtlesim" pkg="turtlesim" type="turtlesim_node"/>
	<node name="clean_node" pkg="ros_essentials_cpp" type="turtlesim_cleaning.py" output="screen"/>
</launch>
```

and then we call
`roslaunch ros_essentials_cpp <filename>.laungh`

## Section 11: Appendix: Motion in ROS (old videos - but still applicable)
## #################################### 

## Section 12: ROS Tools and Utilities
## #################################### 

108
---------------------------------------
Allow a work station to control a robot over the network.
He uses two virtual machines.

First, he modifies the `.bashrc` files in the workstation and on the robot. 

### ROBOT

find the robot's ip address by doing :
```
ifconfig 
```

```bashrc
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=<robot ip address>
export ROS_IP = <robot ip address> 

// display then
echo "ROS_HOSTNAME: "$ROS_HOSTNAME
echo "ROS_IP: "$ROS_IP
echo "ROS_MASTER_URI: "$ROS_MASTER_URI
```

Open new terminal, and we will se the echoed messanges.


### WORKSTATION
Same thing with the workstation
```bashrc
export ROS_IP = <workstation ip address> 
export ROS_HOSTNAME= <workstation ip address> 
export ROS_MASTER_URI=http://<robot ip address>:11311
```

Essentially this allows the workstation to communicate with the topics that are available in the robot. So in practice, we can control remotely the robot.

109
---------------------------------------
Launch files? 
* A launch file is a XML document, which specifies
 	- wich nodes to execute
 	- their parameters
 	- what other launch files to include

* roslaunch is a program that easily launches multiple ROS nodes
* Laucn file has a .launch extension

We have a tag to include a launch file in another launch file
```xml
<launch>
	<include file="$(find ros_essentials_cpp)/src/topic02_motion/launch/turtlesim_teleop.launch"/>
	<node name="turtlesim" pkg="turtlesim" type="turtlesim_node"/>
	<node name="clean_node" pkg="ros_essentials_cpp" type="turtlesim_cleaning.py" output="screen"/>
</launch>
```

we can use parameters defined within these launch files. 

```xml
<param name="x_goal" value="3.0"/>
<param name="y_goal" value="1.0"/>
<node name="clean_node" pkg="ros_essentials_cpp" type="turtlesim_cleaning.py" output="screen"/>
```
in `turtlesim_cleaning.py` we would use...

```python
x_goal = rospy.get_param("x_goal")
y_goal = rospy.get_param("y_goal")
```


110
---------------------------------------

## Section 13: Getting Started with Turtlebot3
## #################################### 

111
---------------------------------------
https://emanual.robotis.com/docs/en/platform/turtlebot3/overview

## Section 14: Perception I: Computer Vision in ROS with OpenCV
## #################################### 

openCV
* open source computer vision library
* BSD License
* Free for both academic and comercial use
* C++/Python/Java
* Windows, macos, Linux, iOS, Android
* Strong focus on real-time (written in C++ and optimized).

Some operation? 
* 2d image processing
* image input/output
* video input/outptu
* Camera Calibration
* video analysis (motion extraction, feature tracking, foreground extraction,)
* Object detection
* Machine learning, deep neural networks
* GPU-Accelerated computer vision
* and much more

Some functionalities
* image segmentation
* image thresholding
* Object detection and recognition
* Drawing
* Edge Detection
* video/image input output


123
---------------------------------------
CvBridge: Bridging Open CV and Ros

Images have to be received through topics... and turns out that the image format supported by open cv is not the same than the one supported by ROS. 
Or rather the opposive, transform images in the ROS format, to a format that open CV understand. 

`rosrun usb_cam usb_cam_node _pixel_format:=yuyv`

135
---------------------------------------
Tu use a RGBD camera, or some periferials, we need to run the drivers, which will be posting info in a topic? 

start openni package

```
sudo apt-get install ros-kinetic-openni2--

roslaunch opanni2 launch opanni2 ... 

rosrun deth_image_to_laser_scan deth_image_to_laserscan image:=camera/depth/image_raw

```

```xml
<remap from ="image" to="/camera/depth/image_raw"/>
```

RVIZ: Ros Visualization, to visualize topics....

rosrun rviz rviz
>> global_options>fixed_frame>camera_link
>> fixed >> ok 
>> add >> laser scan
>> laserscan : topic

136
---------------------------------------

```cpp
sudo apt-get install ros-kinetic-urg-node
rosrun urg_node urg_node

rostopic list
// and scan topic if the sensor is running
rostopic echo /scan
rosrun rviz rviz
rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 1.0 map laser 10
```


Bag File
---------------------------------------
To save///
```
mkdir bagfiles
// -a is for everything
rosbag record -a
```
crtl+c to stop recording

```
rosbag info <name>
rosbag play <name>

```

Subscribing to the laser scanner
---------------------------------------
* start the drivers
* make sure that /scan topic is available
* write a node that subscribes to the /scan topic
* write a callback function that receive /scan messages and process them. 

As always... when working with `cpp` we need to include the instructions in the CMakeLists. Specifically, we need to

```
# Adding the library he defined
add_library(utility_lib src/topic04_perception02_laser/laserscan/utility_lib.cpp)

#laser scan
add_library(laserscan_lib src/topic04_perception02_laser/laserscan/LaserScanner.cpp)
target_link_libraries(laserscan_lib ${catkin_LIBRARIES})
add_dependencies(laserscan_lib ${catkin_EXPORTED_TARGETS})
target_link_libraries(laserscan_lib utility_lib)

# executable
add_executable(scan_subscriber_cpp src/topic04_perception02_laser/scan_subscriber.cpp)
target_link_libraries(scan_subscriber_cpp ${catkin_LIBRAIES})
target_link_libraries(scan_subscriber_cpp laserscan_lib)
```


## Section 15: Perception II: Laser Range Finders (Laser Scanner)
## #################################### 

## Section 16: rosserial: Connecting new Hardware (Arduino) with ROS
## #################################### 

What is rosserial? 

Sometimes we need to develop our own drivers.
However, ros provides rosserial, a protocol to communicate with microcontrollers that are controlling other sensors...

allows new electronic hardware to directly talk to ROS system. 
no need for customer driver and communication protocol. 
rosserial is a protocol for wrapping standard ros serialized messages and multiplexing multiple topics services over a character device such a serial port or network socket. 

different client libraries were devekoped to get ROS up and running on various systems. 
* rosserial_client
* rosserial_arduino
* rosserial_ambeddedlinux
* rosserial_windows
* rosserial_mbed
* rosserial_tivac
* rosserial_...

The ones we will use 
* rosserial_python
* rosserial_server (c++)

* rosserial_arduino

The objective is making microcontrollers like arduino able to public messages directly in the ros topics? 

```arduino
void setup(){
	Serial.begin(9600);	
}
void loop(){
	...
	Serial.print(inches)
	Serial.println();
	delay(100)
}
```

That already makes the arduino sending info to the computer via the usb port. 

We gotta go to http://wiki.ros.org/rosserial for installation files and more tutorials. 

install rosserial arduino
Install libraries 

```
cd arduino-<version>/libraries
rosrun rosserial_arduino make_libraries.py .
```

That generates the library needed to make arduino able to publish in topics? 
We already have ros integrated in arduino. 

Now in arduino you have the examples of ros. 

```Arduino
#include <ros.h>
#include <std_msgs/String.h>
```
The server application in the workstation

```
rosrun rosserial_python serial_node.py /dev/tty<portname>
```

and now we should be able to see the topic the arduino created. 

Something very similar is done to make the arduino subscribe to the topics. 
Also very nice example by default... so nothing reeeeallyyyy new here. 


# ROS for beginnerrs II: Loclization, Navigation and SLAM
## #################################### 

`/odom`
`/ancl_pose` : map frame, refers to the global position on the map. 

Orientation is represented by quaternions and typically have components (x,y,z,w).
THat info is not necessarily readable right away. 
``` 
`) What is the purpose of frames in the context of a robot navigation? (refer to the lecture 9 about frames)

They allow to represent the location and orientation of the robot w.r.t. some reference points/location. 

2) In the lecture 10 (location), what is the difference between amcl_pose locatio and odom location?

The reference frame they use. The amcl_pose uses the global frame, while the odom location uses the odom frame. 

3) In lecture 11, we have talked about robot orientation. What is the representation used to express a rotation angle in ROS?

Quaternions. 

4) Is it easy for a human being to understand the meaning of this rotation representation?

No. 

5) In lecture 12, we presented a simple example of map-based robot navigation.
Describe this process in a few words. 

- We se the navigation objective, i.e. the location the robot is moving towards. 
- Then we need a global planner which, using the information about the map, comes up with a collision-free way of reaching the objective. 
- The we have a local planner that aims at following the computed global path while avoiding collisions with the surroungind moving and static obstacles.
```
## Section 1: What is this course about?
## #################################### 

Frames. How to represent the possition of the robot? 


Combination of position and orientation is the Pose. 
Pose: position and orientation.

What is the location of this robot? 
We need to have a reference,

F{W} = (X^W, Y^W)

How to determine the pose of the robot in different reference frames? 
We need to transform. 

Location of an object is dependent on the frame. 

Typically the robot know its global location, and detect things w.r.t. the robot's coordinate frame. 

Transformation types : translation and rotation. 




2D translation

```latex
\vec{p}_w1 = \vec{p}_w2 + \vec{W1,W2}
``` 

W1 -> flat
W2 -> rotated a theta angle

```
x_w1 = x_w2 cos(theta) - y_w2 sin(theta)
y_w1 = x_w2 sin(theta) + y_w2 cos(theta)

p_w1 = [[cos(theta), -sin(theta)],[sin(theta), cos(theta)]] p_w2
p_w1 = R_w1^w2 p_w2
```


The genera transformation then ends up being...


```
p_w1 = R_w1^w2 p_w2 + \vec{W1,W2}
or
[[x_w1],[y_w1],[1]] = 
	[[cos(theta), -sin(theta), xt],[sin(theta), cos(theta), yt],[0,0,1]] [[x_w2],[y_w2],[1]]
```

[[x_w2],[y_w2],[1]] is called the homogeneous coordinates and they allow to represent rotation and translation.

Counter clock wise rotation angle!!

We always use 3D coordinate systems. 
So what the transformation looks like? 

Consider two frames: W1 (well aligned) and a W2 translated and rotated w.r.t. w1. 
Frames are typically assigned in such a way that `x`  is the longitudinal axis of the robot. 
In those circumstances, the rotation angles are
roll (bank): around x
pitch (attitude): around y
yaw (heading): around z

For every rotation we have the following rotation matrices. 

Rx(theta) = [[1, 0, 		  0],
	  [0, cos(theta), -sin(theta)],
	  [0, sin(theta), cos(theta)]]

Ry(theta) = [[cos(theta),  0, sin(theta)],
      [0, 		    1, 0], 
      [-sin(theta), 0, cos(theta)]]

Rz(theta) = [[cos(theta), -sin(theta), 0],
      [sin(theta), cos(theta),  0],
      [0,  		   0,  			1]]


The general rotation matrix bill then be
R = Rz(alpha)Ry(beta)Rx(gamma)

THen the general transormation matrix end up bein...

[ [w1R_w2], [t]
  [0], [1] ] 

where t is the translation vector from one frame to the other. 
And we nee to use the homogeneous coordinates to describe the position,. 



## Section 2
## #################################### 

## Section 3
## #################################### 

## Section 4
## #################################### 

## Section 5
## #################################### 

**How orientation is represented in 3D space?**
- Three angle representation: Euler rotation vs cardan rotation
- rotation about arbitrary vector
- quaternions

EULER ROTATION SEQUENCE
Involves repetition, but not successive, or rotations about one particular axis. 

CARDAN ROTATION SEQUENCE:
characterized by rotations about all three axes. 

Euler theory: Any two independent orthonormal coordinate frames can be related by a sequence of rotations (not more than three) about coordinate axes, where no two successive rotations may be about the same axis. 

ARBITRARY VECTOR ROTATION
In 3D space, orientation can be expressed as a rotation about some axis that runs through a fixed point on the rigid body. This means, for any rotation, there exists some axis at certain angle around which the rotation occurs. 

Rodrigues Formula: 
`R = I cos(theta) + sin(theta)[u]_x + (1-cos(\theta)) u \times u`

**QUATERNIONS**
Represented by 4 numers. 

q = s < v1 | v2 | v3 > 

< v1 | v2 | v3 >  : represents a vector
q := scalar. 

The actual quaternion is 

q = s + v1 i + v2 j + v3 k
such that
`i**2 + j**2 + k**2 = -1` 

other notation styles might call this

q = q0 + qx i + qy j + qz k

In RES, the notation is (x,y,z,w)

The rotation matrix corresponding to a clockwise/left-handed rotation by the unit quaternion axis...
```
R = [
[q0**2 + q1**2 - q2**2 - q3**2, 2(q1q2-q0q3), 2(q0q2+q1q3)],
[2(q1q2+q0q3), q0**2-q1**2+q2**2-q3**2, 2(q2q3-q0q1)],
[2(q1q3-q0q2), 2(q0q1+q2q3), q0**2-q1**2-q2**2+q3**2]
]
```
https://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToMatrix/hinde.h

Also obtain the quaternion from the Euler angles...
Also the Euler angles from the quaternion...

Why quaternion? 
Cuz, when used to linearize the model of a quadrotor, they were shown to allow better performance than the Euler angles. 

- Compared to Euler angles they are simples to compose and avoid problems of gimbal lock
- Compared to rotation matrices they are more compact, more numerically stable, and more efficient. 
- Quaternions have applications in computer graphics computer vision, robotics, navigation, molecular dynamics, flight dynamics, orbital mechanics of satellites, and crystallographic texture analysis. 


## Section 6 : the TF package: Frames, Transformations and Localization in ROS. 
## #################################### 

WHAT IS TF? 
- TF stands for transofmration library in ROS. 
- It performs computation for transformations between frames.
- It allows to find the pose of any object in any frame using transformations. 
- A robot is a collection of frames attached to its different joints. 

color code to represent frames? 
x -> red
y -> green
z-> blue

A frame is defined in every joint and component of the robot. 

**URDF: Language for the Description of Frames and Transformation in a Robot Model**

In ROS every robot is defined using the Unified Robot Description Format (URDF), which is essentially a xml file showing the properties. 

https://wiki.ros.org/urdf/Tutorials 

Example of a block within the xml filE? 
```
<joint name="base_joint" type="fized">
	<parent link="base_footprint"/>
	<child link="base_link"/>
	<origin xyz="0.0 0.0 0.010" rpy="0 0 0"/>
</joint>
```
Relative position between joints is represented throughout a translation vector `xyz` and a rotation matrix `rpy`. Rotation : roll pitch yaw. 


**WHY TF IS IMPORTANT?** 

Essentially, typically if we want to interact with the world, we need to use coordinates obtained through a camera (at a specific location) and make some other part of the robot interact with the detected object. 
We need to perform transformations between the different frames. 

- performs transformation easily
- The user does not need to worry about frames
- Provides built-in functions to publish and listen to frames in ROS. 


**OVERVIEW OF TF PACKAGE UTILITIES**
The TF package has several ROS nodes that provide utilities to manipulate frames and transformations in ROS. 

- *view_framse*: visualizes the full tree of coordinate transforms. 
- *tf_monitor*: monitors transforms between frames. 
- *tf_echo*: prints specified transform to screen
- *roswtf*: with the tfwtf plugin, helps yo utrack down problems with tf. 
- *static_transform_publisher* is a command line tool for sendind static transforms. 

```
rosrun tf view_frames
rosrun tf tf_monitor
rosrun tf tf_echo odom base_footprint
rosrun tf view_frames
evince frames.pdf
alias tf='cd /var/tmp && rosrun tf view_frames && evince frames.pdf &'
```

**CONVERT ORIENTATION BETWEEN QUATERNION AND ROOL-PITCH-YAW USING TF**

`tf_rotation_convertions.py`


```
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
rpy = tf.transformations.euler_from_quaternion(quaternion)
rpy = tf.transformations.euler_from_quaternion(q)
```

How to launch the nodes for navigation? 
- Start tutlebot3 waffle
- list all topics
- check info od /odom topic and amcl_pose
- understnad how position and orientation are presented
- write script that print the x,y coordinate and yaw angle of the Turtle3 robot. 

The message
`rosmsg show nav_msgs/Odometry` 
contains info regarding the pose (with orientation in quaternions) and the velocity. 

Then, the `rosmsg show geometry_msgs/PoseWithCovarianceStamped` 
and the `rosmsg show geometry_msgs/TwistWithCovarianceStamped` 
message have the post and twist with the covariance? 

```
roslaunch turtlebot3_gazebo turtlebot3_house.launch 
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/ezequiel/catkin_ws/src/ros_course_part2/src/topic03_map_navigation/tb3map/tb3_house_map.yaml
rostopic list
```

Note the topics

```
/odom
/acml_pose
```

**THE TF PACKAGE COMMAND LINE AND UTILITIES**
```
rostopic list
rosrun tf view_frames
rostopic echo tf
rostopic info tf
rosmsg show tf2_msgs/TFMessage
```

some frames 
`base_link` 
`camera_link` 


tf was deprecated, so now we should be using tf2. 
`sudo apt-get install ros-noetic-tf2-tools` 
`rosrun tf2_tools view_frames.py`  

this should be run instead of `rosrun tf view_frames`. 

Now that we have a map, we also have the frame `amcl` to which you can listen to by doing `rostopic echo amcl_pose` 

**Other tools**

`rosrun tf tf_echo map odom` 
gives the transformation from one frame to the other...

`rosrun tf tf_echo odom map`

 with this tf command, we can calculate the transofmration between any pair of frames even if they are not parent-child relationship. 

`rosrun tf tf_echo odom camera_rgb_frame`
we can also set the frequency of the verbose. You esntt 1 Hz? soo...
`rosrun tf tf_echo odom camera_rgb_frame 1`

We can also monitor using `tf_monitor`

```
rosrun tf t2f_monitor odom base_footprint
rosrun tf tf_monitor
```

**PUBLISH TRANSFORMATION BETWEEN TWO FRAMES**

```
roscore
// ther eis no transformation
rostopic list
// publish a static transformation betwee two frames
// the params are [translation] [rotation] parent child broadcast frequency
rosrun tf static_transform_publisher 1 2 3 0.1 0.2 0.3 frame_a frame_b 10
// Now in rostopic list we should have the new tf topic. 
rostopic list
// and we can print again the transform by doing
rosrun tf view_frames
// and to see the broadcast
rosrun tf tf_echo frame_a frame_b
```

We can also do this using a launcher file! Specificalle...
```xml
<launch>
	<node pkg="tf" type="static_transform_publisher" name="frame_a_to_frame_b" args="1 2 3 0.1 0.2 0.3 frame_a frame_b 10"/>
</launch>
```

sace that in a `<path>/file.launch` and launch it with `roslaunch <path>/file.launch` 
For instance there is an example already in the package, that goes like

```
roslaunch ros_course_part2 static_transform_publisher.launch
```

**BROADCASTING TRANSFORMATION FROM NODES**

## Section 7 MAP BASED NAVIGATION OVERVIEW
## #################################### 

**MOBILE ROBOT NAVIGATION OVERVIEW**
==================================================
**MAP-BASED NAVIGATION OVERVIEW**
==================================================

* Localization
* Mapping
* Motion planning or path planning. 

Ros has predefined packages to deal with navigation stack
- move_base: map-based navigation
- gmapping: creates maps using laser scan data
- amcl: localization using map

**SLAM DMONSTRATION AND SICUSSION**
==================================================

```
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_gazebo turtlebot3_house.launch
export TURTLEBOT3_MODEL=waffle_pi
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
export TURTLEBOT3_MODEL=waffle_pi
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
rosrun map_server map_saver -f ~/map
```

There are several SLAM approaches in ROS: 
* gmapping : which contains a ROS wrapper for OpenSlam's Gmapping.
* cartographer : which is a system developed by Google that provides real-time simultaneous localization and mapping (SLAM) in 2D and 3D across multiple platforms and sensor configurations. 
* hector_slam : which is another SLAM approach that can be used without odometry.


The resolution is typicalle m/pixel
negate: negate the image. 


**UNDERSTAND THE STRUCTURE OF MAPS IN ROS**
==================================================

When we want to save the map, we need to save the map into a file. 
We use another node for that 

```
rosrun map_server map_saver -f ~/tb3_house_map
```
map_server is a package responsible for publishing and manipulating maps. 

This generates two files. 
an image file (`.pgm`) and a `yaml` file. 

The image file is just the image of the map. 
the `yaml` file contains metadata as 
```
* path: <file_path>
* resolution: 0.05 (m/pixel)
* origin: [x,y,theta]
* negate: 0
* occupied threshold : 0.65 //threshold above which the cells are considered occupied. 
* free threshold : 0.196 //threshold below which the cells are considered occupied.
```

**UNDERSTAND ROS NODES AND LAUNCH FILE USED FOR SLAM**
==================================================

THe launcher that starts the slam node is...
```
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```
So the launcher is `turtlebot3_slam.launch`.

We can take a look at the file. To do that we need to find it.
We could do 
`
roscd turtlebot3_slam/
cd launch/
sublime ./turtlebot3_slam.launch
`

The file first sets some parameters....
* the robot model. which is taken from the environment variable.
* The slam method. 
* open_rviz arg to true to open it. 

There is another launch file associated to `turtlebot3_gmapping.launch` which contains the parameters of the `gmapping` slam algorithm. 

First it sets arguments related to the frames. 
And then, the `gmapping` node is run with all the parameters 
http://wiki.ros.org/gmapping to know more about all the params. 

some of then. 
Three important frames
* base_frame
* odom_frame
* map_frame
...
* update_rate
* delta: 0.05 // esolution of the map. 
// map limits
* xmin
* xmax
* ymin
* ymax

Now that we have the map, we need to use it for robot navigation. 


**MAP-BASED NAVIGATION DEMO**
==================================================

Command

`
roslaunch turtlebot3_gazebo turtlebot3_house.launch
`

For navigation... we need to load the map of the robot and providing it as input to the navigation stack. 

`
export TURTLEBOT3_MODEL=waffle_pi
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/ros/tb3_house_map.yaml
`

we need set manually the initial pose. 
2D Nav Goal sends the the targeted location. 
Then the stack will calculate a global path. Then a local path planner will try to follow the global path. When the (x,y) position is reached, the robot will rotate. 

* we need to manually set the initial location fo the robot in the map
* we send the goal pose
* the navigation stack then
	* global plan the path : static obstacle-free path
	* local path planner: execute the planned trajectory and avoids dynamic obstacle. 


**THE RECOVERY BEHAVIOR**
==================================================

The robot sometimes performs some bakwards motions to try to get a different initial pose when going through narrow corridors. 
Also, observe that during navigation, we can also perform the so-called clearing process, which basically updates the map info using the sensors, in case there is something initially mapped that dissapeared. 


**UNDERSTAND THE NAVIGATION LAUNCH FILE**
==================================================

Taking a look at the launch file again. 

`
roscd turtlebot3_navigation/
cd launch
sublime turtlebot3_navigation.launch
`

As before this guy, loads the turtlebot3_remote.launch package, that starts the nodes publishing the robot model, and the state broadcaster. 
Then, the map_server node is started with the map file. 

Then the amcl.launch file is launched, which is in charge of estimated the location of the robot in the map using the adaptive montecarlo localization, which uses particle filters for positioning. 
This uses the odometry info and the map. 
Then the navigation stack node is launched. The global and local. 
Finally, the rviz visualization node is launched. 


**WRITING A ROS NODE FOR ROBOT NAVIGATION**
==================================================



**UNDERSTND THE RECOVERY BEHAVIORS OF THE NAVIGATION STACK**
==================================================

**ROBOT SETUP TO SUPORT THE ROS NAVIGATION STACK**
==================================================

We need to set up the robot properly to use the ROS navigation stack. 
It considers the robot is configure in a certain way. 

* sensors transforms
* sensor sources
* odometry
* base controller

Requirements: 
- ROS
- a robot must publish tf transform to describe the relation between coordinate frames. 
	- base_link frame attached to the body
	- base_laser frame attached to the laser scan. 
	- We can define those transforms using the URDF xml file. 
	- Or, writing a node that publishes the static transformation in the appropriate topic. 
- Sensor information: 
	- sensor_msgs/LaserScan
	- sensor_msgs/PointCloud
- Odometry information
	- Requires the robot publish its pose and velocity. 
		- nav_msgs/odometry
	- ros.org/navigation/Tutorials/RobotSetup/Odom
- Base Controller 
	- using the geometry_msgs/Test
	- on the topic cmd_vel
- Mapping
	- map_server. 
	- Navigation stack can work with or without map. 



## Section 8
## #################################### 

**63 NAVIGATION STACK TUNING PROBLEM STATEMENT**
==================================================
**64 TUNING MAX/MIN VELOCITIES AND ACCELERATIONS OF THE ROBOT**
==================================================
**65 GLOBAL PLANNER PARAMETER TUNING**
==================================================
**66 LOCAL PATH PLANNER OVERVIEW**
==================================================
**67 THE DYNAMIC WINDOW APPROACH (dwa) ALGORITHM**
==================================================
**68 TUNING THE SIMULATION TIME OF THE DWA ALGORITHM**
==================================================
**69 DWA TRAJECTORY SCORING**
==================================================
**70 TUNING THE DWA TRAJECTORY SCORES**
==================================================

## Section 9
## #################################### 


**71 Overview** 
==================================================
**72 OVERVIEW OF THE FOLLOWER APPLICATION** 
==================================================
**73 CREATE A TF BROADCASTER FOR THE FRAMES ATTACHED TO THE ROBOT** 
==================================================
**74 TF LISTENER FOR THE FOLLOWER** 
==================================================
**75 BUG ALGORITHMS: OVERVIEW** 
==================================================
**76 BUG0,, BUG1, AND BUG2 APPROACHES** 
==================================================

