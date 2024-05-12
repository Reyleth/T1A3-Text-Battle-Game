#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo Python 3 is installed
else
    echo Python 3 is not installed
    sleep 5
    exit 1
fi

# Check if pip is installed
if command -v pip3 &>/dev/null; then
    echo pip3 is installed
else
    echo pip3 is not installed
    sleep 5
    exit 1
fi

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install packages from requirements.txt
pip3 install -r requirements.txt

# Change Directory to the main.py file
cd src

# Create an executable for the application
pyinstaller main.spec
