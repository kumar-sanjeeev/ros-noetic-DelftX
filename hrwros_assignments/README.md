# Table of Content
 *  [Week1 assignment](#week1-assignment)
 *  [Week2 assignment](#week2-assignment)
 *  [Week3 assignment](#week3-assignment)








# Week1 assignment





# Week2 assignment

- ## week2_assignment 1:
   * **`Task Description`**: 
      * Add the bin in the provided factory environment and place the bin on the opposite side of the conveyor, right in front of ur-10 robot as shown in below picture
      * Bin must be on the floor
      
      ![image](https://user-images.githubusercontent.com/62834697/190726102-e94cef6e-8385-4f63-a4c2-8f701b982474.png)
      
   * **`Solution`** :
      * Step 1: Add the following code change to file `"hrwros_assignmnet1.xacro"`
      
        ```xml
          <!-- Solution  -->
          <!-- call the macro -->
          <xacro:bin_urdf prefix="bin_2_"/>

          <!-- bin 2 -->
          <joint name="bin_2_joint" type="fixed">
            <parent link="world_interface" />
            <child link="bin_2_base_link" />
            <origin xyz="2.0 1.9 0" rpy="0 0 0" />
          </joint>
        ```
      * Step 2: run the following commands in the terminal
        ```shell
        $ source ~/hrwros_ws/devel/setup.bash                                      # source the hrwros_ws
        $ roslaunch hrwros_week2_assignment visualize_hrwros_assignment1.launch    # launch the rviz simulation
        
        ```
  * `Result` : 
  
      ![image](https://user-images.githubusercontent.com/62834697/190728869-b02af5c8-34d9-4501-8801-3a8c72d8afaf.png)

- ## week2_assignment 2:
   * **`Task Description`**: 
      * Add a new object to a factory : a green sphere
      * Sphere should be placed on the opposite side of the conveyor, underneath the stairs at the end of the factory
      
      ![image](https://user-images.githubusercontent.com/62834697/190731996-26c40d98-d2ce-4562-94b1-f980c6acef1c.png)

      
   * **`Solution`** :
      * Step 1: Add the following code change to file `"hrwros_assignmnet2.xacro"`
      
        ```xml
          <!--My Solution -->
          <!-- STEP1- ADD LINK: This will describe the sphere in the world -->
          <link name="sphere_link">
            <visual>
            <origin xyz="0.0 0.0 0.4" rpy="0.0 0.0 0.0"/>
              <geometry>
                <sphere radius="0.4"/>
              </geometry>
              <material name="sphere_link">
                <color rgba="0.0 1.0 0.0 1"/>
              </material>
            </visual>
          </link>

          <!-- Step2-ADD JOINT: To give position to the sphere in the link -->
          <joint name="sphere_link" type="fixed">
            <parent link="world"/>
            <child link="sphere_link"/>
            <origin xyz="4.0 -4.0 0.0" rpy="0.0 0.0 0.0"/>
          </joint>
        ```
      * Step 2: run the following commands in the terminal
        ```shell
        $ source ~/hrwros_ws/devel/setup.bash                                      # source the hrwros_ws
        $ roslaunch hrwros_week2_assignment visualize_hrwros_assignment2.launch    # launch the rviz simulation
        
        ```
  * `Result` : 
  
      ![image](https://user-images.githubusercontent.com/62834697/190730821-8f3d7b20-507e-4074-aa11-f126f2cae48c.png)

- ## week2_assignment 3:
   * **`Task Description`**: 
      * Replace the Robot 2 (the UR5) with Fanuc LR Mate 200ic
      * Robot must be on the pedestal
      
      ![image](https://user-images.githubusercontent.com/62834697/190734934-984d8600-0436-4d1a-b204-ceb3683b4baa.png)

      
   * **`Solution`** :
      * Step 1: Add the following code change to file `"hrwros_assignmnet3.xacro"`
      
        ```xml
          <!--My solution -->
          <xacro:include filename="$(find hrwros_week2_assignment)/urdf/robot/lrmate200ic_macro.xacro"/>
          <xacro:fanuc_lrmate200ic prefix="robot2_" joint_limited="true"/>
          <joint name="robot2-robot2_pedestal_joint" type="fixed">
            <parent link="robot2_pedestal_link" />
            <child link="robot2_base_link" />
            <origin xyz="0 0 0.6" rpy="0 0 ${radians(180)}" />
          </joint>
        ```
      * Step 2: run the following commands in the terminal
        ```shell
        $ source ~/hrwros_ws/devel/setup.bash                                      # source the hrwros_ws
        $ roslaunch hrwros_week2_assignment visualize_hrwros_assignment3.launch    # launch the rviz simulation
        
        ```
  * `Result` : 
  
      ![image](https://user-images.githubusercontent.com/62834697/190739225-f9143bad-8d89-4fc9-8420-3f76d24c59fc.png)

# Week3 assignment

- ## week3_assignment 1:
   * **`Task Description`**: 
      * Visualize the robot in the factory 
      * Provide a good estimation of the robot's initial position
      * Improve quality of localization with the AMCL(Adaptive Monte Carlo Localization)algorithm
      
     ![crop_ass1_gazebo](https://user-images.githubusercontent.com/62834697/191616113-d19c8a19-347e-4734-968c-1d2194c10b8e.png)     ![crop1_ass1_rviz](https://user-images.githubusercontent.com/62834697/191616797-65bc599b-83b2-464a-b53d-c9372ea261f6.png)




      
   * **`Solution`** :
      * Step 2: set the correct file location of the map in the `"amcl_navigation.launch"`
      * Step 1: correct the initial position of the robot in the map `"amcl_navigation.launch"`
      
        ```xml
          <launch>
            <!-- Map server -->
            <arg name="map_file" default="$(find hrwros_week3)/config/map_factory_v1.yaml"/>  <!-- Set correct map file -->
            <arg name="3d_sensor" default="$(env TURTLEBOT_3D_SENSOR)"/>  <!-- r200, kinect, asus_xtion_pro -->

            <node name="map_server" pkg="map_server" type="map_server" args="$(arg map_file)" />

            <!-- Localization -->
            <!-- Assigment 1 Part 2 -->
            <arg name="initial_pose_x" default="-3.999279"/>  <!-- Set correct initial pose x -->
            <arg name="initial_pose_y" default="-0.1999075"/>  <!-- Set correct initial pose y -->
            <arg name="initial_pose_a" default="0.0"/>  <!-- Set correct initial angle  -->
            <arg name="custom_amcl_launch_file" default="$(find turtlebot_navigation)/launch/includes/amcl/$(arg 3d_sensor)_amcl.launch.xml"/>

            <include file="$(arg custom_amcl_launch_file)">
              <arg name="initial_pose_x" value="$(arg initial_pose_x)"/>
              <arg name="initial_pose_y" value="$(arg initial_pose_y)"/>
              <arg name="initial_pose_a" value="$(arg initial_pose_a)"/>
            </include>

            <!-- Move base -->
           <include file="$(find turtlebot_navigation)/launch/includes/move_base.launch.xml"/>
        </launch>  
        ```
      * Step 2: run the following commands in the terminal
        ```shell
        $ source ~/hrwros_ws/devel/setup.bash                                      # source the hrwros_ws
        $ roslaunch hrwros_week3 hrwros_turtlebot_navigation.launch                # launch the factory simulation
        $ roslaunch hrwros_week3_assignment amcl_navigation.launch                 # launch the rviz simulation with correct robot location 
        ```
  
    * `Result` : 
  
      ![git_rviz2](https://user-images.githubusercontent.com/62834697/191618072-563a7f26-993e-4dc0-a503-10a092d4bebc.png)




  
  
