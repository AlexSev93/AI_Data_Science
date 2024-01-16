import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm

# z1
# d = 0.5
# u = uniform(0, d)
# p1 = uniform(0, d).cdf(0.02)
# p2 = 1-uniform(0, d).cdf(d-0.02)
# print(p1+p2)
# print(p1*2)
#
# vars = np.linspace(-1, 1, 1000)
# prob_u = u.pdf(vars)
#
# plt.plot(vars, prob_u)
# plt.axvline(x=0.02)
# plt.axvline(x=d-0.02)
# plt.show()

# z2
# norm_1 = np.random.normal(loc=4, scale=1, size=10)
# norm_2 = np.random.normal(loc=4, scale=3, size=100)
# norm_3 = np.random.normal(loc=4, scale=10, size=1000)
# print(np.mean(norm_1))
# print(np.mean(norm_2))
# print(np.mean(norm_3))

# z3
# n_array = norm(14, 3)
# mean, var = n_array.stats(moments='mv')
# print(mean, var)
# print(n_array.ppf(0.5))
# print(n_array.ppf(0.9))

# z4
# n = 1.5
# s = 0.7
# n_array = norm(n, s)
# vars = np.linspace(n-3*s, n+3*s, 1000)
# prob_norm = n_array.pdf(vars)
#
# plt.figure(figsize=(4, 4))
# plt.subplot(211)
# plt.plot(vars, prob_norm)
#
# plt.subplot(212)
# prob_norm2 = n_array.cdf(vars)
# plt.plot(vars, prob_norm2)
# plt.show()

# z5
# p = 0.7
# q = 1-p
#
# Ppp = p*p
# Pqq = q*q
# Pqp = 1 - Ppp-Pqq
# P = [Pqp, Pqq, Ppp]
# P.sort()
# W = {i: P[i] for i in range(len(P))}
# print(W)

