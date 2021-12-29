import os
import sys
import boto3
from time import time
from time import sleep
import rasterio
from rasterio.plot import show
import xarray as xr
import rioxarray


# Functions needed to run the Tile_to_AOI_moisaicker

def _xr_open_rasterio_retry(s3_file_name):
    cnt=20
    sleeptime=6
    while(cnt>0):
        try:
            da = xr.open_rasterio(s3_file_name)
            print('SUCCESS _xr_open_rasterio_retry', s3_file_name, flush=True)
            return da
        except rasterio.errors.RasterioIOError:
                        print("Unexpected error:", sys.exc_info()[0])
                        print('oops',cnt)
                        print('oops',s3_file_name, flush=True)
                        cnt = cnt - 1
                        sleep(sleeptime)

                        
def xr_build_mosaic_ds(bucket, product, tifs):
    start = time()
    my_da_list =[]
    for tif in tifs:
        try:
            da = _xr_open_rasterio_retry(f's3://{bucket}/'+tif)
        except:
            print('error on ', tif, flush=True)
            print('FATAL error on ', tif, flush=True)

        try:
            da = da.squeeze().drop(labels='band')
            da.name=product
            my_da_list.append(da)
            tnow = time()
            elapsed = tnow - start
            print(tif, elapsed)
        except:
            print('FATAL SQUEEZE error on ', tif, flush=True)

    try:
        DS = xr.merge(my_da_list)
        return(DS)
    except:
        print('FATAL MERGE error on ', tif, flush=True)
        
        
        
def s3_push_delete_local(local_file, bucket, bucket_filepath):
        out_bucket = return_my_bucket(bucket_filepath)
        a = bucket_filepath.split('/')
        bucket_filepath = '/'.join(a[1:]) # strip bucket from path
        print('PUSH', out_bucket, bucket_filepath)
        s3 = boto3.client('s3')
        with open(local_file, "rb") as f:
            s3.upload_fileobj(f, out_bucket, bucket_filepath)
        os.remove(local_file)
        
        
def _run_command(cmd, verbose=False):
    if verbose:
        print(cmd)
    result = os.system(cmd)
    if result != 0:
        raise Exception('command "%s" failed with code %d.' % (cmd, result))

def cog_create_from_tif(src_tif,dst_cog):
    command = f'rio cogeo create {src_tif} {dst_cog}'
    _run_command(command)

def return_my_bucket(prefix_with_slash):
    a = prefix_with_slash.split('/')
    print('a=',a)
    THE_BUCKET=a[0]
    print("the BUCKET=",THE_BUCKET)
    return THE_BUCKET


def xr_write_geotiff_from_ds(DS, primary_name, out_prefix_path):
    print(DS) # DS is the xarray
    print(primary_name) # first tif 
    print(out_prefix_path)

    a = primary_name.split('/')
    just_tif = a[-2] + '/' + a[-1]
    local_tif = a[-1]
    local_cog = 'COG_' + local_tif

    output = out_prefix_path + just_tif
    bucket = 'ws-enduser'
    print(f'OUTPUT=={output}')
    DS.rio.to_raster(local_tif)
    cog_create_from_tif(local_tif, local_cog)
    s3_push_delete_local(local_cog, bucket, output)
    os.remove(local_tif)
    local_xml = local_cog + '.aux.xml'
    os.remove(local_xml)
    
    
