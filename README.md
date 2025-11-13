# C8 - DevOps Activity

This repository demonstrates a simple **Flask web application** integrated with **Continuous Integration (CI)** using **GitHub Actions**.  
It includes automated testing, linting, dependency updates, security scanning, and multi-version Python testing.

---

## Project Overview
The Flask app provides three simple API routes:
- `GET /hello` → returns a greeting message  
- `POST /echo` → echoes back any JSON payload sent  
- `PUT /items/<key>` → creates or updates an item (stored in memory)  
- `DELETE /items/<key>` → deletes an item if it exists  

All endpoints are tested using `pytest`.

---

## Technologies Used
- **Python 3.10–3.12**
- **Flask** — Web framework  
- **pytest** — Unit testing  
- **pytest-cov** — Code coverage  
- **flake8** — Code linting  
- **GitHub Actions** — CI workflows  
- **Dependabot** — Dependency management  
- **CodeQL** — Security analysis

---

## CI/CD Workflows

| Workflow | File | Description |
|-----------|------|-------------|
| **Tests** | `.github/workflows/python-tests.yml` | Runs unit tests on Python 3.10, 3.11, 3.12 |
| **Linting** | `.github/workflows/lint.yml` | Runs Flake8 for style checks |
| **Dependabot** | `.github/dependabot.yml` | Weekly dependency updates |
| **CodeQL** | `.github/workflows/codeql-analysis.yml` | Static code analysis for security vulnerabilities |

All workflows trigger automatically on `push` and `pull_request`.

---

## Running Locally

```
# 1. Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate  

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
