# -*- coding: utf-8 -*-

from ..app import printx

import json

class Remote:
    
    def __init__(self,name,path):
        self.name = name
        self.path = path

        self.repositories = {}

    def load(self):
        pass
        
    def  save(self):
        remotecfg = {
            'repositories':{}
        }
        
        textconfig = json.dumps(remotecfg,ensure_ascii=False,indent=4)
        f = open(self.path,'w')
        f.write(textconfig)
        f.close()
        
        
class ControllerRemote:

    def do_remote_list(self,verbose):
        if verbose==0:
            for rn in self.remotes_order:
                printx(rn)
        else:
            for rn in self.remotes_order:
                remote = self.remotes[rn]
                printx("%-16s %s"%(remote.name, remote.path))
            
        
        
    def do_remote_add(self,name,path):
        if name in self.remotes:
            raise Exception("Remote [%s] already exists"%name)

        self.remotes[name] = Remote(name,path)
        self.remotes_order.append(name)
        
        self.refresh_config()
        self.save_config()
        
    def do_remote_remove(self,name):
        if name not in self.remotes:
            raise Exception("Remote [%s] not found"%name)
        
        del(self.remotes[name])
        self.remotes_order.remove(name)
        
        self.refresh_config()
        self.save_config()
        
    def do_remote_default(self,name):
        self.remote_default = name

    def do_remote_move_before(self,name,namex):
        print "TODO: do_remote_move_before",name,namex

    def do_remote_move_after(self,name,namex):
        print "TODO: do_remote_move_after",name,namex

    def do_remote_create(self,name,path):
        if name not in self.remotes and path is not None:
            self.do_remote_add(name,path)
        else:
            path = self.remotes[name].path
        
        remote = Remote(name,path)
        remote.save()
        

    def do_repos_command(self,repos,proc):
        if repos is None:
            repos = self.repositories_order

        for name in repos:
            repo = self.repositories[name]
            proc(repo)
        

