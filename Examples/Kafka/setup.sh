#!/bin/bash

# mkdir kafka-python-example
# cd kafka-python-example

echo "Creating a virtual environment..."
python3 -m venv venv # Create a virtual environment
source venv/bin/activate # Activate the virtual environment

echo "Installing kafka-python..."
pip install kafka-python`