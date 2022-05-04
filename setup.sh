#!/bin/sh

# # activating the python virtual environment
pip3 install virtualenv
python3 -m venv .
source ./bin/activate

# # required installs
pip3 install python-dotenv
pip3 install flask
pip3 install schedule
pip3 install requests

# # create db
cd db
sqlite3 nasa_facilities.db < nasa_facilities.sql
cd ..

# # run app
python3 app.py