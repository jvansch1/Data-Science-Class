import numpy as np

my_list = [1,2,3]

np_list = np.array(my_list)

print(np_list)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]

matrix = np.array(my_mat)

print(matrix)


# start, send, step
my_range = np.arange(1,10, 2)

print(my_range)

#create array/matrix of zeros

zero_array = np.zeros(3)

zero_matrix = np.zeros((2,3))

print(zero_array)
print(zero_matrix)

ones_array = np.ones(4)

print(ones_array)


#start, stop, number
# evenly spaced numbers bewteen start and stop
result = np.linspace(0,5,1000)

print(result)

#create identity_matrix

id_matrix = np.eye(4)

print(id_matrix)

#random number_arrays

random_array = np.random.rand(4)

print(random_array)

random_matrix = np.random.rand(5,6)

print(random_matrix)

#standard normal distribution around 0

rand_around_zero = np.random.randn(5)
print(rand_around_zero)

# create array of random ints
#low, high, number of integers(only 1 if excluded)
int_array = np.random.randint(1,100, 5)

print(int_array)

arr = np.arange(25)

ranarr = np.random.randint(0,50,10)

reshaped = arr.reshape(5,5)

print(reshaped)
