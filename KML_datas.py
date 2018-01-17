# -*- coding: utf-8 -*-
"""
Point in Polygon queries

"""

import geopandas as gpd
import matplotlib.pyplot as plt
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

#Filepaths
address_fp = r"C:\Users\cscuser\Desktop\TS\ADDRESSES\geocoded_addresses.shp"
poly_fp = r"C:\Users\cscuser\Desktop\TS\KML\PKS_suuralue.kml"

#Read files
address = gpd.read_file(address_fp)
poly = gpd.read_file(poly_fp, driver='KML')

#Select the region
southern = poly.loc[poly['Name']=='Eteläinen']

#Reset the index
southern = southern.reset_index(drop=True)

#Create a mask of the points who are within the area
pip_mask = address.within(southern.loc[0, 'geometry'])

#Select the rows that were inside the Polygon
pip_data = address.loc[pip_mask]

#Visualization
fig, ax = plt.subplots()
poly.plot(ax=ax, facecolor='grey')
southern.plot(ax=ax, color='red')
address.plot(ax=ax, color='blue', markersize=6)
pip_data.plot(ax=ax, color='gold', markersize=6)

#Select points tjat were not under Eteläinen area
address_outpoly = address.loc[~pip_mask]
