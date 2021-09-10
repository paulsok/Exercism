import math


def score(x, y):
    dist = math.sqrt(x * x + y * y)

    if dist > 10:
        return 0
    elif dist > 5:
        return 1
    elif dist > 1:
        return 5
    else:
        return 10
