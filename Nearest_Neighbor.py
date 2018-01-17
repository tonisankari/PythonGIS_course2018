# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:33:20 2018

@author: cscuser
"""

import geopandas as gpd
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points

def nearest(row, geom_union, df1, df2, geom1_col='geometry', geom2_col='geometry', src_column=None):
    """Find the nearest point and return the corresponding value from specified column."""
    # Find the geometry that is closest
    nearest = df2[geom2_col] == nearest_points(row[geom1_col], geom_union)[1]
    # Get the corresponding value from df2 (matching is based on the geometry)
    value = df2[nearest][src_column].get_values()[0]
    return value

pks_fp = r"C:\Users\cscuser\Desktop\TS\KML\PKS_suuralue.kml"
address_fp = r"C:\Users\cscuser\Desktop\TS\ADDRESSES\geocoded_addresses.shp"

pks = gpd.read_file(pks_fp)
address = gpd.read_file (address_fp)

address = address.dropna(subset=['geometry'])

unary = address.unary_union

#Calculate the centroids of the polygons
pks['centroid'] = pks.centroid

pks['nearest_id'] = pks.apply(nearest, geom_union=unary, df1=pks, df2=address, geom1_col='centroid',)

