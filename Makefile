.PHONY: black
black:
	black betfund_solicitor
	black tests

.PHONY: tests
tests:
	pytest --cov=betfund_solicitor --cov-report term-missing .

.PHONY: lint
lint:
	pylint betfund_solicitor