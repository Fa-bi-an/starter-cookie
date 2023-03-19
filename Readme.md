# Starter Cookie
A lightweight cookiecutter template for data science projects using poetry.

## Prerequisites
In order to use this template, you need to have the following packages installed on your system:

- Python
- poetry
- cookiecutter

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
After installing and configuring the cookie you can now create the virtual envionment using poetry:

```bash
poetry shell
```
After creating an virtual project environment, you can now install the predefined packages:

```bash
poetry install
````
## Your good to go
In the notebooks directory you will find a starter notebook. For installing further packages from pypi just run `poetry add <package>`. For more information how to use poetry hava a look in the [documentation](https://python-poetry.org/docs/basic-usage/).

# Last remarks
To get a deeper understanding how to this template works and how to creat your own template vistit [algorithmgym](https://algorithmgym.notion.site/Create-a-cookie-template-54598c90e00341dca38e33b4afce84e5).