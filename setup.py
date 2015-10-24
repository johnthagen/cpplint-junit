from setuptools import setup

import cpplint_junit


def get_long_description():
    description = []
    for file_name in ('README.rst',):
        with open(file_name) as f:
            description.append(f.read())
    return '\n\n'.join(description)


setup(
    name='flake8-strings',
    version=cpplint_junit.__version__,

    description='Converts cpplint output to JUnit format.',
    long_description=get_long_description(),
    keywords='cpplint C++ Google JUnit',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/cpplint-junit',
    license='MIT',

    py_modules=['cpplint-junit'],
    zip_safe=False,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],

    scripts=['cpplint-junit']
)
