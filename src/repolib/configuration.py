#-*- coding: utf-8 -*-

import os
import sys



def load_local_config(filepath):
    config = {
        "repositories":[
            {
                'type': 'git',
                'name': '',
                'path': '',
            },
        ],
        "remotes":[
            {
                'name': 'mobile',
                'path': '/mnt/mobile/repo/repoctl.conf',
            }
        ],
    }
    
    return config
