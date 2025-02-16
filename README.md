***Python Project with CI/CD Pipeline (CircleCI)***

***Overview***

This repository contains a Python project with automated unit tests, integration tests, and test coverage reports powered by CircleCI.

***Features***

✅ Automated unit tests with pytest✅ Test coverage report generated and browsable from CircleCI UI✅ CI/CD pipeline using CircleCI✅ Pre-commit checks with mypy and ruff✅ Modern dependency management using uv

***Setup & Installation***

Clone the repository:
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
Install dependencies:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Run tests:
```sh
pytest --cov=src --cov-report=html
```

View test coverage:

```sh open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

***CI/CD Pipeline (CircleCI)***

How it Works

Push to GitHub → CircleCI triggers the pipeline➡️ Runs:

Unit tests (pytest)

Coverage report (pytest-cov)

Linting (ruff)
Test results are visible in the CircleCI "Tests" tab➡️ Coverage reports are stored as "Artifacts", browsable in CircleCI UI.

***View Test Coverage in CircleCI***

1️⃣ Go to CircleCI Dashboard2️⃣ Open the latest Job Run3️⃣ Navigate to Artifacts4️⃣ Click on test-coverage/index.html to browse the report

***Tech Stack***

Python 3.12

Pytest

CircleCI

Coverage.py

Ruff (Linting)

Mypy (Type Checking)

UV (Dependency Management)

***License***

This project is licensed under the MIT License.

