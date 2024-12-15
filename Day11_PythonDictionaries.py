
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




