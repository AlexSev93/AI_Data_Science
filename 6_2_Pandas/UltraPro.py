import pandas as pd

data = pd.read_csv('data.csv', encoding='cp1250')
data['TotalCost'] = data.Quantity * data.UnitPrice
data.index = pd.to_datetime(data.InvoiceDate)

# z1
# z1 = data.TotalCost.resample('1W').sum()
# print(z1)

# z2
# res = data.TotalCost.resample('D').sum()
# z2 = res.rolling('7D').mean()
# print(z2)

# z3
# data = data.groupby(['Country'])
# z3 = data.TotalCost.resample('1M').sum()
# print(z3)

# z4
