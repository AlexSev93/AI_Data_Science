# z1
# s = 5+4+8+6
# p = (4+6)/s
# print(p)

# z2
# h = 25
# d = 4
# p = 1-(4/25)
# print(p)

# z3
# v = 8
# p = 1/v
# print(p)

# z4
# p8 = 0
# p23 = 0
# p2 = 0
#
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i * j == 8:
#             p8 += 1
#         if i * j >= 23:
#             p23 += 1
#         if i * j % 2 != 0:
#             p2 += 1
#
# print(p8/36, p23/36, p2/36)

# z5
# y = 11
# g = 7
#
#
# def fact(n):
#     answer = 1
#     for i in range(2, n + 1):
#         answer *= i
#     return answer
#
#
# # сочетание из n по m
# def Cnm(n, m):
#     return fact(n) / (fact(n - m) * fact(m))
#
#
# py = Cnm(11, 2) / Cnm(18, 2)
# pg = Cnm(7, 2) / Cnm(18, 2)
# p = py + pg
# print(p)
