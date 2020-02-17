.DEFAULT_GOAL := help

.ONESHELL:

.PHONY: start stop install up help

start: ## This activates the virtual environment
	bash config/venv.sh

install: start ## This activates the virtual environment and installs requirements
	pip3 install -r requirements.txt

stop: ## This deactivates the virtual environment
	bash config/deactivate.sh

up: ## This brings up the app
	bash config/start.sh

help: ## This is the help dialog
	@awk 'BEGIN {FS = ":.*##"; printf "Targets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
