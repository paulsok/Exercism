def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")
    if not series or not length:
        raise ValueError("slice length cannot be zero")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length < 0:
        raise ValueError("slice length cannot be negative")

    return [series[n:n+length] for n in range(0, len(series)-length+1)]
