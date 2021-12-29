#! /bin/bash
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 1999 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 2016 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 2017 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 2018 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y 2019 etasw netet &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run09_13_2020/ -o enduser/DelawareRiverBasin/Run09_13_2020/ward_sandford_customer/ -y Annual etasw netet &
