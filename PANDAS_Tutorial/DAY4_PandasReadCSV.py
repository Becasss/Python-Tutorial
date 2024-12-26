
# Read CSV files: way to store big data sets is to use CSV fiels( comma separated files).



# Example : Load the CSV into a DataFrame:
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())   # Tip: Use to_string() to print the entire DataFrame.

print(df)  # IF you have a large DataFrame with many rows, Pandas will only return the first 5 rows and the last 5 columns.



# max_rows - pd.options.display.max_rows statement.

import pandas as pd
print(pd.options.display.max_rows)    # Output : 60




# Example: Increase the maximum number of rows to display the entire DataFrame:

import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)