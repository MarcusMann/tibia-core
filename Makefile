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
	@pytest --force-regen
