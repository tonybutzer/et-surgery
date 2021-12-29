
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y monthly srf dummy &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y monthly etc dummy
