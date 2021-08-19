## Link for the video:
https://youtu.be/TqnsAHkYgkw

## Screenshots:
![gazebo_world](https://user-images.githubusercontent.com/71475786/130131503-bcec3131-e825-47a3-a262-37334e622883.png)

![creating_map](https://user-images.githubusercontent.com/71475786/130131585-aa463169-34b1-4959-9e4e-85e1aff4e7bb.png)

![slam](https://user-images.githubusercontent.com/71475786/130131621-44174852-cf18-461b-b065-ad715850d2e3.png)


## Creating the map

### 1.Launch gazebo world:
```
roslaunch slam_bot world.launch
```
### 2.Start map building
```
roslaunch slam_bot gmapping.launch
```
### 3.Move the bot around
``` rosrun slam_bot keyboard_teleop.py ``` 


## Save the map:
``` rosrun map_server map_saver -f ~/formulam_ws/src/slam_bot/maps/test_map ```

## Loading the map:

### 1.Launch gazebo world:
``` roslaunch slam_bot world.launch ```
### 2.Launch amcl, move_base and rviz nodes:
``` roslaunch slam_bot amcl_move_base.launch ```

## Install required dependencies:
``` sudo apt-get install ros-melodic-dwa-local-planner ```
```
sudo apt-get install ros-melodic-joy
```
