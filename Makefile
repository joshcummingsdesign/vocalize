all: help

install:
	@./bin/download-model.sh
	@pip install -r requirements.txt

start:
	@./bin/start.sh

help:
	@echo
	@echo Vocalize
	@echo --------
	@echo "make install    Run the installation"
	@echo "make start      Start Vocalize"
	@echo

.PHONY: install start
