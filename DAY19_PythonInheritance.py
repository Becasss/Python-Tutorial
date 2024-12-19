

# Pyhton Inheritance - allows us to define a class that inherits all the methods and properties from another class.

# Parent Class - is the class being inherited from, also called base class.
# Child Class - is the class that inherits from another class, also called derived class.


# Create a parent Class.

# Example: Create a class named Person, with firstname and lastname properties and a printname method:

class Person: 
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

    # Use the Person class to create an object and the execute thr printname method:

x = Person("Bikash", "Yamphu Rai")
x.printname()