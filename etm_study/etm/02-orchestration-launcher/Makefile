graph:
	pyan3 --dot etm-conductor-orchestration-v2.py |dot -Tsvg -o api.svg
    
    
note:
	echo you need an older version of pyan3 - the current one is broke
	echo etm-conductor should use underscore etm_conductor_orch 

testrun:
	docker rm -f testrun
	docker run -it --name testrun tbutzer/etm_docker_image python api_etm.py -i ws-out/CONUS/Run07_23_2021/ -o ws-enduser/CONUS/r50_0_tile/ -y 2000 dd dummy


dummy:
	docker run -it --name testrun tbutzer/etm_docker_image ls


