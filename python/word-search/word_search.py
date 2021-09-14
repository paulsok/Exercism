class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return 'Point({}:{})'.format(self.x, self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not(self == other)


class WordSearch(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = Point(len(puzzle[0]), len(puzzle))

    def value(self, position):
        if 0 <= position.y < self.size.y and 0 <= position.x < self.size.x:
            return self.puzzle[position.y][position.x]

        return ' '

    def search(self, word):
        direct = [Point(*i) for i in
                  [(0, 1), (0, -1), (1, 0), (-1, 0),
                   (1, 1), (-1, -1), (1, -1), (-1, 1)]]

        t_range = [Point(x, y) for y in range(self.size.y)for x in
                   range(self.size.x)]

        for x in t_range:
            if self.value(x) == word[0]:
                for i in direct:
                    end = x
                    for j in word[1:]:
                        end += i
                        if self.value(end) != j:
                            break

                    if self.value(end) == j\
                       and (abs((end - x).x) == len(word) - 1
                       or abs((end - x).y) == len(word) - 1):
                        return x, end

        return None
