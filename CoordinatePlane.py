from Point import Point
from Object import Object
from System import System
import django

print(django.get_version())

A = Object("A", 1, 1, 0, 1, 0, 0, 0, 0)
B = Object("B", 1, 0,0 , 0, 0, 0, 0, 0)
P = Point(0, 6371000)

ObjectList = []
PointList = []


time = 0

ObjectList.append(A)
ObjectList.append(B)
PointList.append(P)
system = System(ObjectList)

for p in PointList:
    p.updateVectors(system.list)
    print(str(P.E))
    print (str(P.g))

for obj in ObjectList:
    obj.updateForces(ObjectList)
    print ("The force on object " + obj.name + " is " + str(obj.Force) + " Newtons at " + str(obj.Force_Direction) + " degrees.")


print "The COM is: (" + system.calculateCOM().__str__()

A.move(1, ObjectList)
print A.x
print A.y

print A.velx
print A.vely

print A.accx
print A.accy

A.updateForces(ObjectList)
print "The force on object " + A.name + " is " + str(A.Force) + " Newtons at " + str(
        A.EForce_Direction) + " degrees."

print "The COM is: (" + system.calculateCOM().__str__()
