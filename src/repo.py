#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import ArgParser
from impl import cmdlineargs_cfg
from impl.controller_cfg import CtlCfg
from impl.cmdlineargs_pre import initialize_ctlcfg, Dcmd, cmd_usage, usage_message, prepare_argd

import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ap = cmdlineargs_cfg.mk_argparser()

if ap.parse_args(sys.argv[1:]):
    
    initialize_ctlcfg(CtlCfg())
    
    argd = prepare_argd(ap.result)
    cmd = argd.get('command','usage')
    fcmd = Dcmd.get(cmd,cmd_usage)
    r = fcmd(argd)
    sys.exit(r)
    
else:
    usage_message()
    sys.exit(-1)

