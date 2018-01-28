class Location(object):
    """description of class"""

    def __init__(self, AxisX, AxisY):
        self.__axisX = int(AxisX)
        self.__axisY = int(AxisY)

    def __getAxisX(self):
        return self.__axisX

    def __setAxisX(self, value):
        self.__axisX = value

    def __getAxisY(self):
        return self.__axisY

    def __setAxisY(self, value):
        self.__axisY = value

    AxisX = property(__getAxisX, __setAxisX)
    AxisY = property(__getAxisY, __setAxisY)
