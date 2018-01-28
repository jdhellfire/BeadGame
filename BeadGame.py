from Game.ProcCtrl import*
from GameUI.UI import*

GameParam = {
                'WIN_NUM_CONDITION':5,
                'BOARD_SIZE':(9,9),
                'BOARD_TEMP':1,
                'START_PLAYER':'Human'  #Human or Pc
    
             }


if __name__ == '__main__':

    Ctrl = ProcCtrl()    
    Ctrl.SetGame(GameParam)
    UI = GameUI(Ctrl)
    UI.SetAppearance(BOARD_SIZE=GameParam['BOARD_SIZE'])
    UI.Run()


