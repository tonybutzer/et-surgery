#! /bin/bash

ROOT=s3://dev-et-data/out/DelawareRiverBasin/Run01_29_2021/
NEWROOT=s3://dev-et-data/out/DelawareRiverBasin/Run01_29_2021_35/

for i in `cat list.txt`; do {
	echo $i;
	echo ${ROOT}$i;
	cmd="aws s3 mv ${ROOT}$i ${NEWROOT}$i --recursive"
	echo $cmd
	$cmd &
	} done;
