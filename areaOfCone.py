'''
Write a python program which creates a class named Cone and write a
function calculate_area which calculates the area of the Cone.
'''
import math
class ConeArea:
    def __init__(self):
        pass
    def getArea(self, r, h):
        #SA=πr(r+sqrt(h**2+r**2))
        return math.pi*r*(r+math.sqrt(h**2+r**2))
coneArea=ConeArea()
radius=input("Input the radius (numeric):")
height=input("Input the height (numeric):")
print("Area is {}".format(coneArea.getArea(float(radius),float(height))))