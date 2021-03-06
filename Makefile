#!make
include .env
export $(shell sed 's/=.*//' .env)
args=$(shell cat .env | grep -v SECRET_KEY | sed 's@^@--build-arg @g' | paste -s -d " ")
build:
	docker build ${args} . --tag ${PROJECT}
remove:
	docker rmi -f ${PROJECT}
run:
	docker run \
		-d \
		--rm \
		-p ${IP}:${PORT}:443 \
		--name=${PROJECT} \
		-v ${STORAGE}${PROJECT}/static:/app/${PROJECT}/static \
		${PROJECT}
stop:
	docker stop ${PROJECT}