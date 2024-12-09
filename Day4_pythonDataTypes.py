# Python Data Types::

# Built-in Data Types: 
        # Text Type: "str" , Numeric Types: "int, float, complex", 
        # Sequence Types: " tuple, list, range" ,Mapping Data Types: "dict" , Set Types: "set, frozenset", 
        # Boolean Types: "bool" , Binary Types: " bytes, bytearray, memoryview"



# Getting the Data Types:
# Example:
x = 5
print(type(x))  # Output: 'int'

y = "Hello, World!"
print(type(y)) # Output: 'Str'

z = 3.14
print(type(z)) # Output: 'float'

a = 1j
print(type(a)) # Output: 'complex'

b = ["application", 'Design', "Layout" ]
print(type(b)) # Output: 'list'

c = ('banana', 'apple', 'Cherry')
print(type(c)) # Output: 'tuple'

d = range(5)
print(d)
print(type(d)) # Output: 'range'

e = {"name": "Bikash", "age": 26}
print(e)
print(type(e)) # output : 'dict'


f = {"apple", "banana", "cherry"}
print(f)
print(type(f))  # Output : 'set'


g = frozenset({"apple", "banana", "cherery"})
print(g)
print(type(g)) # output : 'frozenset'

h = True
print(h)
print(type(h)) # output : 'bool'


i = b"Hello, world!"
print(i)
print(type(i)) # output : 'byte'

j = bytes(5)
print(type(j)) # output : 'bytearray'

k = memoryview(bytes(5))
print(type(k)) # output : 'memoryview'

l = None
print(type(l)) # output : 'None'





# Python Numbers

# Int : Int, or integer, is a whole number, + or -, without decimals, of unlimited length.

x = 10
print(type(x)) # output : 'int'

# Float : Float, or floating point number is a number, + or -, containing one or more decimals.

x = 1.1

print(type(x)) # output : 'float'

y = 34e3
print(y)
print(type(y)) # output : 'float'


# Complex: Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
print(type(x)) # output : 'complex'


# Type Conversion

# Convert from int to float:
x = float(1)

# Convert from float to int:
y = int(2.23)

# Convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


# Random Number: don't have a random() function to make a random number but has a built-in module called random
# that can be used to generate random numbers:

import random
print(random.randrange(1,19))




# Python Casting

# int() - constructs an integer number from an integer literal, a float literal or a string literal

# float() -constructs a float number froman integer literal, a float literal or a string literal

# str() - constructs a string from a wide variety of data types, including strings, bytes, bytearrays, lists, tuples, and dictionaries