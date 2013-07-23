# -*- coding: utf-8 -*-

from .repos.git import RepoGit
from .repos.gitauto import RepoGitAuto
from .repos.rsync import RepoRSync

import json
import os
import sys

RepoD = {rcls.repo_type:rcls for rcls in [RepoGit,RepoGitAuto,RepoRSync]}

class Controller:
    
    def __init__(self):
        self.repositories = {}
        self.repositories_order = []
        self.remotes = {}
        self.remotes_order = []
        
        self.search_config_paths = []

        self.config = None
        self.config_path = None

    def set_config_paths(self,paths):
        self.search_config_paths = paths['search_paths']
        self.default_config_path = paths['default']
    
    def initialize(self):
        if not self.load_config():
            self.default_config()
     
        self.initialize_from_config()
            
    def load_config(self):
        from os.path import abspath,dirname,join
        
        for confpath in self.search_config_paths:
            if not os.path.exists(confpath):
                continue

            conffile = open(confpath)
            config = json.load(conffile)

            self.config = config
            self.config_path = confpath
            
            return True
            
        else:
            return False
        
    def default_config(self):
        config = {
            'repositories': {},
            'remotes': {},
        }
        
        self.config = config
     
    def initialize_from_config(self):
        proto = self.config.get('proto')
        if proto is None:
            self.initialize_from_config_proto_none()
        else:
            raise NotImplementedError
            
    def initialize_from_config_proto_none(self):
        for repoconf in self.config['repositories']:
            reponame = repoconf['name']
            repotype = repoconf['type']
            repocls = RepoD[repotype]
            repopath = repoconf['path']
            self.repositories[reponame] = repocls(reponame,repopath)
            self.repositories_order.append(reponame)
         
     
    def refresh_config(self):
        
        repos = []
        
        for name in self.repositories_order:
            repo = self.repositories[name]
            repos.append({
                'type': repo.repo_type,
                'name': name,
                'path': repo.path,
                })

        remotes = []
        for name in self.remotes_order:
            remote = self.remotes[name]
            remotes.append({
                'name':name
                })
        
        config = {
            'repositories': repos,
            'remotes': remotes,
        }
        
        self.config = config

    def save_config(self): 
        textconfig = json.dumps(self.config,ensure_ascii=False,indent=4)
        if self.config_path is None:
            self.config_path = self.default_config_path
        
        f = open(self.config_path,'w')
        f.write(textconfig)
        f.close()
       
    
    #def add_repo(self,name,repoconf):
    #    repocls = RepoD[repoconf['type']]
    #    self.repositories[name] = repocls(repoconf)
     
    def do_repo_list(self):
        for rn in self.repositories_order:
            print rn
        
        
    def do_repo_add(self,name,repotype,path):
        if name in self.repositories:
            raise Exception("Repository [%s] already exists"%name)

        repocls = RepoD[repotype]
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


    def do_remote_list(self):
        for rn in self.remotes_order:
            print rn
        
        
    def do_remote_add(self,name,repotype,path):
        if name in self.remotes:
            raise Exception("Remote [%s] already exists"%name)

        #repocls = RepoD[repotype]
        #self.repositories[name] = repocls(name,path)
        #self.repository_order.append(name)
        #
        #self.refresh_config()
        #self.save_config()
        
    def do_remote_remove(self,name):
        if name not in self.remotes:
            raise Exception("Remote [%s] not found"%name)
        
        #del(self.repositories[name])
        #self.repository_order.remove(name)
        #
        #self.refresh_config()
        #self.save_config()
        

    def do_status(self,repos=None):
        if repos is None:
            repos = self.repositories_order

        for name in repos:
            repo = self.repositories[name]
            rc = repo.status()
            print "%-15s %-15s : changed %d"%(name,repo.repo_type,rc)
            
    def do_push(self,repos=None):
        print "do_push",repos
        
    def do_pull(self,repos=None):
        print "do_pull",repos
        
