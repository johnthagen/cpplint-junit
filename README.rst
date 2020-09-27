cpplint JUnit Converter
=======================

**Note**: This project has been archived in favor of the
`advanced PyPI hosted version of cpplint <https://pypi.python.org/pypi/cpplint>`_. It will
no longer be maintained.

.. image:: https://travis-ci.com/johnthagen/cpplint-junit.svg
    :target: https://travis-ci.com/johnthagen/cpplint-junit

.. image:: https://codeclimate.com/github/johnthagen/cpplint-junit/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/cpplint-junit

.. image:: https://codeclimate.com/github/johnthagen/cpplint-junit/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/cpplint-junit

.. image:: https://codecov.io/github/johnthagen/cpplint-junit/coverage.svg
    :target: https://codecov.io/github/johnthagen/cpplint-junit

.. image:: https://img.shields.io/pypi/v/cpplint-junit.svg
    :target: https://pypi.python.org/pypi/cpplint-junit

.. image:: https://img.shields.io/pypi/status/cpplint-junit.svg
    :target: https://pypi.python.org/pypi/cpplint-junit

.. image:: https://img.shields.io/pypi/pyversions/cpplint-junit.svg
    :target: https://pypi.python.org/pypi/cpplint-junit/

Tool that converts ``cpplint`` output to JUnit XML format.  Use on your CI servers to get more
helpful feedback.

Note: The `advanced PyPI hosted version of cpplint <https://pypi.python.org/pypi/cpplint>`_
supports JUnit output format natively and is preferred to this package.

Installation
------------

You can install, upgrade, and uninstall ``cpplint-junit`` with these commands:

.. code:: shell-session

    $ pip install cpplint-junit
    $ pip install --upgrade cpplint-junit
    $ pip uninstall cpplint-junit

Usage
-----
Redirect ``cpplint`` ``stderr`` to a file:

.. code:: shell-session

    $ cpplint main.cpp 2> cpplint.txt

Convert it to JUnit XML format:

.. code:: shell-session

    $ cpplint_junit cpplint.txt cpplint_junit.xml

Releases
--------

2.0.1 - 2020-03-29
^^^^^^^^^^^^^^^^^^

- Fix trove classifiers.

2.0.0 - 2020-03-29
^^^^^^^^^^^^^^^^^^

- Drop Python 2.7.

1.3.0 - 2019-12-15
^^^^^^^^^^^^^^^^^^

- Drop Python 3.4 and support Python 3.8.
- Include license file.

1.2.1 - 2019-10-14
^^^^^^^^^^^^^^^^^^

Fix missing ``requirements.txt`` from source distribution that caused package to not install.

1.2.0 - 2018-07-09
^^^^^^^^^^^^^^^^^^

Drop Python 3.3 and support Python 3.7.


1.1.0 - 2016-12-31
^^^^^^^^^^^^^^^^^^

Support Python 3.6.

1.0.1 - 2016-03-05
^^^^^^^^^^^^^^^^^^

Fix Python 2.7 compatibility by catching more general IOError on file not found.

1.0.0 - 2016-02-15
^^^^^^^^^^^^^^^^^^

Release 1.0.  Increase test coverage.

0.2.3 - 2015-11-14
^^^^^^^^^^^^^^^^^^

Use "error" consistently rather than "failure" to refer to results from ``cpplint``.

0.2.2 - 2015-11-14
^^^^^^^^^^^^^^^^^^

Mis-release.

0.2.1 - 2015-10-24
^^^^^^^^^^^^^^^^^^

Added console entry point.

0.1.0 - 2015-10-24
^^^^^^^^^^^^^^^^^^

First release.