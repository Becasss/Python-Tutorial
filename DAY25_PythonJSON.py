

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





# Format the Result  

# Example: Use the indent parameter to define the number of index.
import json

x = {
    "name": "Dhan Bahadur Rai",
    "age":30,
    "married": True,
    "divorced":False,
    "children": ("Udash", "Bikash", "Bishal"),
    "pets": None,
    "cars":[
        {"model": "BMW 230", "mpg": 25.6},
        {"model": "Ford Edges", "mpg":24.1}
    ]}



# use four indents to make it easier to read thee result.

print(json.dumps(x, indent=4, separators=(".", "=")))



# Order the Result - json.dumps() method has parameters to order the keys in the result.


# Example: Use the sor_keys() parameter to specify if the rsult should be shorted or not.

import json

x = {
    "name": "Dhan Bahadur Rai",
    "age":30,
    "married": True,
    "divorced":False,
    "children": ("Udash", "Bikash", "Bishal"),
    "pets": None,
    "cars":[
        {"model": "BMW 230", "mpg": 25.6},
        {"model": "Ford Edges", "mpg":24.1}
    ]}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))