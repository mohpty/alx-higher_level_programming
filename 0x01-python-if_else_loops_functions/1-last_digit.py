#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print(f"Last digit of {number} is {number % 10} ", end='')

    if number % 10 > 5:
        print('and is greater than 5')
    elif number % 10 == 0:
        print('and is 0')
    else:
        print('and is less than 6 and not 0')
elif number < 0:
    print(f"Last digit of {number} is ", end='')
    if (number * -1) % 10 != 0:
        print('-', end='')
    print(f"{(number * -1) % 10} ", end='')
    if (number * -1) % 10 == 0:
        print('and is 0')
    else:
        print('and is less than 6 and not 0')
else:
    print("Last digit of 0 is 0 and is 0")
