import random

AVAILABLE_NAMES = ['John', 'Jane', 'Mary', 'David', 'Alex', 'Max', 'Nick', 'Anastasia', 'Leo']
AVAILABLE_COLORS = ['blue', 'green', 'brown', 'grey', 'black']


class User:

    def __init__(self, name: str, nickname: str, age: int, eye_color: str) -> None:
        self.name = name
        self.nickname = nickname
        self.age = age
        self.eye_color = eye_color

    @property
    def info(self):
        info = {'Name': self.name, 'Nickname': self.nickname, 'Age': self.age, 'Eyes_color': self.eye_color}
        return info

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age


def users_generator(number):
    for usr in range(number):
        name = random.choice(AVAILABLE_NAMES)
        nickname = name + str(random.randrange(10000, 99999))
        age = random.randrange(0, 100)
        eye_color = random.choice(AVAILABLE_COLORS)
        usr = User(name, nickname, age, eye_color)
        yield usr


gen = users_generator(50)
for user in gen:
    print(user.info)
