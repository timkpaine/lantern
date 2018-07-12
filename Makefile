run:  ## clean and make target, run target
	python3 -m lantern 

build:  ## Build the repository
	python3 setup.py build 

tests: ## Clean and Make unit tests
	python3 -m nose -v tests --with-coverage --cover-erase --cover-package=`find lantern -name "*.py" | sed "s=\./==g" | sed "s=/=.=g" | sed "s/\.py//g" | tr '\n' ',' | rev | cut -c2- | rev`
	
test: ## run the tests for travis CI
	@ python3 -m nose -v tests --with-coverage --cover-erase --cover-package=`find lantern -name "*.py" | sed "s=\./==g" | sed "s=/=.=g" | sed "s/\.py//g" | tr '\n' ',' | rev | cut -c2- | rev`

annotate: ## MyPy type annotation check
	mypy -s lantern  

annotate_l: ## MyPy type annotation check - count only
	mypy -s lantern | wc -l 

clean: ## clean the repository
	find . -name "__pycache__" | xargs  rm -rf 
	find . -name "*.pyc" | xargs rm -rf 
	find . -name ".ipynb_checkpoints" | xargs  rm -rf 
	rm -rf .coverage cover htmlcov logs build dist *.egg-info
	make -C ./docs clean

serverextension: install ## enable serverextension
	jupyter serverextension enable --py lantern

labextension: install ## enable labextension
	jupyter labextension install jlab

install:  ## install to site-packages
	python3 setup.py install

preinstall:  ## install dependencies
	python3 -m pip install -r requirements.txt

postinstall:  ## install other requisite labextensions
	jupyter labextension install @jupyter-widgets/jupyterlab-manager
	jupyter labextension install @jupyterlab/plotly-extension
	jupyter labextension install @jpmorganchase/perspective-jupyterlab
	jupyter labextension install jupyterlab_bokeh
	jupyter labextension install bqplot
	jupyter labextension install qgrid

docs:  ## make documentation
	make -C ./docs html
	open ./docs/_build/html/index.html

dist:  ## dist to pypi
	python3 setup.py sdist upload -r pypi

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: clean build run test tests help annotate annotate_l docs
