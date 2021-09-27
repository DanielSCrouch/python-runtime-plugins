#!/bin/bash

echo "Creating venv environment"
python3 -m venv venv
# pip install ....
# pip freeze > requirements.txt
# pip install -f requirements.txt

echo "Activate venv environment"
source venv/bin/activate 

echo "Initialising local Git repository"
git init
