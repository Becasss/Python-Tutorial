
# Viewing The Data: One of the most used method for gettng a quick overview of the DataFrame, is the head() method.

# head() method returns the headers and a specified number of rows, starting form the top.



# Example: Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))



# Example: Print the first 5 rows of the DataFrame:

import pandas as pd
df = pd.read_csv('data.csv')

print(df.head())




# 