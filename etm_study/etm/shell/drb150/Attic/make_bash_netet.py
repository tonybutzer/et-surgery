
'''

docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1964_1970 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1971_1980 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1981_1990 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y years_1991_2000 etasw netet &
'''

def build_docker_run_bash(in1, out, start_year, end_year, product):

        cmds=[]
        years = range(start_year, end_year+1)
        for year in years:
            print(year)
            if (not year%10):
                y9 = str(year+9)
                year_range = 'years_{}_{}'.format(year,y9)

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
            else:
                print('else', year)

        cmd_filename = 'product_cmd_runner_' + product + '.sh'
        with open(cmd_filename, 'w') as f:
            for cmd in cmds:
                print(cmd)
                f.write(cmd+'\n')


print("hello from bash creator")

in1='out/DelawareRiverBasin/Run10_07_2020/'
out='enduser/DelawareRiverBasin/drb150/'
start_year = 1961
end_year = 2099
#product='etc'
product='srf'

build_docker_run_bash(in1, out, start_year, end_year, product)
