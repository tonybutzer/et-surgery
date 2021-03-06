import os
import json

def _write_geojson(filename, coord_list):
    print(coord_list)
    polycs = []
    polycs.append(coord_list)
    geos = []
    for polyc in polycs:
        poly = {
            'type': 'Feature',
            'properties': {},
            'geometry': {
                'type': 'Polygon',
                'coordinates': [polyc]
            }
        }
        geos.append(poly)

    geometries = {
       'type': 'FeatureCollection',
        'features': geos,
    }

    #geo_str = json.dumps(geometries)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(geometries, f, ensure_ascii=False, indent=4)
    print('WROTE filename {}'.format(filename))

def _write_shp(geojson_filename):
    shp_filename = geojson_filename.split('.json')[0] + '.shp'
    print(geojson_filename,shp_filename)
    cmd='ogr2ogr -f \"ESRI Shapefile\" {} {}'.format(shp_filename, geojson_filename)
    os.system(cmd)



def _make_chip_poly(ul_lat, ul_lon, lat_increment, lon_increment):
    coord_list = []
    ul_lat = float(ul_lat)
    ul_lon = float(ul_lon)
    ul_lon_lat = [ul_lon, ul_lat]
    ur_lon_lat = [ul_lon + lon_increment, ul_lat]
    lr_lon_lat = [ul_lon + lon_increment, ul_lat - lat_increment]
    ll_lon_lat = [ul_lon, ul_lat - lat_increment]
    print (ul_lon_lat)
    coord_list.append(ul_lon_lat)
    print (ur_lon_lat)
    coord_list.append(ur_lon_lat)
    print (lr_lon_lat)
    coord_list.append(lr_lon_lat)
    print (ll_lon_lat)
    coord_list.append(ll_lon_lat)
    print (ul_lon_lat)
    coord_list.append(ul_lon_lat)
    return(coord_list)


def _parse_chip_name(chip_name):
    print (chip_name)
    tn = chip_name.split('chip')[-1]
    print(tn)
    ul_lat = tn.split('N')[0]
    tn = tn.split('N')[-1]
    print(tn)
    print(ul_lat)
    ul_lon = tn.split('E')[0]
    print(ul_lon)
    return ul_lat, ul_lon



def _parse_tile_name(tile_name):
    print (tile_name)
    tn = tile_name.split('tile')[-1]
    print(tn)
    ul_lat = tn.split('N')[0]
    tn = tn.split('N')[-1]
    print(tn)
    print(ul_lat)
    ul_lon = tn.split('E')[0]
    print(ul_lon)
    return ul_lat, ul_lon


def make_filename(tile_name, chip_name, extension):
    filename = chip_name + extension
    return(filename)


class GridMeisterTile:
    """
    This class partitions a 10 degree tile into 2 degree chips
    """

    def __init__(self, tile_name, extent, divisor):

        self.tile_name = tile_name
        self.extent = extent

        lon_width = abs(extent[0] - extent[2])
        lat_width = (extent[3] - extent[1])

        self.chip_lat_increment = lat_width / divisor
        self.chip_lon_increment = lon_width / divisor

        print(lon_width, lat_width)
        print(self.chip_lon_increment, self.chip_lat_increment)


    def chip_list(self):
        CHIP_LIST = []
        e = self.extent
        box={'left': e[0], 'bottom':e[1] , 'right': e[2], 'top': e[3]}

        starting_lat = box['top']
        ending_lat = box['bottom']

        print(starting_lat, ending_lat)

        starting_lon = box['left']
        ending_lon = box['right']
        print(starting_lon, ending_lon)

        lat = starting_lat
        while lat > ending_lat:
            print(lat)

            lon = starting_lon
            while lon < ending_lon:
                print(lon)
                chip_name = 'chip' + str(lat) + 'N' + str(lon) +'E'
                CHIP_LIST.append(chip_name)
                lon = lon + self.chip_lon_increment
                lon = round(lon, 2)

            lat = lat - self.chip_lat_increment
            lat = round(lat, 2)

        return CHIP_LIST

    def create_chip_shp(self, chip_name):
        self.aoi_dir = './AOI'
        print(chip_name)
        ul_lat,ul_lon = _parse_chip_name(chip_name)
        print(ul_lat,ul_lon)
        coord_list = _make_chip_poly(ul_lat,ul_lon, self.chip_lat_increment, self.chip_lon_increment)
        print(coord_list)
        filename = make_filename(self.tile_name, chip_name, '.json')
        print(filename)
        full_filename =  self.aoi_dir + '/' + filename
        _write_geojson(full_filename, coord_list)
        _write_shp(full_filename)


    def build_docker_run_bash(self, chip_list, optimize):
        print(chip_list)

        vols = '-v `pwd`/AOI:/home/veget/cloud-veg-et-basin/api_veget/AOI'
        mycwd = os.getcwd()
        image_custom = mycwd.split('/')[-1]
        image = 'tbutzer/' + image_custom
        cmds=[]
        for chip_name in chip_list:
            filename = make_filename(self.tile_name, chip_name, '.shp')
            full_filename =  self.aoi_dir + '/' + filename
            tile=self.tile_name + '/' + chip_name
            #tile = filename.split('.shp')[0]
            #cmd = 'docker run -i {} {} python3 api_veget.py -c running_config -s {}  {}'.format(vols,image,full_filename,tile)
            #cmd = 'docker run -i {} {} python3 bench_api_veget.py -c running_config -s {}  {}'.format(vols,image,full_filename,tile)
            #if not optimize:
            # Remove OPTIMEISTER complexity
            cmd = 'docker run -i {} {} python3 api_veget.py -c running_config -s {} --optimize no  {}'.format(vols,image,full_filename,tile)
            print(cmd)
            logname = filename = make_filename(self.tile_name, chip_name, '.log')
            full_logname = './log' + '/' + logname
            print(full_logname)

            full_cmd = cmd + '  2>&1 | tee  ' + full_logname +'&'
            print(full_cmd)
            cmds.append(full_cmd)

        cmd_filename = 'cmd_runner_' + self.tile_name.split('/')[0] + '.sh'
        with open(cmd_filename,'w') as f:
            for cmd in cmds:
                print(cmd)
                f.write(cmd+'\n')
        f.close()

        cmd_filename = 'test_cmd_runner_' + 'one' + '.sh'
        with open(cmd_filename,'w') as f:
            cmd = cmds[0]
            print(cmd)
            f.write(cmd+'\n')
        f.close()


