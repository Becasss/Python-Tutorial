
# Python RegEx(Regular Expression) - is a sequence of characters that forms a search pattern.


# RegEx Module - built-in package called re, which can be used to work with Regular Expressons.

# Example : Import re module - import re


# RegEx in Python 
# Example: Search the string to see if it starts with "THE" and ends with "Spain":

import re

# check if the string starts with "The" and ends with "Spain"

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x: 
    print("YES! The string starts with 'The' and ends with 'Spain'")
else:
    print("No match")





# The findall() function - returns a list containing all matches.

# Example: Print a list of all matches.
import re

txt = "THe rain in Spain"
x = re.findall("ai", txt)
print(x)        # Output: ['ai', 'ai']

