FROM python:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

RUN python -m pip install --upgrade pip && \
		pip install doubletdetection && \
		pip install scrublet && \
		pip install pandas && \
		pip install scipy

ADD passwd /etc/
ADD group /etc/

