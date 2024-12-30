
# Pandas - Cleaning Data of wrong Format


# Data of Wrong Format - Cells with data of wrong format can make it difficult, or even impossible to analyze data.

# To fix it, you have to options: remove the rows, or convert all cells in the columns into the same format.


# Example: Convert to date - Pandas has a to_dateime() method for this.

import pandas as pd
df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())
