# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:00:47 2018

@author: cscuser
"""

import os
import urllib

def get_filename(url):
    """Parses the filename from url-address"""
    if url.find('/'):
        return url.rsplit('/', 1)[-1]

#Directory path
outdir = r"C:\Users\cscuser\Desktop\TS\RASTERS\DOWNLOAD\Raster_data"

#Create a folder if it does not exist
if not os.path.exists(outdir):
    os.makedirs(outdir)

# File locations
url_list = ["http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133A.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133B.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133C.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133D.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133E.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4133F.tif",

            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4134A.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4134B.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4134C.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4134D.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4134E.tif",
            "http://www.nic.funet.fi/index/geodata/mml/korkeusmalli2m/2017/L4/L41/L4134F.tif",

            "https://etsin.avointiede.fi/storage/f/paituli/ehdot/Latuviitta_ehdot.pdf",
            "https://etsin.avointiede.fi/storage/f/paituli/ehdot/MML_ehdot_CC.txt",
            "https://github.com/Automating-GIS-processes/CSC18/raw/master/data/Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif"
            ]

#Download data files one by one
for url in url_list:
    #Extract the filename from the address
    fname = get_filename(url)
    #Parse the full filepath
    outfp = os.path.join(outdir, fname)
    #Download if the file does not exist
    if not os.path.exists(outfp):
        print("downloading", fname)
        r = urllib.request.urlretrieve(url, outfp)




