docker run -i --name etmv1_2000_netet tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2000 netet dummy  2>&1 | tee  ./log/etmv1_2000_netet&
docker run -i --name etmv1_2003_netet tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2003 netet dummy  2>&1 | tee  ./log/etmv1_2003_netet&
