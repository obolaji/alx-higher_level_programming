#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

a = "is greater than 5"
b = "is 0"
c = "is less than 6 and not 0"
if number > 0:
    lastDigit = number % 10
else:
    lastDigit = number % -10
if lastDigit > 5:
    print("Last digit of {} is {} and ".format(number, lastDigit) + a)
elif lastDigit == 0:
    print("Last digit of {} is {} and ".format(number, lastDigit) + b)
else:
    print("Last digit of {} is {} and ".format(number, lastDigit) + c)
