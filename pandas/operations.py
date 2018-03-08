import numpy as np
import pandas as pd

df = pd.DataFrame({
    "col1": [1, 2, 3, 4],
    "col2": [444, 555, 666, 444],
    "col3": ["abc", "def", "ghi", "xyz"]
})

# unique values

unique_in_column = df["col2"].unique()
print(unique_in_column)

# unique and occurences

occurences = df["col2"].value_counts()
print(occurences)

# conditional selection

selected = df[df["col1"] > 2]
print(selected)

# apply custom function


def times_two(x):
    return x * 2


selected_two = df["col1"].apply(times_two)
print(selected_two)


# use lambda

selected_three = df["col2"].apply(lambda x: x * 2)
print(selected_three)

# get column names

columns = df.columns

print(columns)

# get indices

index = df.index
print(index)

# sort

sort = df.sort_values("col2")
print(sort)

# Check if values are null
# will return a new dataFrame with bool values

is_null = df.isnull()
print(is_null)

# pivot table

data_two = {
    'A': ["foo", "foo", "foo", "bar", "bar", "bar"],
    "B": ["one", "one", "two", "two", "one", "one"],
    "C": ["x", "y", "x", "y", "x", "y"],
    "D": [1, 3, 2, 5, 4, 1]
}

df = pd.DataFrame(data_two)
pivot_table = df.pivot_table(values="D", index=["A", "B"], columns="C")
print(pivot_table)
