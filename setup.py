from setuptools import setup


setup(
    name='cpplint-junit',
    version='2.0.1',

    description='Converts cpplint output to JUnit format.',
    long_description=open('README.rst').read(),
    keywords='cpplint C++ Google JUnit',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/cpplint-junit',

    py_modules=['cpplint_junit'],
    install_requires=open('requirements.txt').readlines(),
    python_requires='<=3.5',
    zip_safe=False,

    license='MIT',
    license_files=['LICENSE.txt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],

    scripts=['cpplint_junit.py'],

    entry_points={
        'console_scripts': [
            'cpplint_junit = cpplint_junit:main',
        ],
    }
)
