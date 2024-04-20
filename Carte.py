# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:47:40 2024

@author: Aëlias
"""
import numpy as np
import System
import Point_3D

class Carte:
    def __init__ (self,
				  name = "Carte0",
				  system = System.System()):
        self.name=name
        self.system=system
        
    def matrix(self):
        X = np.zeros((self.system.plan.w + 1, self.system.plan.h + 1))	
        Imax=0
        I = 0
        for i in range (self.system.plan.w + 1):
            for j in range (self.system.plan.h + 1):
                I = self.system.eclairement(Point_3D(f"Point({i}, {j})", i, j, 0))
                X[i][j]= I
                print(I)
                if I > Imax : 
                    Imax=I
        return (X * 255/Imax)
