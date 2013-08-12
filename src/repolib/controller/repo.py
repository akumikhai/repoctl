# -*- coding: utf-8 -*-

from .base import AController

import os

from ..app import printx

class ControllerRepo:

    def do_repo_list(self,verbose):
        if verbose==0:
            for rn in self.repositories_order:
                printx(rn)
        else:
            for rn in self.repositories_order:
                repo = self.repositories[rn]
                printx("%-16s %-16s %s"%(repo.name, repo.repo_type, repo.path))
            
        
        
    def do_repo_add(self,name,repotype,path):
        if name in self.repositories:
            raise Exception("Repository [%s] already exists"%name)

        path = os.path.abspath(path)

        repocls = AController.get_repocls(self,repotype)
        
        self.repositories[name] = repocls(name,path)
        self.repositories_order.append(name)
     
        self.refresh_config()
        self.save_config()
        
    def do_repo_remove(self,name):
        if name not in self.repositories:
            raise Exception("Repository [%s] not found"%name)
        
        del(self.repositories[name])
        self.repositories_order.remove(name)
        
        self.refresh_config()
        self.save_config()
        
    def do_repo_move_before(self,name,namex):
        if name not in self.repositories:
            raise Exception("Repository [%s] not found"%name)

        self.repositories_order.remove(name)

        if namex is None:
            i = 0
        else:
            if namex not in self.repositories:
                raise Exception("Repository [%s] not found"%namex)

            i = self.repositories_order.index(namex)
        
        self.repositories_order[i:i] = [name]

        self.refresh_config()
        self.save_config()

    def do_repo_move_after(self,name,namex):

        if name not in self.repositories:
            raise Exception("Repository [%s] not found"%name)

        self.repositories_order.remove(name)

        if namex is None:
            i = len(self.repositories_order)
        else:
            if namex not in self.repositories:
                raise Exception("Repository [%s] not found"%namex)
    
            i = self.repositories_order.index(namex)+1

        self.repositories_order[i:i] = [name]

        self.refresh_config()
        self.save_config()

    def do_repo_init(self,name):

        if name not in self.repositories:
            raise Exception("Repository [%s] not found"%name)

        repo = self.repositories[name]
        rc = repo.init()
        r = {'name':name,'path':repo.path}
        return r
        
    def do_repo_drop(self,name):

        if name not in self.repositories:
            raise Exception("Repository [%s] not found"%name)

        repo = self.repositories[name]
        rc = repo.drop()
        r = {'name':name,'path':repo.path}
        return r

    
