'''
Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
'''

class Triangle:
    def __init__(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c

class TriangleArea(Triangle):
    def __init__(self,a,b,c):
        Triangle.__init__(self,a,b,c)

    def getArea(self):
        s=(self._a + self._b + self._c)/2
        return (s*(s-self._a)*(s-self._b)*(s-self._c))**0.5

tArea=TriangleArea(24,30,18)
area=tArea.getArea()
print("Area of the triangle is {}".format(area))