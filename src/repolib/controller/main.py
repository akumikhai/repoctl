# -*- coding: utf-8 -*-

from ..app import printx

class ControllerMain:

    def do_status(self,repos=None):
        def proc_status(repo):
            rc = repo.status()
            printx("%-15s %-15s : changed %d"%(repo.name,repo.repo_type,rc))
        
        self.do_repos_command(repos,proc_status)
            
    def do_push(self,repos=None):
        def proc_push(repo):
            repo.push()
            printx("%-15s %-15s : push completed"%(repo.name,repo.repo_type))
        
        self.do_repos_command(repos,proc_push)
        
    def do_pull(self,repos=None):
        def proc_pull(repo):
            repo.pull()
            printx("%-15s %-15s : pull completed"%(repo.name,repo.repo_type))
        
        self.do_repos_command(repos,proc_pull)


