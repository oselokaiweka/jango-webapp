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
# one-test:
#	python -m pytest -vv test_file_path::test_function

format:
	black src realynx 

lint:
	PYTHONPATH=$(PWD) pylint --disable=R,C src realynx

all: install lint test format