def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers!")

    elif number == 1:
        return 0

    elif number % 2:
        return 1 + steps(3 * number + 1)

    else:
        return 1 + steps(number / 2)
