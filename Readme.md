# Starter Cookie
A lightweight cookiecutter template for data science projects using poetry, inspired by the awesome [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) Project.

## Prerequisites
To use this template, you **need** to have the following packages installed on your system:

- Python
- poetry
- cookiecutter

Optional:
- DVC (if you want to use the functionality)
- Git installed

In general, good to consider, but not necessary:
- Pyenv (for managing different python versions)
- pipx (to install poetry & cookiecutter in an isolated way)

## Installation 
To use the cookie you need to run the following command in your [Terminal](https://support.apple.com/de-de/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)/ cmd:
```bash
cookiecutter https://github.com/Fa-bi-an/starter-cookie.git
```
This command downloads the cookie and starts the setup assistant.

## Usage
### pyenv
After installing and configuring the cookie, you can create the virtual environment using poetry. If you're using [pyenv](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-local) make sure to have the same version of python selected as `local` as you picked while using the setup assistant.

### poetry

```bash
poetry shell
```
After creating a virtual project environment, you can now install the predefined packages:

```bash
poetry install
```
## Optional configuration
Using this cookie and enabling the options via the setup assistant, you can use optional components.

### Install & use pre-commit git hooks
Prerequisite to use pre-commit hooks is that you have the project git initialized with `git init`.

Activate the [pre-commit hooks](https://pre-commit.com/#3-install-the-git-hook-scripts) by running the following command once:

``` bash 
pre-commit install

```
### optional: DVC
If you are using DVC, remember to [add remote storage](https://dvc.org/doc/command-reference/remote#example-add-a-default-local-remote).


## Your good to go!
In the notebooks directory, you will find a starter notebook. For installing  further packages from pypi just run `poetry add <package>`. For more information on how to use poetry, look at the [documentation](https://python-poetry.org/docs/basic-usage/).

# Last remarks
To better understand how this template works and how to create your own template, visit [algorithmgym](https://algorithmgym.notion.site/Create-a-cookie-template-54598c90e00341dca38e33b4afce84e5).


# To-Do's (03/2023):
- add example notebooks
- add those examples to post gen hook