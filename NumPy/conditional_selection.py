import numpy as np

arr = np.arange(0,11)

# see which elements are greater than 5
bool_array = arr > 5

#use returned array of booleans to select elements from original array
print(arr[bool_array])

#shorthand

print(arr[arr > 5])

arr_2d = np.arange(50).reshape(5,10)

print(arr_2d[2:, 6:)
