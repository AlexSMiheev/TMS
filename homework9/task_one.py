class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.__correct_data(a, b, c)
        self.__if_exist(a, b, c)
        self.result = {'result': False, 'description': 'Actions not performed'}
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __correct_data(a, b, c):
        if type(a) == int and type(b) == int and type(c) == int:
            return True
        raise ValueError('Incorrect data')

    @staticmethod
    def __if_exist(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        raise ValueError('No such triangle exists')

    def get_sides(self):
        return f'Triangle: {self.a}, {self.b}, {self.c}'

    def is_right_angled(self):
        angles = [self.a, self.b, self.c]

        c = max(angles)
        angles.remove(c)
        b = max(angles)
        angles.remove(b)
        a = max(angles)
        angles.remove(a)

        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            return True
        else:
            return False

    def __eq__(self, other):
        p1 = self.a + self.b + self.c
        p2 = other.a + other.b + other.c
        return p1 == p2


t1 = Triangle(5, 4, 3)
print(t1.is_right_angled())
t3 = Triangle(11, 11, 20)
print(t3.is_right_angled())
print(t1 != t3)
t2 = Triangle(10, 10, 20)
