# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
n = int(input('Введите нижнюю границу диапазона ')) 
x = int(input('Введите верхнюю границу диапазона ')) 


def Result(n,x):
    list_1 = []
    list_2 = []
    list_3 = []
    
    for i in range(0,10):
        list_1.append(random.randint(1, 50))
        # print(list_1)

    for i in range(len(list_1)):
        if list_1[i]>=n and list_1[i] <= x:
            list_2.append(list_1[i])
        else:
            list_3.append(list_1[i])

     # print(list_2)

    
    
    return list_1,list_2
tuple = Result(n,x)
print(f'Массив систоит из: {tuple[0]} \n В заданный диапазон попадают числа{tuple[1]}')

