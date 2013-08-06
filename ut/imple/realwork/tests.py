# -*- coding: utf-8 -*-

import unittest
from repolib import ut
from .common import TCRealWork, CtlCfg, clear_fs

from repolib import app

#import cmdlineargs_cfg
#from cmdlineargs_pre import Dcmd, cmd_usage, usage_message

class TC_RealWork(TCRealWork):

    __TESTS__ = [
        'test_printx',
        'test_repo',
        'test_repox',
        'test_remote',
        'test_remotex',
        ]

    def test_printx(self):
        app.printx('TEST PRINTX')
        sx = self.pxc.buf.getvalue()
        self.assertEquals(sx,'TEST PRINTX\n')
    
    def assertCmdResult(self,lcmd,lresult):
        lx = self.do_cmd(lcmd)
        self.assertEquals(lx,lresult)

    def test_repo(self):
        self.assertCmdResult(['repo','list'],[])
        self.assertCmdResult(['repo','add','sample','git-auto','tmp/repo/sample'],[])
        self.assertCmdResult(['repo','list'],['sample'])
        self.assertCmdResult(['repo','add','abra','git-auto','tmp/repo/abra'],[])
        self.assertCmdResult(['repo','add','cadabra','git-auto','tmp/repo/cadabra'],[])
        self.assertCmdResult(['repo','list'],['sample','abra','cadabra'])
        self.assertCmdResult(['repo','move-before','cadabra','abra'],[])
        self.assertCmdResult(['repo','list'],['sample','cadabra','abra'])
        self.assertCmdResult(['repo','move-before','abra'],[])
        self.assertCmdResult(['repo','list'],['abra','sample','cadabra'])
        self.assertCmdResult(['repo','move-after','sample'],[])
        self.assertCmdResult(['repo','list'],['abra','cadabra','sample'])

    def test_repox(self):
        self.assertCmdResult(['repo','add','sample','git-auto','tmp/repo/sample'],[])
        self.do_cmd(['repo','init','sample'])
        #raise Exception

    def test_remote(self):
        self.assertCmdResult(['repo','add','sample','git-auto','tmp/repo/sample'],[])
        self.assertCmdResult(['repo','add','abra','git-auto','tmp/repo/abra'],[])
        self.assertCmdResult(['repo','add','cadabra','git-auto','tmp/repo/cadabra'],[])

        self.assertCmdResult(['remote','list'],[])
        self.assertCmdResult(['remote','add','xyz','tmp/remotes/xyz'],[])
        self.assertCmdResult(['remote','list'],['xyz'])
        self.assertCmdResult(['remote','add','zyx','tmp/remotes/zyx'],[])

    def test_remotex(self):
        pass

def suite():
    return ut.tcc_tests(TC_RealWork)
