# Makefile for ft_linear_regression

.PHONY: help setup install uninstall train run test clean fclean

# Default help message
help:
	@echo "Usage:"
	@echo "  make setup     Create virtual environment and activate it"
	@echo "  make install   Install Python dependencies"
	@echo "  make train     Train the linear regression model"
	@echo "  make run       Run the Flask web application"
	@echo "  make test      Run basic tests"
	@echo "  make clean     Remove trained model"
	@echo "  make fclean    Exec clean and remove virtual environment and __pycache__"

# Create virtual environment
setup:
	@python3 -m venv .venv
	@echo "Virtual environment created. Activate it with:"
	@echo "source .venv/bin/activate  # On Unix/macOS"
	@echo ".venv\\Scripts\\activate   # On Windows"

# Install dependencies
install:
	pip install --user --upgrade pip
	pip install --user -r requirements.txt

# Uninstall dependencies
uninstall:
	pip freeze --user | xargs pip uninstall -y

# Train the model
train:
	python3 train.py

# Run the web app
run:
	python3 app.py

# Run tests
test:
	python3 test.py

# Clean project
clean:
	@rm -f ./data/parameters.csv

# Fclean project
fclean:
	$(MAKE) clean
	@rm -rf __pycache__
	@find . -name "*.pyc" -delete

