from itertools import combinations_with_replacement


def find_fewest_coins(coins, target):
    if target == 0:
        return []

    for i in range(1, target // coins[0] + 1):
        for combination in combinations_with_replacement(coins, i):
            if sum(combination) == target:
                return list(combination)

    raise ValueError('not changeble')
