import pandas as pd
import matplotlib.pyplot as plt

# 'Пол', 'Возраст', 'ЗП', 'Город', 'Занятость', 'График',
#        'Опыт (двойное нажатие для полной версии)', 'Образование и ВУЗ',
#        'Ищет работу на должность'

data = pd.read_csv('hh_parsed_new.csv')
print(data.size)

data = data[(data['Возраст'] >= 18) & (data['Возраст'] <= 70)]
data = data[(data['ЗП'] >= 20000) & (data['Возраст'] <= 700_000)]

plt.scatter(data['Опыт (двойное нажатие для полной версии)'], data['Возраст'])
plt.show()

data = data[data['Опыт (двойное нажатие для полной версии)'] <= 700]
print(data.size)

data = data[data['Пол'] == 'Не указан']
data.groupby('Возраст')['ЗП'].mean().plot()
plt.show()

jobs = data['Ищет работу на должность'].value_counts()
print(jobs)

plt.scatter(data['Возраст'], data['ЗП'])
plt.xlabel('Зарплата')
plt.ylabel('Возраст')
plt.show()


langs = ('java', 'python', 'c+')

for lang in langs:
    data_lang = data[data['Ищет работу на должность'].str.lower().str.contains(lang)]
    mean_cash = round(data_lang['ЗП'].mean())
    print(f'средняя зп программиста на {lang} = {mean_cash}')
