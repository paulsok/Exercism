CODONS = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
}


def proteins(strand):
    i = 0
    codon = strand[i:i+3]
    codon_l = []

    while i < len(strand) and CODONS[codon] != 'STOP':
        codon_l.append(CODONS[codon])
        i += 3
        codon = strand[i:i+3]

    return codon_l
