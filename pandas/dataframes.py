import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

# Make a dataFrame with 5 rows and 4 columns, ABCDE are row headers,
# WXYZ are column headers
# Each column is its own series
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])

# get one series
print(df["W"])

# get multiple series
print(df[["W", "Z"]])

# create new column

df["new"] = df["W"] + df["Y"]
print(df)

# remove a column
# if you do not include inplace, then it will not mutate unless saved
# to a new variable
df.drop('new', 1, inplace=True)

print(df)

# drop column
df.drop('E', inplace=True)

print(df)

# select row

row = df.loc['A']
print(row)

# method 2 to grab row

row2 = df.iloc[0]
print(row2)

# get single value(similar to getting element from nested array)

value = df.loc["B", "Y"]
print(value)

# get multiple values

values = df.loc[["A", "B"], ["W", "Y"]]
print(values)
