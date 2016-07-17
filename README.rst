############
Introduction
############
First of all, we use reStructuredText Markup instead of Markdown. Just because.

This is an opinionated skeleton for a Python 3 REST application. This skeleton
doesn't do the start-small approach, but an as-much-as-possible approach. This
can be confusing for beginners or developers that are not familiar with the
various employed components.

Even more important is that this skeleton is **work in progress**.

##########
Components
##########
Let's see which components are worth mentioning and which require documentation:

- `Directory structure`_
- `Configuration`_

  - `.gitignore`_
  - `.editorconfig`_

- `Source Code`_

  - `Encoding`_
  - `main() Function`_
  - `Documenting`_

- Documentation Generator
- Testing
- `Tools`_

  - pip-tools
  - `Tox`_
  - `Paver`_

- Python Packages

  - logging
  - command line options

- Docker

.. _`Directory structure`:

Directory Structure
===================
The project's directory structure is recommended in `The Hitchhikers Guide to
Python <http://docs.python-guide.org/en/latest/writing/structure/>`_.

.. _`Configuration`:

Configuration
=============

.. _`.gitignore`:

.gitignore
----------
The ``.gitignore`` is populated from `gitignore.io <https://www.gitignore.io/>`_.

.. _`.editorconfig`:

.editorconfig
-------------
Use ``.editorconfig`` to define portable editor configuration. See also
`editorconfig.org <http://editorconfig.org/>`_.

.. _`Source Code`:

Source Code
===========

.. _`Encoding`:

Encoding
--------
`PEP 263 <https://www.python.org/dev/peps/pep-0263/>`_ recommends how the source
code encoding can be configured. It boils down to adding `# -*- coding: <encoding name> -*-`
as first or second line to each source code file.

.. _`main() Function`:

main() Function
---------------
Guido van Rossum proposes a ``main()`` function in the
`blog post <http://www.artima.com/forums/flat.jsp?forum=106&thread=4829>`_.
``cli.py`` is modelled after GvR's idea, although the file is split into multiple files.

.. _`Documenting`:

Documenting
-----------
Use Google style docstrings.
http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

.. _`Tools`:

Tools
=====

.. _`Tox`:

Tox
---
Automation and standardisation of tests are run by
`Tox <https://testrun.org/tox/latest/>`_. that is configured in ``tox.ini``.

.. _`Paver`:

Paver
-----
`Paver <https://github.com/paver/paver>`_ is a taskrunner like Make and Rake.

Python Packages
===============

logging
-------
Even if it's tempting, never use ``print()`` instead of proper logging.
- https://github.com/vinta/awesome-python#logging

Docker
======
Docker uses two files ``.dockerignore`` and ``Dockerfile``. The latter is basically
a script how to build a docker image. The former is a file similar to
``.gitignore`` that lists all files and directories that shall be ignored
while building a docker image.
