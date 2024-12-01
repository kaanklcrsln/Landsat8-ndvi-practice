import rasterio
from rasterio import plot

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os
os.listdir(r'C:\Users\ASUS\Desktop\landsat-ndvi\Landsat8')

#

band4 = rasterio.open(r'C:\Users\ASUS\Desktop\landsat-ndvi\Landsat8\LC08_L1TP_042035_20180603_20180615_01_T1_B4_clip.tif') #red

band5 = rasterio.open(r'C:\Users\ASUS\Desktop\landsat-ndvi\Landsat8\LC08_L1TP_042035_20180603_20180615_01_T1_B5_clip.tif') #nir

#

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(band4, ax=ax1, cmap='Blues') #red
plot.show(band5, ax=ax2, cmap='Blues') #nir
fig.tight_layout()

#ndvi calculation, empty cells or nodata cells are reported as 0

ndvi_if = (nir + red) == 0.
ndvi = (nir - red) / (nir + red) 
ndvi[ndvi_if] = 0 
ndvi

#

ndviImage = rasterio.open(r'C:\Users\ASUS\Desktop\landsat-ndvi\Landsat8\ndviImage.tiff','w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()

#

ndvi = rasterio.open(r'C:\Users\ASUS\Desktop\landsat-ndvi\Landsat8\ndviImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(ndvi)
