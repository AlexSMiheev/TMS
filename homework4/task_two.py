import random

digits = list(range(10))
computer_choice = []

for _ in range(4):
    digit = random.choice(digits)
    digits.remove(digit)
    computer_choice.append(str(digit))

computer_choice = ''.join(computer_choice)
print(computer_choice)

while True:
    guess_number = list(input('Угадайте число. 4 цифры: '))
    guess_number = ''.join(guess_number)

    print(guess_number)

    if computer_choice == guess_number:
        print('Вы выйграли!!!')
        break

    cows_counter = 0
    bulls_counter = 0

    for computer_digit, user_digit in zip(computer_choice, guess_number):
        if computer_digit == user_digit:
            bulls_counter += 1
        elif user_digit in computer_choice:
            cows_counter += 1
    print(f'Bulls - {bulls_counter} Cows - {cows_counter}')
