# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:38:49 2024

@author: Aëlias
"""
from Point_2D import Point_2D

class Rectangle :
    """ object class Rectangle
    """

    def __init__(self,
				 name="Rectangle",
				 A=Point_2D("A", 0, 0),
				 B=Point_2D("B", 1, 1)):
        """ Rectangle class constructor
        :name: str name of the rectangle
        :corner1: Point_3D first node of the rectangle
        :corner2: Point_3D second node of the rectangle
        """
        self.name=name
        self.corner1=A
        self.corner2=B

    def perimeter(self):
        return (2*abs(self.corner1.x - self.corner2.x) + 2*abs(self.corner1.y - self.corner2.y))

    def __str__(self):
        return f"Rectangle {self.name} defined by the corners {self.corner1} and {self.corner2}"

    def area(self):
        return (abs(self.corner1.x - self.corner2.x) * abs(self.corner1.y - self.corner2.y))

'''

class Rectangle:
    def __init__(self, name = 'Rectangle', p1 = Point_3D(), p2 = Point_3D()):
        self.name = name
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"({self.name},{self.p1},{self.p2})"

    def length(self):
        return abs(self.p1.x - self.p2.x)

    def width(self):
        return abs(self.p1.y - self.p2.y)

    def perimeter(self):
        return 2*self.length()+2*self.width()

    def area(self):
        return self.length()*self.width()

# Test of the class Rectangle
if __name__ == '__main__':
    Rectangle1 = Rectangle()
    print("Rectangle 1 abscisse = ", type(Rectangle1.p1))
    Rectangle2 = Rectangle(Point(1,1),Point(5,5))
    print("Rectangle 2 Ordonnee = ", Rectangle2.p1)

    print(Rectangle1)
    print(Rectangle2)

    print(Rectangle2.perimeter())
'''
