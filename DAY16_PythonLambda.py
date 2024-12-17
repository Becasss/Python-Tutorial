
# Python Lambda: is a small anonymous function.
# A lambda function can take any number of argumetns, but can only have one expression.

# Syntas: lambda arguments : expression

# Example: Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5)) # Output : 15



# Example: Lambda function can take any number of arguments.

x = lambda a, b : a * b
print(x(4,5)) # Output :20



# Why use lambda function?

def myFUnction(n):
    return lambda a : a * n

mydoubler = myFUnction(2)
print(mydoubler(10)) # Output : 20



# Example: 
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mydoubler = myfunc(4)

print(mydoubler(10)) # Output : 40
print(mydoubler(5)) # Output : 20