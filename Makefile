VERSION=1.0.0
ENV_NAME=dev
ENVIRONMENT_VARIABLES=$(shell grep -v '^\#' src/app/config/${ENV_NAME}/env)

.PHONY: help

PORT=5001

clean:
	@find . -name "*.pyc" 
	@find . -name "*.pyo"
	@find . -name "*.log" 
	@find . -name "__pycache__" -type d 
	@find . -name ".pytest_cache" -type d 
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

lint:
	@black .

check-security-issues: clean
	@bandit -r ./src -ll -x 'tests','migrations' -c bandit.yaml
	@safety check

test:
	@pytest src/app/tests

test-coverage: clean
	@py.test -x --cov=src/app/ --cov-config=setup.cfg --cov-report xml 

test-matching: clean
	@py.test -k $(Q) --pdb -x src/app src/

run:
	@uvicorn src.main:app --reload --port $(PORT)
	
requirements-dev:
	@pip install -U -r requirements.txt

requirements-update:
	@pip freeze > requirements.txt

shell: ## Run repl
	@echo 'Loading shell with settings = $(BASE_SETTINGS)'
	@PYTHONSTARTUP=.startup.py ipython

migrate: ## Apply migrations
	@alembic upgrade head


detect-migrations:  ## Detect missing migrations
	@python $(MANAGE_PY) makemigrations --dry-run --noinput | grep 'No changes detected' -q || (echo 'Missing migration detected!' && exit 1)

envvars:
	@echo "export ${ENVIRONMENT_VARIABLES}"

release-draft: ## Show new release changelog
	towncrier --draft

release-patch: ## Create patch release
	bumpversion patch
	towncrier --yes
	git commit -am 'Update CHANGELOG'

release-minor: ## Create minor release
	bumpversion minor
	towncrier --yes
	git commit -am 'Update CHANGELOG'

release-major: ## Create major release
	bumpversion major
	towncrier --yes
	git commit -am 'Update CHANGELOG'
	