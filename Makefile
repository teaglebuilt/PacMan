DOCKER := docker
DOCKER_COMPOSE := docker-compose
API_CONTAINER := backend
DB_CONTAINER := postgres
FLASK := flask


.PHONY: nuke
nuke:
	${DOCKER} system prune -a

.PHONY: rm-exited-containers
rm-exited-containers:
	${DOCKER} ps -a -q -f status=exited | xargs ${DOCKER} rm -v

.PHONY: up
up:
	${DOCKER_COMPOSE} up --build -d

.PHONY: setup
setup:  
	up
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK}
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db-migrate create-tables

.PHONY: migrate
migrate: build
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db migrate
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db upgrade