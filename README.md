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
    - [ruff](https://github.com/charliermarsh/ruff),
- Tests run with [pytest](https://github.com/pytest-dev/pytest) and plugins, with [coverage](https://github.com/nedbat/coveragepy) support
- Python 3.9 or above
- Auto-generated `CHANGELOG.md` from git commits (using Angular message style)
- All licenses from [choosealicense.com](https://choosealicense.com/appendix/)

## Quick setup and usage

Install copier wit:

```bash
pipx install copier
```
Then:

```bash
copier copy --trust https://github.com/ydethe/pdm_template.git /path/to/your/new/project
```

See the [documentation](https://copier.readthedocs.io/en/stable/)
for more details.
