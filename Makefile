.PHONY: test
test:
	flake8 .
	MYPYPATH=stubs mypy le.py
	coverage run tests.py
	coverage-badge -qfo coverage.svg
	coverage report

.PHONY: sdist bdist_wheel
sdist bdist_wheel: test
	python setup.py $@

.PHONY: upload
upload: test clean sdist bdist_wheel
	twine upload $(twine_options) dist/*

.PHONY: upload_test
upload_test: twine_options = --repository-url https://test.pypi.org/legacy/
upload_test: upload

.PHONY: clean
clean:
	rm -rf build dist le.egg-info __pycache__