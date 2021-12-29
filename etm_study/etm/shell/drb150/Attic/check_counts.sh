#! /bin/bash

product=etc


#for i in {1950..1980} ; do echo $i; aws s3 ls dev-et-data/enduser/DelawareRiverBasin/drb150/$i/ | grep $product | wc ; done
#for i in `seq 1950 10 2100`; do echo $i; done
#for i in  `seq 1950 10 2100`; do echo $i; aws s3 ls dev-et-data/enduser/DelawareRiverBasin/drb150/$i/ | grep $product | wc ; done
for i in {1950..2100} ; do echo $i; aws s3 ls dev-et-data/enduser/DelawareRiverBasin/drb150/$i/ | grep $product | wc ; done
