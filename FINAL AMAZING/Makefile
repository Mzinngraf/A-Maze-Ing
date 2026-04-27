NAME	= a_maze_ing.py
PYTHON	= python3
CONFIG	= config.txt
PIP		= $(PYTHON) -m pip

all: run

install:
	$(PIP) install --upgrade pip
	$(PIP) install flake8 mypy
	poetry install

dist:
	poetry build

run:
	$(PYTHON) $(NAME) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(NAME) $(CONFIG)

lint:
	flake8 .
	mypy $(NAME) --warn-return-any \
	--warn-unused-ignores \
	--ignore-missing-imports \
	--disallow-untyped-defs \
	--check-untyped-defs \
	--exclude 'config.txt' \

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf dist/

.PHONY: all install run debug lint clean