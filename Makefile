build:
	python setup.py sdist bdist_wheel

clean:
	python setup.py clean --all

upload-test:
	twine upload --repository testpypi dist/*