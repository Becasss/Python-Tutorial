
# Python Sets: myset = {"apple", "orange", "cherry"}

# Example 1
thisset = {"apple", "orange", "cherry"}
print(thisset)



# Duplicates Not Allowed

thisset = {"apple", "orange", "cherry", "apple"}
print(thisset)


thisset = {"apple", "banana", True, 1,2}
print(thisset)


thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
print(len(thisset))


# The set() Constructor
thisset = set(('apple', 'banana','cherry')) # Note the double round-brackets
print(thisset)





# Python - Access Set Items 

# Access Items : you cannot access items in a set by referring to an index or a key.

# Example : Loop Through the set, and print the values:
thisset = {"apple", "banana", " Cherry"}
for x in thisset:
    print(x)

print("banana" in thisset)

print("banana" not in thisset)



# Change Items: once a set is created,you cannot change its items, but you can add new items



# Python - Add Items 
# To add one item to a set use the add() method.

# Example:
thisset = {"apple", "Orange", "Cherry"}
thisset.add("kiwi")
print(thisset)




# Add sets: To add items form another set into the current set, usse the update() method.

thisset = {'apple', 'banana', 'cherry'}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
