def distance_traveled() -> int:
    try:
        distance = int(input('Задайте пройденное расстояние: '))
        if distance >= 0:
            return distance
        else:
            print('Параметры должны быть положительные числа '
                  'от 0 до бесконечности.')
            return distance_traveled()
    except ValueError:
        print('параметры должны быть целые числа.')
        return distance_traveled()


def time_spent() -> int:
    try:
        time = int(input('Затраченное время: '))
        if time >= 0:
            return time
        else:
            print('Параметры должны быть положительные числа '
                  'от 0 до бесконечности.')
            return time_spent()
    except ValueError:
        print('параметры должны быть целые числа.')
        return time_spent()


print(f'Средняя скорость на маршруте: {int(distance_traveled() / time_spent())}.')
