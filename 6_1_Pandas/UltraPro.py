import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# z1
files = os.listdir('bookings')
data = []
for file in files:
    table = pd.read_csv(f'bookings/{file}')
    data.append(table)

data = pd.concat(data)

# z2
# print(data.head())
# print(data.shape) #238780 строк из 10 таблиц
# fig, ax = plt.subplots(figsize=(20, 40))
# sns_heatmap = sns.heatmap(data.isnull(),
#                           yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

# z3
data = data.dropna(axis=0, how='all')
data = data.dropna(axis=1, how='all')
# fig, ax = plt.subplots(figsize=(10, 20))
# sns_heatmap = sns.heatmap(data.isnull(),
#                           yticklabels=False, cbar=False, cmap='viridis')
# plt.show()
data = data.fillna('unknown')

# z4
data = data.groupby(['hotel', 'arrival_date_year', 'arrival_date_month'])
print(data.lead_time.count())
