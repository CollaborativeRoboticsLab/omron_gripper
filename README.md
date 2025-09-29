# Omron Gripper

This is a separation of robotiq 2f-85 gripper related code from [OmronAPAC/Omron_TM_ROS2](https://github.com/OmronAPAC/Omron_TM_ROS2)

## Setup

Create a workspace

```sh
mkdir -p omron_ws/src
cd omron_ws/src
```

Install dependencies
```sh
sudo apt install ros-humble-moveit ros-humble-controller-manager ros-humble-joint-trajectory-controller ros-humble-joint-state-broadcaster ros-humble-rmw-cyclonedds-cpp ros-humble-joint-state-publisher ros-humble-joint-state-publisher-gui ros-humble-vision-opencv
```
```sh
pip install pymodbus
```

Clone the repositories into the `src` folder by

```sh
git clone https://github.com/CollaborativeRoboticsLab/omron_arm.git
git clone https://github.com/CollaborativeRoboticsLab/omron_gripper.git
```
finally build by

```sh
cd ..
colcon build
```