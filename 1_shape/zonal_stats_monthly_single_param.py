# zonal mean on polygon and output data in csv file
# Author: Stefanie Kagone, Mac Friedrichs, Tony Butzer, Olena Boiko
# Date: May 2022
# Log: script created
# Conda env: zonal_stats_rasterio (for Steffi)

import os
from time import time
import xarray as xr
#import rioxarray
import fiona
import rasterio
import rasterio.mask as msk
from rasterio.enums import Resampling
import numpy as np
from datetime import date, datetime
from dateutil.rrule import rrule, DAILY, MONTHLY
import pandas as pd


def zonal_stats(shape_path, infile, parameter):
    dicto={"parameter": [], "YYYYMM": [], 'ID': [], 'mean': []}
    # === Zonal Stats ===
    with fiona.open(shape_path, 'r') as shp:
        features = [feature for feature in shp]
        #print(features[0])
        with rasterio.open(infile) as src:
            for f in features:
                src_shp = [f['geometry']]
                print(src_shp)
                #outimage, out_transform = msk.mask(dataset, src_shp, crop=True)
                outimage, out_transform = msk.mask(src, src_shp, crop=True, all_touched=True)
                print(outimage.shape)
                #do historgram
                #SSEBop ET has nodata value as 32767
                #outimage=outimage.astype('float')
                #outimage[outimage==32767] = np.nan
                ws_id = f['properties']['pilot_id']
                ws_mean = np.nanmean(outimage)
                #print(ws_mean)
                ws_year = infile.split('.')[1][-6:-2]
                ws_month = infile.split('.')[1][-2:]
                dicto['mean'].append(ws_mean)
                #dicto['Year'].append(ws_year)
                #dicto['Month'].append(ws_month)
                dicto['YYYYMM'].append('{}_{}'.format(ws_year,ws_month))
                dicto['parameter'].append(parameter)
                dicto['ID'].append(ws_id)
    return dicto


path_mos_dat = r'W:\Projects\VegET_SSEBopET\netet_analysis_20yrs_2022\test_2018'
#shape_path = 'ID_2015_SnakeRiver_WGS84_UTM11.shp'
shape_path = os.path.join(path_mos_dat, 'SnakeRiver_WGS84_UTM11_test.shp')
if os.path.exists(os.path.join(path_mos_dat, shape_path)):
    print('Exists')
else:
    print(f'Whats going on with {os.path.join(path_mos_dat, shape_path)}!!!!!!')

csv_output = r'W:\Projects\VegET_SSEBopET\netet_analysis_20yrs_2022\test_2018'
parameter = 'etasw'
startyear = 2018
endyear = 2018
#num_of_years = 21
outfile_name = 'zonalmean_Snakeriver_2018_test'

a = datetime(startyear, 1, 1)
# count = 12 * num_of_years

i = 1
for dt in rrule(MONTHLY, count=2, dtstart=a):  # 252
    print(dt)
    print(i)
    # print(dt.strftime("%Y-%m")) # this returns string
    year = dt.strftime("%Y")
    month = dt.strftime("%m")
    print('averaging: {}-{}'.format(year, month))
    column_date = ('{}_{}'.format(year, month))

    in_file = os.path.join(path_mos_dat, parameter, year, '{}_{}{}.tif'.format(parameter, year, month))
    print(in_file)

    if i == 1:
        outdict = zonal_stats(shape_path, in_file, parameter)
        # print(f'keys {i}',len(outdict.keys()))
        csvdf = pd.DataFrame(outdict, columns=['parameter', 'ID', 'mean'])
        csvdf.set_index('ID', drop=True, append=False, inplace=True, verify_integrity=False)
        csvdf.rename({'mean': column_date}, axis=1, inplace=True)  # new method
        print(csvdf)
        del (outdict)
    else:
        # print('i am here now')
        outdict = zonal_stats(shape_path, in_file, parameter)
        # print(f'keys {i}',len(outdict.keys()))
        # print(outdict)
        # Create dataframe for next month
        csvdf_1 = pd.DataFrame(outdict, columns=['parameter', 'ID', 'mean'])
        csvdf_1.set_index('ID', drop=True, append=False, inplace=True, verify_integrity=False)
        csvdf_1.rename({'mean': column_date}, axis=1, inplace=True)
        print(csvdf_1)
        # attach the next month to the dataframe as last column
        csvdf = csvdf.join(csvdf_1[column_date])
        print(csvdf)

        # clean up
        del (outdict)
        del (csvdf_1)

    i += 1

csvdf.to_csv(os.path.join(csv_output, '{}_{}.csv'.format(parameter, outfile_name)))
print('done')
