
# try block lets you test a block of code for errors.

# except block lets you handle the error

# else block lets you execute code when there is on error

# finally block lets you execute code, regardless of the result of the  try- and except blocks.




# Exception Handling 

# Example: Try block will generate an exception, because x isnot defined.

try:
    print(x)
except: 
    print("An exception occurred")


# Print one message if the try block raises a NameError and another for other errors.

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An error occurred")


