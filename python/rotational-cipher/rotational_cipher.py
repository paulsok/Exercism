def rotate(text, key):
    alphabit = "abcdefghijklmnopqrstuvwxyz"
    code = alphabit[key:] + alphabit[:key]
    alphabit += alphabit.upper()
    code += code.upper()
    transition = str.maketrans(alphabit, code)

    return text.translate(transition)
