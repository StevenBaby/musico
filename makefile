
build:
	python -m build -n

upload:
	python -m twine upload dist/*

src/ui/%.py: src/ui/%.ui
	pyside6-uic.exe $< -o $@

UI_FILES := src/ui/tuner.py

ui: $(UI_FILES)
	-

.PHONY: clean
clean:
	rm -rf dist
	rm -rf $(UI_FILES)
