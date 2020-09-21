from collections import Counter
import re

def count_words(str_sent):
    return Counter(re.findall(r"[a-z]+'?[a-z]+|[a-z]+|\d+", str_sent.lower()))