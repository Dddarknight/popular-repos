run:
	export FLASK_APP=server.py
	export FLASK_ENV=development
	export FLASK_DEBUG=True
	python -m flask run

gunicorn:
	gunicorn --workers=4 --bind=127.0.0.1:5000 hello_world:app

lint:
	poetry run flake8

install:
	poetry install

test-coverage:
	poetry run pytest --cov=. --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest