
# Python Scope: A variable is only available from inside the region it is created. This is called Scope.

# Local Scope: A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myFunct():
    x = 300
    print(x)

myFunct()