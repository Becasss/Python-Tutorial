
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
