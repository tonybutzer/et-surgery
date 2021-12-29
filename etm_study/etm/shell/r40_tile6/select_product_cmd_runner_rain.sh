docker run -i --name etmv1_1999_rain tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 1999 rain dummy  2>&1 | tee  ./log/etmv1_1999_rain&
docker run -i --name etmv1_2000_rain tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2000 rain dummy  2>&1 | tee  ./log/etmv1_2000_rain&
docker run -i --name etmv1_2001_rain tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2001 rain dummy  2>&1 | tee  ./log/etmv1_2001_rain&
docker run -i --name etmv1_2002_rain tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2002 rain dummy  2>&1 | tee  ./log/etmv1_2002_rain&
docker run -i --name etmv1_2003_rain tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2003 rain dummy  2>&1 | tee  ./log/etmv1_2003_rain&
