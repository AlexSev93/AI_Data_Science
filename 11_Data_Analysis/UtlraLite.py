import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('hh_parsed_new.csv')
# 'Пол', 'Возраст', 'ЗП', 'Город', 'Занятость', 'График',
#        'Опыт (двойное нажатие для полной версии)', 'Образование и ВУЗ',
#        'Ищет работу на должность'


# plt.scatter(data['ЗП'], data['Возраст'])
# plt.xlabel('Зарплата')
# plt.ylabel('Возраст')
# plt.show()
#
# plt.scatter(data['ЗП'], data['Опыт (двойное нажатие для полной версии)'])
# plt.xlabel('Зарплата')
# plt.ylabel('Опыт')
# plt.show()

# univer = dict(data['Образование и ВУЗ'].value_counts())
# plt.bar(univer.keys(), univer.values())
# plt.xticks(rotation=90)
# plt.show()

# cities = dict(data['Город'].value_counts())
# plt.bar(cities.keys(), cities.values())
# plt.xticks(rotation=90)
# plt.show()

graf = dict(data['Занятость'].value_counts()[:10])
plt.bar(graf.keys(), graf.values())
plt.xticks(rotation=90)
plt.show()