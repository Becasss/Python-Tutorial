

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



# Example: Convert a Python object containing all the legal data types.

import json
x = {
    "name": "John",
    "age": 20,
    "married" : True,
    "divorced" : False,
    "children" : ("Bikash", "Bishal"),
    "pets" : None,
    "cars": [{"model": "BMW 230","mpg": 27.5},
             {"model": "Ford Edge", "mpg": 24.1}
             ]
             }


# Convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)





