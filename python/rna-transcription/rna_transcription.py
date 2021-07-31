def to_rna(dna):
    dna_to_rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(dna_to_rna[i] for i in dna)
