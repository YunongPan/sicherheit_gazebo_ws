# sicherheit_gazebo_ws
WZL Projckt - Simulation in Gazebo for security concept. 

## Requirements
- **python-catkin-tools**
  - `sudo apt-get install python-catkin-tools`  
    
- **teleop_twist_keyboard**
  - `sudo apt-get install ros-melodic-teleop-twist-keyboard`  
  
## Installation
1. To test the project please clone this workspace first.  
   
	`cd ~`  
  
	`git clone https://github.com/YunongPan/sicherheit_gazebo_ws.git`  
  
2. Install dependencies  
  
	`cd ~/sicherheit_gazebo_ws`  
  
	`rosdep install --from-paths src --ignore-src -r -y`  
  
3. Build the workspace  
  
	`catkin_make`  
  
4. Copy human model  
  
	Open `~/sicherheit_gazebo_ws/src/gazebo_model`. Copy `human_male_1` folder into `~/.gazebo/models`.  
	
## Testing
1. Source env setting  
  
	`source ~/sicherheit_gazebo_ws/devel/setup.bash`  
  
	`export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:~/sicherheit_gazebo_ws/src/gazebo_plugin/plannar_mover_plugin/build`  
2. Start simulation in Gazebo  
  
	`roslaunch demonstrator_gazebo demonstrator_world.launch`  
  
3. Use keyboard to control the person 
  
	*Note: Click on the current shell and use* `shift +`  
  
	`u i o`  
	`j k l`  
	`m , .`
	  
	*If you are using an* ***German keyboard***, *please pay attention to the position of* `<` *and* `>` *button. Please check more details about usage in: https://github.com/ros-teleop/teleop_twist_keyboard*
  
4. Open another terminal and source the environment.
  
	`source ~/sicherheit_gazebo_ws/devel/setup.bash`  
  
5. Start environment detection.
  
	`roslaunch demonstrator_preprocessing environmental_detection.launch`  
  
6. After the process of step 5 is finished, please start speed controller.
  
	`roslaunch laser_filters demonstrator_filter_total.launch`  
  
  	*You may change the topics of LaserScan in Rviz to observe the filtered LaserScan data. Please change the topics of LaserScan to* ***/laserscan_filtered/front*** *and* ***/laserscan_filtered/rear***   
	
	*Then click back to the first terminal, which is now running the Gazebo and Rviz, to use keyboard to control the movement of the human model.*  
  
	*In the second terminal, the change in speed is displayed*
  


	  
