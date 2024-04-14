#Print_function

print("hello world")
print('hello world')
#you can use 'single qutoes under "double quotes" and vice-versa
print('hello world"world" helo')
print("hello 'wrold' on the rock")


#we cannot use "duble qutoes" inside double quotes and 'single quotes' under single quotes








#------------------------------escape sequences--------------
#backslash --\'BIKASH\' or \"Yamphu\""
print('hello \'world\' world')
print("i am \"bikash\" rai")




#backslash (\n) -- means new line
print("lineA\nline B\n line c")


#backslash (\t)---means new tap
print("I am Bikash\tYamphu rai")


#double backslash (\\) --means a single backslash (\):
print("this is single blackslash \\") #\\ is for backslash
print("this is duble backslash \\\\")
print("hell\bo")





#-----------------------------------------------------comments---------------------
#this is comment and shrot-cut key is ctrl + forwardslash(/) then you can comment easily.









# -----------------------------------------------------escape sequences as  Normal text----------------
#output : line A \n line B
print("line A \\n line B")
print("Line b \\t line B")
print("this is  blackslash \\\\\\")


#output: \" \'
print(" \\\" \\\' ")
#\' = '
#\" = "
# \\\' = \'
# \\\" = \"






#----------------------------------------------exercise 
# print these following lines
# this is \\ double backlash
#  these are /\/\/\/\ mountains
#  he is    awesome (use escape sequence instead of manual spaces   )
# \' \n \t \" (print this as an output)
print("this is \\\\ double backslash")
print("these are //\\//\\//\\//\\ mountains")
print("He is \tawesome")
print("\\\' \\n \\t \\\" ")








# --------------------------------------------short cut keys_------------------------
print(r"line A \n line B")
print("line A \n line B")





# --------------------------------------print emji-------------------------------------
print("\U0001F644")







#-------------------------------------------python as a calculator--------------------------------
print(2 + 3 *7)
print(2/4) #float division
print(4/2)


print(4//2)# integer division
print(2//4)

print(2**3)#exponential

print(2**0.5)

print(round(2**0.5,3))


print(2**3/2*6-4*(3-4/2))


print(3%2) #modulo gives remainder 


print((2+3)/2) #2+3= 5/2
print((2+3)*5/2%6) #5*5/2%6  and 25/2 % 6 again, 12.5 % 6



print(2**3**2)# expontents(right to left)

#Note:*, /, //, % (precedence: left to right)
#Note: +, - (precedence: left to riht)








#---------------------------------------------------Variables----------------------------------------
number1 = 2
print(number1)
number1 = 4
print(number1)
#string, number 
name = "Bikash"
print(name)
name = 123
print(name)
#varales name--rules;
# cannot start with any numbers e.g (1number = 4)
#  starts with letters, _(underscore) -------first letter




user_name = "Bikash Yamphu Rai" #snake case writing
userOneName = "mohit" #camel case writing








#-------------------------------------------summary chapter one-----------------------------------------------------------------
#print function:
print("hellow \"wolrd\" world")
print('hello \'world\' world')

#escape sequence
print("line A lt line B")
print("LIne B")
print("this is backslash \\")



#escapse sequence as normal text
print(r"line A \n line B")



#pthon as a calculator:
print(28+4)
print(4-3)
print(3*6)
print(4/3)#float division
print(4//3)#integer divsion
print(2**3**4)#precedence:right to left


#variables;
name = "bikash"
print(name)


#naming rules:
#1name = "bikash" #error
#name1 = "bikash" #no error
#name$ = "bkash"  #eror
# $name = 123   #error




# convention for variable naming
user_one = "Hari " #snake case writing
userOne = "Bikash" # camel case writing