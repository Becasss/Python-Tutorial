
# Python Classes and Objects


# Create a class - a class is like an object constructor  or a blueprint for creating objects.

class MyClass:
    x = 5

print(MyClass)




# Creat an Object 
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)



# The __init__() Function

# Example : Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 24)

print(p1.name)
print(p1.age)




# The __str__() function : 

# Example: The string representation of an object WITHOUT the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Bikash", 34)

print(p1)


# Example: The string representation of an object WITH the __str__() function:


class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    
p1 = Person("John", 35)

print(p1)




# Objects Methods
