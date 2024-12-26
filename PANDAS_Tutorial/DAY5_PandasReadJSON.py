
# Read JSON - Big data sets often stored, or extracted as JSON.

import pandas as pd
df = pd.read_json('data.json')

print(df.to_string())     # use to_string() to print the entire DataFrame.





# Dictionary as JSON : JSON = Python Dictionary - JSON objects have the same format as Python Dictionaries.


#Example : Load a Python Dictionary into a DataFrame

import pandas as pd

data = {
    "Duaration": {
        'O' : 50,
        'A' : 30,
        'B' : 45,
        'C' : 40
        'D' : 50
    },
    "Calories": {
        'O' : 230,
        'A' : 100,
        'B' : 490,
        'C' : 400,
        'D' : 230
        },
        "Protein": {
        'O' : 30,
        'A' : 20,
        'B' : 40,
        'C' : 50,
        },
    "Carbohydrates": {
        'O' : 10,
        'A' : 5,
        'B' : 30,
        'C' : 40,
        'D' : 10
    },
    "Fats": {
        'O' : 10,
        'A' : 5,
        'B' : 15,
        'C' : 20,
        'D' : 10
    }
}


df = pd.DataFrame(data)

print(df)