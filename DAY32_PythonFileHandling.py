
# Python File Open - open() function takes two parameters ; filename and mode.




# Syntax - f = open(filename).

# code above is the same as : f = open(filename, "rt"). - "r" for read and "t" for text are the default values, you do not need to specify them.




# Open a File on the server
f = open("mymodule.py", "r")

print(f.read())





# Read only Parts of the file

# Example: Return the 5 first characters of the file.
f = open("mymodule.py", "r")

print(f.read(10))




# Read Lines - readline() method.

# Example: Read one line of the file:
f = open("mymodule.py", "r")

print(f.readline())



#Example: Loop through the file by line.
f = open("mymodule.py", "r")

for x in f:
    print(x)





# Close File - It is a good practice to always close the file when you are done with it.

# Example: Close the file when you are finished with it.
f = open("mymodule.py", "r")

print(f.readline())
f.close()