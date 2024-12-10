
# Python Booleans : represents one of two values: True or False

# Example 1
print(10 > 9)           # Output : True
print (10 == 9)         # Output : False
print(10 < 9)           # Output : False

# Example 2
a = 200
b = 22

if b > a:
    print("B is greater than a")
else:
    print("A is greater than or equal to B")





# Evaluate values and variables

# Example:
print(bool("Hello"))   # Output : True
print(bool(12))         # Output :True



# Most Values are True
print(bool("abc"))      # Output : True
print(bool(123))        # Output : True
print(bool(["apple", "orange"]))  # Output : True



# Some Values are False
print(bool("False")) # Output : False
print(bool(None)) # Output : False
print(bool(0))  # Output : False
print(bool('')) # Output : False
print([]) # Output : False
print({}) # Output : False



class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))



# Function can return a Boolean
# Example:
def myFunction():
    return True
print(myFunction()) # Output : True


# Example:
def myfunctions():
    return True
if myfunctions():
    print("Yes")
else:
    print("No")




# isinstance function
x = 200
print(isinstance(x, int)) # Output : True