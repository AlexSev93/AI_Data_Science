import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# z1-2
# x = np.random.randint(-10, 10, 20)
# y = np.random.randint(-10, 10, 20)
#
# plt.figure(figsize=(6, 3))
# plt.plot(x, y, color='r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Самолет')
# plt.grid(True)
# plt.scatter(x, y)
# plt.show()

# z3
# data = {'Яблоки': 10, 'Апельсины': 15, 'Лимоны': 5, 'Лайм': 20}
# names = list(data.keys())
# values = list(data.values())
#
# plt.bar(names, values)
# plt.show()

spis = [1,2,3,4,10,20,30,40]
sns.boxplot(spis, color='g')
plt.show()