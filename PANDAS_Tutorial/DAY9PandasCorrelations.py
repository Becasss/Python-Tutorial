
# Finding Relationship - corr() method calculates the relationship between each column in your data set.

# Show the relationship between the data set.

import pandas as pd
df = pd.read_csv('data.csv')

print(df.corr())
