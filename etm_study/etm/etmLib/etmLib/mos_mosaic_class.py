import re
from .log_logger import log_make_logger
from .log_logger import s3_save_log_file
from .s3_func import s3_list_pseudo_subdirs
from .s3_func import return_s3_list
from .xr_mosaic_func import xr_build_mosaic_ds
from .xr_mosaic_func import xr_write_geotiff_from_ds

def _return_list_of_years(subfolders):
    THE_YEAR_LIST = []
    for path in subfolders:
        #print(path)
        the_year = path.split('/')[-2]
        #print(the_year)
        if 'aaalog' not in the_year:
            THE_YEAR_LIST.append(the_year)
    return THE_YEAR_LIST


class Mos_mosaic:

    def __init__(self, in_prefix_path, year, out_prefix_path, products):
        print("hello from Mos_mosaic class")
        self.log = log_make_logger('Mos_mosaic')
        #self.bucket = n_bucket
        #self.in_bucket = in_bucket
        #self.out_bucket = out_bucket
        self.in_prefix_path = in_prefix_path
        self.products = products
        self.year = year
        self.out_prefix_path = out_prefix_path
        msg = f'{in_prefix_path} {out_prefix_path} , {products}, {year}'
        self.log.info(msg)

    def _return_peers(self, tif_path, subdirs):
        self.log.info(f'{tif_path}, {subdirs}')
        peers = []
        a = tif_path.split('/')
        just_tif = a[-2] + '/' + a[-1]
        for dir in subdirs:
            peer = dir + just_tif
            peers.append(peer)
        
        return(peers)

    def _do_year_range(self, target_year, subfolders):
        a = target_year.split('_')
        start_year = int(a[1])
        end_year = int(a[2])
        
        for year in range(start_year, end_year+1):
            print(year)
            target_year=str(year)
            self._do_one_year(target_year,subfolders)

    
    def _do_one_year_monthly(self, target_year, subfolders):

        target_tifs = []
        sub_sub_sub = subfolders[0] + target_year + '/'
        self.log.info(f'sub is {sub_sub_sub}')
        all_tifs = return_s3_list(self.bucket, sub_sub_sub)
        #print(all_tifs)

        target_product = self.products[0] + '_'
        # Just match the monthly sums -tony
        expression = '.*' + str(target_year) + '[0-9][0-9].tif$'

        for (tif,sz) in all_tifs:
            if target_product in tif:
                #print(tif)
                #print(expression, tif)
                match = re.match(expression, tif)
                if match:
                    target_tifs.append(tif)

        for tif in target_tifs:
            print(tif)
            tif_peers = self._return_peers(tif, subfolders)
            #print(tif_peers)
            product = target_product
            bucket = self.bucket
            ds = xr_build_mosaic_ds(bucket, product, tif_peers)
            primary_name = tif_peers[0]
            xr_write_geotiff_from_ds(ds, primary_name, self.out_prefix_path)

    def _do_one_year(self, target_year, subfolders):

        target_tifs = []
        sub_sub_sub = subfolders[0] + target_year + '/'
        self.log.info(f'sub is {sub_sub_sub}')
        all_tifs = return_s3_list(self.bucket, sub_sub_sub)
        #print(all_tifs)

        target_product = self.products[0] + '_'
        for (tif,sz) in all_tifs:
            if target_product in tif:
                #print(tif)
                target_tifs.append(tif)

        for tif in target_tifs:
            tif_peers = self._return_peers(tif, subfolders)
            #print(tif_peers)
            product = target_product
            bucket = self.bucket
            ds = xr_build_mosaic_ds(bucket, product, tif_peers)
            primary_name = tif_peers[0]
            xr_write_geotiff_from_ds(ds, primary_name, self.out_prefix_path)
            print("wrote: ",primary_name, self.out_prefix_path)

    def run_mosaic(self):
        self.log.info("run_mosaic")
        for prod in self.products:
            self.log.info(f'Mosaic this product: {prod}')

        if not self.in_prefix_path.endswith('/'):
            in_prefix_with_slash = self.in_prefix_path + '/'
        else:
            in_prefix_with_slash = self.in_prefix_path
        self.log.info(in_prefix_with_slash)
        subfolders,bucket = s3_list_pseudo_subdirs(in_prefix_with_slash)
        for folder in subfolders:
            print(folder)
        sub_sub = subfolders[0]
        sub_sub = bucket+'/'+sub_sub
        self.bucket=bucket
        years_list,bucket2 = s3_list_pseudo_subdirs(sub_sub)
        for year in years_list:
            print(year)

        target_year = self.year
        self.log.info(f'target year is {target_year}')
        if 'years_' in target_year:
            self.log.info(f'DOING ALL THE YEARS {target_year}')
            self._do_year_range(target_year,subfolders)
        else:
            if 'monthly' in target_year:
                if '_' in target_year:
                    year = target_year.split('_')[-1]
                    self.log.info(f'DOING YEAR ', year)
                    self._do_one_year_monthly(year,subfolders)
                else:
                    self.log.info('DOING ALL THE YEARS')
                    years = _return_list_of_years(years_list)
                    for year in years:
                        print(year)
                        target_year=year
                        self._do_one_year_monthly(target_year,subfolders)
            else:
                if 'all' in target_year:
                    self.log.info('DOING ALL THE YEARS')
                    years = _return_list_of_years(years_list)
                    for year in years:
                        print(year)
                        target_year=year
                        self._do_one_year(target_year,subfolders)
                else:
                    self._do_one_year(target_year,subfolders)


        
