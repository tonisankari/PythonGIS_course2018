# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:52:44 2018

@author: cscuser
"""

import rasterio
from rasterio.mask import mask
from shapely.geometry import box
import pycrs
import geopandas as gpd
from rasterio.plot import show
from fiona.crs import from_epsg

#Filepaths
fp = r"C:\Users\cscuser\Desktop\TS\RASTERS\DOWNLOAD\Raster_data\p188r018_7t20020529_z34__LV-FIN.tif"
outfp = r"C:\Users\cscuser\Desktop\TS\RASTERS\DOWNLOAD\Raster_data\Helsinki_clipped_p188r018_7t20020529_z34__LV-FIN.tif"

#Read file
data = rasterio.open(fp)

#Create a bounding box
minx, miny = 24.6, 60.0
maxx, maxy = 25.22, 60.35
bbox = box(minx, miny, maxx, maxy)


#Parse the EPSG code automativally from the raster CRS
epsg_code = int(data.crs.data['init'][5:])

#Create a Dataframe of the Bounding box
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))

#Reproject the data to the same one as the raster
geo = geo.to_crs(crs=pycrs.parser.from_epsg_code(epsg_code).to_proj4())

#Extract the coordinates
def getFeatures(gdf):
    import json


