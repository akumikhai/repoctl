# -*- coding: utf-8 -*-

import unittest

from impl import controller_cfg
from impl import cmdlineargs_cfg
from impl.cmdlineargs_pre import initialize_ctlcfg, Dcmd, cmd_usage, usage_message,prepare_argd

from repolib import app
from repolib.cmdlineargs import ArgParser
from repolib.stuff import PrintXCollector, run_cmd

import os
import sys
import shutil

from os.path import abspath,dirname,join

        
CONF_UT = join('tmp','repo-ut.conf')

class CtlCfg(controller_cfg.CtlCfg):
    
    def get_config_paths(self):
        
        path_exe = join(dirname(abspath(sys.argv[0])),CONF_UT)
        path_default = path_exe
        
        R = {
                'search_paths': [
                    path_exe,
                ],
                'default': path_default,
            }
            
        return R

def clear_fs():
    try:
        os.remove(CONF_UT)
    except OSError,e:
        if e.errno==2:
            pass
        else:
            raise
        
    shutil.rmtree('tmp')
    os.mkdir('tmp')


class TCRealWork(unittest.TestCase):

    def setUp(self):
        clear_fs()
        
        self.ap = cmdlineargs_cfg.mk_argparser()
        initialize_ctlcfg(CtlCfg())

        self.pxc = PrintXCollector()
        app._application.printx = self.pxc.printx

    def do_cmd(self,lcmd):
        self.pxc.reset()
        r = self.ap.parse_args(lcmd)
        argd = prepare_argd(self.ap.result) 
        cmd = argd.get('command','usage')
        fcmd = Dcmd.get(cmd,cmd_usage)
        fcmd(argd)
        sout = self.pxc.buf.getvalue()
        
        if sout=='':
            return []
        
        if sout[-1]=='\n':
            sout = sout[:-1]
        
        lout = sout.split('\n')
        return lout

    def assertCmdResult(self,lcmd,lresult):
        lx = self.do_cmd(lcmd)
        self.assertEquals(lx,lresult)

class TC_RW_Common(TCRealWork):

    __TESTS__ = [
        'test_printx',
        ]

    def test_printx(self):
        app.printx('TEST PRINTX')
        sx = self.pxc.buf.getvalue()
        self.assertEquals(sx,'TEST PRINTX\n')
    
