stereo_rig
==========

This repository contains all software that runs on the stereo diving rig.

See the [wiki](https://github.com/UCSD-E4E/stereo_rig/wiki) for complete documentation of the rig.

### Onboard Sensors

* IMU
* Compass
* Pressure sensor
* Stereo IDS uEye Cameras
* <del>Stereo QX100 cameras</del>
* <del>DVL</del>

### Repository Contents

#### ROS Launch Files

Launch files are inside stereo_rig/launch. **Make sure you have sourced devel/setup.bash before conducting a roslaunch.**

* stereo_rig.launch: the main launch file, up-to-date by 2015 May

See stereo_rig.launch for more information

#### ROS Packages

* dvl_driver: ROS driver for Teledyne Explorer DVL
* os5000: ROS driver for OceanServer pressure sensor and compass
* microstrain_3dmgx2_imu: ROS driver for Microstrain IMU
* see3cam: ROS driver built on uvc_camera for See3CAM machine vision cameras
* ueye_external_trigger: ROS node for controlling the external triggering device
* stereo_param_configure: ROS node for controlling the uEye node via topics and messages

#### uEye-External-Trigger

Arduino code + Interfacing ROS node for controlling the external trigger

#### QX100_Servo_Trigger

Arduino code for triggering the QX100s (shutter and on/off button) via servo

#### qx100_interfacing

idk wireless?
