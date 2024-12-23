
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






# Python File Write/Create Files


# Example: open the file "mymodule.py" and append content to the file.

f = open("mymodule.py", "a")
f.write("Now the file has more content than you")
f.close()


# Open and read the file after appending:

f = open("mymodule.py", "r")
print(f.read())
f.close()




# Example: Open the file "mymodule.py" and overwrite the content.

f = open("mymodule.py", "w")
f.write("Woops! I have deleted the contents of mymodule.py")
f.close()


# open and read the file after the overwriting:
f = open("mymodule.py", "r")
print(f.read())




# Create a New File: "x" - Create, "a" - Append, "w" - write




# Example: Create a file called "myfile.txt"
f = open("myfile.txt", "x")         # RESULT: A NEW EMPTY FILE IS CREATED!


# Example: Create a new file if it doesn't exist

f = open("myfile.txt", "w")





# Python Delete Files: To delete a file, you must import the OS module, and run its os.remove() function:

# Example: