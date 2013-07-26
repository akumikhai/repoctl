#-*- coding: utf-8 -*-

from repolib.controller import Controller

import os
import sys

class CtlCfg:

    def default_config(self):
        
        config = {
            "repositories":[
            ],
            "remotes":[
            ],
        }

        return config

    def get_config_paths(self):
        
        from os.path import abspath,dirname,join
        
        path_exe = join(dirname(abspath(sys.argv[0])),'repo.conf')
        #TODO заменить на разбор с "~/"
        path_home = join(os.getenv('HOME',''),'.repo.conf')
        path_default = path_exe
        
        R = {
                'search_paths': [
                    path_exe,
                    path_home,
                ],
                'default': path_default,
            }
            
        return R

    def used_config(self, ctl):
        #if ctl.config_path is None:
        #    print "default config used"
        #else:
        #    print "config from [%s] used"%(ctl.config_path)
        pass

    def mk_controller(self, verbose=True):
        ctl = Controller()
        
        config_paths = self.get_config_paths()
        ctl.set_config_paths(config_paths)
        ctl.initialize()

        if verbose:
            self.used_config(ctl)
        
        return ctl
    
