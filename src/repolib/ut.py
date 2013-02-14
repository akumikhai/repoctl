#-*- coding: utf-8 -*-

import unittest

import types

def tcc_tests(tcc):
    tests = getattr(tcc,'__TESTS__',None)
    if tests is None:
        tests = [tn for tn in dir(tcc) if tn[:5]=='test_' or tn=='runTest']
        
    return unittest.TestSuite([tcc(tn) for tn in tests])


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


def mk_tests_all(lst):
    suite = unittest.TestSuite(
        [objimport(mn).suite() for mn in lst])
   
    return suite
    

def mk_tests_named(test):
    o = objimport(test)

    if isinstance(o,types.ModuleType):

        try:
            suitef = objimport(test+'.suite')
        except AttributeError:
            suitef = objimport(test+'.tests.suite')

        suite = suitef()

    elif isinstance(o,types.FunctionType) and o.__name__=='suite':
        suite = o()

    elif isinstance(o,types.TypeType) and issubclass(o,unittest.TestCase):
        suite = tcc_tests(o)

    elif isinstance(o,types.UnboundMethodType) and isinstance(o.im_class,types.TypeType) and issubclass(o.im_class,unittest.TestCase):
        suite = unittest.TestSuite([o.im_class(o.__name__)])

    else:
        raise NotImplementedError('Unknown')

    return suite

