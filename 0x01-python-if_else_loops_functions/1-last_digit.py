#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit *= -1 if number < 0 else 1  # keeps the sign

string = "Last digit of {} is {}".format(number, last_digit)

if last_digit > 5:
    print("{} and is greater than 5".format(string))
elif last_digit == 0:
    print("{} and is 0".format(string))
else:
    print("{} and is less than 6 and not 0".format(string))
