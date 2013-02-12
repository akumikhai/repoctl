#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
import types
import sys

def usage_message():
    print """\
Usage:
    ./run-tests.py all|<test>
"""


def objimport(pypath):
    lp = pypath.split('.')
    pn = lp.pop(0)
    mp = pn
    o = __import__(pn)
    while True:
        if len(lp)==0:
            break

        if isinstance(o,types.ModuleType):
            pn = lp.pop(0)
            __import__(mp,fromlist=[pn])
            o = getattr(o,pn)
            mp = mp+'.'+pn
        else:
            pn = lp.pop(0)
            o = getattr(o,pn)

    return o

def run_tests_all():
    import cmdlineargs.tests

    suite = unittest.TestSuite([
        cmdlineargs.tests.suite(),
        ])

    unittest.TextTestRunner(verbosity=3).run(suite)

def run_tests_named(test):
    o = objimport(test)

    if isinstance(o,types.ModuleType):

        try:
            suitef = objimport(test+'.suite')
        except AttributeError:
            suitef = objimport(test+'.tests.suite')

        suite = suitef()
        unittest.TextTestRunner(verbosity=3).run(suite)

    elif isinstance(o,types.FunctionType) and o.__name__=='suite':
        suite = o()
        unittest.TextTestRunner(verbosity=3).run(suite)

    elif isinstance(o,types.TypeType) and issubclass(o,unittest.TestCase):
        suite = unittest.TestSuite([o()])
        unittest.TextTestRunner(verbosity=3).run(suite)

    elif isinstance(o,types.UnboundMethodType) and isinstance(o.im_class,types.TypeType) and issubclass(o.im_class,unittest.TestCase):
        suite = unittest.TestSuite([o.im_class(o.__name__)])
        unittest.TextTestRunner(verbosity=3).run(suite)

    else:
        raise NotImplementedError('Unknown')


AL = sys.argv[1:]

if len(AL)==0:
    usage_message()
    sys.exit(0)

if AL[0]=='all':
    run_tests_all()
else:
    t = AL[0]
    run_tests_named(t)
