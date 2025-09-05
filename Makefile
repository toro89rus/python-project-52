build:
	./build.sh

install:
	uv sync

collectstatic:
	uv run python manage.py collectstatic

migrate:
	uv run python manage.py migrate

start:
	uv run python manage.py runserver

start-dev:
	uv run python manage.py runserver --nostatic

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run ruff check task_manager

test:
	uv run manage.py test
