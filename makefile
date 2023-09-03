VERSION:= $(shell python -c "from src import VERSION; print(VERSION) ")

build:
	python -m build -n

upload:
	python -m twine upload dist/*

src/ui/%.py: src/ui/%.ui
	pyside6-uic.exe $< -o $@

UI_FILES := src/ui/tuner.py

ui: $(UI_FILES)
	-

PYINSTALLER_ARGS:=
# PYINSTALLER_ARGS+= --onefile
PYINSTALLER_ARGS+= --noconsole
PYINSTALLER_ARGS+= --noconfirm
PYINSTALLER_ARGS+= --paths ./src
# PYINSTALLER_ARGS+= --paths ./src/ui
PYINSTALLER_ARGS+= -i src/assets/favicon.ico
PYINSTALLER_ARGS+= --add-data 'src/assets/favicon.ico;assets'

dist/tuner-latest.exe: src/tuner.py $(UI_FILES)
	pyinstaller $^ $(PYINSTALLER_ARGS) --name tuner-latest

tuner: dist/tuner-latest.exe
	-

test:
	echo $(VERSION)

.PHONY: clean
clean:
	rm -rf dist
	rm -rf build
	rm -rf $(UI_FILES)
