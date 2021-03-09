# sicherheit_gazebo_ws
WZL Projekt - Simulation in Gazebo for security concept. 

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
  
	`source ~/group_surfing_ws/devel/setup.bash`  
  
	`export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:~/sicherheit_gazebo_ws/src/gazebo_plugin/plannar_mover_plugin/build`  
2. Launch simulation  
  
	`roslaunch demonstrator_gazebo demonstrator_world.launch`  
  
3. Use keyboard to control the person  
  
	Usage please see: https://github.com/ros-teleop/teleop_twist_keyboard  
	  
