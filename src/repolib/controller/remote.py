# -*- coding: utf-8 -*-

from ..app import printx

import json
import os

class Remote:
    
    def __init__(self,name,path):
        self.name = name
        self.path = path

        self.repositories = {}

    def load(self):
        f = open(self.path)
        textconfig = f.read()
        f.close()
        
        remotecfg = json.loads(textconfig)
        
        self.repositories = remotecfg['repositories']
        
    def  save(self):
        remotecfg = {
            'repositories': self.repositories
        }
        
        textconfig = json.dumps(remotecfg,ensure_ascii=False,indent=4)
        f = open(self.path,'w')
        f.write(textconfig)
        f.close()
        
    def do_repo_add(self,name,path):
        if name in self.repositories:
            raise Exception("Repo [%s] already exists in remote [%s]"%(name,self.name))

        self.repositories[name] = {
            'name':name,
            'path':path,
            }
        
    def do_repo_remove(self,name):
        if name not in self.repositories:
            raise Exception("Repo [%s] not found in remote [%s]"%(name,self.name))

        del self.repositories[name]
        
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

        path = os.path.abspath(path)

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
            self.do_remote_add(name, path)
        else:
            path = self.remotes[name].path
        
        remote = Remote(name,path)
        remote.save()
        
    def do_remote_repo_add(self,name,repo_name,path):
        remote = self.remotes[name]
        remote.load()
        remote.do_repo_add(repo_name,path)
        remote.save()
        
    def do_remote_repo_remove(self, name,repo_name):
        print "TODO: do_remote_repo_remove",name,repo_name
        remote = self.remotes[name]
        remote.load()
        remote.do_repo_remove(repo_name)
        remote.save()
        
    def do_remote_repo_list(self,name):
        print "TODO: do_remote_repo_list",name
        

    def do_repos_command(self,repos,proc):
        if repos is None:
            repos = self.repositories_order

        for name in repos:
            repo = self.repositories[name]
            proc(repo)
        

