# ET MOSAIC -- etm github repo

## Creates a Mosiac from smaller chips - example 2 degree**2

## Goals

## ERRORS
- aws s3 ls s3://ws-out/USA/Run08_18_2021/run_r50.0_tile6/r50.0_tile6/chip47.4N-106.8E/2008/etasw_200803.tif
- aws s3 ls s3://ws-out/USA/Run08_18_2021/run_r50.0_tile6/r50.0_tile6/chip47.4N-106.8E/2009/


## Stategy and Tactics
- write an et model verifier - make sure all chips have run and we have a comprehensive set of tifs for all years
- added some better error handling for mosaic 
- 2008 tile6 a good test case
- need to add some validation and retry logic for chip creation - ore better notification - or a babysitter service ...


## Next Steps
- rerun tile6 end to end - maybe tile5 as well -- on bigship - 24 hour turnaround - monitor 25 docker chips actively and identify weakspots - failure points if any.
- cleanup buckets continually
- add tags to buckets for AMI sponsorship


## Running the Code for Monthly

- docker system prune
- cd /opt/etm/02-orchestration-launcher
- vim etm_run.yml  # Adjust the parameters
- python3 

## Killing Docker Containers

```
docker kill `docker ps -q`
```


## Main Components
- docker orchestrators - poor man's kubernetes
- api_etm - main cmdline parameter getter
- etmlib
	- working code - mos_mosaic CLASS

## Building the Docker Image - Important

- cd /opt/etm
- make build

## Self Documenting Approaches
- Makefiles
- Dockerfile

## Steps

- improve the monthly mosaic orchestrator
	- 
- Run the monthly for a few tiles
- Continue to improve the readme
= teach steffi how to run monthly mosaics
- finish USA/CONUS tiles
- have steffi's team build a USA mosaic - by writing the python


### Todo

- lots of code cleanup
- better logging
- failure event handling and retry logic




### Completed


# etm
ET Mosaic Docker Image Development


## Example Monthly

### YAML file

```
ubuntu@ip-10-12-68-129:/opt/etm/02-orchestration-launcher$ cat monthly_etm_run.yml
#products: ['etasw','srf','dd','netet', 'etasw5','etc','rain','snowmelt','snwpk','swe','swf','swi']

products: ['etasw', 'netet']

start_year: 2020
end_year: 2021

unmosaicked_inputs:
        - 'ws-out/USA/Run08_18_2021/run_r50.0_tile5/r50.0_tile5/'
        - 'ws-out/USA/Run08_18_2021/run_r50.0_tile6/r50.0_tile6/'
        - 'ws-out/USA/Run08_18_2021/run_r50.0_tile7/r50.0_tile7/'
        - 'ws-out/USA/Run08_18_2021/run_r50.0_tile8/r50.0_tile8/'
        - 'ws-out/USA/Run08_18_2021/run_r50.0_tile9/r50.0_tile9/'
enduser_cog_output: 'ws-enduser/USA/TBD/'

max_concurrent_containers: 60
max_cpu_percent: 220
min_memory_available: 30

sleep_time: 1
```

#### python3 et-monthly-mosaic-creator.py

- docker ps

```
ubuntu@ip-10-12-68-129:/opt/etm/02-orchestration-launcher$ docker ps
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS     NAMES
3ea327a4cb99   tbutzer/etm_docker_image   "python3 api_etm.py …"   21 seconds ago   Up 21 seconds             etmv1_monthly-_netet_r50.0_tile9
10aa33441ae8   tbutzer/etm_docker_image   "python3 api_etm.py …"   23 seconds ago   Up 22 seconds             etmv1_monthly-_netet_r50.0_tile8
4c0b0c8f4415   tbutzer/etm_docker_image   "python3 api_etm.py …"   24 seconds ago   Up 24 seconds             etmv1_monthly-_netet_r50.0_tile7
a2d26319ec1c   tbutzer/etm_docker_image   "python3 api_etm.py …"   26 seconds ago   Up 25 seconds             etmv1_monthly-_netet_r50.0_tile6
8a6cc161302a   tbutzer/etm_docker_image   "python3 api_etm.py …"   27 seconds ago   Up 27 seconds             etmv1_monthly-_netet_r50.0_tile5
47a5682aee0c   tbutzer/etm_docker_image   "python3 api_etm.py …"   29 seconds ago   Up 28 seconds             etmv1_monthly-_etasw_r50.0_tile9
7dc72507e94e   tbutzer/etm_docker_image   "python3 api_etm.py …"   30 seconds ago   Up 30 seconds             etmv1_monthly-_etasw_r50.0_tile8
3892ce0771bf   tbutzer/etm_docker_image   "python3 api_etm.py …"   31 seconds ago   Up 31 seconds             etmv1_monthly-_etasw_r50.0_tile7
b97eeefbec07   tbutzer/etm_docker_image   "python3 api_etm.py …"   33 seconds ago   Up 32 seconds             etmv1_monthly-_etasw_r50.0_tile6
9ac97896b34d   tbutzer/etm_docker_image   "python3 api_etm.py …"   34 seconds ago   Up 34 seconds             etmv1_monthly-_etasw_r50.0_tile5
```
