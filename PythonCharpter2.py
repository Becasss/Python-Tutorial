# strings
# Collections of characters inside single quotes or double quotes
# ----------------------------------string concatenation:-------------------------
first_name = "Bikash"
last_name = "Yamphu Rai"
full_name = first_name + " " + last_name
print(full_name)

# print(full_name + 3)   #error 
print(full_name + "3")  #no error
print(first_name + str(3)) #no error
print(first_name * 3)





#------------------------------------------------user input-------------------------
# input function:
name = input("type your name ")
print("Hello " + name)



# string
age = input("what is your age ")
print("your age is " + age)




#-----------------------------------------------int function-----------------------------------
number_one = int(input("enter the first number"))
number_two = int(input("enter the second number"))
total = number_one + number_two
print( "The total is " + str(total))

# str 
# integer(4) ----->string("4")



# integer
#str("4")------> 4
number1 = str(4)
number2 = float("44")
number3 = int("33")
print(number2 + number3)

# Float
#str("4")------>4.0




# --------------------------------------------------variable more__________________
name, age = "Bikash" , "27"
print( "Hello" + name +  "Your age is " +  age)






#---------------------------------------------two inputs-----------------------------------------
name = input("enter your name")
age = input("enter your age")
name, age = input("Enter your name and age").split()
print(name)
print(age)





#------------------------------------string formattting_---------------------
name = "Bikash"
age = 26
print("Hello " + name + "your age is " + str(age))  #ugly syntax


print("hello {} your age is {}".format(name, age)) #python 3


print(f"Hello {name} your age is {age}") #python 3.6










# Exercise 2.1
# Ask use to input 3 numbers and you have to print average of three numbers using string formatting.
number1, number2, number3 = input("enter number1, number2, and number3").split(",")
#(number1 + number2 + number3)/3
print(f"the total number is {(int(number1) + int(number2) + int(number3))/3}")




