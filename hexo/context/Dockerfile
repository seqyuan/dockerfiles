FROM node:14.11.0-alpine3.12

MAINTAINER Yuan Zan <seqyuan@gmail.com>

# Install requirements
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
		apk update && apk add --no-cache bash git && \
		if [ -e /bin/sh ];then rm /bin/sh ; fi && \
		if [ -e /bin/bash ];then ln -s /bin/bash /bin/sh ; fi && \
		npm install -g hexo-cli && \
		npm install hexo-deployer-git --save


WORKDIR /app
