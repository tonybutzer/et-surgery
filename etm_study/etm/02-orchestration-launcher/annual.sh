
INPUT=out/DelawareRiverBasin/Run11_11_2020
OUTPUT=enduser/DelawareRiverBasin/drb150b

echo docker run -i tbutzer/etm_docker_image python3 api_etm.py -i ${INPUT} -o ${OUTPUT} -y Annual etasw dummy
docker run -i tbutzer/etm_docker_image python3 api_etm.py -i ${INPUT} -o ${OUTPUT} -y Annual etasw dummy
