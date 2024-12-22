
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



# Else - use else keyword to define a block of code to be executed if no errors were raised.

try:
    print("Hello, world!")
except:
    print("An exception occurred")
else:
    print("Nothing went wrong!") 




# Finally - if specified , will be executed regardless if the try blcok raises an error or not.

try:
    print(x)
except:
    print("Something went wrong!")
finally:
    print("The 'try except' block is executed.")




# Example: Try to open and write to a file that is not writable.

try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing to the file.")

    finally:
        f.close()

except: 
    print("Something went wrong when opening the file.")