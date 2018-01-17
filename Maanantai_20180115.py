# -*- coding: utf-8 -*-

"""

"""


from shapely.geometry import Point
from shapely.geometry import Polygon

def createPointGeom(x_coord=None, y_coord=None):
    """Returns a shapely Point object from coordinates)"""
    if type(x_coord) == float and type(y_coord) == float:
        return Point(x_coord, y_coord)
    else:
        print("Coordinates should be Floats")

def createPolyGeom(points=None):
    if type(points)!=list:
        print("The input should inside a list!")
    if len(points) > 0:
        
        all_points = True
        
        for point in points:
            if not type(point) == Point:
                all_points = False
                
            if all_points == True:
                return Polygon([(p.x, p.y) for p in points])
            else:
                print("All points were not Point objects!")

my_point = createPointGeom(y_coord=3, x_coord=2)
print(my_point)
    
    
