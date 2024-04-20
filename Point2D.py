# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:27:43 2024

@author: Aëlias
"""

class Point_2D:
    """object class Point_2D
    """
    def __init__(self,
                 name='Point',
				 x:int=-1,
				 y:int=-1):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point in 2 dimensions {self.name}({self.x},{self.y})"


# Test of the class Point_2D
if __name__ == '__main__':
    Point1 = Point_2D(0,0)
    print("Point 1 abscisse = ", Point1.x)
    Point2 = Point_2D(1,1)
    print("Point 2 Ordonnee = ", Point2.y)
    
    print(Point1)
    print(Point2)
