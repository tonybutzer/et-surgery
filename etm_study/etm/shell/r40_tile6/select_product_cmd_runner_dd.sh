docker run -i --name etmv1_2003_dd tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2003 dd dummy  2>&1 | tee  ./log/etmv1_2003_dd&
