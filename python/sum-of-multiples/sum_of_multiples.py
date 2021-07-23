def sum_of_multiples(limit, multiples):
    return sum(set(n for m in multiples for n in range(m, limit, m)))
