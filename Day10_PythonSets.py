
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



# Add Any Iterable:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "Oange"]
thisset.update(mylist)
print(thisset)





# Remove Set Items: To remove an item in a set, use the remove() or the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset.discard("apple")
print(thisset)




# Pop() Method: remove a random item by using the pop() method 
thisset = {"apple", "banana", "Chrrry"}
x = thisset.pop()
print(x) # removed item
print(thisset) # the set after removal



# Clear() Method:empties the set

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)



# del keyword will delete the set completely
#thisset = {"apple", "banana", "cherry"}
#del thisset
#print(thisset)




# Python - Loop Sets
# Loop Items - Loop through the set, and print the values
thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)



# Python - Join Sets
# The union() and udate() methods joins all items form both sets.
# The intersection() method keeps ONLY the duplicates
# The difference() method kees the items from the first set that are not in the other sets.
# The symmetric_difference() method keeps only all items EXCEPT the duplicates.


# Union () Methods:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3, 4}
set3 = set1.union(set2)
print(set3)



# Union  () methods:
set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1 | set2
print(set3)



# join multiple sets with the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"d", "e", "f"}
set4 = set1.union(set2, set3)
print(set4)
set5 = set1 | set2 | set3 | set4
print(set5)



# Join a set and a tuple - union() method allows you to join a  set with others data types, like lists or tupls
x = {"a", "b", "c", "d"}
y = (1,2 ,3)
z = x.union(y)
print(z)



# Update() method inserts all the items from one set into another
x = {"a", "b", "c"}
y = {"d", "e", "f"}
x.update(y)
print(x)