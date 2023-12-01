import pandas as pd

# z1
data = pd.read_csv('C:/Users/Admin/PycharmProjects/AI_Data_Science/6_1_Pandas/city_temperature.csv')
# print(data.Country[data.AvgTemperature > 100].nunique())

# z2
# print(data.AvgTemperature.median())

# z3
# print(data[((data.Year == 1995) & (data.Month == 1) & (data.Day == 1) |
#             (data.Year == 2018) & (data.Month == 1) & (data.Day == 1))].shape[0])

# z4
# coutries = list(data.Country.unique())
# print(coutries)

# z5
columns_list = list(data.columns)
translite = ['Регион', 'Страна', 'Штат',
             'Город', 'Месяц', 'День',
             'Год', 'Средняя темепература']
columns_tuple = {}
for i in range(len(columns_list)-1):
    columns_tuple[columns_list[i]] = translite[i]

# columns = {column: translite[columns.index(column)] for column in columns}
data = data.rename(columns=columns_tuple)
# print(data.head())