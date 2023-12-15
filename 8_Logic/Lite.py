from combinatorica import (fact, Cnm,
                           Cnm_p, Per_p,
                           Rnm, Rnm_p)

# z1
print(fact(3))

# z2
print(3 * 3 * 2 * 1)

# z3
print(Cnm(36, 3))

# z4
print(23 * 22)

# z1
a = {2, 4, 6, 8, 10, 12}
b = {3, 6, 9, 12}
print(a & b)

# z2
a = {1, 6, 2, 7, 9, 3}
b = {1, 6, 2, 7, 9, 3}
print(a | b)

# z3
a = {2, 4, 6, 8, 10, 12}
b = {1, 3, 6, 9, 12}
print(a - b)

# z4
a = {1, 6, 2, 7, 9, 3}
b = {1, 6, 2, 7, 9, 3}
print(a & b)
