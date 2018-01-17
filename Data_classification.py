# -*- coding: utf-8 -*-
"""
Data classification
"""

import geopandas as gpd
import pysal as ps

#Filepath
fp = r"C:\Users\cscuser\Desktop\TS\TRAVEL_TIMES_SHP\TravelTimes_to_5975375_RailwayStation.shp"
data = gpd.read_file(fp)

#Remove No Data with -1 value
#Select rows where 'pt_r_t' >= 0
data = data.loc[data['pt_r_t']>=0]

#Plot the data
data.plot(column='pt_r_t', scheme = 'quantiles', k=9, cmap='RdYlBu', linewidth=0)

#Classify the data values in GeoDataFrame
n_classes = 9

#Initialize classifier
classifier = ps.Natural_Breaks.make(k=n_classes)

#Do the classification
classification = data[['pt_r_t']].apply(classifier)

#Rename the column to keep track on the classification method
classification.columns = ['pt_r_t_nb9']

#Join the data back to the original DF
data = data.join(classification)

#Plot
data.plot(column='pt_r_t_nb9', linewidth=0, cmap='RdYlBu', legend=True)


#==============
#CUSTOM CLASSIFIER
#==============


    
def customClassifier2(row, src_col1, src_col2, threshold1, threshold2, output_col):
    # 1. If the value in src_col1 is LOWER than the threshold1 value
    # 2. AND the value in src_col2 is HIGHER than the threshold2 value, give value 1, otherwise give 0
    if row[src_col1] < threshold1 and row[src_col2] > threshold2:
        # Update the output column with value 0
        row[output_col] = 1
    # If area of input geometry is higher than the threshold value update with value 1
    else:
        row[output_col] = 0

    # Return the updated row
    return row

data = data.assign(suitability=None)

data = data.apply(customClassifier2, time_col='pt_t_t', threshold1=20,

