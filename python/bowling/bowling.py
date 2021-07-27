class BowlingGame(object):
    def __init__(self):
        self.__score = 0
        self.__index = 0
        self.__extra = []
        self.__frame = []

    def __game_on(self):
        return self.__index < 10 or self.__extra

    def roll(self, pins):
        if not self.__game_on():
            raise IndexError('Can\'t roll after game is over')

        if pins < 0:
            raise ValueError('Negative roll is invalid')

        self.__frame.append(pins)
        frame_score = sum(self.__frame)
        if frame_score > 10:
            raise ValueError('Pin count exceeds pins on the lane')

        self.__score += len(self.__extra) * pins
        self.__extra = [1 for i in self.__extra if i == 2]

        if self.__index < 10:
            self.__score += pins
            if frame_score == 10:
                self.__extra.append(3 - len(self.__frame))

        if self.__game_on() and (frame_score == 10 or len(self.__frame) == 2):
                self.__frame = []
                self.__index += 1

    def score(self):
        if self.__game_on():
            raise IndexError('Play more')
        return self.__score
