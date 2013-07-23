# -*- coding: utf-8 -*-

import subprocess

from repolib.common import Result

def run_cmd(cwd,argv):
    popen = subprocess.Popen(argv,
                            cwd=cwd,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                        
    popen.stdin.close()

    s_stdout = popen.stdout.read()
    s_stderr = popen.stderr.read()

    popen.wait()
    
    if popen.returncode==0:
        return s_stdout
    else:
        raise Exception('failed execute command %s in %s'%(argv,cwd))

