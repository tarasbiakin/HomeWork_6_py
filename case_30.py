#  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1)d.
# Каждое число вводится с новой строки.


a = int(input('Введите число членов прогрессии '))
a1 = int(input('Введите первое число прогрессии '))
d = int(input('Введите разность членов прогрессии '))


def Result(n,b,c):
    list_1 = []
        
    for i in range(1,n+1):
        list_1.append(a1+(i-1)*d)
        # print(list_1)

    
    
    return list_1

print(f'Элементы арифметической прогрессии {Result(a,a1,d)}')
