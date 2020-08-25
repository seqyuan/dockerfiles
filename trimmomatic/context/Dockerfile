FROM openjdk:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

WORKDIR /bin

RUN yum install -y unzip iotop&& \
		curl -o Trimmomatic-0.39.zip http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip && \
		unzip Trimmomatic-0.39.zip && mv Trimmomatic-0.39/trimmomatic-0.39.jar ./ && \
		chmod a+x ./trimmomatic-0.39.jar && rm -r Trimmomatic-0.39 Trimmomatic-0.39.zip

ADD passwd /etc/
ADD group /etc/

