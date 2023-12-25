DOCKER_COMPOSE = docker-compose
DJANGO_CONTAINER = kami_api_1


up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

exec:
	docker exec -it $(DJANGO_CONTAINER) bash

migrate:
	docker exec -it $(DJANGO_CONTAINER) \
		python manage.py migrate

createsuperuser:
	docker exec -it $(DJANGO_CONTAINER) \
		python manage.py createsuperuser

test:
	docker exec -it $(DJANGO_CONTAINER) \
		python manage.py test

.PHONY: up exec migrate createsuperuser test