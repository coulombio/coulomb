from Object import Object
from Coordinate import Coordinate
from Point import Point
class System(object):
    def __init__(self, list):
        self.list = list


    def calculateCOM(self):
        self.COMx = 0
        self.COMy = 0
        self.totalMass = 0
        for point in self.list:
            self.COMx = self.COMx + (point.mass * point.x)
            self.COMy = self.COMy + (point.mass * point.y)
            self.totalMass = self.totalMass + point.mass
        self.COMx = self.COMx / self.totalMass
        self.COMy = self.COMy / self.totalMass
        self.COM = Point(self.COMx, self.COMy)
        return self.COM


    def add(self, point):
        self.list.append(point)

    def update(self):
        for point in self.list:
            point.move()




