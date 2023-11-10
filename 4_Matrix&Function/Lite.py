import numpy as np

# z1
a1 = np.random.randint(-5, 5, (2, 2))
a2 = np.random.randint(-5, 5, (2, 2))
a3 = np.random.randint(-5, 5, (2, 2))

answer = np.zeros((2, 2))
for i in range(a1.shape[1]):
    for j in range(a2.shape[0]):
        answer[i, j] = np.sum(a1[i] * a2[:, j])

# z2
# def max_min(matrix):
#     return np.max(matrix)-np.min(matrix)
#
# print(max_min(a1))

# z3
# def z3(matrix):
#     return matrix @ matrix.T, np.linalg.inv(matrix @ matrix.T)
#
# print(z3(a1))