run:  ## clean and make target, run target
	python3 -m analytics 

tests: ## Clean and Make unit tests
	python3 -m nose -v analytics/tests --with-coverage --cover-erase --cover-package=`find analytics -name "*.py" | sed "s=\./==g" | sed "s=/=.=g" | sed "s/.py//g" | tr '\n' ',' | rev | cut -c2- | rev`
test: ## run the tests for travis CI
	@ python3 -m nose -v analytics/tests --with-coverage --cover-erase --cover-package=`find analytics -name "*.py" | sed "s=\./==g" | sed "s=/=.=g" | sed "s/.py//g" | tr '\n' ',' | rev | cut -c2- | rev`
 
annotate: ## MyPy type annotation check
	mypy -s analytics  

annotate_l: ## MyPy type annotation check - count only
	mypy -s analytics | wc -l 

clean: ## clean the repository
	find . -name "__pycache__" | xargs  rm -rf 
	find . -name "*.pyc" | xargs rm -rf 
	find . -name ".ipynb_checkpoints" | xargs  rm -rf 
	rm -rf .coverage cover htmlcov logs build dist *.egg-info

example: ## run simple example
	python3 analytics/example.py

install:  ## install to site-packages
	python3 setup.py install

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: clean run test help annotate annotate_l
