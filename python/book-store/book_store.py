from collections import Counter

disc_prices = (0, 800, 1520, 2160, 2560, 3000)

def total(basket):
    books = Counter(basket)
    tot_price = 0
    book_number = []

    while len(books) > 0:
        tot_price += disc_prices[len(books)]
        book_number.append(len(books))

        books = {k: v-1 for k, v in books.items()}
        books = {k: v for k, v in books.items() if v != 0}

    while 3 in book_number and 5 in book_number:
        tot_price -= 40
        book_number.remove(3)
        book_number.remove(5)

    return tot_price