docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y Annual dd dummy  2>&1 | tee  ./log/etm1years_dd_annual &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y Annual netet dummy  2>&1 | tee  ./log/etm1years_netet_annual &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y Annual etc dummy  2>&1 | tee  ./log/etm1years_etc_annual &
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/DelawareRiverBasin/Run10_07_2020/ -o enduser/DelawareRiverBasin/drb150/ -y Annual srf dummy  2>&1 | tee  ./log/etm1years_srf_annual &
