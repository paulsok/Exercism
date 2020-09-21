all_days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

all_gifts = ['twelve Drummers Drumming, ', 'eleven Pipers Piping, ', 'ten Lords-a-Leaping, ', 'nine Ladies Dancing, ',
        'eight Maids-a-Milking, ', 'seven Swans-a-Swimming, ', 'six Geese-a-Laying, ', 'five Gold Rings, ',
        'four Calling Birds, ', 'three French Hens, ', 'two Turtle Doves, and ', 'a Partridge in a Pear Tree.']

def recite(start_verse, end_verse):
    text = []

    for i in range(start_verse - 1, end_verse):
        text.append("On the %s day of Christmas my true love gave to me: " % all_days[i] + "".join(all_gifts[11 - i:12]))

    return text