publish: 
	git add .
	git commit -m "automatic git update from Makefile"
	git push


token:
	cat ~/steffi-token


jup:
	docker run -it -p 80:8888 -v `pwd`:/home/jovyan/notebooks/ pangeo/pangeo-notebook jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'



build:
	docker build -t steffi1 .


run:
	docker run -it steffi1 bash
