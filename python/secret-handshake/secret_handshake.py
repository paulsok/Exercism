def commands(binary_str):
    shake = {0: "wink", 1: "double blink",
             2: "close your eyes", 3: "jump"}
    seq = []

    for x, i in enumerate(binary_str[::-1]):
        if i == "1" and x in shake:
            seq.append(shake[x])

    if binary_str[0] == "1":
        seq.reverse()

    return seq
