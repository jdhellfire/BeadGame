# codeing= utf-8
from graphics import *

from Game.ProcCtrl import *


class GameUI(object):
    """Game Bead GI"""

    def __init__(self, Ctrl):
        self.SetAppearance()

        self.__ctrl = Ctrl
        self.__board = self.__ctrl.GetGameBoard()
        self.__elemObjLst = []
        self.__MsgObjLst = []
        self.__CLICK_ACTION = {
            'BTN_LOAD': self.__btnReloadAction,
            'BTN_EXIT': self.__btnExitAction,
            'BTN_START': self.__btnStartAction,
            'BEAD_TABLE': self.__beadTableAction,
            'NO_DEFINE': self.__noDefineAction

        }

    # ==================主流程

    def Run(self):
        self.__draw()

        ExitFlag = False

        while True:
            self.DrawBead()
            self.__ctrl.SaveGame()

            for player in self.__ctrl.GetPlayerLst():

                if isinstance(player, Pc):
                    self.__pcPlayerHandle(player)

                else:
                    if self.__HMPlayerHandle(player) is None:
                        return

                self.DrawBead()

                Winner = self.__ctrl.VerdictWinLos()
                if Winner is not None:
                    self.UIMsgShow('Winner is %s' % Winner)

                if self.__ctrl.VerdictDraw():
                    self.UIMsgShow('Game is Draw')

            if ExitFlag:
                break

                # ==================UI 外观显示=================

    def SetAppearance(self, CELL_LEN=30, BORDER_LEN=30, BORDER_WIDE=30, BOARD_SIZE=(9, 9), BEAD_SIZE=11):
        self.CELL_LEN = CELL_LEN
        self.BORDER_LEN = BORDER_LEN
        self.BORDER_WIDE = BORDER_WIDE
        self.BOARD_SIZE = BOARD_SIZE
        self.BEAD_SIZE = BEAD_SIZE
        self.BOARD_LEN = (self.BOARD_SIZE[0] - 1) * self.CELL_LEN + 2 * self.BORDER_LEN
        self.BOARD_WIDE = (self.BOARD_SIZE[1] - 1) * self.CELL_LEN + 2 * self.BORDER_WIDE

        print(self.BOARD_LEN, self.BOARD_WIDE)

        self.FROM_ELEM = {
            'BTN_LOAD': {
                'POINT_UPLEFT': Point(self.BORDER_LEN, self.BOARD_WIDE - 20),
                'POINT_DOWNRIGHT': Point(100, self.BOARD_WIDE),
                'COLOR': 'yellow',
                'TEXT': 'LOAD'
            },
            'BTN_EXIT': {
                'POINT_UPLEFT': Point(self.BOARD_LEN - 100, self.BOARD_WIDE - 20),
                'POINT_DOWNRIGHT': Point(self.BOARD_LEN - self.BORDER_LEN, self.BOARD_WIDE),
                'COLOR': 'yellow',
                'TEXT': 'EXIT'

            },
            'BTN_START': {
                'POINT_UPLEFT': Point(self.BOARD_LEN / 2 - 40, self.BOARD_WIDE - 20),
                'POINT_DOWNRIGHT': Point(self.BOARD_LEN / 2 + 40, self.BOARD_WIDE),
                'COLOR': 'yellow',
                'TEXT': 'RESTART'
            },
            'BEAD_TABLE': {
                'POINT_UPLEFT': Point(self.BORDER_LEN, self.BORDER_WIDE),
                'POINT_DOWNRIGHT': Point(self.BOARD_LEN - self.BORDER_LEN,
                                         self.BOARD_WIDE - self.BORDER_WIDE),
            }

        }

    def UIMsgShow(self, Msg):
        MsgText = Text(Point(self.BOARD_LEN / 2, self.BORDER_WIDE / 2), Msg)
        MsgText.setSize = 5
        MsgText.draw(self.__form)
        self.__MsgObjLst.append(MsgText)

    def __draw(self):
        self.__drawForm()
        self.__drawLine()

        for Btn in ['BTN_LOAD', 'BTN_EXIT', 'BTN_START']:
            self.__drawBtn(self.FROM_ELEM[Btn]['POINT_UPLEFT'],
                           self.FROM_ELEM[Btn]['POINT_DOWNRIGHT'],
                           self.FROM_ELEM[Btn]['COLOR'],
                           self.FROM_ELEM[Btn]['TEXT'])

    def __drawForm(self):
        self.__form = GraphWin("BeadGame", width=self.BOARD_LEN, height=self.BOARD_WIDE)
        self.__form.setBackground('blue')

    def __drawLine(self):
        for WIDE in range(self.BOARD_SIZE[1]):
            LineObj = Line(Point(self.BORDER_LEN, WIDE * self.CELL_LEN + self.BORDER_WIDE),
                           Point(self.BOARD_LEN - self.BORDER_LEN, WIDE * self.CELL_LEN + self.BORDER_WIDE))
            LineObj.draw(self.__form)
            self.__elemObjLst.append(LineObj)

        for LEN in range(self.BOARD_SIZE[0]):
            LineObj = Line(Point(LEN * self.CELL_LEN + self.BORDER_LEN, self.BORDER_WIDE),
                           Point(LEN * self.CELL_LEN + self.BORDER_LEN, self.BOARD_WIDE - self.BORDER_WIDE))
            LineObj.draw(self.__form)
            self.__elemObjLst.append(LineObj)

    def __drawBtn(self, Point1, Point2, Color, text):
        objBtn = Rectangle(Point1, Point2)
        objBtn.setFill('yellow')
        objBtn.setOutline('black')
        PBtnCenter = objBtn.getCenter()
        BtnText = Text(PBtnCenter, text)

        objBtn.draw(self.__form)
        BtnText.draw(self.__form)
        return (objBtn, BtnText)

    def DrawBead(self):
        self.__clrForm()
        BeadArry = self.__board.BeadArry
        for axisX in range(len(BeadArry)):
            for axisY in range(len(BeadArry[0])):

                if BeadArry[axisX][axisY].Color == COLOR['BLANK']:
                    continue
                if BeadArry[axisX][axisY].Color == COLOR['BLACK']:
                    Color = 'BLACK'
                else:
                    Color = 'WHITE'

                X = self.BORDER_LEN + axisX * self.CELL_LEN
                Y = self.BORDER_WIDE + axisY * self.CELL_LEN

                circ = Circle(Point(X, Y), self.BEAD_SIZE)
                circ.setFill(Color)
                circ.draw(self.__form)
                self.__elemObjLst.append(circ)

    def __clrForm(self):
        for LineObj in self.__elemObjLst:
            LineObj.undraw()
        self.__drawLine()

    def __clrMsg(self):
        for Msg in self.__MsgObjLst:
            Msg.undraw()

    # ==================鼠标点击及处理==================

    def Click(self):
        return self.__form.getMouse()

    def __clickWhere(self, Pos):
        for Elem in self.FROM_ELEM.keys():
            if self.FROM_ELEM[Elem]['POINT_UPLEFT'].x <= Pos.x < self.FROM_ELEM[Elem]['POINT_DOWNRIGHT'].x and \
                                    self.FROM_ELEM[Elem]['POINT_UPLEFT'].y <= Pos.y < self.FROM_ELEM[Elem][
                        'POINT_DOWNRIGHT'].y:
                print(Elem)
                return Elem
        print('NO_DEFINE')
        return 'NO_DEFINE'

    def __coverPosToArryAxis(self, Pos):
        X = int(Pos.x - self.BORDER_LEN) / self.CELL_LEN
        if int(Pos.x - self.BORDER_LEN) % self.CELL_LEN > 2 * self.CELL_LEN / 3:
            X += 1
        Y = int(Pos.y - self.BORDER_WIDE) / self.CELL_LEN
        if int(Pos.y - self.BORDER_WIDE) % self.CELL_LEN > 2 * self.CELL_LEN / 3:
            Y += 1
        return (X, Y)

    def __pcPlayerHandle(self, player):
        self.__ctrl.AddBeadToGameBoard(player.DownBead())

    def __HMPlayerHandle(self, player):
        while True:
            PosObj = self.Click()
            result = self.__CLICK_ACTION[self.__clickWhere(PosObj)](PosObj, player)
            if not result:
                continue

            return result

    def __btnReloadAction(self, PosObj, player):
        return self.__ctrl.LoadGame()

    def __beadTableAction(self, PosObj, player):
        Pos = self.__coverPosToArryAxis(PosObj)
        return self.__ctrl.AddBeadToGameBoard(player.DownBeadAtPos(Pos[0], Pos[1]))

    def __btnExitAction(self, PosObj, player):
        self.__form.close()
        return False

    def __btnStartAction(self, PosObj, player):
        self.__ctrl.SetGame()
        self.__clrMsg()
        self.DrawBead()
        return True

    def __noDefineAction(self, PosObj, player):
        return True
