from Point import Point
import math
from Coordinate import Coordinate
from Force import Force
class Object(Point):
    def __init__(self, name, mass, charge, x, y, velx, vely, accx, accy, fixed):
        Point.__init__(self, x, y)
        self.name = name
        self.mass = mass
        self.charge = charge
        self.velx = velx
        self.vely = vely
        self.accx = accx
        self.accy = accy
        self.rigid = fixed
        self.ForceList = []
        self.OverrideE = None
        self.OverrideG = None

    def addForce(self, F):
        self.ForceList.append(F)

    def calculateEForce(self, Points, Override):
        if Override is None:
            P = Point(self.x, self.y)
            P.E.calculateEField(Points)
            self.EForce = P.E.r * self.charge
            self.EForce_Direction = P.E.theta
        else:
            self.EForce = Override.r * self.charge
            self.EForce_Direction = Override.theta

    def calculateGForce(self, Points, OverrideG):
        if OverrideG is None:
            P = Point(self.x, self.y)
            P.g.calculateGField(Points)
            self.gForce = P.g.r * self.mass
            self.gForce_Direction = P.g.theta
        else:
            self.gForce = OverrideG.r * self.charge
            self.gForce_Direction = OverrideG.theta


    def OverrideEField(self, OverrideE):
        self.OverrideE = OverrideE

    def OverrideGField(self, OverrideG):
        self.OverrideG = OverrideG

    def updateForces(self, Points,):
        self.calculateEForce(Points, self.OverrideE)
        self.calculateGForce(Points, self.OverrideG)
        self.Forcex = (self.EForce * math.cos(self.EForce_Direction * math.pi /180)) + (self.gForce * math.cos(self.gForce_Direction * math.pi /180))
        self.Forcey = (self.EForce * math.sin(self.EForce_Direction * math.pi /180)) + (self.gForce * math.sin(self.gForce_Direction * math.pi /180))

        for force in self.ForceList:
            self.Forcex = self.Forcex + force.i
            self.Forcey = self.Forcey + force.j

        self.Force = (self.Forcex**2 + self.Forcey**2)**0.5
        self.Force_Direction = math.atan2(self.Forcey, self.Forcex) * 180 / math.pi

    def move(self, time, Points):

        if (self.rigid == False):
            time = time * 10000
            magnitude = 100000000
            self.updateForces(Points)
            for t in range(0, int(time)):
                self.accx = self.Forcex / self.mass
                self.accy = self.Forcey / self.mass

                self.velx = self.velx + (0.0001 * self.accx)
                self.vely = self.vely + (0.0001 * self.accy)

                self.x = self.x + (0.0001 * self.velx)
                self.y = self.y + (0.0001 * self.vely)


                self.updateForces(Points)



    def calculateEnergy(self, Points):
        self.K = 0.5 * self.mass * (self.velx^2 + self.vely^2)

        P = Point( self.x, self.y)

        P.E.calculateVoltage(Points)
        self.UE = P.E.Potential

        P.g.calculateVoltage(Points)
        self.UG = P.g.Potential

        self.E = self.K + self.UG + self.UE