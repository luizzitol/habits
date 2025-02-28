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
	python3 ./backend/manage.py migrate && python3 ./backend/manage.py runserver 8080