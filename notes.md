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

## Section 11: Appendix: Motion in ROS (old videos - but still applicable)
## #################################### 

## Section 12: ROS Tools and Utilities
## #################################### 

## Section 13: Getting Started with Turtlebot3
## #################################### 

## Section 14: Perception I: Computer Vision in ROS with OpenCV
## #################################### 

## Section 15: Perception II: Laser Range Finders (Laser Scanner)
## #################################### 

## Section 16: rosserial: Connecting new Hardware (Arduino) with ROS
## #################################### 

## Section 17: Bonus
## #################################### 