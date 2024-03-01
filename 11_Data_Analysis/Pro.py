import pandas as pd


columns = ('Комнат', 'Метро / ЖД станции', 'От станции', 'Дом', 'Балкон',
            'Санузел', 'Площадь', 'Цена, руб.', 'Бонус агенту', 'Дата',
            'Кол-во дней в экспозиции', 'Источник')

data = pd.read_csv('moscow.csv', sep=";")
data = data[data['Комнат'] != 'Для заметок:']
data = data.drop(columns=['ГРМ', 'Примечание'], axis=1)
data = data.reset_index(drop=True)

data.loc[data['Балкон'].isna(), 'Балкон'] = 'Нет'
data.loc[data['Бонус агенту'].isna(), 'Бонус агенту'] = 0
data.loc[data['Санузел'].isna(), 'Санузел'] = 'Нет'

area = data['Площадь']
area_new = []
for i in range(area.shape[0]):
    n = area[i].replace('/', ',')
    n = n.replace('?', '0')
    try:
        n = sum(map(float, n.split(',')))
    except:
        n = 'Нет'
    area_new.append(n)
data['Площадь'] = area_new
