

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
# print(next(myit)) # Output : None (as there are no more characters in the string)


# Loopig through an interator

# Example: Iterator the values of a tuple
mytuple = ("apple", "orange", "cherry")

for x in mytuple:
    print(x)



# Iterate the characters of a string
mystr = "banana" 
for x in mystr:
    print(x)





# Create an Iterator : __iter__() and __next__() to your object.
# The __iter__() method acts similar, you can do operations (intializing etc), but must always return the iterator object itself.
# __next__() method also allows you to do operations and must return the next items in the sequence.

# Exampel: reate an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



# StopIteration: 
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):P
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
    