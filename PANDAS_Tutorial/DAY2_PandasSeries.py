
# What is a series?  - A pandas series is like a column in a table, is a one-dimensional array holding data of any type.



# Example: Create a simple Pandas series from a list.
import pandas as pd
a = [1, 2, 3, 4, 5]
myvar = pd.Series(a)
print(myvar) 



# Labels
# Example: Return the first value of the series:
print(myvar[0])  # Output: 1