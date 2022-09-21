FROM continuumio/miniconda3:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

WORKDIR /app

#COPY ./DoubletDetection /tmp/DoubletDetection/
COPY ./requirements.txt /tmp

RUN python -m pip install --upgrade pip && \
		cd /tmp && pip install -r requirements.txt
#cd /tmp/DoubletDetection && pip3 install . && \

#ADD seqyuan_doublets.py /usr/bin
#RUN chmod +x /usr/bin/seqyuan_doublets.py

ADD passwd /etc/
ADD group /etc/

