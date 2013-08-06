# -*- coding: utf-8 -*-

from repolib import ut

from . import common
from . import tests_repo
from . import tests_remote

def suite():
    s = ut.tcc_tests(
        common.TC_RW_Common,
        tests_repo.TC_RW_Repo,
        tests_remote.TC_RW_Remote,
        )
    
    return s
