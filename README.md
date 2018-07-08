# ss18_showmaster
Roboy wants to be more entertaining and fun on fairs and other events with audience. Additionally, he is easy to control for us as developers.


## About
This repository consists of four sections to make Roboy more entertaining on fairs.
1. Facial Expressions to show more emotions
2. Generative Model for Chitchat
3. Vision Module
4. Additions to Dialog for playing games

Roboy Showmaster team wants to combine these sections to have an immersive and entertaining conversation.


## How it works


### 1. Facial Expressions
In addition to the old faces and expressions in Unity, the following faces & emotions were added by animating them in Unity and and can be triggered via ROS:
 - suprised Roboy
 - crying Roboy
 - irritated Roboy
 - Roboy wearing sunglasses
 

### 2. Generative Models for Chitchat as a Fallback-Answer
The new model is originating from Facebooks Dialog Research Platform [ParlAI](https://github.com/facebookresearch/ParlAI/). There, several state of the art implementations as well as several datasets are integrated in one platform. For Roboy, the profilememory implementation was choosen based on the Personachat dataset. 

### 3. Snapchat Module
This module is able to apply filter masks on the interlocutor's face. Following filters are implemented: Roboy mask, mustache, pixelated sunglasses, flies, hat, crown and rainbow. The algorithm uses OpenCV and dlib library finding 68 facial landmarks to detect the most important face charateristics and to estimate the tilt angle of the face. The required filter mask is then applied automatically in-face superposition in real time.
The ROS Service Server receives service calls from the dialog as Strings that hold the desired filter. The snapchat module then uses the video information from Roboy's camera to appliy the requested filter onto the detected faces.

### 4. Dialog Games
Three new states for the Roboy [Dialog System](https://github.com/Roboy/roboy_dialog) are implemented: 

- The 20 questions game using an [Akinator Wrapper API](https://github.com/markozajc/Akiwrapper) that is run in children protection mode

- The snapchat game where the user can request a specific face mask to be applied by the snapchat module based on ROS service calls communication with the aforementioned module

- A Choose Game State where Roboy suggests one of the above mentioned games by random choice or the interlocutor can selcet a preferred game


## Getting Started

### Prequisites and Setup
- for Emotions refer to [RoboyUnityFace](https://github.com/Roboy/RoboyUnityFace)
- for ParlAI refer to [ParlAI](https://github.com/Roboy/ParlAI/)
- for Games refer to [Roboy_Dialog](https://github.com/Roboy/roboy_dialog)
- for Snapchat refer to [Roboy_Snapchat](https://github.com/Roboy/roboy_snapchat)

### Running ROS-Master
- Start rosmaster in terminal with 
```
roscore
```

#### Emotions

Install Unity on your computer and pull RoboyUnityFace from GitHub. 

In order to test the animations, it is necessary to disconnect from ROS. This can be reached by changing the code in RoboyUnityFace/Assets/RoboyAnimator.cs The line which must be changed looks like follows. In this line of code, the offline toggle should be set to true.

```
bool offlineToggle = true;
```

Now, all existing animations can be triggered in Unity by starting the play mode and by triggering animations in the Animator column. 

Additional faces can be added. Useful tutorials for starting with Unity can be found on YouTube and on the Unity homepage.


#### ParlAI
- in terminal, run 
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
- in a new terminal
- activate the python 3.6. environment you set up when preparing to work with ParlAI as described [here](https://github.com/Roboy/ParlAI/)
- in `ss18_showmaster/ParlAI/ros_integration` run 
```
python gnlp_ros_srv.py
```
#### Snapchat
- In a new terminal change directory to
```
cd roboy_snapchat/roboy_snapchat_filter/scripts/
```
here, start the snapchat server with
```
rosrun roboy_snapchat_filter snapchat_server.py
```
#### Games
**!make sure ros servers are running before attempting to start dialog!**
- Start the dialog according to the instructions mentioned [here](http://roboydialog.readthedocs.io/en/master/Usage/0_installation.html)
