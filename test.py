#! /usr/bin/env python3

"""cpplint-junit tests."""

import unittest

from cpplint_junit import parse_cpplint


class ParseCpplintTestCase(unittest.TestCase):
    def test_good(self):
        failures = parse_cpplint('tests/cpplint-out-good.txt')
        self.assertEqual(failures, {})

    def test_bad(self):
        file = 'bad.cpp'
        failures = parse_cpplint('tests/cpplint-out-bad.txt')

        self.assertEqual(failures[file][0].file, file)
        self.assertEqual(failures[file][0].line, 0)
        self.assertEqual(failures[file][0].message,
                         'No copyright message found.  You should have a line: "Copyright [year] '
                         '<Copyright Owner>"  [legal/copyright] [5]')

        self.assertEqual(failures[file][1].file, file)
        self.assertEqual(failures[file][1].line, 2)
        self.assertEqual(failures[file][1].message,
                         'Missing spaces around =  [whitespace/operators] [4]')

        self.assertEqual(failures[file][2].file, file)
        self.assertEqual(failures[file][2].line, 3)
        self.assertEqual(failures[file][2].message,
                         'Could not find a newline character at the end of the file.  '
                         '[whitespace/ending_newline] [5]')

    def test_bad2(self):
        file = 'bad2.cpp'
        failures = parse_cpplint('tests/cpplint-out-bad2.txt')

        self.assertEqual(failures[file][0].file, file)
        self.assertEqual(failures[file][0].line, 0)
        self.assertEqual(failures[file][0].message,
                         'No copyright message found.  You should have a line: "Copyright [year] '
                         '<Copyright Owner>"  [legal/copyright] [5]')

        self.assertEqual(failures[file][1].file, file)
        self.assertEqual(failures[file][1].line, 1)
        self.assertEqual(failures[file][1].message,
                         'Missing space before {  [whitespace/braces] [5]')

        self.assertEqual(failures[file][2].file, file)
        self.assertEqual(failures[file][2].line, 1)
        self.assertEqual(failures[file][2].message,
                         'Extra space before ( in function call  [whitespace/parens] [4]')

        self.assertEqual(failures[file][3].file, file)
        self.assertEqual(failures[file][3].line, 2)
        self.assertEqual(failures[file][3].message,
                         'Missing spaces around =  [whitespace/operators] [4]')

        self.assertEqual(failures[file][4].file, file)
        self.assertEqual(failures[file][4].line, 3)
        self.assertEqual(failures[file][4].message,
                         'Could not find a newline character at the end of the file.  '
                         '[whitespace/ending_newline] [5]')

    def test_all(self):
        file1 = 'bad.cpp'
        file2 = 'bad2.cpp'
        failures = parse_cpplint('tests/cpplint-out-all.txt')

        self.assertEqual(failures[file1][0].file, file1)
        self.assertEqual(failures[file1][0].line, 0)
        self.assertEqual(failures[file1][0].message,
                         'No copyright message found.  You should have a line: "Copyright [year] '
                         '<Copyright Owner>"  [legal/copyright] [5]')

        self.assertEqual(failures[file1][1].file, file1)
        self.assertEqual(failures[file1][1].line, 2)
        self.assertEqual(failures[file1][1].message,
                         'Missing spaces around =  [whitespace/operators] [4]')

        self.assertEqual(failures[file1][2].file, file1)
        self.assertEqual(failures[file1][2].line, 3)
        self.assertEqual(failures[file1][2].message,
                         'Could not find a newline character at the end of the file.  '
                         '[whitespace/ending_newline] [5]')

        self.assertEqual(failures[file2][0].file, file2)
        self.assertEqual(failures[file2][0].line, 0)
        self.assertEqual(failures[file2][0].message,
                         'No copyright message found.  You should have a line: "Copyright [year] '
                         '<Copyright Owner>"  [legal/copyright] [5]')

        self.assertEqual(failures[file2][1].file, file2)
        self.assertEqual(failures[file2][1].line, 1)
        self.assertEqual(failures[file2][1].message,
                         'Missing space before {  [whitespace/braces] [5]')

        self.assertEqual(failures[file2][2].file, file2)
        self.assertEqual(failures[file2][2].line, 1)
        self.assertEqual(failures[file2][2].message,
                         'Extra space before ( in function call  [whitespace/parens] [4]')

        self.assertEqual(failures[file2][3].file, file2)
        self.assertEqual(failures[file2][3].line, 2)
        self.assertEqual(failures[file2][3].message,
                         'Missing spaces around =  [whitespace/operators] [4]')

        self.assertEqual(failures[file2][4].file, file2)
        self.assertEqual(failures[file2][4].line, 3)
        self.assertEqual(failures[file2][4].message,
                         'Could not find a newline character at the end of the file.  '
                         '[whitespace/ending_newline] [5]')
