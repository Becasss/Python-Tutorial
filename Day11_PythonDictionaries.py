
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


# Remove Items - pop() - will remove the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020,
    "color": "Red"
}
thisdict.pop("model")
print(thisdict) # Output: {'brand': 'Ford', 'year': 2020, 'color': 'Red'}



# del() keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020,
    "color": "Red"
}
del thisdict["model"]
print(thisdict)


# Clear() method empties the dictionary
thisdict.clear()
print(thisdict)





# Python - Loop Dictonaries

#Example: Print all key names in the dictionary, one by one

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

for y in thisdict:
    print(thisdict[y])


for a in thisdict.values(): # using values() method
    print(a)

for b in thisdict.keys(): # using keys() method
    print(b)


for (x, y) in thisdict.items():
    print(x, y)





# Python - Copy Dictionaries

# Copy a Dictionary - copy() method

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# Another way to make a copy is to use the built-in function buildd().
thsdict = thisdict.copy()
print(thsdict)





# Python - Nested Dictionaries

# Nested Dictionaries - can contain dictionaries, this is called nested dictionaries.

# Example:
myfamilyl = {
    "child1":{
        "name": "Emma",
        "age": 40
    },
    "child2":{
        "name":"TObias",
        "age": 10
    },
    "chid3":{
        "name": "Linus",
        "age": 6
}
}
print(myfamilyl)


# Example:
child1= {
    "name": "Emma",
    "age": 40
},
child2 ={
    "name":"Tobias",
    "age": 10
},
child3 = {
    "name": "Linus",
    "age": 6
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)




# Access Items in Nested Dictionaries

print(myfamilyl["child2"]["name"])




# Loop Through Nested Dictionaries


myVillage = {
    "Num": {
        "name": "NumBazzard",
        "year": 2023
    },
    "people": {
        "population": 10000,
        "density": 100
    },
    "animals": {
        "type": "squirrel",
        "count": 100
    }
}

for x, obj in myVillage.items():
    print(x)
    for y in obj:
        print(y + ":" , obj[y])
