
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



# Arbitary ARguments, *args

def myfunction(*kids):
    print("the Youngest chid is: " + kids[2])

myfunction("Bikash", "Kiran", "Bikram")



# Keyword Arguments : can send arguments with the key = value syntax.

def myFunction(child1, child2, child3):
    print("THe youngest child is " + child3)

myFunction(child1 = "Emil", child2 = "Bkash", child3 = "Kiran")


# Arbitary Keyword Arguments, **Kwargs

def myFunction(**kids):
    print("THe youngest child is " + kids['lname'])

myFunction(fname = "B Ikash", lname = "Rai")
