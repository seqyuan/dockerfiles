FROM centos:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

WORKDIR /bin


RUN yum install -y make gcc unzip && \
		curl -o pigz-2.6.tar.gz http://zlib.net/pigz/pigz-2.6.tar.gz && \
		curl -o zlib-1.2.11.tar.gz http://www.zlib.net/zlib-1.2.11.tar.gz && \
		tar -zxvf zlib-1.2.11.tar.gz && \
		tar -zxvf pigz-2.6.tar.gz && \
		cd zlib-1.2.11 && ./configure && make && make install && \
		cd ../pigz-2.6 && make && cd ../ && \
		curl -o fqtools_plus-master.zip https://codeload.github.com/seqyuan/fqtools_plus/zip/master && \
		unzip fqtools_plus-master.zip && cd fqtools_plus-master/src && make && \
		echo "export PATH=/bin/fqtools_plus/src:\$PATH" >> ~/.bashrc && \
		cd ../../ && rm zlib-1.2.11.tar.gz pigz-2.6.tar.gz fqtools_plus-master.zip && \
		mv fqtools_plus-master/src/fqtools_plus /bin/

ADD passwd /etc/
ADD group /etc/

ADD DownloadOssFile /bin/
ADD uploadLargeFile /bin/

#RUN groupadd -r seqyuan && useradd -r -g seqyuan seqyuan
#USER seqyuan

