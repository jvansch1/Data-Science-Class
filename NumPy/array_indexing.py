import numpy as np

arr = np.arange(0,11)

# broadcast value to selected elements
arr[0:5] = 100

print(arr)

new_array = np.arange(0,11)


# change all values
slice_of_arr = new_array[0:6]
slice_of_arr[:] = 99
print(slice_of_arr)

# specify copy

original_array = np.arange(1,11)
copy = original_array.copy()

copy[0:3] = 1000

print(original_array)
print(copy)

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])

#single bracket

single_bracket_index = arr_2d[1,2]
double_bracket_index = arr_2d[1][2]

print(arr_2d)
print(single_bracket_index)
print(double_bracket_index)

# get certain_section_of_matrix

# get all rows up to and not including 2
# get all colums from 1 until end
matrix_segment = arr_2d[:2, 1:]

print(matrix_segment)

other_matrix_segment = arr_2d[1:, 0:1]

print(other_matrix_segment)
