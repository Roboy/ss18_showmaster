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

Roboy's facial expressions are animated in Unity. The corresponding repository is in https://github.com/Roboy/RoboyUnityFace  

For starting with Unity, clone the repository to your device. For seeing the actual face of Roboy in Unity, go to RoboyUnityFace/assets and open RoboyFace. All existing animations are stored in RoboyUnityFace/assets/animations. Corresponding material (added pictures to show them on the face, e.g. a moustache or sunglasses) are stored in RoboyUnityFace/assets/FaceComponents.

The connection to ROS via code (C#) is stored in RoboyUnityFace/assets/RoboyAnimator.cs

Having started RoboyFace in Unity,there is a Project window. For viewing all existing animations, first click on "face" in the Project Window. In a second step, open the "Animator" window. For viewing existing animations, press the play button on the top and trigger the animations in the "Animator" (Paramters) window. New animations can be added via the Animation window (if the animation or the Animator window is not shown, you can open it by clicking on the "Window" button at the bar on the top of Unity program). 

For all current and new animations, there is the Inspector on the right hand side, which has different functions for changing or modifying existing and new animations. 

If new animations were created, you must add transitions from the idle status to the animation status and back to the idle status. This can also be done in the Animator window. 

In addition to the old faces and expressions in Unity, the following faces & emotions were added in SS18 by animating them in Unity and can be triggered via ROS:
 - suprised Roboy
 - crying Roboy
 - irritated Roboy
 - Roboy wearing sunglasses
 - Roboy wearing spectacles
 - Roboy having a moustache
 

### 2. Generative Models for Chitchat as a Fallback-Answer
The new model is originating from Facebooks Dialog Research Platform [ParlAI](https://github.com/Roboy/ParlAI/). There, several state of the art implementations as well as several datasets are integrated in one platform. For Roboy, the profilememory implementation was choosen based on the Personachat dataset. 

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
- for Emotions refer to [RoboyUnityFace](https://github.com/Roboy/RoboyUnityFace) --> go to face_julian branch
- for ParlAI refer to [ParlAI](https://github.com/Roboy/ParlAI/tree/master/projects/roboy)
- for Games refer to [Roboy_Dialog](https://github.com/Roboy/roboy_dialog)
- for Snapchat refer to [Roboy_Snapchat](https://github.com/Roboy/roboy_snapchat)

### Running ROS-Master
- Start rosmaster in terminal with 
```
roscore
```

#### Emotions

Prerequesites: - Installation of Unity

To start, clone the repository https://github.com/Roboy/RoboyUnityFace.git on your computer. 

More detailed information is written in the upper section howitworks. 

In order to start the animations, it is necessary to disconnect from ROS. Otherwise, Unity will show an error message.  This can be avoided by changing the code in RoboyUnityFace/Assets/RoboyAnimator.cs . The line which must be changed looks like follows. In this line of code, the offline toggle should be set to true.

```
bool offlineToggle = true;
```

Now, all existing animations can be triggered in Unity by starting the play mode and by triggering animations in the Animator column. 

Additional faces could be added. Useful tutorials for starting with Unity can be found on YouTube and on the Unity homepage.


#### ParlAI
Prerequisites
- ParlAI setup as described [here](https://github.com/Roboy/ParlAI/)
- Profilememory model. From scratch, the easiest way to achieve this is to run
```
python projects/convai2/baselines/profilememory/interactive.py 
```
Interaction through ROS
- in terminal, run 
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
- in a new terminal
- activate the python 3.6. environment you set up when preparing to work with ParlAI as described [here](https://github.com/Roboy/ParlAI/)
- in `ss18_showmaster/ParlAI/projects/roboy/ros_integration` run 
```
python gnlp_ros_srv.py
```
- to talk to the model use ROS service call
```
rosservice call /roboy/cognition/generative_nlp/answer "text_input: 'hello'"
```

#### Snapchat
- In a new terminal start the snapchat server with
```
rosrun roboy_snapchat_filter snapchat_server.py
```
#### Games
In config.properties make sure the following parameters are set correctly:
- enable ROS
```
ROS_ENABLED: true
```
- Connect to the proper IP-Adress:
```
ROS_MASTER_IP:
```
- enable ROS-Packages:
```
ROS_ACTIVE_PKGS:
- roboy_filters
```
**!make sure ros servers are running before attempting to start dialog!**
- Start the dialog according to the instructions mentioned [here](http://roboydialog.readthedocs.io/en/master/Usage/0_installation.html)
