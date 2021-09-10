import re


def response(hey_bob):
    if re.sub("[\n\t\r ]", "", hey_bob) == "":
        return "Fine. Be that way!"

    elif all(i.isupper() for i in hey_bob if i.isalpha()) and\
            re.search('[a-zA-Z]', hey_bob):

        if hey_bob.rstrip()[-1] == "?":
            return "Calm down, I know what I'm doing!"

        return "Whoa, chill out!"

    elif hey_bob.rstrip()[-1] == "?":
        return "Sure."

    return "Whatever."
