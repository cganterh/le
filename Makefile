.PHONY: test
test:
	flake8 .
	MYPYPATH=stubs mypy le.py
	coverage run tests.py
	coverage-badge -qfo coverage.svg
	coverage report
