# ROS2 Obstacle Avoidance

## Description

An autonomous TurtleBot3 obstacle avoidance project using ROS2 Jazzy and Gazebo Harmonic.

## Features

- ROS2 Jazzy
- TurtleBot3 Burger
- Gazebo Harmonic
- RViz2
- LaserScan Subscriber
- TwistStamped Publisher
- Smart Left/Right Obstacle Avoidance
- YAML Parameters
- Launch Files

## Requirements

Ubuntu 24.04

ROS2 Jazzy

Gazebo Harmonic

## Build

```bash
cd ~/ros2_ws

colcon build --symlink-install
```

## Run

Terminal 1

```bash
export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Terminal 2

```bash
source install/setup.bash

ros2 launch obstacle_avoidance obstacle_avoidance.launch.py
```

## Topics

Subscribe

```
/scan
```

Publish

```
/cmd_vel
```

## Author

Agilesh Kumar
