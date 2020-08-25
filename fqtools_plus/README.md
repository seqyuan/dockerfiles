#### Dockerfile
```
FROM centos:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

WORKDIR /bin

RUN yum install -y make gcc && \
		curl -o pigz-2.4.tar.gz http://zlib.net/pigz/pigz-2.4.tar.gz && \
		curl -o zlib-1.2.11.tar.gz http://www.zlib.net/zlib-1.2.11.tar.gz && \
		tar -zxvf zlib-1.2.11.tar.gz && \
		tar -zxvf pigz-2.4.tar.gz && \
		cd zlib-1.2.11 && ./configure && make && make install && \
		cd ../pigz-2.4 && make && cd ../ && \
		curl -o fqtools_plus-master.zip https://codeload.github.com/seqyuan/fqtools_plus/zip/master && \
		unzip fqtools_plus-master.zip && cd fqtools_plus-master && make && \
		echo "export PATH=/bin/fqtools_plus:\$PATH" >> ~/.bashrc && \
		cd ../ && rm zlib-1.2.11.tar.gz pigz-2.4.tar.gz fqtools_plus-master.zip

ADD passwd /etc/
ADD group /etc/
```

v1.2.0

/usr/bin/fqtools_plus-master/src/fqtools_plus
