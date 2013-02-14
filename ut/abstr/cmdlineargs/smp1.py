# -*- coding: utf-8 -*-

import unittest
from repolib import ut

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Opt,Seq,Alt,
    Val,VMSingle,VMList)


class TC_Smp1(unittest.TestCase):

    __TESTS__ = [
        'test_no',
        'test_fix',
        'test_str',
        'test_opt1',
        'test_opt2',
        'test_seq1',
        'test_seq2',
        'test_seq3',
        'test_alt',
        ]


    def test_no(self):
        AP = ArgParser(No())
        r = AP.parse_args([])
        self.assertTrue(r)

        r = AP.parse_args(['abra'])
        self.assertFalse(r)

    def test_fix(self):
        AP = ArgParser(Fix('test'))
        
        r = AP.parse_args(['test'])
        self.assertTrue(r)

        r = AP.parse_args([])
        self.assertFalse(r)

        r = AP.parse_args(['abra'])
        self.assertFalse(r)

        r = AP.parse_args(['test','cadabra'])
        self.assertFalse(r)

    
    def test_str(self):
        AP = ArgParser(Str())
        
        r = AP.parse_args(['abra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'abra')

        r = AP.parse_args(['cadabra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'cadabra')

        r = AP.parse_args([])
        self.assertFalse(r)

        r = AP.parse_args(['abra','cadabra'])
        self.assertFalse(r)

    def test_opt1(self):
        AP = ArgParser(Opt('test','t'))

        r = AP.parse_args(['-t'])
        self.assertTrue(r)
        
        r = AP.parse_args(['--test'])
        self.assertTrue(r)
        
        r = AP.parse_args([])
        self.assertFalse(r)
        
        r = AP.parse_args(['abra'])
        self.assertFalse(r)
        
        r = AP.parse_args(['-t','abra'])
        self.assertFalse(r)
        
        r = AP.parse_args(['--test','abra'])
        self.assertFalse(r)
        
        r = AP.parse_args(['--test','-t'])
        self.assertFalse(r)
        

    def test_opt2(self):
        AP = ArgParser(Opt('test','t',Str()))

        r = AP.parse_args(['-t','abra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'abra')
        
        r = AP.parse_args(['--test','cadabra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'cadabra')
        
        r = AP.parse_args(['--test','-t'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'-t')
        
        r = AP.parse_args(['-t','--test'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'--test')
        
        r = AP.parse_args([])
        self.assertFalse(r)
        
        r = AP.parse_args(['abra'])
        self.assertFalse(r)
        
        r = AP.parse_args(['-t'])
        self.assertFalse(r)
        
        r = AP.parse_args(['--test','abra','cadabra'])
        self.assertFalse(r)
        

    def test_seq1(self):
        AP = ArgParser(Seq(Fix('test'),Str()))
        
        r = AP.parse_args(['test','abra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'abra')

        r = AP.parse_args(['test','cadabra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,'cadabra')

        r = AP.parse_args([])
        self.assertFalse(r)

        r = AP.parse_args(['test'])
        self.assertFalse(r)

        r = AP.parse_args(['abra'])
        self.assertFalse(r)

        r = AP.parse_args(['abra','cadabra'])
        self.assertFalse(r)

        r = AP.parse_args(['test','abra','cadabra'])
        self.assertFalse(r)

    def test_seq2(self):
        AP = ArgParser(Val(VMList(),Seq(Str(),Str())))
        
        r = AP.parse_args(['test','abra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,['test','abra'])

        r = AP.parse_args(['test','cadabra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,['test','cadabra'])

        r = AP.parse_args([])
        self.assertFalse(r)

        r = AP.parse_args(['test'])
        self.assertFalse(r)

        r = AP.parse_args(['test','abra','cadabra'])
        self.assertFalse(r)

    def test_seq3(self):
        AP = ArgParser(Seq(Str(),Str()))
        
        self.assertRaises(Exception,AP.parse_args,['cadabra','abra'])

    def test_alt(self):
        AP = ArgParser(Alt(Fix('abra'),Fix('cadabra')))
        
        r = AP.parse_args(['abra'])
        self.assertTrue(r)

        r = AP.parse_args(['cadabra'])
        self.assertTrue(r)

        r = AP.parse_args([])
        self.assertFalse(r)

        r = AP.parse_args(['test'])
        self.assertFalse(r)

        r = AP.parse_args(['abra','cadabra'])
        self.assertFalse(r)

        r = AP.parse_args(['abra','cadabra','test'])
        self.assertFalse(r)


def suite():
    return ut.tcc_tests(TC_Smp1)
        

