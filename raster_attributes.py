# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:36:20 2018

@author: cscuser
"""

import rasterio
from rasterio.plot import show

#Filepath
fp = r"C:\Users\cscuser\Desktop\TS\RASTERS\DOWNLOAD\Raster_data\Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"

#Open the file for reading
raster = rasterio.open(fp)

#Check the CRS
CRS = raster.crs

#Check affine transform
affine = raster.transform

#Dimensions
width = raster.width
height = raster.height

#Check the band count
band_cnt = raster.count

#Bounds of the file
bounds = raster.bounds

#Driver
dataformat = raster.driver

#Meta data from the raster
meta = raster.meta

#Visualize the data
show(raster)

#==================
#GET DATA FROM CHANNELS AND CALCULATE STATISTICS
#==================

red = raster.read(3)
nir = raster.read(4)

#Check datatype
dtype = red.dtype

#Calculate the statistics for all channells
stats = []

#Read all bands at one go
bands = raster.read()

import numpy as np

for band in bands:
    stats.append( {'min': band.min(),
                   'max': band.max(),
                   'median': np.median(band),
                   'mean': band.mean()                 
                   } )


#PLOT
#Visualize near infrared
show(nir, cmap='terrain')

#Visualize the histogram
from rasterio.plot import show_hist
show_hist(raster, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title='Histogram')









    
    
    