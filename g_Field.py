from Vector import Vector
from Coordinate import Coordinate
import math
class g_Field(Vector):

    def __init__(self, p,x,y):
        Vector.__init__(self, x, y)
        self.units = "Newtons per Kilogram"


    def calculateGField(self, Points):

        self.i = 0
        self.j = 0
        self.theta = 0

        for point in Points:
            if (self.x != point.x or self.y != point.y):
                 E = -6.674 * 10**-11 * point.mass/((self.x - point.x)**2 + (self.y - point.y)**2 )

            if (self.x != point.x or self.y != point.y):
             self.i = self.i + ((E * (self.x - point.x) / (((self.x - point.x) ** 2 + (self.y - point.y) ** 2)) ** 0.5))
             self.j = self.j + ((E * (self.y - point.y) / (((self.x - point.x) ** 2 + (self.y - point.y) ** 2)) ** 0.5))

        self.r = (self.i ** 2 + self.j ** 2) ** 0.5
        if (self.i == 0):
            self.theta = 90
        else:
            self.theta = self.theta + math.atan2((self.j) , (self.i)) * 180 / math.pi


    def calculateVoltage (self, Points):
        self.Potential = 0
        for point in Points:
            if (self.x != point.x or self.y != point.y):
                v = -6.674 * 10**-11 * point.mass/(((self.x - point.x)**2 + (self.y - point.y)**2 )**0.5)
                self.Potential = self.Potential + v

    def __str__(self):
        return "The gravitational field" + Vector.__str__(self)
