
from etmLib.s3_func import return_s3_list

'''

docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1964_1970 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1971_1980 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1981_1990 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1991_2000 etasw netet &
'''

def build_year_hash(out, start_year, end_year, product):
    years_hash = {}
    chore_list=[]
    print(out)
    years = range(start_year, end_year+1)
    for year in years:
        path= out + str(year)
        print(path)
        s3_list = return_s3_list('dev-et-data', path)
        prod_list=[]
        for (key,sz) in s3_list:
            if product in key:
                prod_list.append(key)
        if len(prod_list) >= 377:
            print("377 or greater")
        else:
            chore_year = year
            chore_list.append(chore_year)
    return chore_list

def consecutive(chores, binsz):
    range_list=[]
    cnt=0
    consecutive=False
    lastchore = chores[0]-1
    start = chores[0]
    last = chores[0]
    for chore in chores:
        cnt = cnt + 1
        space = chore - lastchore
        print("space chore lastchore:", space, chore, lastchore)
        if (space < 2) and (cnt <= binsz):
            print("conscutive space chore lastchore:", space, chore, lastchore)
            consecutive=True
            last = chore
            lastchore=chore
        else:
            rang='years_' + str(start) + '_' + str(last)
            range_list.append(rang)
            consecutive = False
            start = chore
            last = chore
            lastchore=chore
            cnt=0

    return range_list


def build_actual_bash_file(range_list):
    cmds=[]
    for year_range in range_list:

        image_custom = 'etm_docker_image'
        image = 'tbutzer/' + image_custom
        cmd = 'docker run -i {} python3 api_etm.py -i {} -o {} -y {} {} dummy'.format(image, in1, out, year_range, product)
        print(cmd)
        logname="etm1" + year_range


        full_logname = './log' + '/' + logname
        print(full_logname)

        full_cmd = cmd + '  2>&1 | tee  ' + full_logname +'&'
        print(full_cmd)
        cmds.append(full_cmd)

    cmd_filename = 'select_product_cmd_runner_' + product + '.sh'
    with open(cmd_filename, 'w') as f:
        for cmd in cmds:
            print(cmd)
            f.write(cmd+'\n')


print("hello from bash creator")

in1='out/DelawareRiverBasin/Run10_07_2020/'
out='enduser/DelawareRiverBasin/drb150/'
start_year = 1950
end_year = 1980
#product='netet'
#product='dd'
product='srf'
#product='etc'

chore_list = build_year_hash(out, start_year, end_year, product)
print(chore_list)
ranges = consecutive(chore_list, 2)

print(ranges)
build_actual_bash_file(ranges)
