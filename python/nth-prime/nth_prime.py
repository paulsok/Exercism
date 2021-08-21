def prime(number):
    if number < 1:
        raise ValueError("n must be a positive integer")

    primes_list = [2, 3, 5, 7]
    counter = 10

    while len(primes_list) <= number:
        temp_1 = [counter % i for i in range(2, 1+int(counter**0.5))]
        temp_2 = [x != 0 for x in temp_1]
        if all(temp_2):
            primes_list.append(counter)
        counter += 1

    return primes_list[number-1]
