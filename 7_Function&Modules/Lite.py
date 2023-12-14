# z1
def shut_down(param):
    if param == 'da':
        print('vikl')
    elif param == 'net':
        print('vikl ontkloneno')
    else:
        print('oshibka')


# z2
def list_2(nums):
    sum2 = 0
    for num in nums:
        if num // 2 == 0:
            sum2 += num
    return sum2


# z3
from math import sqrt

ex_list = [i for i in range(10)]
for i in ex_list:
    print(sqrt(i))


# z5
def my_revers(text):
    return text[::-1]
