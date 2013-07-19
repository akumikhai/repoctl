#-*- coding: utf-8 -*-

class RepoGitAuto:
    
    repo_type = 'git-auto'

    def __init__(self,name,path):
        self.name = name
        self.path = path

    def init(self):
        print "[%s] git-auto init"%self.name
        
    def status(self):
        print "[%s] git-auto status"%self.name
        
    def pull(self,remote):
        print "[%s] git-auto pull"%self.name
        
    def push(self,remote):
        print "[%s] git-auto push"%self.name

