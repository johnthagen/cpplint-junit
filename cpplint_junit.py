#! /usr/bin/env python3

"""Converts cpplint output to JUnit XML format."""

import argparse
import collections
import os
import re
import sys
from xml.etree import ElementTree

__version__ = '0.2.1'

EXIT_SUCCESS = 0
EXIT_FAILURE = -1


class CpplintError(object):
    def __init__(self, file, line, message):
        self.file = file
        self.line = line
        self.message = message


def parse_arguments():
    parser = argparse.ArgumentParser(description='Converts cpplint output to JUnit XML format.')
    parser.add_argument('input_file', type=str, help='cpplint stdout text file.')
    parser.add_argument('output_file', type=str, help='JUnit XML output file.')
    return parser.parse_args()


def parse_cpplint(file_name):
    """Parses a cpplint output file.

    Args:
        file_name (str): cpplint output file.

    Returns:
        Dict[str, List[CpplintFailure]]: Parsed failures grouped by file name.

    Raises:
        FileNotFoundError: File does not exist.
    """
    lines = open(file_name, mode='rt').readlines()

    failures = collections.defaultdict(list)
    for line in lines:
        line = line.rstrip()

        match = re.search(r'(\S+):(\d+):\s+(.+)', line)
        if match is not None:
            error = CpplintError(file=match.group(1),
                                 line=int(match.group(2)),
                                 message=match.group(3))
            failures[error.file].append(error)
    return failures


def generate_test_suite(failures, output_file):
    """Writes a JUnit test file from parsed cpplint failures.

    Args:
        failures (Dict[str, List[CpplintFailure]]): Parsed cpplint failures.
        output_file (str): File path to JUnit XML output.

    Returns:
        Nothing.
    """
    test_suite = ElementTree.Element('testsuite')
    test_suite.attrib['errors'] = str(len(failures))
    test_suite.attrib['failures'] = str(0)
    test_suite.attrib['name'] = 'cpplint failures'
    test_suite.attrib['tests'] = str(len(failures))
    test_suite.attrib['time'] = str(1)

    for file_name, errors in failures.items():
        test_case = ElementTree.SubElement(test_suite,
                                           'testcase',
                                           name=os.path.relpath(file_name))
        for error in errors:
            ElementTree.SubElement(test_case,
                                   'failure',
                                   file=os.path.relpath(error.file),
                                   line=str(error.line),
                                   message='{}: {}'.format(error.line, error.message))

    tree = ElementTree.ElementTree(test_suite)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


def main():
    """Main function.

    Returns:
        int: Exit code.
    """
    args = parse_arguments()

    try:
        failures = parse_cpplint(args.input_file)
    except FileNotFoundError as e:
        print(str(e))
        return EXIT_FAILURE

    if len(failures) > 0:
        generate_test_suite(failures, args.output_file)

    return EXIT_SUCCESS

if __name__ == '__main__':
    sys.exit(main())
