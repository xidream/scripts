install:
	pip install -r requirements.txt

autoflake:
	autoflake . -r -i --remove-unused-variables --remove-all-unused-imports

black:
	black .

isort:
	isort . --profile black

format: autoflake black isort
