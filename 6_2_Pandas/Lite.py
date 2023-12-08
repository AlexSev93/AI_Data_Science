import pandas as pd
import numpy as np


data = pd.read_csv('googleplaystore.csv')

# z1
# categories = list(data['Category'].unique())
# for category in categories:
#     print(f'{category} ---> {data[data.Category==category].shape[0]}')

# z2
# data_sort = data.sort_values(by='Rating', ascending=False)
# print(data_sort)

# z3
# data = data[(data.Rating >= 3) & (data.Rating <= 5)]
# free_app = data[data.Type == 'Free'].shape[0]
# paid_app = data[data.Type == 'Paid'].shape[0]
# print(f'платные-->{paid_app}, бесплатные-->{free_app}')

# z4
# new_index = list(np.random.randint(0, data.shape[0], data.shape[0]))
# print(data.head())
# data.index = new_index
# print(data.head())

# z5
# null_cell = data.isna().sum().sum()
# print(f'пустых ячеек -- {null_cell}, {null_cell/(data.shape[0]*data.shape[1])*100}%')