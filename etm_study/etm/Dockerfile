FROM tbutzer/et-base-python

ENV VERS=1.1

RUN apt-get update && \
	apt-get install -y vim

# What do we really need here - should prune this Greg
RUN \
	pip install --no-cache "rio-cogeo==2.0.1" && \
	pip install --no-cache xarray && \
	pip install --no-cache rioxarray 
	


ENV TONY_VERS=1.9
RUN mkdir -p /home/etm \
	&& mkdir -p /home/etm/api_etm/log

COPY etmLib /home/etm/etmLib
COPY api_etm /home/etm/api_etm

RUN (cd /home/etm/etmLib; make)

# Certificate Hell Fix!
RUN apt-get install ca-certificates && mkdir -p /etc/pki/tls/certs && \
	cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

WORKDIR /home/etm/api_etm
