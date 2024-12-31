
# Plotting - Pandas uses the plot() method to create diagrams.



# Example: Import pyplot form matplotlib and visualize our DataFrame.

import sys
import matplotlib
matplotlib.use('Agg'
               )
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()
plt.show()

# Two lines to make our compiler able to draw:

plt.savefig(sys.stdout.buffer)

sys.stdout.flush()

