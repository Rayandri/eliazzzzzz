# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:38:49 2024

@author: Aëlias
"""
from Point_2D import Point_2D
from Rectangle import Rectangle

class Plane:
    
    def __init__(self,
				 name="plane",
				 Rect=Rectangle("Rect", Point_2D("A", 0,0),Point_2D("B",1,1))):
        self.name=name
        self.rectangle=Rect
        self.w = abs(Rect.corner1.x - Rect.corner2.x)
        self.l= abs(Rect.corner1.y - Rect.corner2.y)
		
    def __str__(self):
        return f"Plane {self.name} characterised by the rectangle {self.rectangle} of width{self.w} and of length{self.l}"

'''
    def __init__(self, name = 'Plan',
                 p1 = Point_3D(),
                 p2 = Point_3D()):
        """ Plan class constructor
        :p1: first node of the plan
        :p2: second node of the plan
        """
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.height = p1.z
        self.length = abs(self.p1.x - self.p2.x)
        self.width = abs(self.p1.y - self.p2.y)
        
    def __str__(self):
        return f"({self.name},{self.p1},{self.p2},{self.height},{self.length},{self.width})"

    def perimeter(self):
        return 2*self.length+2*self.width
    
    def area(self):
        return self.length*self.width

if __name__ == '__main__':
    Plan1 = Plan()
    print("Plan 1 abscisse = ", type(Plan1.p1))
    Plan2 = Plan(Point_3D(1,1,0),Point_3D(5,5,0))
    print("Plan 2 Ordonnee = ", Plan2.p1)
    
    print(Plan1)
    print(Plan2)
    
    print(Plan2.perimeter())
'''