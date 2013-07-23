#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import ArgParser
import cmdlineargs_cfg
from cmdlineargs_pre import Dcmd, cmd_usage, usage_message

import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ap = cmdlineargs_cfg.mk_argparser()

if ap.parse_args(sys.argv[1:]):
    cmd = ap.result.get('command','usage')
    fcmd = Dcmd.get(cmd,cmd_usage)
    r = fcmd(ap.result)
    sys.exit(r)
    
else:
    usage_message()
    sys.exit(-1)

