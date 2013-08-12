# -*- coding: utf-8 -*-

from .base import AController
from .repo import ControllerRepo
from .remote import Remote, ControllerRemote
from .main import ControllerMain

from ..repos.git import RepoGit
from ..repos.gitauto import RepoGitAuto
from ..repos.rsync import RepoRSync

from ..app import printx

import json
import os
import sys

RepoD = {rcls.repo_type:rcls for rcls in [RepoGit,RepoGitAuto,RepoRSync]}

class Controller(AController,ControllerRepo,ControllerRemote,ControllerMain):

    def get_repocls_impl(self,repotype):
        return RepoD[repotype]
     

        

