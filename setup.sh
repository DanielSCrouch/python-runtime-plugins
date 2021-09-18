#!/bin/bash

echo "Creating venv environment"
python3 -m venv venv

echo "Activate venv environment"
source venv/bin/activate 

echo "Initialising local Git repository"
git init
