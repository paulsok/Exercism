def is_valid(isbn):
    numbers = [int(c) for c in isbn if c.isdigit()][::-1]
    if isbn.endswith('X'):
        numbers.insert(0, 10)

    return False if len(numbers) != 10 else sum([x * (i + 1) for i, x in
                                                enumerate(numbers)]) % 11 == 0
