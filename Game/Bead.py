COLOR = {'BLACK': '@', 'WHITE': 'O', 'BLANK': ' '}


class Bead(object):
    """description of class"""

    def __init__(self, Position, BColor):
        self.Position = Position
        self.__Color = BColor

    def __getColor(self):
        return self.__Color

    def __setColor(self, value):
        self.__Color = value

    Color = property(__getColor, __setColor)
