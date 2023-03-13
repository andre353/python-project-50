install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint	

test:
	poetry run pytest

.PHONY: install build publish package-install gendiff lint selfcheck check test