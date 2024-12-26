
# What is a series?  - A pandas series is like a column in a table, is a one-dimensional array holding data of any type.



# Example: Create a simple Pandas series from a list.
import pandas as pd
a = [1, 2, 3, 4, 5]
myvar = pd.Series(a)
print(myvar) 



# Labels
# Example: Return the first value of the series:
print(myvar[0])  # Output: 1



# Create labels - with index argument, you can name your own labels.

# Example: create your own labels:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


print(myvar['x']) # Output:1

# Note: WHen you have created labels, you  can access an item by referring to the label.




