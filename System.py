from Object import Object
from Force import Force
from Coordinate import Coordinate
from Point import Point
class System(Object):
    def __init__(self, list):
        Object.__init__(self, None, None, None, None, None, None, None, None, None, None)
        self.list = list
        self.ExternalForces = []
        self.Force = Force()


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


    def calculateExternalForces(self):
        self.ExternalForces = []
        fx = 0
        fy = 0
        for point in self.list:
            for force in point.ForceList:
                self.ExternalForces.append(force)
        for force in self.ExternalForces:
            fx = fx + force.i
            fy = fy + force.j
        self.Force.setVectorRect(fx, fy)





    def add(self, point):
        self.list.append(point)



    def update(self):
        for point in self.list:
            point.move()




