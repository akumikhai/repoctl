# -*- coding: utf-8 -*-

import unittest
from repolib import ut

import cmdlineargs_cfg

class TC_CmdLineArgs(unittest.TestCase):

    __TESTS__ = [
        'test_no',
        'test_version',
        'test_help',
        'test_repo',
        'test_remote',
        'test_main',
        'test_fails',
        ]

    def setUp(self):
        self.ap = cmdlineargs_cfg.mk_argparser()

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

    def test_repo(self):
        
        r = self.ap.parse_args(['repo','list'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'repo_list'})

        r = self.ap.parse_args(['repo','add','xyz','drv','/abra/shvabra/xyz'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'repo_add','name':'xyz','type':'drv','path':'/abra/shvabra/xyz'})

        r = self.ap.parse_args(['repo','remove','xyz'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'repo_remove', 'name':'xyz'})

    
    def test_remote(self):
        r = self.ap.parse_args(['remote','list'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'remote_list'})

        r = self.ap.parse_args(['remote','add','xyz','/abra/shvabra/xyz'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'remote_add','name':'xyz','path':'/abra/shvabra/xyz'})

        r = self.ap.parse_args(['remote','remove','xyz'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'remote_remove', 'name':'xyz'})
        
    def test_main(self):
        r = self.ap.parse_args(['status'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'status', 'repos':[]})

        r = self.ap.parse_args(['pull'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'pull', 'repos':[]})

        r = self.ap.parse_args(['push'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'push', 'repos':[]})
    
    def test_fails(self):
        r = self.ap.parse_args(['abra'])
        self.assertFalse(r)

        r = self.ap.parse_args(['test','cadabra'])
        self.assertFalse(r)


def suite():
    return ut.tcc_tests(TC_CmdLineArgs)
