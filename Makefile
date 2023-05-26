test:
	pytest --cov-config=.coveragerc --cov=src

lint:
	ruff ./src/