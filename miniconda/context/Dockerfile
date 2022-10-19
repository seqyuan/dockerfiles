FROM continuumio/miniconda3:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

WORKDIR /app

COPY ./requirements.txt /app

RUN apt-get update && \
		apt-get install -y make \
		libxt-dev \
		gcc \
		libcurl4-openssl-dev \
		g++ \
#		pandoc \
#		pandoc-citeproc \
#		libcurl4-gnutls-dev \
#		libcairo2-dev \
#		libxt-dev \
#		xtail \
#		libssl-dev \
#		build-essential \
#		libxml2-dev \
#		libhdf5-dev \
#		libudunits2-dev \
		imagemagick \
		wget && \
		python -m pip install --upgrade pip && \
		pip install -r requirements.txt

RUN pip install -r requirements_2.txt

#cd /tmp/DoubletDetection && pip3 install . && \

#ADD seqyuan_doublets.py /usr/bin
#RUN chmod +x /usr/bin/seqyuan_doublets.py

ADD passwd /etc/
ADD group /etc/

