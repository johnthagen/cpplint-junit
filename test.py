#! /usr/bin/env python3

"""cpplint-junit tests."""

import sys
import unittest

from cpplint_junit import CpplintError, generate_test_suite, parse_arguments, parse_cpplint


class ParseCpplintTestCase(unittest.TestCase):
    def test_good(self):  # type: () -> None
        failures = parse_cpplint('tests/cpplint-out-good.txt')
        self.assertEqual(failures, {})

    def test_bad(self):  # type: () -> None
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

    def test_bad2(self):  # type: () -> None
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

    def test_all(self):  # type: () -> None
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


class GenerateTestSuiteTestCase(unittest.TestCase):
    def test_single(self):  # type: () -> None
        errors = {'file_name':
                  [CpplintError('file_name',
                                4,
                                'error message')]}
        tree = generate_test_suite(errors)
        root = tree.getroot()
        self.assertEqual(root.get('errors'), str(1))
        self.assertEqual(root.get('failures'), str(0))
        self.assertEqual(root.get('tests'), str(1))

        test_case_element = root.find('testcase')
        self.assertEqual(test_case_element.get('name'), 'file_name')

        error_element = test_case_element.find('error')
        self.assertEqual(error_element.get('file'), 'file_name')
        self.assertEqual(error_element.get('line'), str(4))
        self.assertEqual(error_element.get('message'), '4: error message')


class ParseArgumentsTestCase(unittest.TestCase):
    def test_no_arguments(self):  # type: () -> None
        with self.assertRaises(SystemExit):
            # Suppress argparse stderr.
            class NullWriter:
                def write(self, s):  # type: (str) -> None
                    pass

            sys.stderr = NullWriter()
            parse_arguments()


if __name__ == '__main__':
    unittest.main()
