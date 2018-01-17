# -*- coding: utf-8 -*-
"""

"""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
from fiona.crs import from_epsg
import pycrs

#Create a new GeoDataFrame
geo = gpd.GeoDataFrame()

#Create a 'geometry' column
geo['geometry'] = None

#Create a few more columns to GeoDataFrame
geo = geo.assign(name=None, area=None, centroid=None)


#Coordinates of Senate Square
coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(shell=coordinates)

#Insert the Polygon into the GeoDataFrame
geo.loc[0, 'geometry'] = poly

#Define the coordinate reference system
crs = pycrs.parser.from_epsg_code(4326).to_proj4()


