
# Python Polymorphism - means many forms and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


# Function Polymorphism - len() function

# String - for strings len() returns the number of characters.
x = "Hello World!"
print(len(x))  # Output: 12



# Tupe - for tuples len() returns the number of items in the tuple.

mytuple = ("apple", "orange", "cherry")
print(len(mytuple))  # Output: 3


# Dictionary - for tuples len() returns the number of key/value pairs in the dictionary.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))  # Output: 3



# Class polymorphism - often used in Class mehtods, where we can have multiple classes with the same method name.

# Example : Different classes with the same method:
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")
    

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")   # Create a car object
boat1 = Boat("Yatch", "Touring 20")  # Create a Boat Object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    x.move()  # Output: Drive!, Sail!, Fly!



# Inheritance Class Polymorphism - 

# Example: Create a class called vechicle and make car, Boat, Plane child classes of vechicle.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        pass

    def move(self):
        print("Move")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail")

class Plane(Vehicle):
    def move(self):
        print("Fly")


car1 = Car("Ford", "Mustang")  # Create a Car Object
boat1 = Boat("Ibiza", "Touring 20") # Create aboat Object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()  # Output: Ford, Mustang, Move, Ibiza, Touring 20, Sail, Boeing, 747, Fly  