.PHONY: run
run:
	docker-compose build && docker-compose up

.PHONY: shell
shell:
	docker-compose exec backend sh -c  'python manage.py shell'
