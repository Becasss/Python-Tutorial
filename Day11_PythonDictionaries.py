
# Python Dictionaries : Dictionaries are used to store data values in key:values pairs.


# Example: Create and print a dictionary
thisdict ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



# Dictionary Items are ordered, changeable and do not allow duplicates.

print(thisdict['model'])   # output: Mustang




# Duplicates are Not Allowed : Dictionaries cannot have two items with the same key:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "model": "Fiesta"
}
print(thisdict) # Output: {'brand': 'Ford', 'model':'Fiesta', 'year':1964}


# Dictionary Length : len() function

print(len(thisdict)) # Output: 3

# type() function

print(type(thisdict)) # Output: dict


# the dict() Constructor function

mydict = dict(name = "John", age =34, country = "United States")
print(mydict) # Output:{'name':'John', 'age':34, 'country':'United States'}



# Python - Accessing Dictionary Items

# Accessing Items - by refering to its key name, inside square brackets.

thisdict = {
    "name": "John",
    "age": 34,
    "city": "New York"
}

x = thisdict['city']
print(x)  # Output: "New York"


# There is also a method called get() that will give you the same result.

y = thisdict['name']
print(y) # Output: "John"




# Get Keys() - will return a list of all the keys in the dictionary.

a = thisdict.keys()
print(a)  # Output: ['name], 'age', 'city']


# Example: 
car = {
    "name" : "Ford",
    "model": "Mustang",
    "year" : 1964
}

b = car.keys() # before the change

print(b) # Output: ['name', 'model', 'year']
car['color'] = "white" 

print(b) # Output: ['name', 'model, 'year', 'color']


# Get Values() - will return a list of values in the dictionary.

c = thisdict.values()
print(c) # Output: ['New York', 34, 'United States']


# Example:

fruits = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}
d = fruits.values()
print(d) # before the change
fruits["grape"] = 4
print(d) # after the change



# Get Items() - will return a list of tuples containing each key-value pair in the dictionary.


e = fruits.items()
print(e) # Output: [('apple', 1), ('banana', 2), ('cherry', 3), ('grape', 4)]

fruits["kiwi"] = 5
print(e) # after the change




# Check if Key Exists() - 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'mode' is of the keys in thisdict")




# Python - Chnage Dictionary Items

# Change Values:
thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
thisdict["year"] = 2020
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# Update Dictionary - update() method will update the dictionary with the from the given arguements

thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
thisdict.update({"year": 2020, "color": "red"})
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}



# Add items: done by using a new index key and assign a value to it.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" :2020
}
thisdict["color"] = "Red"
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'Red'}


# Update Dictionary - will update the dictionary with items from a given argument.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" :2020
}

thisdict.update({"color": "Red"})
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'Red'}