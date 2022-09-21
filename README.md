# Hello(Real) World with ROS- Robot Operating System
This repository contains all the ROS pkgs that I am developing during learning ROS by following TU Delft MOOC course [Hello(Real) World with ROS-Robot Operating System](https://ocw.tudelft.nl/courses/hello-real-world-ros-robot-operating-system/). This course is also available at [`edx.org`](https://www.edx.org/course/hello-real-world-with-ros-robot-operating-system) for certification.

## Course Contents/Learning Objectives
- **Week1: ROS Essentials**
  - Introduction to ROS Nodes,Topics, Services and Actions. 
* **Week2: Build your own robot environment**
  * Software representation of URDF
  * ROS parameter server 
  * Real world object representations to the simulation environment
* **Week3: Autonomous Navigation**
  * Map creation with GMapping package
  * Autonomously navigate a known map with ROS navigation
* **Week4: Manipulation**
  * Motion planning
  * Pick and place behavious using industrial robotis with ROS Moveit
* **Week5: Robot Vision**
  * Object Detetcion
  * Pose estimation
* **Week6: Final Project**
  * Build a production line application with two industrial robot arms and a mobile robot
  
## ros-noetic-DelftX repository description: 
- **`hrwros`** is the top level folder that contains ros pkgs inside it
- **`hrwros_assignments`** is the another top level folder that contains ros pkgs for weekly based assignments
- **`hrwros_utilities`** is the ros pkgs for useful functions
- **`ros1_course_content`** contains all ros pkgs that I developed during following this course. Basic purpose is to implement all the stuff taught in the     course, to get better understanding of code and learning debugging.


![image](https://user-images.githubusercontent.com/62834697/190458690-d9badd1b-da90-42da-acb1-baa92753d5db.png)


## Environment Setup:
**If ROS-Noetic is not installed** [follow this](http://wiki.ros.org/noetic/Installation/Ubuntu)

`If ROS-Noetic Version already installed in the system` : Run the following commands in the linux terminal to setup the ros workspace with turtlebot3 packages.
```shell
$ cd ~/catkin_ws/src             # will only run if catkin_ws is available at root directory
$ git git@github.com:kumar-sanjeeev/ros-noetic-DelftX.git
$ cd ~/catkin_ws && catkin_make  # to build ros packages
```
## Weekly assignment Solutions
- [Week1 assignmnet](hrwros_assignments/README.md)
- [Week2 assignment](hrwros_assignments/README.md)
- [Week3 assignment](hrwros_assignments/README.md)


