# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:42:02 2018

@author: cscuser
"""

import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os
import pycrs

#Filepaths
dirpath = r"C:\Users\cscuser\Desktop\TS\RASTERS\DOWNLOAD\Raster_data"
outfp = r"C:\Users\cscuser\Desktop\TS\RASTERS\DOWNLOAD\Raster_data\Helsinki_DEM_2x2m_Mosaic.tif"

#Search criteria
search_criteria = "L*.tif"
q = os.path.join(dirpath, search_criteria)

#Find relevant files using glob
dem_fps = glob.glob(q)

#Create a list for the open raster files
src_files_to_mosaic = []


for fp in dem_fps:
    src = rasterio.open(fp)
    src_files_to_mosaic.append(src)

#Create a mosaic out of the rasters
mosaic, out_trans = merge(src_files_to_mosaic)

#Save the mosaic into your computer
out_meta = src.meta.copy()
out_meta.update(
        {'height': mosaic.shape[1],
         'width': mosaic.shape[2],
         'transform': out_trans,
         'crs': pycrs.parser.from_epsg_code(3067).to_proj4()
                
         })


#Write the file into disk
with rasterio.open(outfp, 'w', **out_meta) as dest:
    dest.write(mosaic)




