# string indexing
language = "python"
 
 # positions (index number)

 # p = 0, -6
 # y = 1, -5
 # t = 2, -4
 # h = 3, -3
 # o = 4, -2
 # n = 5, -1

print(language[4])
print(language[-4])








# slicing / selecting sub sequences
lang = "Python"
# print(lang[3])
# syntax - [start argument : stop argument]
print(lang[0:4])
print(lang[-3:])


# step argument
# sytax - [start argument : stop argument - 1 : step]
print(lang[0:5:2])
print("BIKASH"[0:5:2])
print("BIKASH"[::3])
print("BIKASH"[5::-1])
print("BIKASH"[-1::-1])
print("BIKASH"[::-1])




# exercise:
# Ask user name and print back user name in reversae order. Note : try to make your program in 2 lines using string formatting.
name = input("enter your name:")
print(f"reverse of your name is {name[-1::-1]}")




# String method part one
name = "BiKaSh YaMpHu rAi"

# len() function
print(len(name))


# lower() function:
print(name.lower())


# upper () function:
print(name.upper())


# title() method:
print(name.title())


# count() method:
print(name.count("h"))









# take two comma separated inputs from user 1) user's name, example-"Bikash"  2) a single character, "h"
name, char = input("enter your name and charcter sepearted by comma:").split(",")
print(f"length of your name is {len(name)}")
#print(f"charcter count: {name.count("char")}") # case sensitive

# name.lower().count(char.lower())  #case sensitive







# strip_method:
name = "  BiKASH   "
dots = '................'
#lstrip() method
print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
print(name.replace(' ', "") + dots)







# replace () method
string = 'she is beautiful and she is good dancer'
print(string.replace(" ", "_"))
print(string.replace("is", "was",2))


# find () method:
print(string.find('is', ))
is_pos1 = string.find("is")  # is_pos1 ----> number
is_pos2 = string.find("is", is_pos1 + 1)
print(is_pos2)





# center Method:
name = "bkash"
#**bikash**, 11
print(name.center(12, "*"))
name = input("enter your name:")
print(name.center(len(name) + 8, "*"))




# string are immutable: cannot be replace once string name is created


string = "string"
print(string.replace('t', "T"))
print(string)






# assignment operators:
name = "Bikash"
#name = name + "it" # name +=  "it"
name += "it"
print(name)


age = 23
age += 1
print(age)


age = 2
age *= 4
print(age)