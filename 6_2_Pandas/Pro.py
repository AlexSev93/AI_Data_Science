import pandas as pd

data = pd.read_csv('data.csv', encoding='cp1250')

# z1
data.index = pd.to_datetime(data.InvoiceDate)
data.drop('InvoiceDate', axis=1)
# print(data.head())

# z2
z2 = data['2010-12-07 13:00:00':'2010-12-07 13:01:00']
# print(z2)

# z3
# unique_des = data.Description.nunique()
# countries = data.Country.unique()
# print(unique_des, countries)

# z4
# cor = data.corr(method='spearman')
# quantil = data.quantile([0.01, 0.5, 0.99])
# print(quantil)

# z5
z5 = data.CustomerID[data.index.weekday == 0].nunique()
print(z5)
