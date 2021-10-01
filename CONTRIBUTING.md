# Contributing to Discourtesy

Thanks for being interested in contributing to the Discourtesy project! There are two different ways of contributing, which are being explained in further detail below.

## Feature Request

Discourtesy was created to satisfy a very specific use-case, so it is impossible to have considered every way of using this framework. If there is something that you feel is missing, feel free to create an issue describing the shortcoming or to create a pull request implementing the new feature.

This library aims to provide a simple [Starlette-based][starlette] web server to handle Discord interactions.

In no way, it intends to

- provide a testing suite;
- provide typings for public functions;
- provide objects for interactions or responses;
- provide methods to register commands or components.

## Bug Report / Fix

Upon discovering a bug, please create an issue. This way, I can confirm the problem and swiftly implement a fix. Alternatively, feel free to submit a pull request with a short description of the bug and your proposed solution.

Please try to include

- the version number of Python and Discourtesy;
- the type and version of the operating system;
- any relevant information about the tech stack.

## Code Style

The Discourtesy project adheres to the [PEP 8][pep-8] code style guidelines. [`black`][black] and [`flake8`][flake8] are being used to enforce this. This boils down to the usage of double quotes and a maximum line length of 79 characters.

Furthermore, the usage of full sentences and British English is preferred where applicable.

[black]: <https://black.readthedocs.io/en/stable/>
[flake8]: <https://flake8.pycqa.org/en/stable/>
[pep-8]: <https://www.python.org/dev/peps/pep-0008/>
[starlette]: <https://www.starlette.io/>
