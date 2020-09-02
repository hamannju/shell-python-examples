#!/bin/bash

export TEST_VAR1=100 # These variables work in Python
export TEST_VAR2=200
export TEST_VAR3=300

TEST_VAR4=400 # This variable does not work in Python

echo $TEST_VAR4

# Pass the first two arguments of the SHELL script to the PYTHON script
python3 script.py $1 $2