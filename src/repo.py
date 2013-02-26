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

def cmd_version():
    print "cmd_version"

def cmd_help():
    print "cmd_help"
    
def cmd_pullall():
    print "cmd_pullall"

def cmd_pushall():
    print "cmd_pushall"
    

ap = cmdlineargs_cfg.mk_argparser()

if ap.parse_args(sys.argv[1:]):
    print ap.result
else:
    usage_message()
    sys.exit(-1)

