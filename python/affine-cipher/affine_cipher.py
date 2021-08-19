from math import gcd
from string import ascii_lowercase as alphabet


def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime!')

    encode = []
    for x in plain_text:
        if x.lower() in alphabet:
            temp = alphabet[(a * alphabet.index(x.lower()) + b) % 26]
            encode.append(temp)
        elif x.isdigit():
            encode.append(x)

    x = 5
    while x < len(encode):
        encode.insert(x, " ")
        x += 6

    return "".join(encode)


def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError('a and 26 are not coprime!')

    decode = []
    n = 1
    while a * n % 26 != 1:
        n += 1

    for x in ciphered_text:
        if x in alphabet:
            decode.append(alphabet[n * (alphabet.index(x) - b) % 26])
        elif x.isdigit():
            decode.append(x)

    return "".join(decode)
