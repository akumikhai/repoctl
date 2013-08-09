#-*- coding: utf-8 -*-

#import controller_cfg as ctlcfg

from repolib.app import printx

_ctlcfg = None

def initialize_ctlcfg(ctlcfg):
    global _ctlcfg
    _ctlcfg = ctlcfg


def usage_message():
    printx("""\
Usage:
    repoctl <command>

<command>

    version
    help
    repo <repo-sub-command>
    
    status <repo>*
    pull <repo>*
    push <repo>*

<repo-sub-command>
    list
    add <name> <type> <path>
    remove <name>
    init <name>
    drop <name>

<remote-sub-command>
    list
    add <name> <path>
    remove <name>

""")

def prepare_argd(argd):
    argd = argd.copy()
    sverbose = argd.get('verbose','1')
    argd['verbose'] = int(sverbose)
    return argd

def cmd_usage(argd):
    usage_message()

def cmd_version(argd):
    print "TODO: cmd_version"

def cmd_help(argd):
    usage_message()


def cmd_repo_list(argd):
    ctl = _ctlcfg.mk_controller()

    ctl.do_repo_list(
        verbose=argd.get('verbose'),
        )
    
def cmd_repo_add(argd):
    ctl = _ctlcfg.mk_controller()

    ctl.do_repo_add(
        name=argd['name'],
        repotype=argd['type'],
        path=argd['path'],
        )
    
def cmd_repo_remove(argd):
    ctl = _ctlcfg.mk_controller()

    ctl.do_repo_remove(
        name=argd['name'],
        )
    
def cmd_repo_move_before(argd):
    ctl = _ctlcfg.mk_controller()

    ctl.do_repo_move_before(
        name=argd['name'],
        namex=argd.get('name2'),
        )
    
def cmd_repo_move_after(argd):
    ctl = _ctlcfg.mk_controller()

    ctl.do_repo_move_after(
        name=argd['name'],
        namex=argd.get('name2'),
        )
    
def cmd_repo_init(argd):
    ctl = _ctlcfg.mk_controller()

    r = ctl.do_repo_init(
        name=argd['name'],
        )

    verbose = argd.get('verbose',1)
    if verbose>0:
        printx("Local repository [%s] at [%s] initialized"%(r['name'],r['path']))
    
def cmd_repo_drop(argd):
    ctl = _ctlcfg.mk_controller()
    r = ctl.do_repo_drop(
        name=argd['name'],
        )
    
    printx("Local repository [%s] at [%s] dropped"%(r['name'],r['path']))
    

def cmd_remote_list(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_list(
        verbose=argd.get('verbose'),
    )
    
def cmd_remote_add(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_add(
        name=argd['name'],
        path=argd['path'],
        )
    
def cmd_remote_remove(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_remove(
        name=argd['name'],
        )
    
def cmd_remote_default(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_default(
        name=argd['name']
        )
    
def cmd_remote_move_before(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_move_before(
        name=argd['name'],
        namex=argd.get('name2'),
        )
    
def cmd_remote_move_after(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_move_after(
        name=argd['name'],
        namex=argd.get('name2'),
        )
    
def cmd_remote_create(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_create(
        name=argd['name'],
        path=argd.get('path'),
        )
    
def cmd_remote_repo_add(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_repo_add(
        name=argd['name'],
        repo_name=argd['repo_name'],
        path=argd.get('path'),
        )
    
def cmd_remote_repo_remove(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_repo_remove(
        name=argd['name'],
        repo_name=argd['repo_name'],
        )
    
def cmd_remote_repo_list(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_repo_init(
        name=argd['name'],
        )
    
def cmd_remote_repo_init(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_repo_init(
        name=argd['name'],
        repo_name=argd['repo_name'],
        )
    
def cmd_remote_repo_drop(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_remote_repo_drop(
        name=argd['name'],
        repo_name=argd['repo_name'],
        )
    
    
def cmd_status(argd):
    ctl = _ctlcfg.mk_controller()
    repolist = argd['repos']
    
    if len(repolist)==0 or (repolist==['all']):
        repolist = None
    
    ctl.do_status(
        repos=repolist
        )

def cmd_pull(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_pull(
        repos=argd['repos']
        )

def cmd_push(argd):
    ctl = _ctlcfg.mk_controller()
    ctl.do_push(
        repos=argd['repos']
        )

Dcmd = {
    'usage': cmd_usage,
    'version': cmd_version,
    'help': cmd_help,
    
    'repo_list': cmd_repo_list,
    'repo_add': cmd_repo_add,
    'repo_remove': cmd_repo_remove,
    'repo_move_before': cmd_repo_move_before,
    'repo_move_after': cmd_repo_move_after,
    'repo_init': cmd_repo_init,
    'repo_drop': cmd_repo_drop,
    
    'remote_list': cmd_remote_list,
    'remote_add': cmd_remote_add,
    'remote_remove': cmd_remote_remove,
    'remote_default': cmd_remote_default,
    'remote_create': cmd_remote_create,
    'remote_repo_add': cmd_remote_repo_add,
    'remote_repo_remove': cmd_remote_repo_remove,
    'remote_repo_list': cmd_remote_repo_list,
    'remote_repo_init': cmd_remote_repo_init,
    'remote_repo_drop': cmd_remote_repo_drop,
    
    'status': cmd_status,
    'pull': cmd_pull,
    'push': cmd_push,
}

