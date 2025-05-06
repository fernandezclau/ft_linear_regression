# Makefile for ft_linear_regression

.PHONY: help setup install train run test clean

# Default help message
help:
	@echo "Usage:"
	@echo "  make setup     Create virtual environment and activate it"
	@echo "  make install   Install Python dependencies"
	@echo "  make train     Train the linear regression model"
	@echo "  make run       Run the Flask web application"
	@echo "  make test      Run basic tests"
	@echo "  make clean     Remove virtual environment and __pycache__"

# Create virtual environment
setup:
	@python3 -m venv .venv
	@echo "Virtual environment created. Activate it with:"
	@echo "source .venv/bin/activate  # On Unix/macOS"
	@echo ".venv\\Scripts\\activate   # On Windows"

# Install dependencies
install:
	@.venv/bin/pip install --upgrade pip
	@.venv/bin/pip install -r requirements.txt

# Train the model
train:
	@.venv/bin/python train.py

# Run the web app
run:
	@.venv/bin/python app.py

# Run tests
test:
	@.venv/bin/python test.py

# Clean project
clean:
	@rm -f ./data/parameters.csv

# Fclean project
fclean:
	clean
	@rm -rf __pycache__ .venv
	@find . -name "*.pyc" -delete

