from Game.Bead import*
from Game.Board import*
import copy
class Memory(object):
    """description of class"""
     
       
    def __init__(self):
        self.__BoardLst = []
        self.__CurrentRecordIndex = -1



    def Save(self,GameBoard):
        self.__CurrentRecordIndex += 1
        self.__BoardLst.append(GameBoard)


    def Load(self):
        Record = self.__BoardLst[abs(self.__CurrentRecordIndex -1)]       
        return copy.deepcopy(Record)




