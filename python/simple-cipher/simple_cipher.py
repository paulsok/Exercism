import random
from itertools import cycle
from string import ascii_lowercase as letters


class Cipher:
    def __init__(self, key=None):
        if not key:
            self.key = "".join(random.choice(letters) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            encoded.append(letters[(ord(ch1) % 97 + ord(ch2) % 97) % 26])
        return "".join(encoded)

    def decode(self, text):
        decoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            decoded.append(letters[(ord(ch1) % 97 - ord(ch2) % 97) % 26])
        return "".join(decoded)
