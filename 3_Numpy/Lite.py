import numpy as np

# z1
# my_array = np.loadtxt('train_vector_1.csv')
# print(type(my_array))

# z2
# def mean(array):
#     s = 0
#     for i in array:
#         s += i
#     return s/len(array)
#
#
# print(mean(my_array))
# print(mean(list(my_array)))

# z3
# my_array2 = np.loadtxt('iris.csv', delimiter=',')
# for i in range(my_array2.shape[1]):
#     print(sum(my_array2[:,i]))


# 4
# my_array3 = np.random.randint(11, 40, (3, 3))
# print(my_array3)
# print(my_array3[my_array3 < 20])
# print(my_array3.sum())

# 5
a = ('aaa', 23, 4.4)
b = ('bbb', 15, 5.7)
c = ('ccc', 22, 11.3)
dt = np.dtype([('name', 'U5'), ('age', int), ('mean', float)])
my_array5 = np.array([c,a,b], dtype=dt)
print(my_array5)
# print(np.sort(my_array5, order='age'))


for val in my_array5:
    val[1] = 10
print(my_array5)
# print(np.sort(my_array5, order='name'))