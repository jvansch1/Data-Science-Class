import numpy as np

zero_array = np.zeros(10)

print(zero_array)

one_array = np.ones(10)

print(one_array)

five_array = np.full(10, 5)

print(five_array)

evens = np.arange(10,51,2)

print(evens)

matrix = np.arange(0,9).reshape((3,3))

print(matrix)

matrix_id = np.identity(3)

print(matrix_id)

linear = np.linspace(0,1,20)

print(linear)

original = np.arange(1,26).reshape(5,5)

solution_one = original[2:, 1:]

print(solution_one)

solution_two = original[3][4]

print(solution_two)

solution_three = original[0:3, 1:2]
print(solution_three)

solution_four = original[4]

print(solution_four)

solution_five = original[3:]

print(solution_five)

mat_sum = original.sum()

print(mat_sum)

mat_std_dev = np.std(original)

print(mat_std_dev)

column_sum = original.sum(axis=0)

print(column_sum)
