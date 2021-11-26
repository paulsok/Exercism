def is_valid_number(string):
    return string.isdecimal() or string[0] == '-' and string[1:].isdecimal()


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

    result = int(words[2])
    index = 3

    while index < len(words):
        if index + 1 < len(words) and words[index] in ["plus", "minus"] and is_valid_number(words[index+1]):
            if words[index] == "plus":
                result += int(words[index+1])
            else:
                result -= int(words[index+1])
            index += 2

        elif index + 2 < len(words) and words[index] in ["multiplied", "divided"] and words[index+1] == "by" and is_valid_number(words[index+2]):
            if words[index] == "multiplied":
                result *= int(words[index+2])
            else:
                result /= int(words[index+2])
            index += 3

        elif index + 4 < len(words) and words[index:index+3] == ["raised", "to", "the"] and len(words[index+3]) > 2\
                                    and words[index+3][-2:] in ["th", "st", "nd"] and is_valid_number(words[index+3][:-2]) and words[index+4] == 'power':
            result **= int(words[index+3][:-2])
            index += 5

        elif words[index] in ["plus", "minus", "multiplied", "divided", "raised"]:
            if index + 1 < len(words) and words[index+1] in ["plus", "minus", "multiplied", "divided", "raised"] and words[index] != words[index+1]:
                raise ValueError("unknown operation")
            raise ValueError("syntax error")

        else:
            if is_valid_number(words[index]):
                if index == 3 and index + 2 < len(words) and is_valid_number(words[index+2]):
                    raise ValueError("unknown operation")
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

    return result
