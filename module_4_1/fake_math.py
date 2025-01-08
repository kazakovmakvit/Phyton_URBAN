from math import inf

def fake_divide(first, second):
    try:
        return print(f'Деление первого числа на второе: {first/second} (fake_divide)')
    except ZeroDivisionError:
        print(f'Деление на 0 равно: {float(inf)} (fake_divide)')
