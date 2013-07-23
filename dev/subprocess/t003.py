#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.stuff import run_cmd

repo_path = '/home/mivl/proj/repoctl'

r = run_cmd(repo_path,['git','status','--porcelain'])

if r.success:
    print r.data

