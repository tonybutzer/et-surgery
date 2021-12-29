
'''
Steffi's List

this is the list of outputs of the VegET model (Oct 2020) sorted by importance:

     


        
        Eta (Etasw)
            Surface Runoff (SRF)
                Deep drainage (DD)
                    netet (netet)
                        crop eta (etc)
                            final soil water (SWf)
                                Snowpack (SNWpk)
                                    Rain
                                        snow water equivalent (SWE)
                                            snow melt (snow_melt)
                                                initial soil water (SWi)
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

        cmd_filename = './script/product_cmd_runner_' + product + '.sh'
        with open(cmd_filename, 'w') as f:
            for cmd in cmds:
                print(cmd)
                f.write(cmd+'\n')


print("hello from bash creator")

in1='out/DelawareRiverBasin/Run11_17_2020/'
out='enduser/DelawareRiverBasin/drb150_1117/'
start_year = 1950
end_year = 2099
product='etasw'

#Eta (Etasw)
#Surface Runoff (SRF)
#Deep drainage (DD)
#netet (netet)
#crop eta (etc)
#final soil water (SWf)

products = ['etasw', 'srf', 'dd', 'netet', 'etc', 'swf']

for product in products:
    build_docker_run_bash(in1, out, start_year, end_year, product)
