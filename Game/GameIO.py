class GameIO(object):
    """description of class"""
    def __init__(self,GameBoard):
        self.__gameBoard = GameBoard

    def PrintGameBoard(self):
        print('\n'+'='* self.__gameBoard.LEN)
        for axisX in range(self.__gameBoard.LEN):
            Line =[]
            for axisY in range(self.__gameBoard.WIDE):
                Line.append( self.__gameBoard.BeadArry[axisX][axisY].Color)
            print(Line)




