import math

from Coordinate import Coordinate
from E_Field import E_Field
from g_Field import g_Field
class Point(Coordinate):


    def __init__(self,x, y):
        Coordinate.__init__(self, x, y)
        self.E = E_Field(self, x, y)
        self.g = g_Field(self, x, y)
        self.OverrideE = None
        self.OverrideG = None

    def updateVectors(self, ObjectList):
        if self.OverrideE is None:
            self.E.calculateEField(ObjectList)
        else:
            self.E.setVectorRect(self.OverrideE.i, self.OverrideE.j)
        if self.OverrideG is None:
            self.g.calculateGField(ObjectList)
        else:
            self.g.setVectorRect(self.OverrideG.i, self.OverrideG.j)


    def OverrideEField(self, OverrideE):
        self.OverrideE = OverrideE

    def OverrideGField(self, OverrideG):
        self.OverrideG = OverrideG