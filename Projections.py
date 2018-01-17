# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:02:52 2018

@author: cscuser
"""

import geopandas as gpd

#File patch
fp = r"C:\Users\cscuser\Desktop\TS\EUROPE_BORDERS\Europe_borders.shp"
data = gpd.read_file(fp)

#Reproject the data into EPSG3035 projection
data_proj = data.to_crs(epsg=3035)

#Reproject2
#data_proj2 = data.to.crs(pycrs.parser.from_esri_code(37205).to_proj4())



