class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row >= 8:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column >= 8:
            raise ValueError("column not on board")
        self.x = row
        self.y = column

    def can_attack(self, another_queen):
        if another_queen.x == self.x and another_queen.y == self.y:
            raise ValueError("Invalid queen position: both queens in the same square")
        return any((self.x == another_queen.x, self.y == another_queen.y,
                    abs(self.x - another_queen.x) == abs(self.y - another_queen.y)))
