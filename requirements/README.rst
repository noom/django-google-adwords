========================
 pip requirements files
========================

Index
=====

* :file:`requirements/default.txt`

    Default requirements for any version of Python.

* :file:`requirements/default-sans-django.txt`

    Tox-friendly requirements, excluding Django.

* :file:`requirements/test.txt`

    Requirements needed to run the full unittest suite via ./runtests.py

* :file:`requirements/pkgutils.txt`

    Extra requirements required to perform package distribution maintenance.

Examples
========

Installing requirements
-----------------------

::

    $ pip install -U -r requirements/default.txt

Running the tests
-----------------

::

    $ pip install -U -r requirements/default.txt
    $ pip install -U -r requirements/test.txt
