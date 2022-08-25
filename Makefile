run:
	export FLASK_APP=popular_repos.py
	export FLASK_DEBUG=development
	python -m flask run

gunicorn:
	gunicorn --workers=4 --bind=127.0.0.1:5000 hello_world:app

lint:
	poetry run flake8

install:
	poetry install

test-coverage:
	poetry run pytest --cov-report xml

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest