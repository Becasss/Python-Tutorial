

# Python Iterators - is an object that contains a countable number of values.


# Ietrator VS Iterable - 


# Example: Return an interator form a tuple and print each value:

mytupe = ("apple", "orange", "cherry")
myit = iter(mytupe)

print(next(myit)) # Output : apple
print(next(myit))   # Output : orange
print(next(myit)) # Output : cherry


# Example: Strngs are also iterable objects, containing a sequence of characters.
mystr = "banana"
myit = iter(mystr)

print(next(myit)) # Output :b
print(next(myit)) # Output : a
print(next(myit)) # Output : n
print(next(myit)) # Output : a
print(next(myit)) # Output : n
print(next(myit)) # Output : a
print(next(myit)) # Output : None (as there are no more characters in the string)



