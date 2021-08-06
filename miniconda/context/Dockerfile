FROM continuumio/miniconda3:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

ADD DoubletDetection-master.zip /tmp

RUN apt-get install zip && cd /tmp && unzip DoubletDetection-master.zip && cd DoubletDetection-master && pip3 install . && \

RUN python -m pip install --upgrade pip && \
	pip install scrublet && \
	pip install pandas && \
	pip install scipy

ADD seqyuan_doublets.py /usr/bin
RUN chmod +x /usr/bin/seqyuan_doublets.py

ADD passwd /etc/
ADD group /etc/

