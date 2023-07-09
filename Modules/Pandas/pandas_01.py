import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # install : pip install matplotlib

# https://sdc-james.gitbook.io/onebook/4.-numpy-and-scipy/4.4-pandas/4.4.1-pandas

dict = {'a':1,'b':2,'c':3,'d':4}
data = [1, 3, 5, 7, 9]
u = pd.Series(dict)
print(u)
s = pd.Series(data)
print(s)

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

print(pd.__version__ )
 
"""
    error : Cannot interpret '<attribute 'dtype' of 'numpy.generic' objects>' as a data type 
    발생하면  pandas를 업그레이드 하라. 
""" 

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20190102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)


dates = pd.date_range('20190101', periods=6)  
    
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))  
   
print(df)  
print(df.head())  
print(df.tail(3))  
print(df.index)  
print(df.columns)  
print(df.values)  
print(df.describe())  
print(df.T)  
print(df.sort_index(axis=1, ascending=False))  
print(df.sort_values(by='B'))  
print(df['A'])  
print(df[0:3])  
print(df.loc[dates[0]])  
print(df.iloc[3:5, 0:2])  
print(df[df.A > 0])  
print(df.mean())  
print(df.apply(np.cumsum)) 

 
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')  
  
ts = pd.Series(np.random.randn(len(prng)), prng)  
  
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9  
  
print(ts.head())  
 
 
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))  
ts = ts.cumsum()  
ts.plot()  
plt.show()  
 


