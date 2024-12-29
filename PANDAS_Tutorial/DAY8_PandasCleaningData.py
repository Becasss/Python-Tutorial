
# Pandas - Cleaning Data

# Data Cleaning - means fixing bad data in your data set and could be empty cells, data in wrong format, wrong data, duplicates.



# Pandas  - Cleaning Empty Cells - empty cells can potentially give you a wrong result when you analyze data.



# Remove Rows - one way to deal with empty cells is to remove rows that contain empty cells.


# Example : Return a new Data Frame with no empty cells.

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string()) 


# Notice in the result that some rows have been removed (row 18, 22, and 28).
# These rows had cells with empty values.

# Note: By default, the dropna() method returns a new DataFrame and will not change the original.



# Example: Remove all rows with NULL values:
import pandas as pd
df = pd.read_csv('data.csv')

df.dropna(inplace = True) 
print(df.to_string()) 

# Notice in the result that some rows have been removed (row 18, 22, and 28).
# These rows had cells with empty values.

# Note: Now,the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values form the original DataFrame.




# Replace Empty Values - fillna() method allows us to replace emtpy values with a value:


# Example: Replace NULL values with a number 130:

import pandas as pd
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df.to_string())

# Notice in the result: empty cells got the value 130 (in row 18, 22, and 28).




# Replace Only For specified Columns

# Example : Replace NULL values in the "Calories" column with the number 130:

import pandas as pd
df = pd.read_csv('data.csv')

df['Calories'].fillna(130, inplace = True)

print(df.to_string())

# This operation inserts 130 in emtpy cells in the "Calories" column (row 18 and 28).



# Replace Using Mean, Median and Mode

# Pandas uses the mean(), median() and mode() methods to calculate the respectie values for s specified columns.

# Example: Calculate Mean, and replace any empty values with it:
import pandas as pd
df = pd.read_csv('data.csv')

x = df['Calories'].mean()

df['Calories'].fillna(x, inplace=True)

print(df.to_string())


# As you can see in row 18 and 28, the empty values form "Calories" was replace with the mean: 304.68
# Mean = the average value (the sum of all values divided by number of values).


