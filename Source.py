# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:24:44 2024

@author: Aëlias
"""
import numpy as np
from Point_3D import Point_3D

class Source:
    def __init__(self,
                 name="S",
				 location = Point_3D("S",0,0,1),
				 theta=1,
				 phi=0,
				 psi=np.pi,
			     I0=1):
        """ Source class constructor
        :name: str name of the source
        :location: Point_3D place of the source in the space
        :theta: float angle translating the overture of the source illumination
        phi : float angle
        psi : float angle
        I0 : float intensity of the source
        """
        self.name=name
        self.location = location
        self.etalement=theta
        self.intensity=I0
        self.phi=phi #phi angle in the plane (x,y), in [0, 2pi] =
        self.psi=psi #psi angle in the plane of incidence in ]O, pi/2] relative to the horizontal (PI/2 = normal incidence)

    def __str__(self):
        return f"Point source {self.name} of coordinates {self.location}, of intensity {self.intensity}, of half-angle {self.theta}, of direction {self.phi} in the plan yz and {self.psi} in the plane xy"
'''
class Source:
    """ objet class Source
    """
    def __init__(self, name="S",
                 location = Point_3D("S",0,0,1),
                 theta=0,
                 phi=0,
                 psi=0,
                 I0=1):
        self.name=name
        self.location = location
        self.etalement=theta
        self.intensity=I0
        self.phi=phi
        self.psi=psi

    def __str__(self):
        return f"Source ponctuelle {self.name} de coordonnées {self.location},d'intensité {self.intensity} de demi angle {self.theta}, de direction {self.phi} dans le plan yz et {self.psi} dans le plan xy"
'''
