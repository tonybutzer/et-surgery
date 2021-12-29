docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 1999 srf dummy  2>&1 | tee  ./log/etm11999&
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2000 srf dummy  2>&1 | tee  ./log/etm12000&
