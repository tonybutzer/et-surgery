#! /bin/bash

 aws s3 ls dev-et-data/enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/2000/ | grep dd | wc

 for i in {1950..2019} ; do echo $i; aws s3 ls dev-et-data/enduser/DelawareRiverBasin/r_01_29_2021_drb35pct/$i/ | grep srf | wc ; done
