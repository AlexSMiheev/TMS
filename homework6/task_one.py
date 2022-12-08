from math import sqrt

#Понимаю что это будет работать только с четным количеством аргументов
# , но сейчас очень много работы навалилось...
def route_calculation(*args):
    distance = 0
    coordinates = list(args)
    for n in coordinates:
        x_first, y_first = n
        coordinates.pop(0)
        for c in coordinates:
            x_second, y_second = c
            coordinates.pop(0)
            calculation_x = pow(int(x_second) - int(x_first), 2)
            calculation_y = pow(int(y_second) - int(y_first), 2)
            distance = int(distance) + int(sqrt(calculation_x + calculation_y))
    return  distance

print(route_calculation((1, 1), (1, 2), (3, 4), (5, 6)))
