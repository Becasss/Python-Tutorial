

# Variables : are containers for storing data values.

# Creating Variables: Python has no command for declaring a variable.

# Example 1:
myVariable = "Hello World!"
x = 34
print(myVariable)   # Output: "Hello World!"
print(x)            # Output: 34



# Example 2:
y = 5
y = "Hello World!"
print(y)  # Output: "Hello World!"



# Casting: If you want to specify the data type of a variable, this can be done with casting.

# Example 3:
x = str(34)
y = int(34)
print(x)  # Output: "34"
print(y)  # Output: 34
print(type(x)) # Output: string
print(type(y)) # Output: integer



# Single or Double Quotes? : String variables can be declared either by using single or double quotes.

# Example 4:
a = "Bikash"
print(a) # Output: "Bikash" -- Double quotes

b = 'Yamphu'
print(b) # Output: "Yamphu" -- single quotes



# Case-Sensitive: Variables names are case-sensitive
b = 4
B = "Bikash Rai"
print(b)
print(B)
# age, Age, AGE are three different variables in python.



# Variables Naming

# Legal Variables Names:
myvar = "myvar"
my_var = "my_var"
_my_var = "_my_var"
myVar = "myVar"
MYVAR = "myVar"
myvar2 = "myVar"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)






# Multi Words Variable Names
camelCase = "thisIsCamelCase"
print(camelCase)
kebabCase = "this-is-kebab-case"
print(kebabCase)
snake_case = "this_is_snake_case"
print(snake_case)
PascalCase = "MyVariablename"
print(PascalCase)



# Python Variables - Assign Multiple Variables

# Many Values to Multiple Variables
#Example1:
f,g,h = "Orange", "Banana", "Cherry"

print(f) # Output: Orange
print(g) # Output: Banana
print(h) # Output: Cherry

# Notes: Make sure the number of variables matches the number of values, or else you will get an error.


# One value to Multiple Variables
q = w= e = "Bikash Yamphu Rai"
print(q) # Output : Bikash Yamphu Rai
print(w) # Output : Bikash Yamphu Rai
print(e) # Output : Bikash Yamphu Rai


# Unpack a collection
fruits = ["apple", "orange", "banana"]
a, b, c = fruits
print(a) # Output: apple
print(b) # Output: orange
print(c) # Output: banana




# Output variables : The print() function is often used to output variables

l = "Python is awesome"
print(l) # Output: Python is awesome


c = "Python"
d = "is awesome"
print(c, d) # Output: Python is awesome