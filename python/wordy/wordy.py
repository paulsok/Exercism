def answer(question):
    if question == "":
        raise ValueError("No question, really?")
    if question[-1] != "?":
        raise ValueError("There is no question mark!")

    words = question[:-1].split(' ')

    if len(words) < 3:
        raise ValueError("syntax error")
    if words[0] != "What" or words[1] != "is":
        raise ValueError("unknown operation")
    if not is_valid_number(words[2]):
        raise ValueError("syntax error")
    return None
