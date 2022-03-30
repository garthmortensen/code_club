#!/bin/bash
# create virtual environment
python -m venv venv

# check for linux directory structure, then continue setup
DIR_LINUX=./venv/bin/activate
if [ -f "$DIR_LINUX" ]; then
	echo "$DIR_LINUX exists. This is a linux/mac box. Activating venv"
	source venv/bin/activate
	echo "Pip installing packages"
	pip install -r requirements.txt
fi

# check for windows directory structure, then continue setup
DIR_WIN=./venv/Scripts/activate
if [ -f "$DIR_WIN" ]; then
	echo "$DIR_WIN exists. This is a windows box. Activating venv."
	source venv/Scripts/activate
	echo "Pip installing packages"
	pip install -r requirements.txt
fi

# get the data
python ./gimme_data.py
