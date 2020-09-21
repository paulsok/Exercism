def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b): 
        raise ValueError('The length of the DNA strands is different!')

    return  sum([n!=m for n, m in zip(strand_a, strand_b)])