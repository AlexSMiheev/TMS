fibo_numbers = [0, 1]

number = int(input('Give me a number '))

for i in range(number):
    fibo_numbers.append(fibo_numbers[0] + fibo_numbers[1])
    fibo_numbers.pop(0)

print(fibo_numbers[0])