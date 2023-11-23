import pandas as pd
import numpy as np

data = pd.read_csv('city_temperature.csv')
# print(data.head())

#z1
# zero = data['State'].isna().sum()
# print(zero)

#z2
# data_2 = data.fillna('No')
# print(data_2.head())

#z3
# print(data['Country'].unique())
# print(data['City'].unique())
# print(data['Year'].unique())

#z4
# print(data[data['Country'] == 'Russia'])
# print(data[data['Country'] == 'Russia'].size)

#z5
# data['New_Temp'] = (data['AvgTemperature'] - 32) * 5/9
# print(data.head())
