.PHONY: run-dev
run-dev:
	docker-compose up --build

.PHONY: run-prod
run-prod:
	docker-compose -f docker-compose.prod.yml up --build -d

.PHONY: ssh
ssh:
	docker-compose exec backend /bin/sh

.PHONY: run-backend
run-backend:
	python3 ./backend/api-server/manage.py migrate && python3 ./backend/api-server/manage.py runserver 8000

.PHONY: makemigrations
makemigrations:
	DJANGO_SETTINGS_MODULE=core.settings python3 ./backend/api-server/manage.py makemigrations 

.PHONY: migrate
migrate:
	DJANGO_SETTINGS_MODULE=core.settings python3 ./backend/api-server/manage.py migrate 