# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:49:55 2024

@author: Aëlias
"""

import numpy as np
import Source
import Plane
#import Point_3D


class System:
    
    def __init__(self,
				 name="system0",
				 sources = [Source()],
				 plane = Plane(),
				 obstacles = []):
        self.name=name
        self.sources=sources
        self.plane=plane
        self.obstacles = obstacles
        
    def __str__(self):
        return f"System {self.name} of sources {self.sources} and of plane {self.plan}"
    
    def vecteurs_sombres(self, num_source, num_obstacle):
        V=[]
        S = self.sources[num_source]
        for P in self.obstacles[num_obstacle]:
            V.append ((P[0] - S.location.x, P[1] - S.location.y, P[2] - S.location.z))
        return V
    
    def points_sombres(self):
        Ps=[]
        for n in range (len(self.sources)):
            source = self.sources[n]
            Vt=[]
            for num_obstacle in range (len(self.obstacles)):
                Vt.append (self.vecteurs_sombres(n, num_obstacle))
        
            for i in Vt:
                for j in i:
                    x = (round(source.location.x - j[0] * source.location.z/j[2]), round(source.location.y - j[1] * source.location.z/j[2]))
                    if x not in Ps and j[2]!=0 and self.plan.rectangle.corner2.x >= x[0] >= 0 and self.plan.rectangle.corner2.y >= x[1] >= 0 :
                        Ps.append(x)
        return Ps
    
    def indicatrice(self, Point, num_source):
        source = self.sources[num_source]
        
        dx = Point.x - source.location.x
        dy = Point.y - source.location.y
        dz = Point.z - source.location.z
        
        d = np.sqrt(dx**2 + dy**2 + dz**2)
        
        x_ = np.cos(source.phi) * np.sin(source.psi)
        y_ = np.sin(source.phi) * np.sin(source.psi)
        z_ = np.cos(source.psi)
        
        alpha = np.arccos((x_*dx + y_*dy + z_*dz)/d)
        
        return ([source.intensity * np.exp(-(4*np.log(2))*(alpha/source.etalement)**2), d])
    
    def eclairement(self, Point):
        
        if ((Point.x, Point.y)) in self.points_sombres():
            return 0
        else:
            
            E=0
            d=0
            for i in range (len(self.sources)):
                d = self.indicatrice(Point, i)[1]
                psi_ = np.arccos(self.sources[i].location.z/d )
                E+= self.indicatrice(Point, i)[0] * np.cos(psi_) / d**2
            return E

'''
class System:
    def __init__(self, name="systeme0",
                 sources = [Source()],
                 plan = Plan()):
        self.name=name
        self.sources=sources
        self.plan=plan
    
    def __str__(self):
        return f"Système {self.name} de sources {self.sources} de plan {self.plan}"
    
    def indicatrice(self, alpha = 0 , num_source = 0):
        source = self.sources[num_source]
        return source.intensity * np.exp(-(4*np.log(2))*(alpha/source.etalement)^2)
    
    def eclairement(self, Point = Point_3D("M", 0, 0, 0)):
        E=0
        d=0
        for i in range (len(self.sources)):
            dx = Point.x - self.sources[i].location.x
            dy = Point.y - self.sources[i].location.y
            dz = Point.z - self.sources[i].location.z
            d= np.sqrt(dx^2 + dy^2 + dz^2 )
            alpha = np.arccos(self.sources[i].location.z/d )
            E+= self.indicatrice(self, alpha, i) * np.cos(alpha) / d^2
'''