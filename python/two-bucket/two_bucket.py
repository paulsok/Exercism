def measure(bucket_one, bucket_two, goal, start_bucket):
    if bucket_two == goal and start_bucket == 'one':
        return 2, 'two', bucket_one

    elif bucket_one == goal and start_bucket == 'two':
        return 2, 'one', bucket_two

    elif start_bucket == 'two':
        bucket_one, bucket_two = bucket_two, bucket_one

    n, m = bucket_one, 0
    steps = 1

    while True:
        if n == goal:
            return steps, 'one' if start_bucket == 'one' else 'two', m

        elif n == bucket_one or m == 0:
            x = min(n, bucket_two - m)
            m += x
            n -= x

        elif n == 0:
            n = bucket_one

        elif m == bucket_two:
            m = 0

        elif m == goal:
            return steps, 'two' if start_bucket == 'one' else 'one', n

        steps += 1
