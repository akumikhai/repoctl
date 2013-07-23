#-*- coding: utf-8 -*-

class RepoGit:
    
    repo_type = 'git'

    def __init__(self,name,path):
        self.name = name
        self.path = path

    def init(self):
        print "[%s] git init"%self.name
        
    def status(self):
        #print "[%s] git status"%self.name
        return 0
        
    def pull(self,remote):
        print "[%s] git pull"%self.name
        
    def push(self,remote):
        print "[%s] git push"%self.name

