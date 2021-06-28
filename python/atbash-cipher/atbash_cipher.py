plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"


def cleanup(text):
    return ''.join(a.lower() for a in text if a.isalnum())


def encode(text):
    text = cleanup(text)
    text = text.translate(text.maketrans(plain, cipher))
    return ' '.join(text[i:i+5] for i in range(0, len(text), 5))


def decode(text):
    return text.translate(text.maketrans(plain, cipher)).replace(" ", "")
