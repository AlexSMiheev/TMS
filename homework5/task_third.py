char = input('say the letter: ')

text = open('text.txt')
quantity = 0
for i in text:
    for c in i:
        if c.lower() == char.lower():
            quantity += 1

print(f'Result: the letter occurs {quantity} times in the text.')
