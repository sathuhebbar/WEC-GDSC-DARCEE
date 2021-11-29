# THIS IS A ONE-TIME SETUP!

#******* PYTHON SETUP**************

# Set-up the python3 venv
python3 -m venv darcee-env

# Activate the venv
source darcee-env/bin/activate

# Install the dependencies
pip3 install -r requirements.txt

# Done with the VM
deactivate

#******* PYTHON SETUP**************

#******* DOCKER SETUP**************

# Directory for docker
cd docker

# Create the required image
docker build --tag darcee_executor_image .

# Return
cd ..

#******* DOCKER SETUP**************