"""File that defines available development tasks"""

from os.path import dirname, realpath
from invoke import task

PROJECT_DIRECTORY = dirname(realpath(__file__))
SERVER_DIRECTORY = f"{PROJECT_DIRECTORY}/server"
SERVER_ENTRYPOINT = f"{SERVER_DIRECTORY}/entrypoint.sh"
SERVER_TESTS_DIRECTORY = f"{SERVER_DIRECTORY}/tests"
CLIENT_DIRECTORY = f"{PROJECT_DIRECTORY}/client"
CLIENT_TESTS_DIRECTORY = f"{CLIENT_DIRECTORY}/src/__tests__"
PYLINT_CONFIG = f"{SERVER_DIRECTORY}/.pylintrc"
PYTHON_FILES = '$(find . -iname "*.py")'


@task
def pyformat(context):
    """
    Formats Python code using black
    """
    print("\nFormatting Python code...\n")
    context.run(f"black {PYTHON_FILES}")


@task
def tsformat(context):
    """
    Formats Typescript code (and JSON) using prettier
    """
    print("\nFormatting Typescript code...\n")
    context.run(f"cd client && yarn prettier --write .")


@task()
def pylint(context):
    """
    Lints Python code using pylint
    """
    print("\nLinting Python code...\n")

    context.run(f"pylint --exit-zero --rcfile {PYLINT_CONFIG} {PYTHON_FILES}")


@task()
def pycomp(context):
    """
    Calculates cyclomatic complexity of Python code
    """
    print(f"\nCalculating cyclomatic complexity in {SERVER_DIRECTORY}...\n")
    context.run(f"radon cc -a {SERVER_DIRECTORY}")


@task()
def pysec(context):
    """
    Finds common security issues in Python code
    """
    print(f"\nLooking for common security issues in {SERVER_DIRECTORY}...\n")
    context.run(f"bandit -r --exit-zero {SERVER_DIRECTORY}")


@task()
def pytest(context):
    """
    Runs Python tests
    """
    print(f"\nRunning tests in {SERVER_TESTS_DIRECTORY}...\n")
    context.run(f"pytest {SERVER_TESTS_DIRECTORY}")


@task()
def tstest(context):
    """
    Runs Typescript tests
    """
    print(f"\nRunning tests in {CLIENT_TESTS_DIRECTORY}...\n")
    context.run(f"cd {CLIENT_TESTS_DIRECTORY} && yarn test --watchAll=false")


@task(pyformat, pylint, pycomp, pysec)
def pycheck(context):
    """
    Format, lint, analyze code complexity, and security code scan
    """


@task()
def pydep(context):
    """
    Installs Python project dependencies
    """
    print("\nInstalling all Python project dependencies...\n")
    context.run(f"pipenv sync --dev")


@task()
def tsdep(context):
    """
    Installs Typescript project dependencies
    """
    print("\nInstalling all Typescript project dependencies...\n")
    context.run(f"cd {CLIENT_DIRECTORY} && yarn install")


@task(pydep, tsdep,)
def alldep(context):
    """
    Installs all project dependencies
    """


@task()
def server(context):
    """
    Starts the server with database container
    """
    print("\nStarting the server...\n")
    context.run(SERVER_ENTRYPOINT)


@task()
def client(context):
    """
    Starts the client
    """
    print("\nStarting the client...\n")
    context.run(f"cd {CLIENT_DIRECTORY} && yarn start")
