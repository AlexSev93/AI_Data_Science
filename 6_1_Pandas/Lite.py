import pandas as pd
import numpy as np

data = pd.read_csv('city_temperature.csv')
print(data.head())

#z1
zero = data['State'].isna().sum()
print(zero)
