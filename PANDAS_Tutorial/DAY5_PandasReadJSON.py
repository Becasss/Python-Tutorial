
# Read JSON - Big data sets often stored, or extracted as JSON.

import pandas as pd
df = pd.read_json('data.json')

print(df.to_string())     # use to_string() to print the entire DataFrame.
