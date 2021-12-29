#! /bin/bash

product=etasw
#product=dd

#product=netet

#for i in {1950..2099} ; do echo $i; aws s3 ls dev-et-data/enduser/DelawareRiverBasin/drb150_nofunswitch/$i/ | grep $product | wc ; done
for i in {1950..2099} ; do echo $i; aws s3 ls dev-et-data/enduser/DelawareRiverBasin/drb150c/$i/ | grep $product | wc -l ; done
