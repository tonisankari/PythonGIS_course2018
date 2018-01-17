# -*- coding: utf-8 -*-
"""
Geokoodaus
TS
"""

import pandas as pd
import geopandas as gpd
from geopandas.tools import geocode
from geopy.geocoders import Nominatim
from shapely.geometry import Point
import pycrs

#Filepath to addresses
fp = r"C:\Users\cscuser\Desktop\TS\ADDRESSES\addresses.txt"
data = pd.read_csv(fp, sep=';', encoding='utf8')

#Geocode the address
geo = geocode(data['addr'], provider='nominatim')

#------
#Add more control to geocoding
#------

geolocator = Nominatim()


#Create new columns for Point and geocoded addresses
data = data.assign(geometry=None, address=None)

#Iterate over the rows
for idx, row in data.iterrows():
    #Geocode the location
    location = geolocator.geocode(row['addr'])
    #If the location was found, then create a Point out of it
    if location:
        point = Point(location.longitude, location.latitude)
        address = location.address
        #Add the point and address to the DataFrame
        data.loc[idx, 'geometry'] = point
        data.loc[idx, 'address'] = address
    else:
        data.loc[idx, 'geometry'] = None
        data.loc[idx, 'address'] = None

#Save to shapefile
CRS = pycrs.parser.from_epsg_code(4326).to_proj4()
geodf = gpd.GeoDataFrame(data, geometry='geometry', crs=CRS)
outfp = r"C:\Users\cscuser\Desktop\TS\ADDRESSES\geocoded_addresses.shp"
geodf.to_file(outfp)

geo2 = gpd.read_file(outfp)