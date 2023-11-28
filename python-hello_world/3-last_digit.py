#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
comparison = ""

if last_digit < 6 and last_digit != 0:
    comparison = f"and is less than 6 and not 0"
elif last_digit > 5:
    comparison = f"and is greater than 5"
else:
    comparison = f"and is 0"

print(f"Last digit of {number} is {last_digit} {comparison}")
