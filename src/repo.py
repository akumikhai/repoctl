#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import ArgParser
import cmdlineargs_cfg

import sys

def usage_message():
    print """\
Usage:
    repoctl <command> <options>
"""

def cmd_usage(argd):
    usage_message()

def cmd_version(argd):
    print "cmd_version"

def cmd_help(argd):
    usage_message()
    
def cmd_pullall(argd):
    print "cmd_pullall"

def cmd_pushall(argd):
    print "cmd_pushall"
    

Dcmd = {
    'usage': cmd_usage,
    'version': cmd_version,
    'help': cmd_help,
    'pullall': cmd_pullall,
    'pushall': cmd_pushall,
}


ap = cmdlineargs_cfg.mk_argparser()

if ap.parse_args(sys.argv[1:]):
    cmd = ap.result.get('command','usage')
    fcmd = Dcmd[cmd]

    r = fcmd(ap.result)
    sys.exit(r)
    
else:
    usage_message()
    sys.exit(-1)

