# -*- coding: utf-8 -*-

import unittest
from repolib import ut

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,
    Name,Val,
    VMSingle,VMList,VMDict)


class TC_CmdLineArgs(unittest.TestCase):

    __TESTS__ = [
        'test_no',
        'test_version',
        'test_help',
        'test_main',
        'test_fails',
        ]

    def setUp(self):
        self.ap = ArgParser(Val(VMDict(),Alt(
            Name('command',Alt(
                Fix('version',value=True),
                Arg('version','V',valname=True),
                )),
            Name('command',Alt(
                Fix('help',value=True),
                Arg('help','h',valname=True),
                )),
            Name('command',Fix('pullall',value=True)),
            Name('command',Fix('pushall',value=True)),
            No(),
        )))

    def test_no(self):

        r = self.ap.parse_args([])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{})

    def test_version(self):

        r = self.ap.parse_args(['version'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'version'})

        r = self.ap.parse_args(['-V'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'version'})

        r = self.ap.parse_args(['--version'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'version'})

    def test_help(self):

        r = self.ap.parse_args(['help'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'help'})

        r = self.ap.parse_args(['-h'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'help'})

        r = self.ap.parse_args(['--help'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'help'})

    def test_main(self):
        
        r = self.ap.parse_args(['pullall'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'pullall'})

        r = self.ap.parse_args(['pushall'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'pushall'})

    
    def test_fails(self):
        r = self.ap.parse_args(['abra'])
        self.assertFalse(r)

        r = self.ap.parse_args(['test','cadabra'])
        self.assertFalse(r)


def suite():
    return ut.tcc_tests(TC_CmdLineArgs)
