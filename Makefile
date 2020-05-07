.PHONY: test
test:
	@pytest -vv --cov=crawler tests

.PHONY: check
check:
	@black . --check --exclude=test_character

.PHONY: format
format:
	@black . --exclude=test_character

.PHONY: test-update
test-update:
	@pytest --force-regen
