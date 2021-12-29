from etmLib.st_status import st_build_year_counts

out='enduser/DelawareRiverBasin/drb150/'
start_year = 1950
end_year = 2099
products = ['etc', 'etasw', 'dd', 'srf', 'netet']
product = 'dd'

mydict = st_build_year_counts(out, start_year, end_year, product)

for key in sorted(mydict):
        print( "%s: %s" % (key, mydict[key]))

