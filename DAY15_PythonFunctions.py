
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

def myfction(*kids):
    print("the Youngest chid is: " + kids[1])

myfction("Bikash", "Kiran", "Bikram")



# Keyword Arguments : can send arguments with the key = value syntax.

def myFunction(child1, child2, child3):
    print("THe youngest child is " + child3)

myFunction(child1 = "Emil", child2 = "Bkash", child3 = "Kiran")


# Arbitary Keyword Arguments, **Kwargs

def myFunction(**kids):
    print("THe youngest child is " + kids['lname'])

myFunction(fname = "B Ikash", lname = "Rai")




# Default Parameter Value: 

def myFUnction(country = "Nepal"):
    print(f"I am from {country}.")

myFUnction("Sweden")
myFUnction("Romania")
myFUnction()  # The default value will be used in this case.  # Output : I am from Nepal.
myFUnction("Switzerland")


# Passing a List as an Argument

def myFunction(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
myFunction(fruits)



# Return Values - to let a function return a value, use the return statement.

def myFunction(x):
    return 5 * x

print(myFunction(2))    # Output : 10
print(myFunction(5)) # Output : 25


# The Pass Statement 
def myFunction(x):
    pass    # Having a empty function definition  like this, would raise an error without pass statement.


# Position - ONly Arguments
def myPosition(x, /):
    print(f"the position is {x}.")
myPosition(10)  # Output : 10



# Combine Position - only and keyword - only

def my_function(a,b,/, *, c, d):
    print(a + b + c + d)

my_function(1, 2, c=3, d=4)  # Output : 10



# Recursion - which means defined function can call itself.

def tri_recrusion(k):
    if(k > 0):
        result = k + tri_recrusion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recrusion(6)
