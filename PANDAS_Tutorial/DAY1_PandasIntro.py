
'''Pandas is a Python library used for working with data sets.
 Pandas is used to analyze data.
 It has functions for analyzing, cleaning, exploring, and manipulating data.
 
 Data Science : is a branch of computer science where we study how to store, use and analyze data for deriving information form it.'''



# Installation of Pandas: install pandas


# Import Pandas: import pandas

# Example: 
import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [4, 5, 6]

}


myvar = pd.DataFrame(mydataset)

print(myvar)




# Pandas as pd : is usually imported under the pd alias.



# Checking Pandas Version: __version__  attribute

import pandas as pd
print(pd.__version__)