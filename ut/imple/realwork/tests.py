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
from repolib.stuff import PrintXCollector

import os
import sys

class CtlCfg(controller_cfg.CtlCfg):
    
    def get_config_paths(self):
        
        from os.path import abspath,dirname,join
        
        path_exe = join(dirname(abspath(sys.argv[0])),'repo.conf')
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
        'test_repo_list',
        ]

    def setUp(self):
        self.ap = cmdlineargs_cfg.mk_argparser()
        
        initialize_ctlcfg(CtlCfg())

        self.pxc = PrintXCollector()

        app._printx = self.pxc.printx

    def test_repo_list(self):
        r = self.ap.parse_args(['repo','list'])
        cmd = self.ap.result.get('command','usage')
        fcmd = Dcmd.get(cmd,cmd_usage)
        fcmd(self.ap.result)

        sout = self.pxc.buf.getvalue()

        print "DEV: [%s]"%sout

    def test_repo_add(self):
        
        r = self.ap.parse_args(['repo','list'])
        fcmd = Dcmd.get(cmd,cmd_usage)
        r = fcmd(ap.result)

        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'repo_list'})

        r = self.ap.parse_args(['repo','add','xyz','drv','/abra/shvabra/xyz'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'repo_add','name':'xyz','type':'drv','path':'/abra/shvabra/xyz'})

        r = self.ap.parse_args(['repo','remove','xyz'])
        self.assertTrue(r)
        self.assertEquals(self.ap.result,{'command':'repo_remove', 'name':'xyz'})

def suite():
    return ut.tcc_tests(TC_RealWork)
