# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:20:09 2018

@author: cscuser
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point LineString

#Filepath
txt_fp = r"C:\Users\cscuser\Desktop\TS\TRAVEL_TIMES_TXT\travelTimes_2015_Helsinki.txt"
excel_fp = r"C:\Users\cscuser\Desktop\TS\TRAVEL_TIMES_EXCEL\travelTimes_2015_Helsinki.xslx"


#stream = open(txt_fp, 'r')
#stream.readline()
#stream.close()

#Read the data in
data = pd.read_csv(txt_fp, sep=';')


#Read the data from Excel
data = pd.read_excel(excel_fp, sheet_name="travelTimes_2015_Helsinki")

#Create Points from coordinates
data['origin_point'] = data.apply(lambda row: Point(row['from_x'], row['from_y']), axis=1)
data['dest_point'] = data.apply(lambda row: Point(row['to_x'], row['to_y']), axis=1)

#Create a GeoDataFrame
geo = gpd.GeoDataFrame(data, geometry='dest_point', crs={'init':'epsg4326'})


