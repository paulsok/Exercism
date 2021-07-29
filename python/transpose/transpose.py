from itertools import zip_longest


def transpose(s):
    a = zip_longest(*s.splitlines(), fillvalue='$')

    return '\n'.join(''.join(w).rstrip('$').replace('$', ' ') for w in a)
