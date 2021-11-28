build:
	docker build . --tag website
remove:
	docker rmi -f website
run:
	docker run \
		--rm \
		--net=host \
		website \
		bash -c \
		"python manage.py runserver 80.87.200.64:443"