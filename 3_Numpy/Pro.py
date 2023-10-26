import numpy as np

#z1
my_array = np.loadtxt('iris.csv', delimiter=',', dtype=np.float32)
my_gen_array = np.random.randint(-5, 5, my_array.shape)

#z2
# multiply = np.array([my_gen_array[i]*my_array[i]
#                      for i in range(my_array.shape[0])])
# stack = np.vstack((my_array, my_gen_array))
# print(stack)
# concat = np.concatenate((my_array, my_gen_array), axis=0)
# print(concat)
# split = np.vsplit(stack, 4)
# print(split)
# print(type(split)) # list
# print(len(split))

#z3