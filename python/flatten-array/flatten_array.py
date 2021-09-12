def flatten(iterable):
    flattenn = []

    for i in iterable:
        if type(i) in (list, tuple):
            flattenn.extend(flatten(i))
        elif i is not None:
            flattenn.append(i)

    return flattenn
