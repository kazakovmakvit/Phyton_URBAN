first = int(input('Введите first число: '))
second = int(input('Введите second число: '))
third = int(input('Введите third число: '))

if first == second and first == third:
    print('Все числа одинаковые')
elif first == second or first == third or second == third:
    print('2 числа равны')
else:
    print('нет равных чисел')
