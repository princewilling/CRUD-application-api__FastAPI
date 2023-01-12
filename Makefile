install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black app/*.py tests/*.py 

lint:
	#flake8 | # pylint
	pylint --disable=R,C app/*.py tests/*.py

test:
	pip install pytest
	pytest -x

build:
	#build container

deploy:
	#deploy

all: install format lint test deploy
