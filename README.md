# Sagewhale

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/made-with-typescript.svg)](https://forthebadge.com)

<img src="./static/sagewhale-logo.svg" width=60% height=60%>

Sagewhale is a web application that allows ingestion of JSON or CSV files containing email subscriber performance data. The data can be analyzed and visualized to give insights about different product types in relation to subscriber demographics.

## Server

### Prerequisites

**Disclaimer:** The instructions below assume MacOS. If you're on a Windows machine, you will have to use `scoop` or `chocolatey` to install `pyenv`, `pipenv`, and `docker`. The setup may be different.

Local machine dependencies:

- `pyenv`: Install by running `brew install pyenv`
  - Make sure to install python version by running `pyenv install <PYTHON_VERSION>`
    - You can get the list of avaliable versions by running `pyenv install --list`
  - Set global python version by running `pyenv global <PYTHON_VERSION>`
- `pipenv`: Install by running `brew install pipenv`

### Setup

To get the project setup, run the following command in this project directory:

```bash
pipenv sync --dev
```

This will install the necessary project dependencies as well as developed-related tools based on the `Pipfile.lock`. This file is our source of truth for all things dependency.

To start development of the `server`, remember to start a virtual environment with (uses `pyenv` global version):
```bash
pipenv shell
```
OR with a specified version that you have already installed with `pyenv`:
```bash
pipenv shell --python <PYTHON_VERSION>
```

### Run

TBD

### Development Tasks

Running `invoke --list` will list out all available development tasks defined in the `tasks.py` file:

```bash
Available tasks:

  pycheck    Format, lint, analyze code complexity, and security code scan
  pycomp     Calculates cyclomatic complexity of Python code
  pyformat   Formats Python code using black
  pylint     Lints Python code using pylint
  pysec      Finds common security issues in Python code
  server     Starts the server with database container
```

These are useful to use DURING development to help you develop smarter, more efficiently, and to coding standards.

## Client

### Prerequisites

TBD

### Setup

TBD

### Run

TBD
