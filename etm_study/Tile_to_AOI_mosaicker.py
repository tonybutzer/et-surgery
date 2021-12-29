import os
import sys
import boto3
from time import time
from time import sleep
import rasterio
from rasterio.plot import show
import xarray as xr
import rioxarray

from Tile_to_AOI_mosaicker_funcs import *

#month = '10'
#months = ['01','02','03','04','05','06'] 
months = ['07','08','09','10','11','12'] 
years = ['2020']
         
         #, '2006', '2007', '2008', '2009', '2010',
         #'2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
         
bucket = 'ws-enduser'
product = 'etasw'
tiles = ['USA/r37.0_tile0','USA/r37.0_tile1','USA/r37.0_tile2','USA/r37.0_tile3',
         'USA/r50.0_tile5','USA/r50.0_tile6','USA/r50.0_tile7','USA/r50.0_tile8','USA/r50.0_tile9']
out_prefix_path = bucket+'/USA/conus_mos/' # it gets the "year" folder from the function

for year in years:
    for mon in months:
        tif_list = []
        for tile in tiles:
            tif_list.append(tile+'/'+year+'/'+product+'_'+year+mon+'.tif')
        print('Those are the tiles included in the AOI: ')
        print(tif_list)

        print('Mosaicking -- {} {}'.format(year, mon))
        # builds a xarray mosaic in memory
        DS = xr_build_mosaic_ds(bucket, product, tif_list)
        primary_name = tif_list[0]  #first tif in list
        # outputs a geotiff (COG) from the mosaic in memory and places it into the S3 bucket
        xr_write_geotiff_from_ds(DS, primary_name, out_prefix_path)
