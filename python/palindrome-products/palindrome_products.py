def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor should be grather than max_factor!")

    result = []
    factors = []
    value = None

    for i in reversed(range(min_factor, max_factor+1)):
        for j in reversed(range(min_factor, max_factor+1)):
            if str(i * j) == str(i * j)[::-1]:
                if value is None:
                    value = i * j

                elif i * j >= value:
                    value = i * j
                    factors.append([i, j])

    for f in reversed(factors):
        if sorted(f) not in result:
            result.append(f)

    return value, result[:]


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor should be grather than max_factor!")

    factors = []
    value = None

    for i in range(min_factor, max_factor+1):
        for j in range(min_factor, max_factor+1):
            if str(i * j) == str(i * j)[::-1]:
                if not value:
                    value = i * j
                    factors.append([i, j])
                    break

        if value is not None:
            break

    return value, factors
