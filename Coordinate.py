import math
class Coordinate(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def getDistance(self, point):
        r = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return r

    def getAngle(self, point):
        theta = math.atan2((point.y - self.y) , (point.x - self.x)) * 180 / math.pi
        return

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"