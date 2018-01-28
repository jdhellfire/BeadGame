import unittest
from  Game.Bead  import *
from  Game.Board import *
from  Game.Location import *
from  Game.Player import *
from  Game.GameIO import *
from  Game.ProcCtrl import *

class Test_GameFT(unittest.TestCase):
    def test_ATC_000_001(self):
        '''Board Add Bead and Get'''
        CreateBead = Bead(Location(0,0),COLOR['WHITE'])
        GameBoard = Board()
        GameBoard.AddBead(CreateBead)
        ObtainBead= GameBoard.GetBead(Location(0,0))
        self.assertEqual(CreateBead,ObtainBead,'Bead Add and Set Fail')
    
    def test_ATC_000_002(self):
        '''Human Down A Chess'''
        GameBoard = Board()
        HumanPlayer = Human(COLOR['BLACK'],GameBoard)
        bead = HumanPlayer.DownBeadAtPos(0,0)
        self.assertEqual(bead.Color,COLOR['BLACK'])  
        self.assert_(bead.Position.AxisX==0 and bead.Position.AxisY==0)

    def test_ATC_000_003(self):
        '''PC Down A Chess'''
        GameBoard = Board()
        PcPlayer = Pc(COLOR['WHITE'],GameBoard)
        bead = PcPlayer.DownBead()
        self.assertEqual(bead.Color,COLOR['WHITE'])
        
    def test_ATC_000_004(self):
        '''Human Down A Chess At duplicate place'''
        GameBoard = Board()
        HuManPlayer = Human(COLOR['BLACK'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(0,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(0,0)
        self.assertEqual(None,bead)
    
    #def test_ATC_000_005(self):
    #    '''Display hole Game Board'''
    #    GameBoard = Board()
    #    Displayer = GameIO(GameBoard)
    #    Displayer.PrintGameBoard()

    ##======Verdict Arithmetic Test===========
    def test_ATC_001_001(self):
        '''Check Continuous Bead Cnt'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(0,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(1,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(2,0)
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        SameCount = Arithmetic.GetSameColorBeadCnt(range(9),[0]*9)
        SameCount1 = Arithmetic.GetSameColorBeadCnt([0]*9,range(9))
        Displayer = GameIO(GameBoard)
        Displayer.PrintGameBoard()

        self.assertEqual(3,SameCount)
        self.assertEqual(1,SameCount1)

   
    ##=======LefUpCorner==========
    def test_ATC_002_001(self):
        '''LeftUp Corner Down 3 Continuous Bead,Check Winner'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(0,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(1,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(2,0)
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        WinnerColor = Arithmetic.VerdictWinner(3)
        self.assertEqual(COLOR['WHITE'],WinnerColor)
    
    def test_ATC_002_002(self): 
        '''LeftUp Corner Right 3 Continuous Bead,Check Winner'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(0,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(0,1)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(0,2)
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        WinnerColor = Arithmetic.VerdictWinner(3)
        self.assertEqual(COLOR['WHITE'],WinnerColor)

    def test_ATC_002_003(self):
        '''LeftUp Corner RightDown 3 Continuous Bead,Check Winner'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(0,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(1,1)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(2,2)
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        WinnerColor = Arithmetic.VerdictWinner(3)
        Displayer = GameIO(GameBoard)
        Displayer.PrintGameBoard()
        self.assertEqual(COLOR['WHITE'],WinnerColor)

    def test_ATC_002_003(self):
        '''LeftDown Corner UP 3 Continuous Bead,Check Winner'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(8,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(7,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(6,0)
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        WinnerColor = Arithmetic.VerdictWinner(3)
        Displayer = GameIO(GameBoard)
        Displayer.PrintGameBoard()
        self.assertEqual(COLOR['WHITE'],WinnerColor)
    
    def test_ATC_002_003(self):
        '''LeftDown Corner Right 3 Continuous Bead,Check Winner'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(8,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(8,1)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(8,2)
        GameBoard.AddBead(bead)
        PcPlayer = Pc(COLOR['BLACK'],GameBoard)
        bead = PcPlayer.DownBead()
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        WinnerColor = Arithmetic.VerdictWinner(3)
        Displayer = GameIO(GameBoard)
        Displayer.PrintGameBoard()
        self.assertEqual(COLOR['WHITE'],WinnerColor)

    def test_ATC_002_004(self):
        '''LeftDown Corner UpRight 3 Continuous Bead,Check Winner'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(8,0)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(7,1)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(6,2)
        GameBoard.AddBead(bead)
        PcPlayer = Pc(COLOR['BLACK'],GameBoard)
        bead = PcPlayer.DownBead()
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        WinnerColor = Arithmetic.VerdictWinner(3)
        Displayer = GameIO(GameBoard)
        Displayer.PrintGameBoard()
        self.assertEqual(COLOR['WHITE'],WinnerColor)


    def test_ATC_002_005(self):
        '''Center Corner Up 3 Continuous Bead,Check Winner'''
        GameBoard  = Board()
        HuManPlayer = Human(COLOR['WHITE'],GameBoard)
        bead = HuManPlayer.DownBeadAtPos(2,3)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(3,3)
        GameBoard.AddBead(bead)
        bead = HuManPlayer.DownBeadAtPos(1,3)
        GameBoard.AddBead(bead)
        PcPlayer = Pc(COLOR['BLACK'],GameBoard)
        bead = PcPlayer.DownBead()
        GameBoard.AddBead(bead)
        Arithmetic = Verdict(GameBoard.BeadArry)
        WinnerColor = Arithmetic.VerdictWinner(3)
        Displayer = GameIO(GameBoard)
        Displayer.PrintGameBoard()
        self.assertEqual(COLOR['WHITE'],WinnerColor)


    def test_ATC_003_006(self):
        '''Game Draw test'''
        GameBoard  = Board()
        GameBoard.InitBoard(COLOR['WHITE'])
        Arithmetic = Verdict(GameBoard.BeadArry)
        Displayer = GameIO(GameBoard)
        Displayer.PrintGameBoard()
        result = Arithmetic.VerdictDraw()
        self.assertAlmostEqual(True,True)



if __name__ == '__main__':


    unittest.main()
