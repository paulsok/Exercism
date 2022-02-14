def is_paired(input_string):
    opened = "[{("
    closed = "]})"
    stack = []

    for char in input_string:
        if char in opened:
            stack.append(char)

        elif char in closed:
            if not stack or opened[closed.index(char)] != stack.pop():
                return False

    return not stack
