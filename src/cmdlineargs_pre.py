#-*- coding: utf-8 -*-

import controller_cfg

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
    
def cmd_repo_move_before(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_repo_move_before(argd['name'],argd.get('name2'))
    
def cmd_repo_move_after(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_repo_move_after(argd['name'],argd.get('name2'))
    

def cmd_remote_list(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_remote_list()
    
def cmd_remote_add(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_remote_add(argd['name'],argd['type'],argd['path'])
    
def cmd_remote_remove(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_remote_remove(argd['name'])
    
def cmd_remote_default(argd):
    ctl = controller_cfg.mk_controller()
    ctl.do_remote_default(argd['name'])
    
    
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
    'repo_move_before': cmd_repo_move_before,
    'repo_move_after': cmd_repo_move_after,
    
    'remote_list': cmd_remote_list,
    'remote_add': cmd_remote_add,
    'remote_remove': cmd_remote_remove,
    'remote_default': cmd_remote_default,
    
    'status': cmd_status,
    'pull': cmd_pull,
    'push': cmd_push,
}

