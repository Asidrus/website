build:
	docker build . --tag website
remove:
	docker rmi -f website
run:
	docker run \
		--rm \
		--net=host \
		--name='website' \
		-d \
		website
stop:
	docker stop website
