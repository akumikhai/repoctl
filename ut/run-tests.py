#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import types
import sys

from repolib import ut

def usage_message():
    print """\
Usage:
    ./run-tests.py all|<test>
"""

TEST_ROOTS = [
    'abstr.cmdlineargs.tests',
    'imple.cmdlineargs.tests',
    'imple.realwork.tests',
]

def run_tests_all():
    suite = ut.mk_tests_all(TEST_ROOTS)
    unittest.TextTestRunner(verbosity=3).run(suite)

def run_tests_named(test):
    suite = ut.mk_tests_named(test)
    unittest.TextTestRunner(verbosity=3).run(suite)

AL = sys.argv[1:]

if len(AL)==0:
    usage_message()
    sys.exit(0)

if AL[0]=='all':
    run_tests_all()
else:
    t = AL[0]
    run_tests_named(t)
