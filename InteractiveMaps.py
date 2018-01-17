# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:56:53 2018

@author: cscuser
"""

from bokeh.plotting import figure, save

#Initialize the figure
p = figure(title="My first interactive plot!")

#Define coordinates
x_coords = [0,1,2,3,4]
y_coords = [5,4,3,2,1]

#Create circle 
p.circle(x=x_coords, y=y_coords, size=10, color='red')

#Save the plot to disk
outfp = r"C:\Users\cscuser\Desktop\TS\INTERACTIVEMAPS\points.html"
save(obj=p, filename=outfp)




#Filepaths
#fp = r"C:\Users\cscuser\Desktop\TS\INTERACTIVEMAPS\

