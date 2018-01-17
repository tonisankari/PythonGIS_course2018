# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:08:17 2018

@author: cscuser
"""

import geopandas as gpd

#File path
pop_fp = r"C:\Users\cscuser\Desktop\TS\POPULATION\Vaestotietoruudukko_2015.shp"
address_fp = r"C:\Users\cscuser\Desktop\TS\ADDRESSES\geocoded_addresses.shp"


#Read the files
pop = gpd.read_file(pop_fp)
address = gpd.read_file (address_fp)

#Exclude the NaNs if they exist in geometry column
pop = pop.dropna(subset=['geometry'])
address = address.dropna(subset=['geometry'])

#Reproject the data
address = address.to_crs(pop.crs)

#Spatial join
join = gpd.sjoin(address, pop, op='within')
join2 = gpd.sjoin(pop, address, op='contains')




