# -*- coding: utf-8 -*-

import unittest
from repolib import ut

#import cmdlineargs_cfg
#from cmdlineargs_pre import Dcmd, cmd_usage, usage_message

from repolib.cmdlineargs import ArgParser
from impl import cmdlineargs_cfg
from impl import controller_cfg
from impl.cmdlineargs_pre import initialize_ctlcfg, Dcmd, cmd_usage, usage_message

from repolib import app
from repolib.stuff import PrintXCollector, run_cmd

import os
import sys
import shutil

class CtlCfg(controller_cfg.CtlCfg):
    
    def get_config_paths(self):
        
        from os.path import abspath,dirname,join
        
        path_exe = join(dirname(abspath(sys.argv[0])),'repo-ut.conf')
        path_default = path_exe
        
        R = {
                'search_paths': [
                    path_exe,
                ],
                'default': path_default,
            }
            
        return R


class TC_RealWork(unittest.TestCase):

    __TESTS__ = [
        'test_printx',
        'test_repo',
        'test_repox',
        'test_remote',
        ]

    def setUp(self):
        self.clear_fs()
        
        self.ap = cmdlineargs_cfg.mk_argparser()
        initialize_ctlcfg(CtlCfg())

        self.pxc = PrintXCollector()
        app._application.printx = self.pxc.printx

    def clear_fs(self):
        try:
            os.remove('repo-ut.conf')
        except OSError,e:
            if e.errno==2:
                pass
            else:
                raise
            
        shutil.rmtree('tmp')
        os.mkdir('tmp')

    def do_cmd(self,lcmd):
        self.pxc.reset()
        r = self.ap.parse_args(lcmd)
        cmd = self.ap.result.get('command','usage')
        fcmd = Dcmd.get(cmd,cmd_usage)
        fcmd(self.ap.result)
        sout = self.pxc.buf.getvalue()
        
        if sout=='':
            return []
        
        if sout[-1]=='\n':
            sout = sout[:-1]
        
        lout = sout.split('\n')
        return lout

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


def suite():
    return ut.tcc_tests(TC_RealWork)
