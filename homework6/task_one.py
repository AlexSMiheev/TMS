def distance(*args):
    distance_sum = 0
    for index, coords in enumerate(args):
        if index == len(args) - 1:
            break
        x1, y1 = coords
        x2, y2 = args[index + 1]
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        distance_sum += length
    return int(distance_sum)


print(distance((1, 1), (1, 2), (3, 4), (5, 6)))
