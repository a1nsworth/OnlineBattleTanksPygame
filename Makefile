build:
	docker-compose build

stop:
	docker-compose stop

down:
	docker-compose down

run:
	docker-compose up

run-it:
	docker-compose exec server sh
