import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm

# z1
# nu = 0
# sig = 4
# n_arr = norm(nu, sig)
# vars = np.linspace(nu-3*sig, nu+3*sig, 1000)
# prob = n_arr.pdf(vars)
#
# plt.plot(vars, prob)
# plt.axvline(x=6, color='red')
# plt.axvline(x=-6, color='red')
# plt.show()
#
# print(n_arr.cdf(6)- n_arr.cdf(-6))


# z2
# t = 5
# X = {i:i/5 for i in range(6)}
# print(X)
# uni = uniform(0, 5)
# p = uni.cdf(2)
# print(p)


# z3
# nu = 161
# sig = 4
# n_arr = norm(nu, sig)
# vars = np.linspace(nu-3*sig, nu+3*sig, 1000)
# prob = n_arr.pdf(vars)
#
# plt.plot(vars, prob)
# plt.axvline(x=152, color='red')
# plt.axvline(x=158, color='red')
# plt.show()
#
# print(n_arr.cdf(158) - n_arr.cdf(152))

# z4
# nu = 100
# sig = 12
# n_arr = norm(nu, sig)
# vars = np.linspace(nu-3*sig, nu+3*sig, 1000)
# prob = n_arr.pdf(vars)
#
# plt.plot(vars, prob)
# plt.axvline(x=20, color='red')
# plt.axvline(x=30, color='red')
# plt.show()
#
# print(n_arr.cdf(30) - n_arr.cdf(20))

# nu = round(nu/7)
# sig = round(sig/7)
# print(nu, sig)
# n_arr = norm(nu, sig)
# vars = np.linspace(nu-3*sig, nu+3*sig, 1000)
# prob = n_arr.pdf(vars)
#
# plt.plot(vars, prob)
# plt.axvline(x=1, color='red')
# plt.axvline(x=0, color='red')
# plt.show()
#
# print(1 - n_arr.cdf(1))

# z5
dist_list = [] # пустой лист, куда запишется распределение с нужными параметрами

#1
mu = 0
sigm = 4
norm_ = norm(mu,sigm)
dist_list.append(norm_)
#2
unif = uniform(loc=0,scale=5)
dist_list.append(unif)
#З
mu = 161
sigm = 4
norm_ = norm(mu,sigm)
dist_list.append(norm_)
#4a
mu = 100
std = 12
gaus1 = norm(mu, std)
dist_list.append(gaus1)
#4б
mu = 100/7
std /= 7
gaus2 = norm(mu, std)
dist_list.append(gaus2)


def dist_moments(dist_):
  mean, var,_,_ = dist_.stats(moments='mvsk')
  print("Среднее: {}".format(mean))
  print("Вариация: {}".format(var))
  print("Квантиль 0.25: {}".format(dist_.ppf(0.25)))
  print("Квантиль 0.9: {}".format(dist_.ppf(0.9)))


# Теперь проходимся циклом по всем распределениям
for i,d in enumerate(dist_list):
  print(f'Для Задачи: {i+1}')
  dist_moments(d)
  print('-'*20)