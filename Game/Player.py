import random
from Game.Location import *
from Game.Bead import *
from Game.Memory import *

class Player(object):
    """description of class"""
    def DownBead(self):pass


class Human(Player):

    def __init__(self,BColor,GameBoard):
        self.__color = BColor
        self.__gameBoard = GameBoard
  
    def DownBead(self):
        return Bead(self.__GetBeadLocation(),self.__color)

    def DownBeadAtPos(self,axisX,axisY):
        if self.__isPosNotEmpty(Location(axisX, axisY)):
            return Bead(Location(axisX,axisY),self.__color)
        return None

    def __GetBeadLocation(self):
        while True:
            Pos=input("\nPlease Input Bead Axis(X,Y):")
            Position = Location(Pos[0],Pos[1])
            if self.__isPosNotEmpty(Position):
                return Position
            print('\nThis Place has Bead,Input again!')

    def __isPosNotEmpty(self,Position):
        EmptyCellLst = self.__gameBoard.GetEmptyCell()
        if (Position.AxisX,Position.AxisY) in EmptyCellLst:
            return True
        return False

    def __getColor(self):
        return self.__color

    def __setColor(self):
        pass
    Color = property(__getColor,__setColor)


class Pc(Player):
    def __init__(self,BColor,GameBoard):
        self.__color = BColor
        self.__gameBoard = GameBoard

    def DownBead(self):
        EmptyCellLst = self.__gameBoard.GetEmptyCell()
        Pos = random.sample(EmptyCellLst,1)[0] 
        return Bead(Location(Pos[0],Pos[1]),self.__color)
    

    def DownBeadAtPos(self,axisX,axisY):
        return self.DownBead()


    def __getColor(self):
        return self.__color

    def __setColor(self):
        pass
    Color = property(__getColor,__setColor)


            