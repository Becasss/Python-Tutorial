
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