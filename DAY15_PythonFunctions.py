
# Python Functions - a block of code which only runs when it is called.

# You can pass data, kown as parameters, into a function.


def myFunction():       # Creating a function
    print("Hello, myFriend BIkash Yamphu Rai")

myFunction()            # Calling a function




# Arguments - Information can be passed into functions as arguments. 
# Arguments are specified after the function name, inside the parentheses.

def myFunction(fname):
    print("Hello, " + fname)

myFunction("Bikash")        # Calling a function
myFunction("Kiran")
myFunction("Bikram") 

# Note : Arguments are often shortened to args in Python documentation.


# Parameters or Arguments - From a Function's Perspective.
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


# Number of Arguments

def myFunction(fname, lname):
    print(fname + " " + lname)
    
myFunction("Bikash", "Yamphu Rai")

