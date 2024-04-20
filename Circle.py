# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:10:47 2024

@author: Aëlias
"""
import numpy as np
from Point2D import Point_2D

class Circle :
    
    def __init__(self,
				 name="Circle",
				 O=Point_2D("O", 0, 0),
				 R=Point_2D("R", 0, 1)):
        
        self.name=name
        self.centre=O
        self.R=R
        self.radius = np.sqrt((self.centre.x - self.R.x)**2 + (self.centre.y - self.R.y)**2)
        
    def __str__(self):
        return f"Circle {self.name} centred at {self.centre} with radius {self.radius}"
    
    def perimeter(self):
        return 2 * np.pi * self.radius
    
    def area(self):
        return np.pi * self.radius**2

'''

class Circle:
    """ object class Circle
    """
    def __init__(self,
                 center: Point_2D,
                 radius: Point_2D,
                 name : str = 'Circle'):
        """ Circle class constructor
        :name: name of the circle
        :c: center of the circle
        :r: point of the circle to define its radius
        """
        self.name = name
        self.c = c
        self.r = r
    
    def __str__(self):
        return f"({self.c},{self.r})"
    
    def radius(self):
        return ((self.c.x-self.r.x)**2 + (self.c.y-self.r.y)**2)**(1/2)
    
    def perimeter(self):
        return 2*np.pi*self.radius()
    
    def area(self):
        return np.pi*self.radius()**2


# Test of the class Circle
if __name__ == '__main__':
    Circle1 = Circle()
    print("Circle 1 abscisse = ", Circle1.c)
    Circle2 = Circle(Point_2D(1,1),Point_2D(5,5))
    print("Circle 2 Ordonnee = ", Circle2.r)
    
    print(Circle1)
    print(Circle2)
    
    print(Circle2.perimeter())
'''
