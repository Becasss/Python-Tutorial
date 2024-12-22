
# Python String Formatting 

# F - strings 

# Example : Create an f-string:
txt = f"The price is 49 dollars."
print(txt)



# Placeholders and modifiers - to format values in an f-string, add placeholders{}, a placeholder can contain variables,
# operators, functions and modifiers to format the values.


# Example: Add a placeholder for the price variable:
price = 49
txt = f"The price is {price} dollars."
print(txt)


# Example : Display the price with 2 decimals:

price = 59
txt = f"The prics is {price:.2f} dollars."
print(txt)  # Output : The price is 59.00 dollars.



# Perform Operations in F - strings.

# Example: Perform a math operation in the placeholders and return the result.

txt = f"The price is {20 * 39} dollars."
print(txt)  # Output : The price is 780 dollars.


# Example: Add taxes before displaying the price.

price = 59
tax = 0.25
txt = f"the price is {price * tax} dollars."
print(txt)  # Output : the price is 14.75 dollars.


# You can if...else statements insdie the placeholders.
# Return "Expensive" if the price is over 50, otherwise return "Cheap:
price = 49
txt  = f"It is very {"Expensive" if price > 50 else "cheap"}."

print(txt)