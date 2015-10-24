cpplint JUnit Converter
=======================

.. image:: https://badge.fury.io/py/cpplint-junit.png
    :target: http://badge.fury.io/py/cpplint-junit

Tool that converts cpplint output to JUnit XML format.

Usage
-----
Redirect ``cpplint`` ``stderr`` to a file:

.. code:: shell-session

    $ cpplint main.cpp 2> cpplint.txt

Convert it to JUnit XML format:

.. code:: shell-session

    $ cpplint_junit cpplint.txt cpplint_junit.xml