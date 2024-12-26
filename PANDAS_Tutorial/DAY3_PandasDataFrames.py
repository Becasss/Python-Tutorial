
# What is a DataFrame? - A pandas DataFrame is a 2 dimensional data structure, like a 2 dimesional array, or a table with rows and columns.



# Example: Create a simple Pandas DataFrame

import pandas as pd
data = {
    'calories': [230, 100, 490],
    'duration': [50,30, 45]
}


# load data infot a DataFrame object:
df = pd.DataFrame(data)

print(df)
print(df.loc[0])        # loc attribute - refer to the row index.



print(df.loc[[0,1]])        # use a list of indexes.


# Note : When using [] , the result is a pandas DataFrame.






# Named Indexes: With the index argument, you can name your own indexes.

# Example: Add a list of names to give each row and a name:

import pandas as pd

data = {
    'calories': [230, 100, 490],
    'duration': [50,30, 45]
}

df = pd.DataFrame(data, index = ['day1', 'day2', 'day3'])

print(df)