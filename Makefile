install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# python -m pytest -vv --cov=main  test_*.py

format:	
	black *.py

lint:
	ruff check *.py

deploy:
	#deploy goes here
		
all: install test format lint deploy