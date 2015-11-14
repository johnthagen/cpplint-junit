cpplint JUnit Converter
=======================

.. image:: https://badge.fury.io/py/cpplint-junit.png
    :target: http://badge.fury.io/py/cpplint-junit

Tool that converts ``cpplint`` output to JUnit XML format.  Use on your CI servers to get more
helpful feedback.

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

0.2.2 - 2015-11-14
^^^^^^^^^^^^^^^^^^

Use "error" consistantly rather than "failure" to refer to results from ``cpplint``.

0.2.1 - 2015-10-24
^^^^^^^^^^^^^^^^^^

Added console entry point.

0.1.0 - 2015-10-24
^^^^^^^^^^^^^^^^^^

First release.