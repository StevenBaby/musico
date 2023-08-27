
build:
	python -m build -n

upload:
	python -m twine upload dist/*

src/ui/%.py: src/ui/%.ui
	pyside6-uic.exe $< > $@

ui: src/ui/tuner.py
	-

.PHONY: clean
clean:
	rm -rf dist
