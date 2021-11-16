class PhoneNumber:
    def __init__(self, number):
        digits = []

        for char in number:
            if char.isdecimal():
                digits.append(char)
            if char.isalpha():
                raise ValueError("letters not permitted")
            if char in "!\"#$%&'*+,/:;<=>?@[\]^_`{|}~":
                if not digits and char == '+':
                    continue
                else:
                    raise ValueError("punctuations not permitted")
        if len(digits) < 10:
            raise ValueError("incorrect number of digits")
        if len(digits) > 11:
            raise ValueError("more than 11 digits")
        if len(digits) == 11:
            if digits[0] != '1':
                raise ValueError("11 digits must start with 1")
            del digits[0]
        if digits[0] == '0':
            raise ValueError("area code cannot start with zero")
        if digits[0] == '1':
            raise ValueError("area code cannot start with one")
        if digits[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == '1':
            raise ValueError("exchange code cannot start with one")

        self.number = "".join(digits)
        self.area_code = "".join(digits[:3])
        self.exchange_code = "".join(digits[3:6])
        self.subscriber_number = "".join(digits[6:])

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
