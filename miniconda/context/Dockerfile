FROM continuumio/miniconda3:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

RUN python -m pip install --upgrade pip && \
		git clone git@github.com:JonathanShor/DoubletDetection.git && cd DoubletDetection && pip3 install . && \
		pip install scrublet && \
		pip install pandas && \
		pip install scipy

ADD seqyuan_doublets.py /usr/bin
RUN chmod +x /usr/bin/seqyuan_doublets.py

ADD passwd /etc/
ADD group /etc/

