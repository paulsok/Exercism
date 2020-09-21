def is_isogram(string):
    
    string_cl = string.replace(" ", "").replace("-", "").lower()

    return len(string_cl) == len(set(string_cl))


x = 4