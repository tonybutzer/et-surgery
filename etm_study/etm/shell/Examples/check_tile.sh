#! /bin/bash

product=dd_
product=srf_
product=etasw_

dir=dev-et-data/enduser/CONUS/r40tile6


for i in {1999..2003} ; do echo $i; aws s3 ls ${dir}/$i/ | grep ${product} | wc ; done
