# Software Architecture and Design

## 1. Table of Contents

- [1. Table of Contents](#1-table-of-contents)
- [2. About The Project](#2-about-the-project)
    - [2.1. Submission Title](#21-submission-title)
    - [2.2. Developer Names](#22-developer-names)
    - [2.3. Release Notes](#23-release-notes)
    - [2.4. Built With](#24-built-with)
- [3. Getting Setup](#3-getting-setup)
    - [3.1. Contents of Submission](#31-contents-of-submission)
    - [3.2. Prerequisites](#32-prerequisites)
    - [3.3. Installation](#33-installation)
- [4. Usage](#4-usage)
- [5. Acknowledgements](#5-acknowledgements)

## 2. About The Project

### 2.1. Submission Title

Complaint Management System

### 2.2. Developer Names

Thomas Joseph Webster

### 2.3. Release Notes

This is the assessment project for the Software Architecture and Design (SAaD) module. This assignment required that I fully conceptualise and record the architectural, database and security decisions, and then implement some of these designs into a Proof of Concept.

### 2.4. Built With

- Python (Flask)
- SQLite3
- HTML/CSS
- JavaScript
- JWT (PyJWT)
- bcrypt

## 3. Getting Setup


### 3.1. Contents of Submission

**POC**

    - frontend/ - Flask frontend serving HTML templates
    - user_service/ - User authentication microservice
    - problem_service/ - Problem management microservice
    - tenant_service/ - Tenant management microservice
    - templates/ - HTML templates (login, dashboard, create problem)
    - static/ - CSS stylesheets
    - tests/ - pytest and Selenium test files
    - tenant_service.db - Tenant database
    - user_service.db - User database
    - problem_service.db - Problem database
    - requirements.txt - Python dependencies

**Images**

    - test_results/ - Test result screenshots 
    - C4/ - C4 Diagrams (png and raw drawio)
    - Wireframe/ - Wireframes (png and raw drawio)
    - other/ - Everything else (png and raw drawio)


### 3.2. Prerequisites

- Python 3.12+
- pip (For installing from `requirements.txt`)

### 3.3. Installation

1. Download and unzip the file
2. Open folder with IDE of choice
3. Open a terminal and cd into the SAAD folder
4. Run `python -m venv venv`
5. Run `source venv/bin/activate` to activate venv (Linux/Mac) or `venv\Scripts\activate` (Windows)
6. Run `pip install -r requirements.txt`
7. After installation, open four terminals
8. Activate venv in each terminal and cd into the SAAD folder
9. Run each command in a separate terminal:
   - `python tenant_service/app.py`
   - `python user_service/app.py`
   - `python problem_service/app.py`
   - `python frontend/app.py`
10. Open a web browser and navigate to `http://127.0.0.1:5000/`

**Test Credentials:** test@barclays.com / password123

**Running Tests:**
```bash
source venv/bin/activate
pytest tests/ -v
```

## 4. Usage
**Login:** Enter credentials to receive JWT token and access dashboard

**View Problems:** Dashboard displays all problems for your tenant with status badges

**Create Problem:** Click "Create Problem", enter title (max 50 chars) and optional description

**Update Status:** Click "Close Problem" on the dashboard to close a problem ticket



## 5. Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyJWT Documentation](https://pyjwt.readthedocs.io/)
- [bcrypt Documentation](https://pypi.org/project/bcrypt/)
- [Flask-CORS Documentation](https://flask-cors.readthedocs.io/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
