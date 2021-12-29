docker run -i --name etmv1_1999_etc tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 1999 etc dummy  2>&1 | tee  ./log/etmv1_1999_etc&
docker run -i --name etmv1_2000_etc tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2000 etc dummy  2>&1 | tee  ./log/etmv1_2000_etc&
docker run -i --name etmv1_2001_etc tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2001 etc dummy  2>&1 | tee  ./log/etmv1_2001_etc&
docker run -i --name etmv1_2002_etc tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2002 etc dummy  2>&1 | tee  ./log/etmv1_2002_etc&
docker run -i --name etmv1_2003_etc tbutzer/etm_docker_image python3 api_etm.py -i out/CONUS/Run03_26_2021/ -o enduser/CONUS/r40tile6/ -y 2003 etc dummy  2>&1 | tee  ./log/etmv1_2003_etc&
