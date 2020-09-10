BASEDIR=$(CURDIR)
contextDir=$(CURDIR)/context
dockerfile=Dockerfile
imagename=alpine
TAG=v0.0.1

dockerHub=registry.cn-hangzhou.aliyuncs.com/seqyuan

build:
	sudo docker build -t $(dockerHub)/$(imagename):$(TAG) -f $(contextDir)/$(dockerfile) $(contextDir)

test:
	sudo docker run -it $(dockerHub)/$(imagename):$(TAG) /bin/bash

push:
	sudo docker push $(dockerHub)/$(imagename):$(TAG)

pull:
	sudo docker pull $(dockerHub)/$(imagename):$(TAG)

help:
	@echo 'Makefile for $(imagename) docker image                       '
	@echo '                                                             '
	@echo 'Usage:                                                       '
	@echo '   make build         build $(imagename) docker image        '
	@echo '   make test          test the image                         '
	@echo '   make push          push the image to Docker hub registry  '
	@echo '   make pull          pull the image from Docker registry    '
