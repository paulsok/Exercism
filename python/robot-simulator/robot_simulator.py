# Globals for the directions
# Change the values as you see fit
EAST = lambda x, y: (x + 1, y)
WEST = lambda x, y: (x - 1, y)
SOUTH = lambda x, y: (x, y - 1)
NORTH = lambda x, y: (x, y + 1)
DIREC = (EAST, SOUTH, WEST, NORTH)


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.NEWS = direction
        self.xy = (x, y)

    def move(self, cmd: str):
        for s in cmd:
            if s == 'A':
                self.xy = self.NEWS(*self.xy)
            else:
                m = (s == 'L') * 2 - 1
                idx = DIREC.index(self.NEWS) - m
                self.NEWS = DIREC[idx % 4]

    @property
    def coordinates(self):
        return self.xy

    @property
    def direction(self):
        return self.NEWS
