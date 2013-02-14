# -*- coding: utf-8 -*-

import unittest

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Opt,Seq,Alt,
    Val,VMSingle,VMList,VMDict)


class TC_CmdLineArgs(unittest.TestCase):

    def runTest(self):
        AP = ArgParser(Val(VMDict(),Alt(
            Opt('version','V'),
            Opt('help','h'),
            No(),
        )))
        
        r = AP.parse_args([])
        self.assertTrue(r)

        r = AP.parse_args(['-V'])
        self.assertTrue(r)

        r = AP.parse_args(['--version'])
        self.assertTrue(r)

        r = AP.parse_args(['abra'])
        self.assertFalse(r)

        r = AP.parse_args(['test','cadabra'])
        self.assertFalse(r)

    
def suite():
    return unittest.TestSuite([
        TC_CmdLineArgs(),
        ])
