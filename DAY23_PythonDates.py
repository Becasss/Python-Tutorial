
# Python Dates - we can import a module named datetime to work with dates as date objects.


# Example: Import the datetime module and display the current date.
import datetime

x = datetime.datetime.now()

print(x)



# example: Return the year and name of weekday

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
