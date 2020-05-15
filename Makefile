.PHONY: test
test:
	@pytest -vv --cov=crawler tests

.PHONY: check
check:
	@black . --check --exclude=test_character
	@autoflake -r crawler --check

.PHONY: format
format:
	@black . --exclude=test_character
	@autoflake -r crawler --in-place --remove-unused-variables --remove-all-unused-imports

.PHONY: test-update
test-update:
	@pytest -vv --force-regen


.PHONY: clean-pyc clean-build clean
clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr *.egg

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +