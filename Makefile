.PHONY: test
test:
	MYPYPATH=stubs mypy le.py
	coverage run tests.py
	coverage report
