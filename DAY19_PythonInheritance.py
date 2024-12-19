

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




# Create a child class: 
# Example: Use the student class to create an object and then execute the printname method


class Person:
    def __init__(self,fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()





# ADD the __init__ () Function: 

# Example: Add the __init__() function to the student class:

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x = Student("Mike", "Olsen")

x.printname()





# Use the super() Function - will make the child inherit all the methods and properties from its parent.

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

z = Student("John", "John")
z.printname()




# Add Properties 

# Example: Add a property called graduationyear to the Student class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname, lname):
        super(). __init__(fname,lname)
        self.graduationyear = 2019

x = Student("Mike", "Tyson")
print(x.graduationyear)


# Example: Add a year parameter and pass the correct year when creating objects.

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printnam(self):
        print(self.firstname, self.lastname)    


class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname, year)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2089)
print(x.graduationyear)


