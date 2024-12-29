
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
