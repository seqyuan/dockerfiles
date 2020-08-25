# image-SOAPnuke
SOAPnuke docker image

`/bin/SOAPnuke-SOAPnuke2.1.0/SOAPnuke`

Version: 2.1.0

Dockerfile
```
FROM seqyuan/base:v0.0.1

MAINTAINER Yuan Zan <seqyuan@gmail.com>

WORKDIR /bin

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
		apk add gcc g++ make && \
		wget  http://www.zlib.net/zlib-1.2.11.tar.gz && \
		tar -zxvf zlib-1.2.11.tar.gz && \
		cd zlib-1.2.11 && \
		./configure && \
		make && \
		make install && \
		cd ../ && \
		wget https://codeload.github.com/BGI-flexlab/SOAPnuke/zip/SOAPnuke2.1.0 && \
		unzip SOAPnuke2.1.0 && \
		cd SOAPnuke-SOAPnuke2.1.0 && \
		make && \
		echo "export PATH=/bin/SOAPnuke-SOAPnuke2.1.0:\$PATH" >> ~/.bashrc
```
