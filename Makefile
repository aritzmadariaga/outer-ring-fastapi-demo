.PHONY: help up down logs migrate seed unit integration test docs lint format check-types

# Ensure .env file exists
ifeq ($(wildcard ./.env),)
$(shell cp ./.env.example ./.env)
endif

help:
	@echo "Commands:"
	@echo "  up             : Build and start containers."
	@echo "  down           : Stop and remove containers and volumes."
	@echo "  logs           : Follow application logs."
	@echo "  migrate        : Generate and apply migrations."
	@echo "  seed           : Populate database with initial data."
	@echo "  unit           : Run unit tests."
	@echo "  integration    : Run integration tests."
	@echo "  test           : Run all tests with coverage."
	@echo "  docs           : Build Sphinx documentation."
	@echo "  lint           : Run ruff linter."
	@echo "  format         : Run black and isort."
	@echo "  check-types    : Run mypy for static type checking."

up:
	docker compose up -d --build

down:
	docker compose down -v

logs:
	docker compose logs -f app

migrate:
	docker compose exec app alembic revision --autogenerate -m "Initial migration"
	docker compose exec app alembic upgrade head

seed:
	docker compose exec app python scripts/seed.py

# To run tests, we use `docker compose run` to ensure a clean environment
unit:
	docker compose run --rm app pytest tests/unit

integration:
	docker compose run --rm app pytest tests/integration

test:
	rm -f .coverage*
	docker compose run --rm -e COVERAGE_FILE=/app/.coverage app pytest --cov --cov-report=term-missing --cov-fail-under=85


docs:
	docker compose run --rm app sphinx-build -b html docs/source docs/build

lint:
	docker compose run --rm -e PYTHONPATH=/app/src app ruff check --no-cache src tests

format:
	docker compose run --rm app black src tests && docker compose run --rm app isort src tests

check-types:
	docker compose run --rm app mypy src
