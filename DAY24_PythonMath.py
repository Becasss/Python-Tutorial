
# Python  Math :

# Built-in Math Functions - min() and max() functions can be used to fing the lowest or hightest value in an iterable.

x = min(8,7,1,3,5,6,0,2,6)

y = max(8,7,1,3,5,6,0)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number.

# Example
x = abs(-5.23)
print(x)        # Output : 5.23




# The pow(x,y) function returns the value of x to the power of y.

# Example: Return the value of 4 to the power of 5.
x = pow(4,5)
print(x)        # Output : 1024



# Math Module: 

# math.sqrt() method - returns the square root of a number.

import math
x = math.sqrt(64)
print(x)        # Output : 8.0



# math.ceil() method - rounds a number upwards to its nearest integer.
# math.floor() method rounds a number downwards to its nearest integer.

# Example: 
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)        # Output : 2
print(y)        # Output : 1



# math.pi constant, returns the value of PI(3.14)

import math
x = math.pi
print(x)        # Output : 3.141592653589793