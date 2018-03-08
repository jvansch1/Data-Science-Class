import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = { 'a': 10, 'b': 20, 'c': 30 }

series = pd.Series(data = my_data)

print(series)

labeled_series = pd.Series(my_data, labels)
# labeled_series = pd.Series(d)

print(labeled_series)

ser1 = pd.Series([1,2,3,4], ["USA", "Germany", "USSR", "Japan"])
print(ser1)
ser2 = pd.Series([1,2,5,4], ["USA", "Germany", "Italy", "Japan"])

ser3 = ser1 + ser2


# Adds two series together
# If it cannot find a key in both series it will insert NaN 
print(ser3)
