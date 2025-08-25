build:
	./build.sh

install:
	uv sync

collecstatic:
	uv run python manage.py collecstatic

migrate:
	uv run python manage.py migrate

start:
	uv run python manage.py runserver

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run ruff check task_manager
