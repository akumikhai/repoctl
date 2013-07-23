#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import subprocess

from repolib.common import Result

repo_path = '/home/mivl/proj/repoctl'

def git_status(path):
    popen = subprocess.Popen(['git','status','--porcelain'],
                            cwd=path,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )

    #print popen

    popen.stdin.close()
    s_stdout = popen.stdout.read()
    s_stderr = popen.stderr.read()

    #print 'STDERR [%s]'%s_stderr
    #print 'STDOUT [%s]'%s_stdout

    if len(s_stderr)==0:
        return Result(True,s_stdout)
    else:
        return Result(False,s_stderr)


r = git_status(repo_path)
if r.success:
    print r.data

