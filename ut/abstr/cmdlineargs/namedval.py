# -*- coding: utf-8 -*-

import unittest
from repolib import ut

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,Opt,Plus,
    Val,Name,
    VMSingle,VMList,VMDict)


class TC_NamedVal(unittest.TestCase):

    __TESTS__ = [
        'test_strs',
        'test_arg',
        ]


    def test_strs(self):
        AP = ArgParser(Val(VMDict(),Seq(Name('x',Str()),Name('y',Str()))))
        
        r = AP.parse_args(['abra','cadabra'])
        self.assertTrue(r)
        self.assertEquals(AP.result,{'x':'abra','y':'cadabra'})

        r = AP.parse_args(['abra','shvabra','cadabra'])
        self.assertFalse(r)

    def test_arg(self):
        AP = ArgParser(Val(VMDict(),
            Seq(
                Arg('abra','a',Str()),
                Arg('cadabra','c',Str()),
            )))

        r = AP.parse_args(['--abra','x','--cadabra','y'])
        self.assertTrue(r)
        self.assertEquals(AP.result,{'abra':'x','cadabra':'y'})

def suite():
    return ut.tcc_tests(TC_NamedVal)
        

