class ConnectGame:
    def __init__(self, board):
        self.board = board.replace(' ', '').split('\n')

    def get_winner(self):
        visited, visit = set(), []
        directions = [(-1, 0), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 1)]

        for y in range(len(self.board)):
            visit.append((0, y, 'X'))

        for x in range(len(self.board[0])):
            visit.append((x, 0, 'O'))

        while visit:
            temp = visit.pop(0)

            if temp in visited:
                continue

            visited.add(temp)
            x, y, key = temp

            if y < 0 or y >= len(self.board):
                continue

            if x < 0 or x >= len(self.board[y]):
                continue

            if self.board[y][x] != key:
                continue

            if key == 'X' and x == len(self.board[0]) - 1:
                return key

            elif key == 'O' and y == len(self.board) - 1:
                return key

            for _x, _y in directions:
                visit.append((x + _x, y + _y, key))

        return ''
