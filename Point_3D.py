# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:27:43 2024

@author: Aëlias
"""

#from Point_2D import Point_2D

class Point_3D:

    def __init__(self, name="P3D", x=0, y=0, z=0):
        self.name=name
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return f"Point3D {self.name}({self.x},{self.y}, {self.z})"



'''
class Point_3D(Point_2D):
	""" object class Point_3D, inherit from Point_2D
	"""
	def __init__(self,z:int):
		""" Point_3D class constructor
        :z: height of the point
		"""
		self.z = z

	def __str__(self):
		return f"({self.name},{self.x},{self.y},{self.z})"


# Test of the class Point
if __name__ == '__main__':
    Point1 = Point_3D(Point_2D('A',0,0),0)
    print("Point 1 abscisse = ", Point1.x)
    Point2 = Point_3D(Point_2D('B',1,1),0)
    print("Point 2 Ordonnee = ", Point2.y)

    print(Point1)
    print(Point2)
'''