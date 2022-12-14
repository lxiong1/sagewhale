# Sagewhale

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/made-with-typescript.svg)](https://forthebadge.com)

<img src="./static/sagewhale-logo.svg" width=60% height=60%>

Sagewhale is a web application that allows ingestion of JSON or CSV files containing email subscriber performance data. The data can be analyzed and visualized to give insights about emailed product performances in relation to subscriber demographics.

## Server

### Technology Stack

High-level stack but not exclusive to:
- `python`
- `pipenv`
- `flask`
- `flask-restx`
- `flask-sqlalchemy`
- `pytest`
- `pytest-mock`
- `invoke`
- `docker`
- `docker-compose`
- `postgresql`

### Prerequisites

**Disclaimer:** The instructions below assume MacOS. If you're on a Windows machine, you will have to use `scoop` or `chocolatey` as your machine package managers. The setup may be different. Also be sure to check out official documentation on setup if necessary.

Local machine dependencies:

- `pyenv`: Install by running `brew install pyenv`
  - Make sure to install python version by running `pyenv install <PYTHON_VERSION>`
    - You can get the list of avaliable versions by running `pyenv install --list`
  - Set global python version by running `pyenv global <PYTHON_VERSION>`
- `pipenv`: Install by running `brew install pipenv`
- `docker`: Install by running `brew install docker`
  - **Make sure you have this running on your machine as the `server` depends on it**
- `docker-compose`: Install by running `brew install docker-compose`

### Setup

*Note: The setup assumes you have installed local machine dependencies properly.*

To get the project setup, run the following command in this project directory:

```bash
invoke pydep
```
OR
```bash
pipenv sync --dev
```

This will install the necessary project dependencies based on the `Pipfile.lock`. This file is our source of truth for all things dependency.

To start development of the `server`, remember to start a virtual environment with (uses `pyenv` global version):
```bash
pipenv shell
```
OR with a specified version that you have already installed with `pyenv`:
```bash
pipenv shell --python <PYTHON_VERSION>
```

This is very important because due to the setup as it is an enclosed environment. Trying to run tools like `invoke` will not work without the virtual environment unless you installed these tools globally.

### Run

Simply run:
```bash
invoke server
```

The [development task](#development-tasks) runs the `entrypoint.sh` file. Shortcut way to not have to think about how to stand it up since most useful tasks are under the `invoke` command. Another thing to note is that a `data` directory will be created at the root of the project to mount to the database container that is stood up during startup for persistence.

You can visit `http://localhost:5000` for the Swagger documentation after startup.

## Client

### Technology Stack

High-level stack but not exclusive to:
- `typescript`
- `nodejs`
- `react`
- `chakra-ui`
- `react-testing-library`

### Prerequisites

**Disclaimer:** The instructions below assume MacOS. If you're on a Windows machine, you will have to use `scoop` or `chocolatey` as your machine package managers. The setup may be different. Also be sure to check out official documentation on setup if necessary.

Local machine dependencies:

- `volta`: Install by running `curl https://get.volta.sh | bash`
  - Make sure to install a `node` version by running `volta install node@<VERSION>`
  - Make sure to install `yarn` by running `volta install yarn`

### Setup

*Note: The setup assumes you have installed local machine dependencies properly.*

To get the project setup, run the following command in this project directory:

```bash
invoke tsdep
```
OR
```bash
cd client && yarn install
```

### Run

Simply run:
```bash
invoke client
```

You can visit `http://localhost:3000` to see the application after startup.

## Development Tasks

Running `invoke --list` will list out all available development tasks defined in the `tasks.py` file:

```bash
Available tasks:

  alldep     Installs all project dependencies
  client     Starts the client
  pycheck    Format, lint, analyze code complexity, and security code scan
  pycomp     Calculates cyclomatic complexity of Python code
  pydep      Installs Python project dependencies
  pyformat   Formats Python code using black
  pylint     Lints Python code using pylint
  pysec      Finds common security issues in Python code
  pytest     Runs Python tests
  server     Starts the server with database container
  tsdep      Installs Typescript project dependencies
  tsformat   Formats Typescript code (and JSON) using prettier
  tstest     Runs Typescript tests
```

These tasks are not meant to be Python-specific although it is python dependent. They are agnostic of programming language and can be used to define and run any development tasks. It's useful to use them **during** development to help you build smarter, more efficiently, and to coding standards.

## Project Time Estimation & Actual Time Spent

**Time Estimation**

I estimated that this project could be completed within a week assuming 6-8 hours for 5 days. However, I don't think that it is as easy as saying this because it really depends on how much time an engineer should spend on the small details like refactoring for readability, investigating gaps where errors can occur, investigating performance bottlenecks or improvements, researching appropriate design patterns with given situations, etc. These things bring in factors that can't quite be estimated well for. With all the aforementioned considered, I would estimate a couple of weeks to optimize the project.

**Actual Time Spent**

I roughly spent about 24 hours on the project and didn't complete it. I think this is fine considering my [introspection](#introspection).

## What's Built, TODOs, & Improvement Considerations

What was built but not exclusive to:
- Server with GET and POST endpoints
  - GET retrieves all subscriber information
  - POST extracts uploaded JSON file and its content and stores data in database (`Mockeroo` data in `static`)
- Containerized database with data persistence and schema
- Created development tasks defined from one tool `invoke`
- Basic swagger API information on server
- Client UI with upload button that can pick files
- In the middle of creating ability to make POST requests to server after file upload

TODOs based on project ask:
  - Support for CSV file on POST endpoint (JSON only support at the moment)
  - Create charts on client-side
  - Create insights based on data

Improvements that can be made but not exclusive to:
- Proper error handling on server-side
- Better accommodate potential error scenarios
- API Key authentication on server-side
- Pre-commit implementation to static analyze (format, lint, code coverage report, security scan code, security scan dependencies, etc.)
- Code coverage service (e.g. SonarCloud) for both server and client
- Set up CI/CD pipeline (e.g. Github Actions)
  - Initial static analysis check
  - Run unit/integration tests
  - Build versioned artifacts to store in repository manager
  - Deploy through promoting environment (dev, test, prod)
  - etc.
- IaC (e.g Terraform) to standup and configure cloud servers
- Deployments using cloud services (e.g. GCP)
- Configure environments for testing purposes for both server and client
- Create data factories for tests
- Quick smoke tests (assuming system built enough)
- Log at critical points in server and client
- Aggregate logs to observability platforms (e.g Splunk)
- Create alerts on critical errors based on observations

## Introspection

When starting project `sagewhale`, I wanted to use frameworks, tools, and libraries that I'm either vaguely exposed to or weren't too familiar with. These included `flask-restx`, `react`, `chakra-ui`, etc. To no surprise, front-end work was what I was less comfortable working on because most of my engineering career had to do with the backend. I learned quite a lot from this experience and although I couldn't spend as much time as I wanted to with the given week, I'm stil proud of what I created regardless.

I often think back to all the little nuances and moments of frustations that I (and I'm sure other engineers) encountered when creating something from scratch. Sometimes it's just the machine itself, like trying to develop on my M1 Macbook that doesn't quite work the same way as Intel Macbooks and brings its own set of problems because it's so new. It often reminds me that great engineers are the one who perserveres and adapts through the continuous frustrations that this career brings.

On a high note, I think `sagewhale` was a good project to work on even though I didn't complete it (though can any project be truly completed?) the project ask.
