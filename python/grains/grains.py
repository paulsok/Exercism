def square(number):
    if number < 1 or number > 64:
        raise ValueError("Only numbers between 1 - 64 are accepted")

    return 2 ** (number - 1)


def total():
    return sum(2 ** x for x in range(0, 64))
