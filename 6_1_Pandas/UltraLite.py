import pandas as pd
import numpy as np

# z1
data = np.zeros((4, 7), dtype=int)
line = np.array([0, 1, 2, 3, 4, 5, 6])
for i in range(1, 4):
    new_line = line * i
    data[i] = new_line

data = pd.DataFrame(data)
print(data)

#z2
print(data.sum())

#z3
# print(data.shape)

#z4
# print(data[2])
# print(data[4])

#z5
# new_column = [0, 7, 14, 21]
# data[7] = new_column
# print(data)