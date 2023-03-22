# Starter Cookie
A lightweight cookiecutter template for data science projects using poetry, inspired by the awesome [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) Project.

## Prerequisites
In order to use this template, you **need** to have the following packages installed on your system:

- Python
- poetry
- cookiecutter
- DVC (if you wan't to use the functionality)

optional:
- Pyenv (for managing different python versions)
- pipx (to install poetry & cookecutter in an isolated way)

## Installation 
To use the cookie you need to run:
```bash
cookiecutter https://github.com/Fa-bi-an/starter-cookie.git
```
This command downloads the cookie and starts the setup assistant.

## Usage
### pyenv
After installing and configuring the cookie you are now able to create the virtual envionment using poetry. If you're using [pyenv](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local) make sure to have the same version of python selected as `local` as you picked while using the setup assistant.

### poetry

```bash
poetry shell
```
After creating an virtual project environment, you can now install the predefined packages:

```bash
poetry install
```
### optional DVC
If you are using DVC, don't forget to [add a remote storage](https://dvc.org/doc/command-reference/remote#example-add-a-default-local-remote).

## Your good to go!
In the notebooks directory you will find a starter notebook. For installing further packages from pypi just run `poetry add <package>`. For more information how to use poetry hava a look in the [documentation](https://python-poetry.org/docs/basic-usage/).

# Last remarks
To get a deeper understanding how this template works and how to create your own template, visit [algorithmgym](https://algorithmgym.notion.site/Create-a-cookie-template-54598c90e00341dca38e33b4afce84e5).


# To-Do's (03/2023):
- add .pre-commit hooks to project
- add example notebooks
- add those examples to post gen hook