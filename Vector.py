from Coordinate import Coordinate
import math
class Vector(Coordinate):
    p = Coordinate
    def __init__(self, x, y):
        Coordinate.__init__(self, x, y)
        self.p = 0
        self.i = 0
        self.j = 0
        self.r = 0
        self.theta = 0
        self.units = 0

    def __str__(self):
       return " at (" + str(self.x) + ", " + str(self.y) + ") is (" + str(self.i) + ", " + str(self.j) + ") " + self.units + ", which is " + str(self.r) + " " + self.units + " at " + str(self.theta) + " degrees."

