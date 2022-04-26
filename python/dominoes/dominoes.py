def check_all_chains(unused, chain=[]):
    if len(unused) == 0 and (len(chain) == 0 or chain[0][0] == chain[-1][1]):
        return chain

    for i, stone in enumerate(unused):
        left = unused[:i] + unused[i+1:]
        for piece in (stone, stone[::-1]):
            if chain and chain[-1][1] != piece[0]:
                continue
            if res := check_all_chains(left, chain + [piece]):
                return res
    return None


def can_chain(dominoes):
    return check_all_chains(dominoes)
