#!/usr/bin/env python3

import os
import sys

print("Home is " + os.environ["HOME"])  # The HOME directory of the current user
print("The directory of this script is: " + os.environ["PWD"])  # The current working directory


# Our three test variables defined earlier
print(os.environ["TEST_VAR1"])
print(os.environ["TEST_VAR2"])
print(os.environ["TEST_VAR3"])


# TEST_VAR4 is not exported by the shell script and therefore does not exist in the environment -> Error
try:
    var4 = os.environ["TEST_VAR4"]
    print(var4)
except KeyError:
    print("Test_VAR4 is not defined properly")


print(sys.argv[0])  # Name of the current program


# This is pretty shitty but works :)
if len(sys.argv) > 1:
    print(sys.argv[1])

if len(sys.argv) > 2:
    print(sys.argv[2])
