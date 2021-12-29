#! /bin/bash
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 2004 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 2005 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 2006 etasw netet &
