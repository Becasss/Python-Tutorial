

# Python JSON - is a syntax for storing and exchanging data.


# JSON in Python 

# import json


# Parse JSON - convert form JSON to python 
# If you have a JSOn string, you can parse it by using the json.loads() method.


# Example: Convert form JSON to python:

import json

# some JSON:
x = '{"name": "John", "age":30, "city": "New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])




# Convert Pytho objects into JSON strings, and print the values:

import json

print(json.dumps({"name":"Bikash","age":30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("apple"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))