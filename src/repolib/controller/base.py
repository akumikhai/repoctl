# -*- coding: utf-8 -*-

from .remote import Remote

import json
import os
import sys

class AController:

    def __init__(self):
        self.repositories = {}
        self.repositories_order = []
        self.remotes = {}
        self.remotes_order = []
        self.remote_default = None
        
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
            repocls = self.get_repocls(repotype)
            repopath = repoconf['path']
            self.repositories[reponame] = repocls(reponame,repopath)
            self.repositories_order.append(reponame)
         
        for remoteconf in self.config['remotes']:
            remotename = remoteconf['name']
            remotepath = remoteconf['path']
            self.remotes[remotename] = Remote(remotename,remotepath)
            self.remotes_order.append(remotename)


    def get_repocls(self,repotype):
        return self.get_repocls_impl(repotype)
     
    def get_repocls_impl(self,repotype):
        raise NotImplementedError
     
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
                'name':name,
                'path':remote.path
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
       
    
    
