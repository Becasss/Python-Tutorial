# Python For Loops - for loop is used for iterating over a sequence(either a set, a tuple, a dictionary, a set or a string).


# Example :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# lOOPING THROUGH A STRING

for x in "banana":
    print(x)


# LOOPING THROUGH A DICTIONARY

for x in "Banana":
    print(x)  


# The Break Statement:   we can stop the loop before it has looped through all the items.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


# The continue statement


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



# The Range Function: To loop through a set of code a specific number of times.

for x in range(6):
    print(x)