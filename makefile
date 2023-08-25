
build:
	python -m build -n

upload:
	python -m twine upload dist/*

.PHONY: clean
clean:
	rm -rf dist
