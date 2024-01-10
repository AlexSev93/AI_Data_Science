# z1
# p3 = 0.853
# q = 1-p3
# p = 1-q**(1/3)
# print(p)

# z2
# l1 = 64
# l2 = 63
# k = l1*l2
# p = l1*14/k
# print(p)

# z3
# p = 1/2
# q = 1-p
# p20 = p**20
# print(p20)
#
#
def fact(n):
    f = 1
    for x in range(1, n + 1):
        f *= x

    return f


# Сочетания
def C_n_m(n, m):
    return fact(n) / (fact(n - m) * fact(m))


#
# # формула бернули
# # Pn(k)=Cnk*p^k*(1-p)^(n-k)
# # n - количество испытаний, k - количество наступлений событий, Cnk - сочетание
# # p - вероятность наступления события при каждом испытании
# bern = 0
# for i in range(10, 21):
#     bern = bern + C_n_m(20, i)*p**i*q**(20-i)
# print(bern)

# z4
# Cnm = C_n_m(36, 5)
# k, t = C_n_m(4, 1), C_n_m(4, 1)
# other = C_n_m(28, 3)
# v = k*t*other
# print(Cnm, v)
# p = v/Cnm
# print(p)

# z5
# k = C_n_m(24, 2)
# gg = C_n_m(19, 2)
# bb = C_n_m(4, 2)
#
# bg = C_n_m(19,1)*C_n_m(4,1)
#
# pgg = gg / k
# pbb = bb / k
# pgb = bg / k
# print(pbb, pgb, pgg)
