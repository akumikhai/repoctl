# -*- coding: utf-8 -*-

import unittest
from repolib import ut
from .common import TCRealWork, CtlCfg, clear_fs

from repolib import app

import os

def frl(name,repotype,path):
    return u"%-16s %-16s %s"%(name,repotype,os.path.abspath(path))

class TC_RW_Repo(TCRealWork):

    __TESTS__ = [
        'test_repo',
        'test_repox',
        ]

    def test_repo(self):
        self.assertCmdResult(['repo','list'],[])
        
        self.assertCmdResult(['repo','add','sample','git-auto','tmp/repo/sample'],[])
        self.assertCmdResult(['repo','list'],[frl('sample','git-auto','tmp/repo/sample')])
        
        self.assertCmdResult(['repo','add','abra','git-auto','tmp/repo/abra'],[])
        self.assertCmdResult(['repo','add','cadabra','git-auto','tmp/repo/cadabra'],[])
        self.assertCmdResult(['repo','list'],[
            frl('sample','git-auto','tmp/repo/sample'),
            frl('abra','git-auto','tmp/repo/abra'),
            frl('cadabra','git-auto','tmp/repo/cadabra')])
        
        self.assertCmdResult(['repo','move-before','cadabra','abra'],[])
        self.assertCmdResult(['repo','-v','0','list'],['sample','cadabra','abra'])
        self.assertCmdResult(['repo','move-before','abra'],[])
        self.assertCmdResult(['repo','-v','0','list'],['abra','sample','cadabra'])
        self.assertCmdResult(['repo','move-after','sample'],[])
        self.assertCmdResult(['repo','-v','0','list'],['abra','cadabra','sample'])

    def test_repox(self):
        self.assertCmdResult(['repo','add','sample','git-auto','tmp/repo/sample'],[])
        self.assertCmdResult(['repo','-v','0','init','sample'],[])
        #raise Exception

