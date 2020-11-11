from collections import Counter

disc_prices = (0, 800, 1520, 2160, 2560, 3000)

def total(basket):

    tot_price = 0
    books = Counter(basket)
    book_number = list()

    while len(books) > 0:
        tot_price += disc_prices[len(books)]
        book_number.append(len(books))

        books = {i: j-1 for i, j in books.items()}
        books = {i: j for i, j in books.items() if j != 0}

    while 3 in book_number and 5 in book_number:
        tot_price -= 40
        book_number.remove(3)
        book_number.remove(5)

    return tot_price