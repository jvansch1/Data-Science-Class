import numpy as np
import pandas as pd
from numpy.random import randn

outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
heir_index = list(zip(outside, inside))
heir_index = pd.MultiIndex.from_tuples(heir_index)

print(heir_index)

df = pd.DataFrame(randn(6, 2), heir_index, ["A", "B"])
print(df)

value = df.loc["G1"].loc[1].loc["A"]
print(value)

# give indices names

named = df.index.names = ["Groups", "Num"]
print(df)

# Cross section of dataFrame

# Return index 1 and at level Num for each Group
cross = df.xs(1, level="Num")

print(cross)
