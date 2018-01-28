from Game.Bead import *
class Verdict:


    def __init__(self,Arry):
        self.__arry = Arry
        self.__len = len(self.__arry)
        self.__wide = len(self.__arry[0])


    def GetSameColorBeadCnt(self,axisXRange,axisYRange):
        Color = self.__arry[axisXRange[0]][axisYRange[0]].Color
        Count = 0

        for axisX,axisY in zip(axisXRange,axisYRange):
            if self.__arry[axisX][axisY].Color == COLOR['BLANK']:
                    return Count
            if self.__arry[axisX][axisY].Color == Color :
                    Count += 1
        return Count

    def VerdictDraw(self):
        for axisX in range(self.__len):
            for axisY in range(self.__wide):
                if self.__arry[axisX][axisY].Color == COLOR['BLANK']:
                    return False
        return True


  
    def VerdictWinner(self,ConditionNum):
        len = self.__len
        wide = self.__wide

        for axisX in range(self.__len):
            for axisY in range(self.__wide):
                RangeDict = self.__getRangeDict(axisX,axisY,self.__len,self.__wide)
                for Direction in RangeDict.keys():
                    Cnt = self.GetSameColorBeadCnt(RangeDict[Direction]['X'],RangeDict[Direction]['Y'])
                    if Cnt >= ConditionNum:
                        return self.__arry[axisX][axisY].Color

        return None
                                
    def __getRangeDict(self,axisX,axisY,BoardLen,BoardWide):
        LeftBorder  = -1
        UpBorder    = -1
        RightBorder = BoardLen
        DownBorder  = BoardWide
       
        RangeDict = {
                        'UP'        :{'X':range(axisX,LeftBorder,-1), 'Y':[axisY] * BoardWide},
                        'RIGHT'     :{'X':range(axisX,RightBorder,1), 'Y':[axisY] * BoardWide},
                        'UP'        :{'X':[axisX] * BoardLen,         'Y':range(axisY,UpBorder,-1)},
                        'DOWN'      :{'X':[axisX] * BoardLen,         'Y':range(axisY,DownBorder,1)},
                        'UP_LEFT'   :{'X':range(axisX,LeftBorder,-1), 'Y':range(axisY,UpBorder,-1)},
                        'UP_RIGHT'  :{'X':range(axisX,RightBorder),   'Y':range(axisY,UpBorder,-1)},
                        'DOWN_LEFT' :{'X':range(axisX,LeftBorder,-1), 'Y':range(axisY,DownBorder)},
                        'DOWN_RIGHT':{'X':range(axisX,RightBorder),   'Y':range(axisY,DownBorder)}
                    }
        return RangeDict        


