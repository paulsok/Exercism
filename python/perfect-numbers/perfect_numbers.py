def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    al_sum = sum((i + number // i if i != number // i else i
                       for i in range(1, int(number ** 0.5) + 1)
                       if number % i == 0)) - number

    if al_sum < number:
        return "deficient"

    if al_sum > number:
        return "abundant"

    return "perfect"
