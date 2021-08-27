ones = ('zero', 'one', 'two', 'three',
        'four', 'five', 'six', 'seven',
        'eight', 'nine', 'ten', 'eleven',
        'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen')

tens = ('zero', 'ten', 'twenty', 'thirty',
        'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety')


def say(number):
    if number < 0 or number >= 1e12:
        raise ValueError("Number out of range")

    if number < 20:
        return ones[int(number)]
    elif number < 100:
        ten, remainder = divmod(number, 10)
        return tens[int(ten)] + ('-' + say(remainder) if remainder > 0 else '')
    elif number < 1000:
        hundred, remainder = divmod(number, 100)
        return ones[int(hundred)] + ' hundred' + (' ' + say(remainder) if remainder > 0 else '')
    elif number < 1000000:
        thousand, remainder = divmod(number, 1000)
        return say(thousand) + ' thousand' + (' ' + say(remainder) if remainder > 0 else '')
    elif number < 1e9:
        million, remainder = divmod(number, 1e6)
        return say(million) + ' million' + (' ' + say(remainder) if remainder > 0 else '')
    else:
        billion, remainder = divmod(number, 1e9)
        return say(billion) + ' billion' + (' ' + say(remainder) if remainder > 0 else '')
