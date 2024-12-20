

# Python Modules - cosider a module to be the same as code library.

# Create a module 

# Example : Save this code in a file named mymodule.py
"""
def greeting(name):
print("Hello, " + name)"""

# Use a module - by using the import statement

import mymodule
mymodule.greeting("Jonathan")

# Note: When using a function from a module, use the syntax: module_name.function _name.




# Variables in Module

import mymodule
a = mymodule.person1["age"]
print(a)  # Output: 30



# Naming a Module : Re-naming a Module 

import mymodule as mx
mx.greeting("Jane")


# Built-in Modules

# Import and use the platform module.

import platform
x = platform.system()

print(x) # Output:windows



# Using the dir() function

# Example: List all the defined names belonging to the platform module.
import platform
x = dir(platform)

print(x)