import math


def is_armstrong_number(number):
    if number < 10:
        return True

    mypow = int(math.log10(number) + 1)
    num = number
    total = 0

    while num > 0:
        total += pow(int(num % 10), mypow)
        num = int(num / 10)

    return number == total
