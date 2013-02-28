from .repos.git import RepoGit
from .repos.rsync import RepoRSync

RepoD = {rcls.repo_type:rcls for rcls in [RepoGit,RepoRSync]}

class Controller:
    
    @classmethod
    def from_config(cls,config):
        C = cls()
    
    def __init__(self):
        self.repositories = {}
        self.remotes = {}
    
    def to_config(self):
        
        repos = [{
                    'type': repo.repo_type,
                    'name': name
                    } for name,repo in self.repositories.items()]
        
        remotes = [{
                        'name':name
                        } for name,remote in self.remotes.items()]
        
        config = {
            'repositories': repos,
            'remotes': remotes,
        }
        
        return config
    
    def add_repo(self,name,repoconf):
        repocls = RepoD[repoconf['type']]
        self.repositories[name] = repocls(repoconf)
        
