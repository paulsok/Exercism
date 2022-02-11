import math


padding = lambda st, col_num: st + " " * (col_num - len(st))


def cipher_text(plain_text):
    text = "".join(x for x in plain_text.lower() if x.isalnum())
    if not text:
        return ""

    rows = math.ceil(math.sqrt(len(text)))
    cols = math.ceil(len(text)/rows)

    return " ".join(padding(text[i::rows], cols) for i in range(rows))
