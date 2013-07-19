#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import ArgParser
import cmdlineargs_cfg
import controller_cfg

import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def usage_message():
    print """\
Usage:
    repoctl <repo-command>

<repo-command>

    version
    help
    add <name> <type> <path>
    remove <name>
    status <repo>*
    pull <repo>*
    push <repo>*

"""

def cmd_usage(argd):
    usage_message()

def cmd_version(argd):
    print "cmd_version"

def cmd_help(argd):
    usage_message()

def cmd_repo_list(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_repo_list()
    
def cmd_repo_add(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_repo_add(argd['name'],argd['type'],argd['path'])
    
def cmd_repo_remove(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_repo_remove(argd['name'])
    
def cmd_status(argd):
    ctl = controller_cfg.mk_controller()
    repolist = argd['repos']
    if len(repolist)==0 or (repolist==['all']):
        repolist = None
    ctl.do_status(repolist)

def cmd_pull(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_pull(argd['repos'])

def cmd_push(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_push(argd['repos'])
    

Dcmd = {
    'usage': cmd_usage,
    'version': cmd_version,
    'help': cmd_help,
    
    'repo_list': cmd_repo_list,
    'repo_add': cmd_repo_add,
    'repo_remove': cmd_repo_remove,
    
    'status': cmd_status,
    'pull': cmd_pull,
    'push': cmd_push,
}


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

