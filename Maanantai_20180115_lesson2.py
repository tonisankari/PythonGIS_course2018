# -*- coding: utf-8 -*-
"""
Lesson 2

"""

import geopandas as gpd
import pandas as pd

#Filepaths
fp = r"C:\Users\cscuser\Desktop\TS\DAMSELFISH\DAMSELFISH_distributions.shp"
outfp = r"C:\Users\cscuser\Desktop\TS\DAMSELFISH\DAMSELFISH_distributions_selection.shp"

#Read the data
data = gpd.read_file(fp)

#Select attributes and certain rows the data
selection = data.loc[data['YEAR']==2012, ['YEAR', 'geometry', 'BINOMIAL']]
selection_all = data.loc[data['YEAR']==2012]

#Write the selection to shapefile
selection.to_file(outfp)

#Create a new column with the area of the Polygons
data['area_decimal_degrees'] = data.area
data['centroid'] = data.centroid

#Centroids
centroids = data[['centroid', 'BINOMIAL', 'YEAR']]

#Rename 'centroid' to 'geometry'
centroids = centroids.rename(columns={'centroid': 'geometry'})

#Convert the Pandas DataFrame to GeoDataFrame
centroids = gdp.GeoDataFrame(centroids, 'geometry') crs='epsg:4326'

