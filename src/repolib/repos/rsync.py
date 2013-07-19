#-*- coding: utf-8 -*-

class RepoRSync:
    
    repo_type = 'rsync'

    def __init__(self,name,path):
        self.name = name
        self.path = path

    def init(self):
        print "[%s] rsync init"%self.name
        
    def status(self):
        print "[%s] rsync status"%self.name
        
    def pull(self,remote):
        print "[%s] rsync pull"%self.name
        
    def push(self,remote):
        print "[%s] rsync push"%self.name

