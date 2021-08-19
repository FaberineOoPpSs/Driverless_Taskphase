## Link for the video:
https://youtu.be/TqnsAHkYgkw

## Creating the map

### 1.Launch gazebo world:
roslaunch slam_bot world.launch
### 2.Start map building
roslaunch slam_bot gmapping_demo.launch
### 3.Launch rviz
roslaunch slam_bot rviz_gmapping.launch
### 4.Move the bot around
rosrun slam_bot keyboard_teleop.py 


## Save the map:
rosrun map_server map_saver -f ~/formulam_ws/src/slam_bot/maps/test_map

## Loading the map:

### 1.Launch gazebo world:
roslaunch slam_bot world.launch
### 2.Launch amcl, move_base and rviz nodes:
roslaunch slam_bot amcl_move_base.launch

## Install required dependencies:
sudo apt-get install ros-melodic-dwa-local-planner
sudo apt-get install ros-melodic-joy
