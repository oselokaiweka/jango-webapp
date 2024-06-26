# Makefile for managing project

# Install dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Apply database migrations
migrate:
	python manage.py migrate

# Start the development server
runserver:
	python manage.py runserver

# Run test
test:
	python -m pytest -vv --cov=src --cov=realynx src.tests realynx

# Invoke debugger on test fail
debug:
	python -m pytest -vv --pdb 

# Drop to pdb for first three failures
debug-maxfail:
	python -m pytest -vv --pdb --maxfail=3 

# Test a pecified file or directory (uncomment)
 one-test:
	python -m pytest -vv test_file_path::test_function

format:
	black src realynx 

lint:
	PYTHONPATH=$(PWD) pylint --disable=R,C src realynx

# Build Docker container
docker-build:
	docker-compose build

# Start Docker container in the background
docker-up:
	docker-compose up

# Stop Docker container
docker-stop:
	docker-compose stop

# Remove Docker container
docker-down:
	docker-compose down

# Restart Docker container
docker-restart:
	docker-compose restart

# Show Docker container logs
docker-logs:
	docker-compose logs -f

# Rebuild and start the container
docker-rebuild: docker-down docker-build docker-up

# Run the Docker container interactively (for debugging)
docker-interactive:
	docker-compose run --service-ports realynx_django_app bash

# Clean up Docker resources (stopped containers, unused images, etc.)
docker-clean:
	docker system prune -f

# Default task to run all steps
all: install lint test format

# Docker task to build, start and show logs
docker-all: docker-build docker-up docker-logs

all2: install lint test format docker-build docker-up docker-logs