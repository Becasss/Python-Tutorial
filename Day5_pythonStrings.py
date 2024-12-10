

# Strings : surrounded by either single quotes or double quotation marks. - "Hello" or 'Hello'.


# Assign String to a variable:
 #Example:
a = "Hello, world!"
print(a) # Output: Hello


# Multiline Strings:
b = """Lorem ipsum dolor sit amet, consectetur adip
elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 
ut aliquip ex ea commodo consequat."""
print(b)  
#Note: in the result, the line breaks are inserted at the same position as in the code. 



# Strings are arrays:
print(a[1])     # Output : world



# Looping through a string
# Example:
for x in "Banana":
    print(x)

# String Length
print(len(b)) # Output :226


# Check String
txt = "The best thigns in life are free"
print("free" in txt) # Output : True

if "free" in txt:
    print("Yes, Free is in txt") # Output : False
else:
    print("No, Free is not in txt") # Output : True


# Check if NOT
text = "The best things in life are free"
print("expensive" not in txt) # Output : True

if "expensive" not in txt:
    print("Yes, Expensive is not in txt") # Output : True





# Python - Slicing Strings

c = "Hello, world!"
print(c[2:5]) # Output : llo


# Slice from the start:
print(c[:5]) # Output : Hello

# Slice from the end:
print(c[2:]) # Output : llo, world


# Negative indexing
print(c[-5:-2]) # Output : orl



# Python - Modify Strings

d = "  Hello, Bikash Yamphu Rai" # Upper Case - upper()
print(d.upper()) # Output : HELLO, BIKASH YAMPHU RAI

print(d.lower()) # Output : hello, bikash yamphu rai -- lower case - lower()


# Remove Whitespace - strip() method

print(d.strip()) # Output : Hello, BIkash Yamphu Rai



# Replace String - replace() method

print(d.replace("H", "A"))

