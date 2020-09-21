class Matrix:
    def __init__(self, string):
        self._matrix_list = [[int(n) for n in m.split()] for m in string.split('\n')]

    def row(self, index):
        return self._matrix_list[index-1].copy()

    def column(self, index):
        return [row[index-1] for row in self._matrix_list]