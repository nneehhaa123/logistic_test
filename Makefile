install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=. --cov-report=lcov */*.py

format:	
	black */*.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py */*.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
	#streamlit run prediction/app.py
	docker build -t insurnce_tool .
	docker run -p 8501:8501 insurnce_tool

		
all: install lint test format deploy
