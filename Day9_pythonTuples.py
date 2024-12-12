
# Python Tuples: mytuple = ("apple", "banana", "orange")


# Access Tuples: 

# Example: 
thistuple = ("apple", "banana", "orange")
print(thistuple)

# Note: The firs item has index 0.


# Negative Indexing:
print(thistuple[-2])    #Output : banana


# Check If items:

if "apple" in thistuple:
    print("Yes, apple is in thistuple") # Output : Yes, apple is in thistuple





# Updte Tuple : Tuples are unchangeable, meanig that you can't change3 , add or remove items once the tuple is created.

# Change the tuple: 

# Example:
x = ('apple', 'banana', 'orange')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)  # Output: ('apple', 'kiwi', 'orange')


# Add the items:
thistuple = ('banna', 'cherry', 'apple')
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)
print(thistuple)  # Output: ('banna', 'cherry', 'apple', 'orange')


# Remove Items:

thistuple = ('apple', 'banana', 'cherry')
y = list(thistuple)
y.remove('apple')
thistuple = tuple(y)
print(thistuple)  # Output: ('banana', 'cherry')




# Unpacking a Tuple:
fruits = ('apple', 'banana', 'cherry')
(green, blue, yellow) = fruits
print(green) # Output: apple
print(blue)  # Output: banana



# Using Asterisk*:

fruits = ('apple', 'banana', 'cherry', 'raspberry')
(green, blue, *yellow) = fruits
print(green) # Output: apple
print(blue)  # Output: banana
print(yellow)  # Output: ['cherry', 'raspberry']



# Loop through a Tuple:

thistuple = ('apple', 'banana', 'cherry', 'raspberry')
for x in thistuple:
    print(x)



# Loop through the Index Numbers

thistuple = ('apple','banana','cherry','raspberry')
for i in range(len(thistuple)):
    print(thistuple[i])




# Using a while loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1



# python - Join Tuples

# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)


# Multiply Tuples:
fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2
print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
