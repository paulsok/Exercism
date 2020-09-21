import re

def abbreviate(words):
    letters = re.findall(r"([a-zA-Z'^]+)", words)

    return "".join(i[0].upper() for i in letters)