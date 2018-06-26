# ss18_showmaster
Roboy wishes to be more entertaining and impressive. With his new skills he is reliably able to attract people to its presence independent to their relation to him. He appeals as well to an audience as to a group of developers, satisfying both of their preferences.


## About
This repository consists of four sections to make Roboy more entertaining on fairs.
1. Facial Expressions to show more emotions
2. Generative Model for Chitchat
3. Vision Module
4. Additions to Dialog for playing games

Roboy Showmaster team wants to combine these sections to have an immersive and entertaining conversation.


## How it works

# 1. Facial Expressions
are implemented in Unity ....

# 2. Generative Models
uses ParlAI ....

# 3. Vision Module
The ROS Service Server receives service calls from the dialog as Strings that hold the desired filter. The vision module streams the video information from Roboy's camera to an iPad and applies the requested filter to the detected faces. The algorithm uses OpenCV and dlib library finding 68 facial landmarks to detect the most important face charateristics and to estimate the tilt angle of the face. The required filter mask is then applied automatically in-face superposition in real time. Following filters have been implemented: Roboy mask, mustache, pixelated sunglasses, flies, hat, crown and rainbow.

# 4. Dialog Games
The Dialog implements two games: 

-The 20 questions game using an Akinator Wrapper API that is run in children protection mode and 
-the Snapchat-Game that communicates with the Vision Server and requests the desired filters through service calls.

## Getting Started

Start roscore in terminal with `roscore`

In a new terminal, go to /roboy_snapchat_filter/scripts/ directory and start the vision server with `rosrun roboy_snapchat_filter snapchat_server.py`
  
Start the dialog with `mvn exec:java -Dexec.mainClass="roboy.dialog.DialogSystem"`
