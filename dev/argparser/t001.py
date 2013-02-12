#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import parse_args,Fix #Alt,Req,Fix,Value

def usage_msg():
    print """\
Usage:
"""

def version():
    print """\
Help:
"""

def help():
    print """\
Help:
"""

def cmd1():
    pass
    
def cmd2():
    pass
    
#AP = ArgParser()
#Alt(
#    Value('version',Req(Alt(Fix('-v'),Fix('--version')))),
#    Value('help',Req(Alt(Fix('-h'),Fix('--help')))),
#    Value
#)

P1 = Fix('test')

t1 = parse_args(P1,['test'])
print t1

