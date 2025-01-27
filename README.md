# Comparison of SEI zero-dimensional models

<!-- [![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussions][github-discussions-badge]][github-discussions-link] -->

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->

<!-- [actions-badge]:            https://github.com/mmsg-warwick/zero-dimension-comparison-SEI/workflows/CI/badge.svg
[actions-link]:             https://github.com/mmsg-warwick/zero-dimension-comparison-SEI/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/zero-dimension-comparison-SEI
[conda-link]:               https://github.com/conda-forge/zero-dimension-comparison-SEI-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/mmsg-warwick/zero-dimension-comparison-SEI/discussions
[pypi-link]:                https://pypi.org/project/zero-dimension-comparison-SEI/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/zero-dimension-comparison-SEI
[pypi-version]:             https://img.shields.io/pypi/v/zero-dimension-comparison-SEI
[rtd-badge]:                https://readthedocs.org/projects/zero-dimension-comparison-SEI/badge/?version=latest
[rtd-link]:                 https://zero-dimension-comparison-SEI.readthedocs.io/en/latest/?badge=latest -->

<!-- prettier-ignore-end -->

The project compares different common zero-dimensional models (limited mechanisms) for solid electrolyte interphase (SEI) growth in lithium-ion batteries, focusing on the formation cycle and early cycles, using PyBaMM.
es on features not yet available in the latest PyBaMM release. It accompanies the article
> K. Manmi, M. Tuchel, E. Kendrick, F. Brosa Planella, [A Comparison of Standard SEI Growth Models in the Context of Battery Formation](https://doi.org/10.1149/1945-7111/ad8548), J. Electrochem. Soc., 171 (2024) 100530.

This work is supported by [The Faraday Institution](https://www.faraday.ac.uk) "Multi-Scale Modelling" project [EP/S003053/1 grant number FIRG059].

## 🚀 Installing the package
The package is not yet available on PyPI so it needs to be installed from the source code. These instructions assume that you have a compatible Python version installed (between 3.9 and 3.12).

### Linux and macOS
First clone the repository, either from the command line or using a Git client:

```bash
git clone git@github.com:mmsg-warwick/zero-dimension-comparison-SEI.git
```

If you do not have nox installed, install it with

```bash
python3 -m pip install nox
```

Then, navigate to the repository you just cloned and run

```bash
nox -s dev
```

This will create a virtual environment called `venv` in your current directory and install the package in editable mode with all the development dependencies. To activate the virtual environment, run

```bash
source env/bin/activate
```

You can now run the examples in the `examples` directory.

If needed, you can deactivate your virtual environment with

```bash
deactivate
```

### Windows
First clone the repository, either from the command line or using a Git client:

```bash
git clone git@github.com:mmsg-warwick/zero-dimension-comparison-SEI.git
```

If you do not have nox installed, install it with

```bash
python3 -m pip install nox
```

Then, navigate to the repository you just cloned and run

```bash
nox -s dev
```

This will create a virtual environment called `venv` in your current directory and install the package in editable mode with all the development dependencies. To activate the virtual environment, run

```bash
venv\Scripts\activate.bat
```
if you are using Command Prompt, or
```bash
venv\Scripts\Activate.ps1
```
if you are using PowerShell.


You can now run the examples in the `examples` directory.

If needed, you can deactivate your virtual environment with

```bash
deactivate
```
