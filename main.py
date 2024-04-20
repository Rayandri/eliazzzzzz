# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:11:06 2024

@author: Aëlias
"""

from Carte import Carte
from System import System
from Source import Source
from Plane import Plane
from Rectangle import Rectangle
import Point_3D
from Point_3D import Point_3D
import numpy as np
import matplotlib.pyplot as plt
# from TroisD import *
from Point2D import Point_2D
import Point2D
print(Point2D.Point_2D)


def Obstacle_Rectangulaire_Parallele(corner1=Point2D.Point_2D("A", 0, 0),
                                     corner2=Point_2D("B", 1, 1),
                                     height=1):
    L = []
    for x in range(min(corner1.x, corner2.x), max(corner1.x, corner2.x) + 1):
        for y in range(min(corner1.y, corner2.y), max(corner1.y, corner2.y) + 1):
            L.append((x, y, height))
    return L


# %%
CARTE4 = Carte("C4",
               System("sys4",
                      [Source("S41", Point_3D("PS41", 50, 150, 20), 100, 0, np.pi, 100), Source(
                      ), Source("S42", Point_3D("PS42", 120, 160, 20), 1000, 0, np.pi, 100)], Plane
                      ("PL4",
                       Rectangle(
                           "Rect4",
                           Point_2D("A4", 0, 0),
                           Point_2D("B4", 200, 200)
                       )
                       )
                      )
               )
CARTE5 = Carte("C5", System("sys5", [Source("S5", Point_3D("PS5", 5, 5, 3), 1000, np.pi/2, np.pi /
               2 + np.pi/4, 1)], Plane("P5", Rectangle("Rect5", Point_2D("A5", 0, 0), Point_2D("B5", 10, 10)))))
CARTE2 = Carte("bozo", System("sysbozo", [Source(), Source("zobo", Point_3D("sus", 1, 1, 2))], Plane(
    "plandebozo", Rectangle("rectbozo", Point_2D("A", 0, 0), Point_2D("B", 10, 10)))))
CARTE3 = Carte("Carte3", System("sys3", [Source("S3", Point_3D("p3", 25, 25, 100), 1, np.pi, np.pi, 10000)], Plane("plan3", Rectangle(
    "rect3", Point_2D("A3", 0, 0), Point_2D("B3", 50, 50))), [Obstacle_Rectangulaire_Parallele(Point_2D("AO", 20, 20), Point_2D("B0", 30, 30), 50)]))

CARTE7 = Carte("C7", System("s7", [Source("S7", Point_3D("PS7", 25, 15, 20), 0.5, np.pi/2, np.pi /
               2 + np.pi/4, 1)], Plane("p7", Rectangle("rect7", Point_2D("A7", 0, 0), Point_2D("B7", 50, 50)))))
CARTE8 = Carte("C8", System("s8", [Source("S8", Point_3D("PS8", 25, 15, 20), 0.5, np.pi/2, np.pi/2 + np.pi/4, 1)], Plane("p8", Rectangle("rect8", Point_2D("A8", 0, 0), Point_2D("B8", 50, 50))), [
               Obstacle_Rectangulaire_Parallele(Point_2D("AO8", 24, 0), Point_2D("B08", 26, 50), 0.1), Obstacle_Rectangulaire_Parallele(Point_2D("A208", 20, 27), Point_2D("B208", 30, 29), 5)]))
CARTE6 = Carte("C6", System("sys6", [Source("S6", Point_3D("PS6", 20, 50, 3), 100, 0, np.pi/2 + np.pi/4, 1)],
               Plane("plan6", Rectangle("Rect6", Point_2D("A6", 0, 0), Point_2D("B6", 100, 100)))))

# %% Affichage


def showcarte(C):
    plt.imshow(C.matrix())
    plt.show()

# %%


if __name__ == '__main__':
    Rectangle1 = Rectangle()
    print("Rectangle 1 abscisse = ", type(Rectangle1.corner1))
    Rectangle2 = Rectangle(Point_2D(1, 1), Point_2D(5, 5))
    print("Rectangle 2 Ordonnee = ", Rectangle2.corner1)

    print(Rectangle1)
    print(Rectangle2)

    print(Rectangle2.perimeter())
    
    

# %%

if __name__ == '__main__':
    Plan1 = Plane()
    print("Plan 1 abscisse = ", type(Plan1.l))
    Rectangle_temporaire = Rectangle(Point_3D(1, 1, 0), Point_3D(5, 5, 0))
    Plan2 = Plane("Plan2", Rectangle_temporaire)
    print("Plan 2 Ordonnee = ", Plan2.l)

    print(Plan1)
    print(Plan2)

    print(Plan2.perimeter())

    showcarte(CARTE4)
