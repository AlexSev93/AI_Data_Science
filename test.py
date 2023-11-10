import numpy as np

arr = np.random.randint(0, 100, size = 20) #Создаем случайный массив
print('Созданный массив: ', arr) #Выводим информацию 
arr_diff = arr[1:] - arr[:-1] #Считаем производные
print(arr[1:])
print(arr[:-1])
