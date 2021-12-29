Image=tbutzer/etm_docker_image

token:
	cat ~/github-token
hello:
	echo hello - did you mean make build instead or make publish
	find . -size +100M
	git status
publish: token
	#git remote set-url origin git@github.com:tonybutzer/etops.git
	git remote set-url origin https://github.com/tonybutzer/etm.git
	git config --global user.email tonybutzer@gmail.com
	git config --global user.name tonybutzer
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push


docker-enable:
	#sudo groupadd docker
	sudo usermod -aG docker ubuntu

build:
	docker build -t ${Image} .

run:
	docker run -it ${Image} bash

exec:
	docker exec -it ${Image} bash

images:
	docker image ls
	echo ================================================================================
	docker image ls | grep greg


docker-jup:
	docker build -f Dockerfile.jup -t tbutzer/local-jup .


jup-run:
	docker run -it -p 8080:8888 -v /var/run/docker.sock:/var/run/docker.sock -v `pwd`:/home tbutzer/local-jup jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'
