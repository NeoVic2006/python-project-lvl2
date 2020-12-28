install:
		@poetry install

lint:
		poetry run flake8 gendiff
	
test:
		poetry run pytest -q tests/tests.py 
		poetry run pytest --cov=gendiff --cov-report xml tests/tests.py