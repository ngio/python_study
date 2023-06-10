""" Pandas Tutorial
https://www.w3schools.com/python/pandas/default.asp

Pandas is a Python library.
Pandas is used to analyze data.
"""

#import pandas
import pandas as pd #Now the Pandas package can be referred to as pd instead of pandas.


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)


import pandas as pd
print(pd.__version__)
