# WEC-GDSC-DARCEE
# DARCEE == DARCEE's Another Remote Code Execution Engine

DARCEE is a highly primitive code executor. As of now, we
only support Python and Ruby. We will definitely improve DARCEE.
Thank you!

## Frameworks:
We've used Flask and gunicorn here. The HTML file uses Bootstrap.
Docker is used to create and manage containers.

## Features:
1. Can handle simple read-eval-print kind of code.
2. Supports as many workers as the user desires.
3. Four languages are supported as of now, but adding more is easy! Just edit
   the lang-config json file , add the package set and the command to execute.
4. Uses the debian:11 base container image

## Installation
System Requirements: <br>
  1. python3 and pip3 <br>
  2. A functional internet connection <br>
  3. The ```docker``` suite and you being allowed to execute ```docker``` commands without sudo <br>
  
Basic set-up <br>
  1. Download the zip and extract it somewhere <br>
  2. cd to that directory in a terminal <br>
  3. ```bash setup.bash ``` <br>

This finishes the setup. <br>

## Running
To run the app => in the same folder, do <br>
  1. ``` source darcee-env/bin/activate ``` <br>
  2. Replace x in this command with the number of CPUs you have and run it: ``` gunicorn --workers=(2 * x + 1) app:app``` <br>
  3. Navigate to localhost:8000 on your browser <br>
  4. Enjoy! <br>

To stop the server,
  1. ```Ctrl + C```
  2. ```deactivate```

Some things:
  1. If the error stream shows a message resembling 'Process Killed',
     you might be using too much memory. Also, lack of output may be
     indicative of the program encountering some kind of error during
     execution.
  2. The time limit is 5s. Memory limit is 256M. 
  3. Don't run nasty things, nasty things might happen!

## Demo Video link:
https://drive.google.com/file/d/199MATQPErSB9IkF9f4ffSfUGMyVCaEpd/view?usp=sharing

<em> Thank you WEC NITK! </em>
