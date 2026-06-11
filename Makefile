.PHONY: up down build test report logs clean

up:
	docker compose up

build:
	docker compose up --build

up-detached:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	python -m pytest tests/

report:
	python report-generator/generate_report.py examples/evidence-admin-auth.json --output reports/generated-admin-auth-report.md

clean:
	docker compose down --volumes --remove-orphans
