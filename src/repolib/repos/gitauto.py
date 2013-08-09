#-*- coding: utf-8 -*-

from repolib.stuff import run_cmd

import os
import shutil

class RepoGitAuto:
    
    repo_type = 'git-auto'

    def __init__(self,name,path):
        self.name = name
        self.path = path

    def init(self):
        #print "[%s] git-auto init"%self.name
        
        os.makedirs(self.path)
        run_cmd(self.path,['git','init'])
        
    def drop(self):
        shutil.rmtree(self.path)
        
    def status(self):
        r = run_cmd(self.path,['git','status','--porcelain'])

        if len(r)==0:
            rl = 0
        else:
            rl = len(r.split('\n'))

        return rl
        
        
    def pull(self,remote):
        #r = run_cmd(self.path,['git','status','--porcelain'])
        print "TODO: [%s] git-auto pull"%self.name
        return
        r = run_cmd(self.path,['git','fetch',remote-repo-path])
        r = run_cmd(self.path,['git','pull','--rebase',remote-repo-path])
        
    def push(self,remote):
        print "TODO: [%s] git-auto push"%self.name

