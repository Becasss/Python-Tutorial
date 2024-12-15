
# Python If...Else

# Python conditions and If statements
'''Equals : a == b
Not Equals : a != b
less than : a < b
less than or equal to : a <= b
greater than : a > b
greater than or equal to : a >= b
'''



# If statement: 
# Example:
a = 33
b = 200
if b > a:
    print("b is greater than a")



# Elif statement: if the previous conditions were not true, then try this condition.

z = 33
c = 33
if z > c:
    print("z is greater than c")
elif z == c:
    print("z and c are equal")



# Else Statement: catches anything which isn't caught by the preceding conditions.

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



# shorthand If - if you have only one statement to execute, you can put it on the same line as the if statement.
a = 200
b = 33
if a > b: print("a is greater than b")



# Short Hand if ... Else :
a = 200
b = 33
print("A") if a > b else print("B")
