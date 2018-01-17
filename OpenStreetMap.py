# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:01:17 2018

@author: cscuser
"""


import osmnx as ox
import matplotlib.pyplot as plt

#Specify the place what you are looking for
place_name = "Kamppi, Helsinki, Finland"

#Fetch the streets
graph = ox.graph_from_place(place_name)

#Plot
fig, ax = ox.plot_graph(graph)
#ox.plot_graph_folium(graph)
#graph_map = ox.plot_graph_folium(graph)
#outfp = r"C:\Users\cscuser\Desktop\TS\GRAPHS\graph1.html"

#Fetch buildings from OSM
buildings = ox.buildings_from_place(place_name)
buildings.plot()

#Fetch region foot print
footprint = ox.gdf_from_place(place_name)
footprint.plot()

#Convert the graph to GeoDataFrames
nodes, edges = ox.graph_to_gdfs(graph)

#Define the figure, 
fig, ax = plt.subplots()
footprint.plot(ax=ax, facecolor='black')
buildings.plot(ax=ax, facecolor='khaki', edgecolor='white', alpha=0.7)
edges.plot(ax=ax, linewidth=1, edgecolor='#CD5C5C')


           
           
           