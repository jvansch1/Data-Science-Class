import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)

# conditional selection
# will return booleans in place of data values
# where the condition is true
greater_than_zero = df > 0

print(greater_than_zero)

#get NaN where false and values where true
print(df[greater_than_zero])

# in one step

print(df[df > 0])

# select certain rows or columns


# grab column W and then for each value see if greater than zero
selected = df["W"] > 0

print(selected)

filtered = df[df["W"] > 0]

print(filtered)

# grab all rows in dataFrame where z < 0 and then get column X and Y

filtered_two = df[df["Z"] < 0][["X", 'Y']]
print(filtered_two)

# multiple conditions
# W > 0 and Y > 1
# Have to use ampersand instead of and/ | instead of or
# Must put conditions in parenthesis
multiple = df[(df["W"] > 0) & (df["Y"] > 1)]
print(multiple)

# reset indices to numerical value
# old index becomes column

indices = df.reset_index()

print(indices)

newind = "CA NY WY OR CO".split()

df["States"] = newind

print(df)

# Set column to be index

new_col_two = df.set_index("States")
print(new_col_two)
