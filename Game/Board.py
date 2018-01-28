from Game.Location import *
from Game.Bead import *


class Board(object):
    """container of Bead"""

    def __init__(self, Color=COLOR['BLANK'], TempNum=0):
        self.LEN = 9
        self.WIDE = 9
        self.InitBoard(Color=Color, TempNum=TempNum)

    def InitBoard(self, Color=COLOR['BLANK'], TempNum=0):
        self.__beadArry = Template(self.LEN, self.WIDE, Color).CreateBeadArry(TempNum)

    def AddBead(self, bead):
        try:
            print(bead)
            self.__beadArry[bead.Position.AxisX][bead.Position.AxisY] = bead
        except Exception as e:
            print(e)
            print("Add Bead Fail")
            return False
        return True

    def GetBead(self, Position):
        return self.__beadArry[Position.AxisX][Position.AxisY]

    def GetEmptyCell(self):
        EmptyCellLst = []
        for AxisX in range(self.LEN):
            for AxisY in range(self.WIDE):
                if self.__beadArry[AxisX][AxisY].Color == COLOR['BLANK']:
                    EmptyCellLst.append((AxisX, AxisY))

        return EmptyCellLst

    def __getBeadArry(self):
        return self.__beadArry

    def __setBeadArry(self, value):
        self.__beadArry = value

    BeadArry = property(__getBeadArry, __setBeadArry)


class Template:
    def __init__(self, ArryLen, ArryWide, InitColor=COLOR['BLANK']):
        self.__Len = ArryLen
        self.__Wide = ArryWide

        self.__TEMPLATE = {
            1: {(0, 0, COLOR['BLACK']), (self.__Len - 1, 0, COLOR['WHITE']),

                (0, self.__Wide - 1, COLOR['BLACK']), (self.__Len - 1, self.__Wide - 1, COLOR['WHITE'])},

        }

        self.__beadArry = [[0 for ArryX in range(self.__Len)] \
                           for ArryY in range(self.__Wide)]

        for AxisX in range(self.__Len):
            for AxisY in range(self.__Wide):
                self.__beadArry[AxisX][AxisY] = Bead(Location(AxisX, AxisY), InitColor)

    def CreateBeadArry(self, TempNum):
        num = self.__TEMPLATE.keys()
        print(num)
        #if self.__TEMPLATE.has_key(TempNum):
        if TempNum in self.__TEMPLATE.keys():
            for BeadInfo in self.__TEMPLATE[TempNum]:
                self.__beadArry[BeadInfo[0]][BeadInfo[1]].Color = BeadInfo[2]
                print(self.__beadArry[BeadInfo[0]][BeadInfo[1]].Color)
        return self.__beadArry
