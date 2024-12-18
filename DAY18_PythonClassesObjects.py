
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

# Example: Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hello my name is {self.name}.")

p1 = Person("Bikash", 34)
p1.greeting()  # Output : Hello my name is Bikash.



# The Self Parameter - The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

# Example: Use the words mysillyobject and abc instead of self:


class Person:
    def __init__(mysillyobject, name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def greeting(abc):
        print(f"Hello my name is {abc.name}." )

p1 = Person("John", 23)
p1.greeting()  # Output : Hello my name is John.




# Modify Object Properties :
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"Hello my name is {self.name}")

p1 = Person("John", 23)

p1.age = 22
print(p1.age)