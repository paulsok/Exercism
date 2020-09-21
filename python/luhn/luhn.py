class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if self.card_num.isnumeric() and len(self.card_num) > 1:
            card_num_rev = [int(x) for x in self.card_num][::-1]

            for i in range(len(card_num_rev)):
                if i % 2 == 1:
                    if card_num_rev[i] * 2 > 9:
                        card_num_rev[i] = card_num_rev[i] * 2 - 9
                    else:
                        card_num_rev[i] = card_num_rev[i] * 2

            if sum(card_num_rev) % 10 == 0:
                return True

        return False
