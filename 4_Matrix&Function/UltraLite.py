import numpy as np

# z1
x = 10
y = np.random.randint(-5, 5, 5)

z_zinv = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
while True:
    z = np.random.randint(-5, 5, (3, 3))
    if np.linalg.det(z) != 0:
        z_inv = np.linalg.inv(z)
        if np.array_equal(z @ z_inv, z_zinv):
            print(z)
            print(z_inv)
            print(z@z_inv)
            break
# z2
# print(x+y)
# print(x*y)
# print(z/x)
# print(z+x)

# z3
# zt = z.T
# zi = np.linalg.inv(z)
# print(zt)
# print(zi)
# print(z @ zi)
