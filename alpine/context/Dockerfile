FROM alpine:latest

MAINTAINER Yuan Zan <seqyuan@gmail.com>

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
	apk update && apk add --no-cache \
	ttf-dejavu sqlite bash && \
	mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \
	if [ -e /bin/sh ];then rm /bin/sh ; fi \
	&& if [ -e /bin/bash ];then ln -s /bin/bash /bin/sh ; fi


ADD passwd /etc/
ADD group /etc/

