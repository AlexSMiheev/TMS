def is_right_angle_triangle(a, b, c):
    angles = [a, b, c]
    result = {}

    c = max(angles)
    angles.remove(c)
    b = max(angles)
    angles.remove(b)
    a = max(angles)

    if a + b > c and a + c > b and b + c > a:
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            result['result'] = True
            result['description'] = 'the triangle is right-angled'
            return result
        else:
            result['result'] = False
            result['description'] = 'the triangle is not right-angled'
            return result
    else:
        result['result'] = False
        result['description'] = 'no such triangle exists'
        return result


print(is_right_angle_triangle(5, 4, 3))
