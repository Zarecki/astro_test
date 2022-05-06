#!/bin/sh

# # setup
sudo apt update
sudp apt-get update
sudo apt-get install python3-pip
sudo apt install sqlite3

# # activating the python virtual environment
pip3 install virtualenv
echo virtual environment installed

python3 -m venv .
echo venv called

source ./bin/activate
echo activated

# # required installs
pip3 install python-dotenv
pip3 install flask
pip3 install schedule
pip3 install requests
echo pip installs finished

# # create db
sqlite3 db/nasa_facilities.db < db/nasa_facilities.sql
echo db seeded

# # runs schedule script
# ./schedule_script.sh

# # run app
python3 app.py
echo app running

# # deactivate venv on app close
deactivate
