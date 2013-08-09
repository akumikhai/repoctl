# -*- coding: utf-8 -*-

import unittest
from repolib import ut
from .common import TCRealWork, CtlCfg, clear_fs

from repolib import app

class TC_RW_Remote(TCRealWork):

    __TESTS__ = [
        'test_remote',
        'test_remotex',
        ]

    def test_remote(self):
        self.assertCmdResult(['repo','add','sample','git-auto','tmp/repo/sample'],[])
        self.assertCmdResult(['repo','add','abra','git-auto','tmp/repo/abra'],[])
        self.assertCmdResult(['repo','add','cadabra','git-auto','tmp/repo/cadabra'],[])

        self.assertCmdResult(['remote','-v','0','list'],[])
        self.assertCmdResult(['remote','add','xyz','tmp/remotes/xyz'],[])
        self.assertCmdResult(['remote','-v','0','list'],['xyz'])
        self.assertCmdResult(['remote','add','zyx','tmp/remotes/zyx'],[])

    def test_remotex(self):
        pass

