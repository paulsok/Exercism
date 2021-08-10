def encode(values):
    encoding = []

    for i in values:
        st = []
        mask = 0

        while not mask or i:
            st.append(mask | (i & 0x7f))
            i >>= 7
            mask = 0x80

        encoding += reversed(st)

    return encoding


def decode(encoding):
    if len(encoding) and (encoding[-1] & 0x80):
        raise ValueError("Incomplete encoding")

    t = 0
    ans = []

    for byte in encoding:
        t = (t << 7) | (byte & 0x7f)
        if byte & 0x80 == 0:
            ans.append(t)
            t = 0

    return ans
