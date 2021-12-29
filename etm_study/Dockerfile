FROM tbutzer/et-base-python

RUN pip install xarray \
    && pip install rioxarray

RUN mkdir -p /home/usa

COPY *.py /home/usa/

WORKDIR /home/usa
