import numpy as np
import pandas as pd

d = {"A": [1, 2, np.nan], "B": [5, np.nan, np.nan], "C": [1, 2, 3]}
df = pd.DataFrame(d)

print(df)

# drop missing values

# drop row with one or more missing value
dropped = df.dropna()

print(dropped)

# drop columns

dropped_two = df.dropna(axis=1)
print(dropped_two)

# set threshold(number of non NaN values required)

dropped_three = df.dropna(thresh=2)
print(dropped_three)

# fill missing values

filled = df.fillna(value="FILL VALUE")
print(filled)
