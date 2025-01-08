def true_divide(first, second):
    try:
        return print(f'Деление первого числа на второе: {first/second} (true_divide)')
    except ZeroDivisionError:
        print('Ошибка, Деление на 0 (true_divide)')

