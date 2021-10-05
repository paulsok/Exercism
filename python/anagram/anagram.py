def find_anagrams(word, candidates):
    word = word.lower()

    return [x for x in candidates if sorted(word) == sorted(x.lower())
            and word != x.lower()]
