from Coordinate import Coordinate
import math
class Vector(object):
    p = Coordinate
    def __init__(self):
        self.p = 0
        self.i = 0
        self.j = 0
        self.r = 0
        self.theta = 0
        self.units = ""

    def setVectorPolar (self, magnitude, direction):
        self.r = magnitude
        self.theta = direction
        self.resolve(self.r, self.theta)

    def setVectorRect(self, x, y):
        self.i = x
        self.j = y
        self.combine(self.i, self.j)

    def combine (self, x, y):
        self.r = (x**2 + y**2)**0.5
        self.theta = math.atan2((y) , (x)) * 180 / math.pi

    def resolve(self, magnitude, direction):
        self.i = self.r * math.cos(self.theta * math.pi /180)
        self.j = self.r * math.sin(self.theta * math.pi /180)

    def __str__(self):
       return "(" + str(self.i) + ", " + str(self.j) + ") " + self.units + ", which is " + str(self.r) + " " + self.units + " at " + str(self.theta) + " degrees."

