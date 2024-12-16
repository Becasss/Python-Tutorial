# Python While Loops: Python has two primitive loop commands - while loops and for loops


# While Loop: a set of statements as long as a condition is true.

# Example: 
i = 1
while i < 6:
    print(i)
    i += 1


# Break Statement: can stop loop even if the while condition is true.


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# Continue Statement: can stop the current iteration and continue with the next.

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# Else Statement: can run a block of code once when the condition no longer is true.

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("i is no longer less than 5")