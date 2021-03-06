# func_adl

 Construct hierarchical data queries using SQL-like concepts in python

[![GitHub Actions Status](https://github.com/iris-hep/func_adl/workflows/CI/CD/badge.svg)](https://github.com/iris-hep/func_adl/actions)
[![Code Coverage](https://codecov.io/gh/iris-hep/func_adl/graph/badge.svg)](https://codecov.io/gh/iris-hep/func_adl)

[![PyPI version](https://badge.fury.io/py/func-adl.svg)](https://badge.fury.io/py/func-adl)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/func-adl.svg)](https://pypi.org/project/func-adl/)

This is the base package that has the backend-agnostic code to query hierarchical data. In all likelihood you will want to install
one of the following packages:

- func_adl.xAOD: for running on an ATLAS experiment xAOD file hosted in ServiceX
- func_adl.xAOD.backend: for running on a local file using docker
