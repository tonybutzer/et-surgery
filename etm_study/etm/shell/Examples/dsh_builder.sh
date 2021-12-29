#! /bin/bash

sleepTime=15000

for i in {2003..2009}; do echo docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y $i netet netet \&; done
echo sleep $sleeptime
for i in {2010..2015}; do echo docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y $i netet netet \&; done
