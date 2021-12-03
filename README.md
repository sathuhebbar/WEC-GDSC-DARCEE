# WEC-GDSC-DARCEE
# DARCEE == DARCEE's Another Remote Code Execution Engine

DARCEE is a highly primitive code executor. As of now, we
only support Python and Ruby. We will definitely improve DARCEE.
Thank you!

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
  2. ``` gunicorn --workers=(2 * NUMBER OF CPUs + 1) app:app``` <br>
  3. Navigate to localhost:8000 on your browser <br>
  4. Enjoy! <br>

To stop the server,
  1. ```Ctrl + C```
  2. ```deactivate```
