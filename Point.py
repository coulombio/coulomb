import math

from Coordinate import Coordinate
from E_Field import E_Field
from g_Field import g_Field
class Point(Coordinate):


    def __init__(self,x, y):
       Coordinate.__init__(self, x, y)
       self.E = E_Field(self, x, y)
       self.g = g_Field(self, x, y)

    def updateVectors(self, ObjectList):

        self.E.calculateEField(ObjectList)
        self.g.calculateGField(ObjectList)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"