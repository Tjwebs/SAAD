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
- [5. Roadmap](#5-roadmap)
- [6. Acknowledgements](#6-acknowledgements)

## 2. About The Project

### 2.1. Submission Title

Complaint Management System

### 2.2. Developer Names

Thomas Joseph Webster

### 2.3. Release Notes

This is the assessment project for the Software Architecture and Design (SAaD) module. This assignment required that I fully conceptualise and record the architectural, database and security decisions, and then implement some of these designs into a Proof of Concept.

### 2.4. Built With

This section should be dedicated to what you used to make your project. All major frameworks should be listed, for example:

- Python
- SQLite3
- HTML/CSS
- JavaScript
- SQL Server

## 3. Getting Setup

Download and unzip the file.

Open folder with IDE of choice.

Open a terminal cd into the SAAD folder then run "python -m venv path/to/venv/"

Run "source /path/to/SAAD/venv/bin/activate" to activate venv

Then run "pip install -r requirements.txt"

After installation is finished open four terminals

Make sure the venv is active in each terminal and you are cd'd into the root SAAD folder.

Run the following lines of code each in a separate terminal as they must stay running (the order doesn't matter)

1. "python tenant_service/app.py"
2. "python problem_service/app.py"
3. "python user_service/app/py"
4. "python frontend/app.py"
Open a web browser and in the search bar type in "http://127.0.0.1:5000/"

If you wish to run the non-postman tests open a new terminal, cd to SAAD folder, activate venv and type "pytest tests/ -v" The results will be displayed in the terminal
### 3.1. Contents of Submission

List all contents of your submission here, such as:

- HTML/CSS/JS for all pages
- AccountController.cs
- Quote.cs
- Login.cs
- Unit-Testing.docx
- etc...

### 3.2. Prerequisites

In this section, outline any prerequisites for running the software, such as:

- ASP.NET Core
- Visual Studio 2019
- Microsoft.Data.SqlClient
- etc...

### 3.3. Installation

Explain how to install your software to run. For example "Unzip the submission folder and load it into IntelliJ IDEA. Ensure you have the prerequisites installed and are imported correctly. Install the Microsoft.Data.SqlClient NuGet package using Package Manager etc..."

Use Screenshots if possible for installing packages, or link to documentation (can also include this in the acknowledgements).

## 4. Usage

Use this section for showing examples of how the software can be used. Include screenshots, code snippets etc. Also link to any documentation you may have here.

## 5. Roadmap

Explain your roadmap. What have you developed so far? What would be developed in future releases? Link to Github Issues if you use them.

## 6. Acknowledgements

Use this final section for listing links to any resources you have used, frameworks, information sources etc...

- [ASP.NET Core documentation](https://docs.microsoft.com/en-us/aspnet/core/?view=aspnetcore-5.0)
- [Microsoft.Data.SqlClient documentation](https://www.nuget.org/packages/Microsoft.Data.SqlClient/)
- [Procure to Pay system](https://kissflow.com/procurement/procure-to-pay-process-guide/)
