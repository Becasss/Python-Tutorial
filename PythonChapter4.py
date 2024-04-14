#  # functions:
# # name = "Bikash"
# # print(len(name))


# #Basic of Functions:

# # def add_two(a, b):
#     # return a+b

# # total = add_two(5,4)
# # print(total)

# # print(add_two(4,6))



# # a = int(input("enter the first number: "))
# # b = int(input("enter the second number: "))
# # total = add_two(a, b)
# # print(total)




# # first_name = input("enter your name: ")
# # last_name = input("enter your name: ")
# # print(add_two(first_name, last_name))



# # return vs print


# #-------------------------------- return--------------
# # def add_three(a, b, c):
# #     return a+b+c

# # print(add_three(5,5,5))



# # ---------------------------------print--------------
# def add_three(a,b,c):
#     print(a+b+c)

# add_three(5,5,5)





# # functions practice:
# def last_char(name):
#     return name[-1]

# print(last_char("BIkash"))
# # print(last_char(8))   # error





# # def odd_even(num):

# #     if num%2 ==0:
# #         return "even"
# #     else:
# #         return "odd"
    
# # print(odd_even(9))



# # next way calculation:

# def even_odd(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"


# print(even_odd(10))






# def is_even(num):
#     if num%2 == 0:
#         return True
#     return False

# print(is_even(9))




# def is_even(num):# (parameter)
#     return num%2 == 0
# print(is_even(10))# (argument)







# def song():
#     return "Happy birthday song"

# print(song())







# # exercise1----------chapter4---------------
# # define a function which takes two numbers as a input and return greater of two numbers.
# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# num1 = int(input("eter the first number:"))
# num2 = int(input("enter the second number"))
# bigger = greater(num1, num2)


# print(f"{bigger} is greater")







# def greates(a,b,c):  # parameter == (a,b,c)
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c


# num1 = int(input("enter the first number:"))
# num2 = int(input("enter the second number:"))
# num3 = int(input("enter the third number"))
# greatest = greates(num1, num2, num3)
# print(f"{greatest} is the greast")








# # Function inside function:
# # greater(a,b)------>a or b 
# # greater(a or b, c)----------> greatest


# def new_greatest(a,b,c):
#     bigger = greater(a,b)  # retrun (greater(a,b), c))
#     return greater(bigger,c)
# print(new_greatest(100,20,490))



# # kiss - keep it simple stupid





# #  define is_palindrome function that take one word in string as input 
# # and return True if it is palindrome else return False


# # palindrome  - word that reads same backwards as forwards


# # examle
# # is_palindrome ("madam") -------------------> True
# # is_palindrome("naman")---------------------> True
# # is_palindrome("horse")---------------------> False



# # logic (algorithm)
# # step 1 -> reverse the string
# # step2-> compare reversed string with original string



# def is_palindrome(word):
#     reversed_word = word[::-1]   # if word == word[::-1]
#     if word == reversed_word:     #     return True
#         return True               # return False 
#     else:
#         return False
    
# print(is_palindrome("naman"))
# print(is_palindrome("horse"))



# # shortest way to do palindrome:

# # def is_palindrome(word):
#     # return word == word[::-1]




# # fibonacci series:
# # 0 1 1 2 3 5 8 13 21 34



# # 1 -------->  0
# # 2 ---------> 0 1
# # 3 ---------> 0 1 1



# # for i in range(1,11):
#     # print(i, end = "")



# def fibonacci_seq(n):
#     a = 0 
#     b = 1
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a, b)
#     else:
#         print(a, b, end = " ")
#         for i in range(n-2):
#             c = a + b # c = 1
#             a = b     # a = 1
#             b = c     # b = 1
#             print(b, end = " ")


# fibonacci_seq(10)










# # default parameters :
# def user_info(first_name, last_name, age= 24):
#     print(f"Your first name is {first_name}")
#     print(f"Yoour last name is {last_name}")
#     print(f"your age is {age}")


# user_info("Harsit", "Rai", 23)








# # scope:

x = 5           # global varaible
def fun():
    x = 7        # local variables
    return x
print(x)
print(fun())
print(x)