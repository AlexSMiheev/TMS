import random

list_of_numder = []
for number in range(10):
    list_of_numder.append(random.randrange(-100, 100))

print(list_of_numder)
list_of_numder[2] = random.randrange(-100, 100)
list_of_numder.pop(6)
print(list_of_numder)
