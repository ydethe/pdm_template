# PDM Copier

[Copier](https://github.com/copier-org/copier) template
for Python projects managed by [PDM](https://github.com/pdm-project/pdm).

This copier template is mainly for my own usage,
but feel free to try it out, or fork it!

## Features

- [PDM](https://github.com/pdm-project/pdm) setup, with pre-defined `pyproject.toml`
- Documentation built with [pdoc3](https://pdoc3.github.io/pdoc/)
- Pre-configured tools for code formatting, quality analysis and testing:
    - [black](https://github.com/psf/black),
    - [blacken-docs](https://github.com/adamchainz/blacken-docs),
    - [ssort](https://github.com/bwhmather/ssort),
    - [ruff](https://github.com/charliermarsh/ruff),
    - [mypy](https://github.com/python/mypy),
- Tests run with [pytest](https://github.com/pytest-dev/pytest) and plugins, with [coverage](https://github.com/nedbat/coveragepy) support
- Python 3.9 or above
- Auto-generated `CHANGELOG.md` from git commits (using Angular message style)
- All licenses from [choosealicense.com](https://choosealicense.com/appendix/)

## Quick setup and usage
### Prerequisite
Install pipx, then copier and pdm with:

```bash
sudo apt install pipx
pipx install pdm
pipx install copier
```

Add your git identifiers:

```bash
git config --global init.defaultBranch master
git config --global user.name "Prenom NOM"
git config --global user.email "prenom.nom@spacex.com"
git config --global pull.rebase true
```

### Project creation 
To create a project, type:

```bash
copier copy --trust https://github.com/ydethe/pdm_template.git /path/to/your/new/project
```

See the [documentation](https://copier.readthedocs.io/en/stable/)
for more details.

This command creates:
* The `pyproject.toml` file. [See here](https://packaging.python.org/en/latest/guides/writing-pyproject-toml) for more information
* A virtual environment in the project's folder, called .venv
* A [src-layout](https://backend.pdm-project.org/build_config/#the-src-layout) for the project's sources
* A `tests` folder, with an example test that can be run with [pytest](https://docs.pytest.org/en/8.0.x/): `pdm run pytest`
* A `.gitignore` file customized for python
* A [`.pre-commit-config.yaml`](https://pre-commit.com/#2-add-a-pre-commit-configuration) file that embeds the following hooks:
    * `check-changelog` to update the `CHANGELOG.md` file ([see on github](https://github.com/ydethe/pdm_template))
    * `extract-todo` to extract TODO comments from code and write it in `TODO.md` ([see on github](https://github.com/ydethe/pdm_template))
    * `check-case-conflict` to check for files that would conflict in case-insensitive filesystems
    * `check-merge-conflict` to check for files that contain merge conflict strings
    * `mixed-line-ending` to replace or check mixed line ending
    * `trailing-whitespace` to trim trailing whitespace
    * [`black`](https://black.readthedocs.io/en/stable/) to refactor code
    * `blacken-docs` to run black on python code blocks in documentation files
    * [`ruff`](https://docs.astral.sh/ruff/) to check code consistency
* A `CHANGELOG.md` file (updated by pre-commit hooks) that describes the changes between two git tags
* A `README.md` file that describes your project
* A `TODO.md` file that keeps track of all 'TODO' comments in your code

The following packets are installed in the venv:

|  Package  |   Category  |   Role  |  
| :-:  |  :-:  |  :-:  |  
| [rich](https://rich.readthedocs.io/en/stable/introduction.html)  |  packet  |  Nice progress bar  |  
| [setuptools-scm](https://setuptools-scm.readthedocs.io/en/latest/)  |  packet  |  So that the package's code can determine its own version  |  
| [numpy](https://numpy.org/doc/stable/index.html)  |  packet  |  A very useful set of functions  |  
| [coverage-badge](https://github.com/dbrgn/coverage-badge?tab=readme-ov-file#coveragepy-badge)  |  dev  |  generate coverage badges using Coverage.py  |  
| [docstr-coverage](https://github.com/HunterMcGushion/docstr_coverage?tab=readme-ov-file#example) | dev | measure your Python source code's docstring coverage | 
| [ipython](https://ipython.org/) | dev | provides a rich architecture for interactive computing | 
| [pre-commit](https://pre-commit.com/index.html) | dev | A framework for managing and maintaining multi-language pre-commit hooks | 
| [snakeviz](https://jiffyclub.github.io/snakeviz/) | dev | browser based graphical viewer for the output of Python’s cProfile module | 
| [black](https://black.readthedocs.io/en/stable/) | maintain | The uncompromising code formatter | 
| [blacken-docs](https://github.com/adamchainz/blacken-docs?tab=readme-ov-file) | maintain | Run Black on Python code blocks in documentation files | 
| [git-changelog](https://pawamoy.github.io/git-changelog/) | maintain | Automatic Changelog generator using Jinja2 templates. From git logs to change logs | 
| [mypy](https://mypy-lang.org/) | quality | static type checker | 
| [ruff](https://docs.astral.sh/ruff/) | quality | An extremely fast Python linter and code formatter, written in Rust | 
| [pdoc3](https://pdoc3.github.io/pdoc/doc/pdoc) | doc | Auto-generate API documentation for Python projects | 
| [genbadge[all]](https://smarie.github.io/python-genbadge/) | doc | genbadge provides a set of commandline utilities to generate badges for tools that do not provide one | 
| [pdm-copier](https://github.com/ydethe/pdm_template) | doc | To fix javascript in pdoc3 generated doc | 
| [pytest](https://docs.pytest.org/en/8.0.x/) | test | The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries | 
| [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) | test | This plugin produces coverage reports | 
| [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/index.html) | test | pytest plugin that provides a mocker fixture which is a thin-wrapper around the patching API provided by the mock package | 
| [pytest-instafail](https://github.com/pytest-dev/pytest-instafail?tab=readme-ov-file#pytest-instafail) | test | pytest plugin that shows failures and errors instantly instead of waiting until the end of test session | 
| [pytest-picked](https://github.com/anapaulagomes/pytest-picked?tab=readme-ov-file#pytest-picked) | test | Run the tests related to the unstaged files or the current branch (according to Git) | 
| [pytest-sugar](https://github.com/Teemu/pytest-sugar?tab=readme-ov-file#pytest-sugar-) | test | pytest plugin that shows failures and errors instantly, adding a progress bar, improving the test results, and making the output look better | 
| [pytest-html](https://pytest-html.readthedocs.io/en/latest/) | test | pytest-html is a plugin for pytest that generates a HTML report for test results | 

### Usage
**In the case where you just created a package with copier**

You can:
* activate the venv: `source .venv/bin/activate`
* add a python package to the main list: `pdm add [package]`
* add a python package to one of the dev list (among dev, maintain, quality, doc and test): `pdm add -dG [list] [package]`
* Run all tests: `pdm run pytest`
* Run only a subset of the tests: `pdm run pytest -k '[pattern_to_filter_tests]`. See [pytest doc](https://docs.pytest.org/en/6.2.x/usage.html#specifying-tests-selecting-tests)
* build the package's doc: `pdm doc`. This creates a `htmldoc` folder, which contains all the doc + tests results
* build the distributable python package: `pdm build`. This creates a `dist` folder with the generated package
* publish the distributable python package on artifactory: `pdm publish -r company`. **You must have tagged and pushed your tag just before this**

**In the case where you cloned package from bitbucket**

You can:
* create a venv: `pdm venv create python3.xx`
* tell pdm to use this venv: `pdm use --venv in-project`
* activate the venv: `source .venv/bin/activate`
* run `pdm install`. This will install all necessary packages to run the cloned pcakage
* add a python package to the main list: `pdm add [package]`
* add a python package to one of the dev list (among dev, maintain, quality, doc and test): `pdm add -dG [list] [package]`
* Run all tests: `pdm run pytest`
* Run only a subset of the tests: `pdm run pytest -k '[pattern_to_filter_tests]`. See [pytest doc](https://docs.pytest.org/en/6.2.x/usage.html#specifying-tests-selecting-tests)
* build the package's doc: `pdm doc`. This creates a `htmldoc` folder, which contains all the doc + tests results
* build the distributable python package: `pdm build`. This creates a `dist` folder with the generated package
