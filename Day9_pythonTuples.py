
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