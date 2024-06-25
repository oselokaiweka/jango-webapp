# Makefile for managing project

# Define the django project directory
PROJ_DIR=property_webapp_project
MANAGER=$(PROJ_DIR)/manage.py

# Install dependencies
install:
	pip install --upgrade pip && pip install -r requirements.txt

# Apply database migrations
migrate:
	python manage.py migrate

# Start the development server
runserver:
	python $(MANAGER) runserver


test:
	python -m pytest -vv --cov=src --cov=$(PROJ_DIR) tests
	
	python -m pytest --nbval notebook.ipynb # Tests project jupyter notebook

debug:
	python -m pytest -vv --pdb # Invoke debugger on test fail

debug-maxfail:
	python -m pytest -vv --pdb --maxfail=3 # Drop to pdb for first three failures

one-test:
	python -m pytest -vv tests/test_greeting.py::test_my_name4

format:
	black src mylib 

lint:
	PYTHONPATH=$(PWD) pylint --disable=R,C src mylib

all: install lint test format