#! /bin/bash

product=dd_
product=etasw_
product=srf_

product=$1

dir=dev-et-data/enduser/CONUS/r40tile6


for i in {1999..2003} ; do echo $i; aws s3 ls ${dir}/$i/ | grep ${product} | wc ; done
