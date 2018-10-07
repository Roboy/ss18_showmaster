# ss18_showmaster
Roboy wants to be more entertaining and fun on fairs and other events with audience. Additionally, he is easy to control for us as developers.


## About
This repository consists of four sections to make Roboy more entertaining on fairs.
1. Facial Expressions to show more emotions
2. Generative Model for Chitchat
3. Vision Module
4. Additions to Dialog for playing games and leading a conversation autonomously

Roboy Showmaster team wants to combine these sections to have an immersive and entertaining conversation.


## How it works
### 1. Facial Expressions
Roboy's facial expressions are animated in Unity. The corresponding repository is in https://github.com/Roboy/RoboyUnityFace  

In addition to the old faces and expressions in Unity, the following faces & emotions were added in SS18 by animating them in Unity and can be triggered via dialogue and manually via the keyboard (useful for fairs):
 - tongue out (keyboard : D), happy (Q), lucky (Y), pissed (N), angry (A), irritated (X), hypno eyes (V), colored hypno eyes (U), rolling  eyes (I), surprised (Z), pirate (P), cryingRoboy (C), glasses (G), moustache (M), pink sunglasses (F)
 
Futher instructions and documentation can be found in the README https://github.com/Roboy/RoboyUnityFace

### 2. Generative Models for Chitchat as a Fallback-Answer
The new model is originating from Facebooks Dialog Research Platform [ParlAI](https://github.com/Roboy/ParlAI/). There, several state of the art implementations as well as several datasets are integrated in one platform. For Roboy, the profilememory implementation was choosen based on the Personachat dataset. 

### 3. Snapchat Module
This module is able to apply filter masks on the interlocutor's face. Following filters are implemented: Roboy mask, mustache, pixelated sunglasses, flies, hat, crown and rainbow. The algorithm uses OpenCV and dlib library finding 68 facial landmarks to detect the most important face charateristics and to estimate the tilt angle of the face. The required filter mask is then applied automatically in-face superposition in real time.
The ROS Service Server receives service calls from the dialog as Strings that hold the desired filter. The snapchat module then uses the video information from Roboy's camera to appliy the requested filter onto the detected faces.

### 4. Vision Module using Neural Compute Sticks
The Movidius™ Neural Compute Stick ([NCS](https://developer.movidius.com/)) is a tiny fanless deep learning device that allows us to run a live video stream for detecting and classifying persons and objects without heavy GPU power. When presenting Roboy on fairs or events, Neural Compute Sticks and nuke computer are needed only to run the vision module for the [Dialog Fair Show](#dialog-fair-show). Through vision Roboy is able to extract information about his environment which guides through the different states in the Dialog Fair Show.

### 5. Dialog Games
For playing games, three new states for the Roboy [Dialog System](https://github.com/Roboy/roboy_dialog) are implemented: 

- The 20 questions game using an [Akinator Wrapper API](https://github.com/markozajc/Akiwrapper) that is run in children protection mode

- The snapchat game where the user can request a specific face mask to be applied by the snapchat module based on ROS service calls communication with the aforementioned module

- A Choose Game State where Roboy suggests one of the above mentioned games by random choice or the interlocutor can selcet a preferred game

### 6. Dialog Fair Show
The goal of the Fair Show is to have an autonomous interaction between Roboy and the visitor on fairs. Autonomous in this case means that Roboy can perceive his environment and can start a conversation on his own if a person is interested/listening. Roboy students no longer need to control the according programs.

<img src="https://github.com/Roboy/ss18_showmaster/blob/devel/fairshow_diagram.jpg" width="500" height="400" />

## Getting Started
### Prequisites and Setup
- for Emotions refer to [RoboyUnityFace](https://github.com/Roboy/RoboyUnityFace)  
- for ParlAI refer to [ParlAI](https://github.com/Roboy/ParlAI/tree/master/projects/roboy)
- for Dialog refer to [Roboy_Dialog](https://github.com/Roboy/roboy_dialog)
- for Snapchat refer to [Roboy_Snapchat](https://github.com/Roboy/roboy_snapchat)
- for Vision with Neural Computing Sticks refer to [Roboy/ros_intel_movidius_ncs](https://github.com/Roboy/ros_intel_movidius_ncs)

## Running the Code
### Running ROS-Master
- Start rosmaster in terminal with 
```
roscore
```

### Emotions
Prerequesites: 
- Installation of Unity

To start, clone the repository https://github.com/Roboy/RoboyUnityFace.git to your computer. 

More detailed information is given in the README in https://github.com/Roboy/RoboyUnityFace

### ParlAI
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

### Snapchat
- In a new terminal start the snapchat server with
```
rosrun roboy_snapchat_filter snapchat_server.py
```

### Games or FairShow?
#### For Games
In config.properties of the Dialog code make sure the following parameters are set correctly:
- enable ROS
```
ROS_ENABLED: true
```
- Connect to the proper IP-Adress (the one your ROS-Master is running on):
```
ROS_MASTER_IP: XXX.XX.XX.XX
```
- enable ROS-Packages:
```
ROS_ACTIVE_PKGS:
- roboy_filters
- roboy_gnlp
- roboy_face
```
- select the correct Personality (both GamePersonality and OrdinaryPersonality are able to play games)
```
PERSONALITY_FILE: "resources/personalityFiles/OrdinaryPersonality.json"
```

**!make sure ros servers are running before attempting to start dialog!**
- Start the dialog according to the instructions mentioned [here](http://roboydialog.readthedocs.io/en/master/Usage/0_installation.html)

#### For FairShow
##### Start Vision
launch file boaboasafhdaslkdhjfskvdfghaiteuwojfkgha

##### Start Dialog
In config.properties make sure the following parameters are set correctly:
- enable ROS
```
ROS_ENABLED: true
```
- Connect to the proper IP-Adress (the one your ROS-Master is running on):
```
ROS_MASTER_IP: XXX.XX.XX.XX
```
- enable ROS-Packages:
```
ROS_ACTIVE_PKGS:
- roboy_filters
- roboy_gnlp
- roboy_face
- roboy_vision
```
- disable
```
INFINITE_REPETITION: false
```
- select the correct Personality
```
PERSONALITY_FILE: "resources/personalityFiles/FairShowPersonality.json"
```

**!make sure ros servers are running before attempting to start dialog!**
- Start the dialog according to the instructions mentioned [here](http://roboydialog.readthedocs.io/en/master/Usage/0_installation.html)
