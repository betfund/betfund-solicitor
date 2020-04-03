.PHONY: black
black:
	black betfund_solicitor

.PHONY: tests
tests:
	pytest --cov=betfund_solicitor .

.PHONY: lint
lint:
	pylint betfund_solicitor