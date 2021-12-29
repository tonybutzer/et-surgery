from etmLib.st_status import st_build_year_counts

out='enduser/CONUS/r40tile6/'
start_year = 1999
end_year = 2003
products = ['etasw', 'dd', 'srf' ]

mydict = st_build_year_counts(out, start_year, end_year, product)

for key in sorted(mydict):
        print( "%s: %s" % (key, mydict[key]))

