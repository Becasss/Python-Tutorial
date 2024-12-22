
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


# Example: Return an empty list if no match was found.
import re
txt = "The rain in spain"
x = re.findall("Portugal", txt)
print(x)        # Output: []



# The Search() FUnction - searches the string for a match, and retuns a Match object if there is a match.

# Example: Search for the first white-space character in the string.
import re
txt = "THe rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:",x.start())


# Example: Make a search that returns no match.

import re
txt = "The rain in Spanish"

x = re.search("Portugal", txt)
print(x) # Output: []



# The Split() FUnction - returns a list where the string has been split at each match.

# Split at each white-space character
import re
txt = "The rain in spanish"
x = re.split("\s", txt)
print(x)        # Output: ['The', 'rain', 'in', 'spanish']



# Example: Splt the string only at the first occurrence.

import re

# split the string at the first white-space character

txt = "The rain in spanish"
x = re.split("\s", txt, 1)
print(x)



# THe sub() Function - replaces the matches with the text of your choice.

# Example: Replace every white-space character with the number 9.
import re

txt = "The rain in spanish"

x = re.sub("\s", "9", txt)
print(x)


# count parameter

# Example: replace the first 2 occurrences

import re
# Replace the first two occurrences of a white-space character with the digit 9.

txt = "The rain in spanish"
x = re.sub("\s", "9", txt, 2)

print(x)        #Output : The9rain9in Spanish



# Math Object - is an object containing information about the search and the result.

# Example: Do a search that will return a Math Object
import re

# The search () function returns a Match Object.

txt = "The rain in Spain"

x = re.search("ai", txt)
print(x)





# Example: .span() returns a tuple object the start-, and end positions of the match
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)

print(x.span())  # Output: (12, 17)




# .string returns the string passed into the fuction.

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)  # Output: The rain in Spain


# .group() returns a the part of the string where there was a match.

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Output: Spain





# Note : If there is no match, the value None is returned, instead of the Match Object.