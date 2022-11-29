from math import sqrt

x_first = input('X для первой точки: ')
y_first = input('Y для первой точки: ')
x_second = input('X для второй точки:')
y_second = input('Y для второй точки:')

try:
    print(f'Если координаты первой точки {x_first} и {y_first}, '
          f'а координаты для второй {x_second} и {y_second}, '
          f'то расстояние между ними составит - '
          f'{sqrt(int(x_second) - int(x_first)) ** 2 + (int(y_second) - int(y_first)) ** 2}')
except ValueError:
    print('Невозможно рассчитать в этом измерении.')
