
# Python Lists : mylist = ["apple", "orange", "cherry"]

# List are used to store multiple items in a single variable
# Example:
thislist = ['apple', 'orange', 'cherry']
print(thislist)



# Lits Items : are orderd, changeable and allow duplicate values


# Ordered : if you add new items to a list, the new items will be placed at the end of the list

# Changeable: meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates : Since list are indexed, lists can have items with the same value.
# Example: 
list1 = ['apple', 'orange', 'cherry', 'apple']
print(list1)
print(list1[3])


# List Length: len() function

print(len(list1))


# List Items -  Data Types

list2 = [1,2,3,4,5,6,7,8,9]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


list4 = ['abc', 1 , True, "male", 23]
print(list4)   # a list can contain different data types:



# The list() constructor

list5 = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(list5)


# Python Collections (Arrays)
# List : is a collection which is ordered and changeable. Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
# Set : is a collection which is unordered, unchangeable and unindexed. No duplicate members.
# Dictionary : is a collection which is orderd and changeable. No duplicate members.




# Python - Access List Items

# Access Items: list items are indexed and you can access them by refering to the index number:
print(thislist[1])  # output : orange


if "apple" in thislist:     # Check if Item Exists
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")




# Python - Change List Items

# Change Item Value : To change the value of a specific item, refer to the index number.

thislist[1] = "Blackcurrant"
print(thislist)  # output : ['apple', 'Blackcurrant', 'cherry']


# Change a range of items values
thislist1 = ['apple', 'banana', 'cherry', 'orange', 'kiwi','mango']
thislist1[1:3] = ['blackcurrant', 'watermelon']
print(thislist1)  # output : ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


# Insert Items : insert() method inserts an item at the specified index.
thislist1.insert(2, 'grape')
print(thislist1)  # output : ['apple', 'blackcurrant', 'grape', 'watermelon', 'orange', 'kiwi', 'mango']





# Python - ADd List Items

# Append Items : append() method inserts an item to the end of the list.

thislist.append("Orange")
print(thislist) # output : ['apple', 'Blackcurrant', 'cherry', 'mango']


# Extend List: 
thislist.extend(thislist1)
print(thislist)  # The elemlents will be added to the end of the list.


# ADD any Iterable: extend() method does not have to append lists, you can add any iterable object(tuples, sets, dictionaries)

thislst = ["apple", "bannabin", "Cherry"]
thistuple = ('Kiwi', ' Orange')
thislst.extend(thistuple)
print(thislst)  # output : ['apple', 'bannabin', 'Cherry', 'Kiwi', 'Orange']






# Python - Remove List Items

# Remove Specified Item - remove() method removes specified items.

# Example:
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)  # output : ['banana', 'cherry']


# Remove Specified Index - pop() method removes the item at the specified index.
thislst = ['cheerry', "banana", 'orange','mango']
thislst.pop(1)
print(thislst)  # Output: ['cherry', "orange", 'mango']

# If you don't specify an index, the pop() method removes the last item from the list.


# del keyword - removes the specified index.

del thislst[0]
print(thislst)


# Clear the list - clear() method empties the list.