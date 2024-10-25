import os
import sys

from setuptools import find_packages, setup  # noqa: F401


# Taken from Numba
def _guard_python_version(max_python):
    version_module = None
    try:
        from packaging import version as version_module
    except ImportError:
        try:
            from setuptools._vendor.packaging import version as version_module
        except ImportError:
            pass

    if version_module is None:
        return

    current_python = version_module.parse(".".join(map(str, sys.version_info[:3])))
    max_python = version_module.parse(max_python)

    if not current_python < max_python:
        raise RuntimeError(
            f"Cannot install on Python version {current_python} as Python {max_python}+ is not yet supported."
        )


_guard_python_version(max_python="3.13")

# extras_require = {
#     "test": [
#         "pytest",
#         "pytest-asyncio",
#         "pytest-cov",
#         "flake8",
#         "coverage",
#         "twine",
#         "wheel",
#         "astunparse",
#         "black",
#         "isort",
#         "numpy",
#     ]
# }
# extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(
    packages=["func_adl", "func_adl/ast"],
)
