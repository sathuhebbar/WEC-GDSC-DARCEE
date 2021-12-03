import json

# Generating the dockerfile
# A lot of hardcoding
# Steps:
#  Use the debian:11 base image
#  Make unpriveleged user 'dummy' with a home folder
#  Update package database and install the required compilers
# For the containers:
#  Run as user 'dummy'
#  Working directory is the home directory of 'dummy'


with open('lang-config.json', 'r') as file:
    langs = json.load(file)

ls = ["FROM debian:11", "RUN useradd --create-home dummy"]

# Always do these together
# -y --> yes to all questions
s = 'RUN apt-get update && apt-get -y install '

for x in langs:
    s += langs[x]['package'] + ' '
ls.append(s)

ls += ["USER dummy", "WORKDIR /home/dummy"]

with open('docker/Dockerfile', 'w') as dfile:
    for x in ls:
        dfile.write(x + '\n')
