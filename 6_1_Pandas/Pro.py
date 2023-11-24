import pandas as pd
import numpy as np

# z1
data = pd.read_csv('train.csv', delimiter=',', index_col=0)
# print(data.head())

# z2
# count = data.shape[0]
# size = data.size
# print(f'записи = {count}, размер={size}', end='----------- \n')
# print(f'типы {data.info()}', end='----------- \n')
# print(f'пустые записи {data.isna().sum()}', end='----------- \n')
# print(f'статистика {data.describe()}', end='----------- \n')

# z3
columns = data.columns[data.isna().sum() > 200]
# print(columns)
data_1 = data.drop(columns, axis=1)

# z4
houses = data_1[(data_1['SalePrice'] > 300000) &
                (data_1['YrSold'] == 2007) &
                (data_1['PoolArea'] > 0)]
# print(houses)

# z5
rand = np.random.randint(0, 2, data_1.shape[0])
data_1['Flag'] = rand
# print(data_1.Flag)