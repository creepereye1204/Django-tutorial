.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit autoupdate

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m core.manage migrations

.PHONY: run-server
run-server:
	poetry run python -m core.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit ;