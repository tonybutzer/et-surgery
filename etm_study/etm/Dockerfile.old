FROM python

ENV VERS=1.1

RUN apt-get update && \
	apt-get install -y vim

# What do we really need here - should prune this Greg
RUN \
	pip install --no-cache matplotlib && \
	pip install --no-cache matplotlib_venn && \
	pip install --no-cache pandas && \
	pip install --no-cache seaborn && \
	pip install --no-cache plotly && \
	pip install --no-cache plotly.express && \
	pip install --no-cache rasterio && \
	pip install --no-cache awscli && \
	pip install --no-cache s3fs && \
	pip install --no-cache ffmpeg && \
	pip install --no-cache pika && \
	pip install --no-cache dash && \
	pip install --no-cache boto3 && \
	pip install --no-cache fiona && \
	pip install --no-cache rio-cogeo && \
	pip install --no-cache xarray && \
	pip install --no-cache rioxarray 
	


ENV TONY_VERS=1.5
RUN mkdir -p /home/etm \
	&& mkdir -p /home/etm/api_etm/log

COPY etmLib /home/etm/etmLib
COPY api_etm /home/etm/api_etm

RUN (cd /home/etm/etmLib; make)

# Certificate Hell Fix!
RUN apt-get install ca-certificates && mkdir -p /etc/pki/tls/certs && \
	cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

WORKDIR /home/etm/api_etm
