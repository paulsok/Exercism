def triplets_with_sum(number):
    triplets = []
    for x in range(1, number):
        temp = check(x, number)
        temp.sort()

        if len(temp) > 0 and temp not in triplets:
            triplets.append(temp)

    return triplets


def check(x, number):
    q = number - x
    n = (q ** 2 + x ** 2) / (2 * q)
    m = number - n - x

    if m == int(m) and n == int(n) and m > 0 and n > 0:
        return [x, int(m), int(n)]
    return []
