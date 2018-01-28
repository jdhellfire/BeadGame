import copy
from Game.GameIO import *
from Game.Board import *
from Game.Bead import *
from Game.Player import *
from Game.Arithmetic import *
from Game.Memory import *


class ProcCtrl(object):
    """description of class"""

    def __init__(self):
        self.__initGame()
        self.__gameParaM = None

    def SetGame(self, ParaM=None):
        if None == ParaM:
            ParaM = self.__gameParaM
        try:
            self.__winNumCondition = ParaM['WIN_NUM_CONDITION']
            if 'Human' == ParaM['START_PLAYER'] or 'Pc' == ParaM['START_PLAYER']:
                self.__startPlayer = ParaM['START_PLAYER']

            self.__gameBoard.LEN = ParaM['BOARD_SIZE'][0]
            self.__gameBoard.WIDE = ParaM['BOARD_SIZE'][1]
            self.__gameBoard.InitBoard(TempNum=ParaM['BOARD_TEMP'])
            self.__verdict = Verdict(self.__gameBoard.BeadArry)
        except:
            print('Param Error')
            return
        self.__gameParaM = ParaM

    def LoadGame(self):
        BeadArry = self.__memory.Load()
        if None != BeadArry:
            self.__gameBoard.BeadArry = BeadArry
            self.__gameIO.PrintGameBoard()
            self.__verdict = Verdict(self.__gameBoard.BeadArry)
            return True
        return False

    def SaveGame(self):
        self.__gameIO.PrintGameBoard()
        self.__memory.Save(copy.deepcopy(self.__gameBoard.BeadArry))

    def VerdictWinLos(self):
        Color = self.__verdict.VerdictWinner(self.__winNumCondition)
        if None != Color:
            return Color
        return None

    def VerdictDraw(self):
        if True == self.__verdict.VerdictDraw():
            return True
        return False

    def GetPlayerLst(self):
        if 'Human' == self.__startPlayer:
            return [self.__playerHM, self.__playerPc]
        return [self.__playerPc, self.__playerHM]

    def AddBeadToGameBoard(self, bead):
        return self.__gameBoard.AddBead(bead)

    def GetGameBoard(self):
        return self.__gameBoard

    def __initGame(self):
        self.__winNumCondition = 3
        self.__startPlayer = 'Pc'
        self.__gameBoard = Board()
        self.__memory = Memory()
        self.__verdict = Verdict(self.__gameBoard.BeadArry)
        self.__gameIO = GameIO(self.__gameBoard)
        self.__playerHM = Human(COLOR['WHITE'], self.__gameBoard)
        self.__playerPc = Pc(COLOR['BLACK'], self.__gameBoard)
        self.SaveGame()
