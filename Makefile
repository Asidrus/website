#!make
include .env
export $(shell sed 's/=.*//' .env)
args=$(shell cat .env | sed 's@^@--build-arg @g' | paste -s -d " ")
build:
	docker build ${args} . --tag ${PROJECT}
remove:
	docker rmi -f ${PROJECT}
run:
	docker run \
		-d \
		--rm \
		--net=host \
		--name=${PROJECT} \
		-v ${STORAGE}${PROJECT}:${STORAGE} \
		${PROJECT}
stop:
	docker stop ${PROJECT}
