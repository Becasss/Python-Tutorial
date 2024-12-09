# # # # # # # # If Statement:
# # # # # # # # syntax
# # # # # # # # if condition: 
# # # # # # #     # code if condition is true then this code will execute
# # # # # # #     # code

# # # # # # # age = input("Enter your age:")
# # # # # # # age = int(age)
# # # # # # # if age >= 14:
# # # # # # #     print("You are above 14.")
# # # # # # # else:
# # # # # # #     print("Your are still small boy.")






# # # # # # # # pass statement:
# # # # # # # x = 18
# # # # # # # if x > 18:
# # # # # # #     pass







# # # # # # # # Exercise , Number guessing game:
# # # # # # # # make a variable, like winning_number and assign any number to it.
# # # # # # # # ask user to guess a number. 
# # # # # # # # if user guessed correctly then print "You win!!!"
# # # # # # # # if user didn't guessed correctly then: 
# # # # # # #     #if user guessed lower than acutal number then print "Too low"
# # # # # # #     # if user guessed higher than acutal number then print "too high"

# # # # # # # # google "how to generate random number in python " to generate random "
# # # # # # # # winning number
# # # # # # # winning_number = 24
# # # # # # # user_input = input("Guess a number between 1 to 100")
# # # # # # # user_input = int(user_input)
# # # # # # # if user_input == winning_number:
# # # # # # #     print("You win!")
# # # # # # # else:
# # # # # # #     if user_input > winning_number:
# # # # # # #         print("to high")
# # # # # # #     else:
# # # # # # #         print("too low")




# # # # # # # # and , or operator:
# # # # # # # # check two conditions at same time:
# # # # # # # # name = "bikash"
# # # # # # # # age = 16
# # # # # # # # if name == "bikash" and age == 123:
# # # # # # # #     print("condtion true")
# # # # # # # # else:
# # # # # # # #     print("condition FAlse")
# # # # # # # # in "and" operator both condition should be true otherwise it will gives false condition.


# # # # # # # # city = "kathmandu"
# # # # # # # # word_no = 12
# # # # # # # # if city == "kathmandu" or word_no == 11:
# # # # # # # #     print("Condition true")
# # # # # # # # else:
# # # # # # # #     print("condition false")







# # # # # # # # exercisse - watch coco
# # # # # # # # ask user's name and age if user's name start with ('a' or "A" ) and age is above 10 then
# # # # # # # # print 'you can watch coco movie'
# # # # # # # # else print "sorry, you cannot watch coco


# # # # # # # # name, aage = input("enter your name and age").split(",")
# # # # # # # # aage = int(aage)
# # # # # # # # if (name[0] == "a" or name[0]== 'A') and aage >= 10:
# # # # # # # #     print("you can watch coco movie")
# # # # # # # # else:
# # # # # # # #     print("sorry you cannot watch coco")


# # # # # # # user_name = input("enter your name please: ")
# # # # # # # user_age = input("enter your age please: ")
# # # # # # # user_age = int(user_age)
# # # # # # # if user_age >= 10 and (user_name[0]=="a" or user_name[0] == "A"):
# # # # # # #     print("you can watch coco")
# # # # # # # else:
# # # # # # #     print("Youu cannt watch coco")






# # # # # # # # if elif else statement:

# # # # # # # # user_age = input('enter your age: ')
# # # # # # # # user_age = int(user_age)
# # # # # # # # if 0<user_age<=3:
# # # # # # # #     print("Tiket price: free")
# # # # # # # # elif 3<user_age<=10:
# # # # # # # #     print("Tiket price:150")
# # # # # # # # elif 10<user_age<=60:
# # # # # # # #     print("ticket price: RS.250")
# # # # # # # # else:
# # # # # # # #     print("ticket price: 200")





# # # # # # # # then_in keyword:
# # # # # # # name = "BIkash"
# # # # # # # # in keyword
# # # # # # # # if with in
# # # # # # # if 'a' in name:
# # # # # # #     print("a is presnet in name")
# # # # # # # else:
# # # # # # #     print('not present')





# # # # # # # # check empty or not:
# # # # # # #  important

# # # # # # # name = "abc"
# # # # # # # if name: # true if string is not empty.
# # # # # # #       print("string is not empty")
# # # # # # # else:
# # # # # # #       print("String is empty")


# # # # # # # name = input("enter your name:")
# # # # # # # if name:
# # # # # # #     print(f"Your name is {name}")
# # # # # # # else:
# # # # # # #     print("you didn't type anything.")





# # # # # # # loops 
# # # # # # # while loop, for loop
# # # # # # i = 1
# # # # # # while i<=10:
# # # # # #     print(f"helo world {i}")
# # # # # #     i += 1




# # # # # # # sum : 1 to 10 (or any numer)

# # # # # # total = 0
# # # # # # i = 1
# # # # # # while i <= 10:
# # # # # #     total += i
# # # # # #     i += 1  
# # # # # # print(total)  




# # # # # # # exercise:
# # # # # # # sum of n natural numbers
# # # # # # # ask a user for natural number(n)
# # # # # # # print total from 1 t n

# # # # # # n = input("enter a natural number:")
# # # # # # n = int(n)
# # # # # # total = 0
# # # # # # i = 1
# # # # # # while i <= n:
# # # # # #     total += i
# # # # # #     i += 1
# # # # # # print(f" the total natural number is {total}")



# # # # # # problem:
# # # # # # ask user to input a number containing more than one digit
# # # # # # example - 1256
# # # # # # calculate 1+2+5+6 and print


# # # # # n = input("enter a number containing more than one digit: ")
# # # # # total = 0
# # # # # i = 0
# # # # # while i < len(n):
# # # # #     total += int(n[i])
# # # # #     i += 1
# # # # # print(total)






# # # # # # exercise:
# # # # # # example -Bikash Yamphu Rai
# # # # # # print count of each words:
# # # # # # output:
# # # # #         # B : 1
# # # # #         # i : 2
# # # # #         # k : 1
# # # # #         # a : 3
# # # # #         # s : 1
# # # # #         # h : 2
# # # # #         # Y : 1
# # # # #         # m : 1
# # # # #         # p : 1
# # # # #         # h : 1
# # # # #         # u : 1


# # # # # name = input("Enter a user_name :")
# # # # # # harsit vashisth
# # # # # # name.count("h"), name.count(name[0]) =2
# # # # # # name.coutn("a"), name.count(name[1]) = 1
# # # # # # name.count("r"), name.count(name[2]) = 1
# # # # # # name.count("s"), name.count(name[3]) = 1 
# # # # # # nmae.count("h"), name.count(name[4]) = 2
# # # # # # name.count("i"), name.count(name[5]) = 1
# # # # # # name.count("t"), name.count(name[6]) = 1

# # # # # temp_var = ""
# # # # # i = 0
# # # # # while i < len(name):
# # # # #     if name[i] not in temp_var:
# # # # #         temp_var += name[i]
# # # # #         print(f"{name[i]}:{name.count(name[i])}")
# # # # #     i += 1




# # # # # # infinite loop

# # # # # # i = 0
# # # # # # while i  <= 10:
# # # # # #     print("hello world")










# # # # # # for loop with range functions:


# # # # for i in range(10):
# # # #     print("hello world")
# # # #     print(f"hellow world: {i}")


# # # # for i in range(1,15):
# # # #     print(f"Hi bikash rai: {i}")






# # # # # sum from 1 to 10
# # # # # 1+2+3+4+.....+10

# # # # total = 0
# # # # for i in range(1, 11):
# # # #     total += i
# # # # print(total)




# # # # n = int(input("enter the number:"))
# # # # total = 0
# # # # for i in range(1,n+1):
# # # #     total += i
# # # # print(total)











# # # # practive for loop
# # # # ask user a number like 12345
# # # # calculate sum of digits --> 1 + 2 + 3 + 4 +

# # # # logic
# # # # num = "12345"  , length = 5
# # # # int(num[0])--->1
# # # # int(num[1])---->2
# # # # int(num[3])---->3
# # # # int(num[4])----->4
# # # # int(num[5])----->5
# # # # i -------> 0 to 4


# # # total = 0
# # # num = input("enter the number: ")
# # # for i in range(0,len(num)):
# # #     total += int(num[i])
# # # print(total)








# # # # practice for loop
# # # # ask for name and count each character
# # # # "Harsti vashisth"
# # # # H : 1
# # # # a : 1
# # # # r : 1
# # # # s : 1
# # # # h : 2




# # # name = input("enter your name:")
# # # temp =""
# # # for i in range(len(name)):
# # #     if name[i] not in temp:
# # #         print(f"{name[i]}: {name.count(name[i])}")
# # #         temp += name[i]








# # # # break and continue keywrod

# # # # 1 to 10 print
# # # for i in range(1,11):
# # #     if i == 5:
# # #         break
# # #     print(i)



# # # # continue keywrod:
# # # # print 1 to 10, but not 5

# # # for i in range(1,11):
# # #     if i == 5:
# # #         continue
# # #     print(i)





# # # # MODIFY NUMBER GUESSING GAME

# # # import random
# # # winning_number = random.randint(1,100)
# # # winning_number = 43
# # # guess = 1
# # # number = int(input("guess a number between 1 to 100"))
# # # game_over = False

# # # while not game_over:
# # #     if number == winning_number:
# # #         print("you win, and you guessed this number in {guess} times")
# # #         game_over = True
# # #     else:
# # #         if number <= winning_number:
# # #             print("too low")
# # #             guess += 1
# # #             number = int(input("guess again!"))
# # #         else:
# # #             print("too high")
# # #             guess += 1
# # #             number = int(input("Guess again!"))
# # #         





# # # DRY - don't repeat yourself

# # winning_number = 50
# # guess = 1
# # number = int(input("enter your number"))
# # game_over = False

# # while not game_over:
# #     if number == winning_number:
# #         print(f" you win and your guessed this number in {guess} times")
# #         game_over = True

# #     else:
# #         if number < winning_number:
# #             print("too low")
# #         else:
# #             print("too high")
# #         guess += 1
# #         number = int(input("guess again: "))








# # step argument:
# for i in range(1,11,2):
#     print(i)



# for i in range(10,1, -2):
#     print(i)








# # for_loop_ strings

# name = "bikash"
# for i in range(len(name)):
#     print(name[i])




# name = "BIkash"
# for i in name:      # only in python
#     print(i)



# num = input("enter a number:")
# total = 0
# for i in num:
#     total += int(i)
# print(total)







# summary:
# if statement
name = "sirjana" 
if name == "bikash" or name == "Bikash":
    print("Your are bikash")
elif name == "Sirjana" or name == "sirjana":
    print("you are sirjana")
else:
    print("You are not bikash")




# while loop
i = 0
while i < 10:
    print("heloo world")
    i += 1


# for loop:

for i in range(10):
    print(i)