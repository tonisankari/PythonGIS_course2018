# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 14:35:34 2018

@author: cscuser
"""

import geopandas as gpd
from bokeh.plotting import save, figure
from bokeh.models import GeoJSONDataSource

#Filepaths
address_fp = r"C:\Users\cscuser\Desktop\TS\INTERACTIVEMAPS\addresses.shp"

#Read the data
address = gpd.read_file(address_fp)

#Reproject
address = address.to_crs(epsg=3067)

#Convert the GeoDataFrame
point_src = GeoJSONDataSource(geojson=address.to_json())

#Initialize
p = figure(title='Station map')
p.circle(x='x', y='y', source=point_src, color='green', size=8)

#Save to file
outfp = r"C:\Users\cscuser\Desktop\TS\INTERACTIVEMAPS\address_map.html"
save(p, outfp)


