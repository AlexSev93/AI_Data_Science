import numpy as np

# z1
my_array = np.loadtxt('iris.csv', delimiter=',', dtype=np.float32)
my_gen_array = np.random.randint(-5, 5, my_array.shape)

# z2
# multiply = np.array(my_gen_array*my_array)
# stack = np.vstack((my_array, my_gen_array))
# print(stack)
# concat = np.concatenate((my_array, my_gen_array), axis=0)
# print(concat)
# split = np.vsplit(stack, 4)
# print(split)
# print(type(split)) # list
# print(len(split))

# z3
# answer = my_array[(my_array > 3) & (my_array < 5)]
# print(answer)

# z4
array_4 = np.random.uniform(15, 37, (2, 3, 4))
print(array_4)

# z5 Как 3
array_5 = np.full((2, 3, 4), 'small', dtype='U10')
array_5[(array_4 > 20) & (array_4 < 30)] = 'medium'
array_5[array_4 > 30] = 'large'
print(array_5)
