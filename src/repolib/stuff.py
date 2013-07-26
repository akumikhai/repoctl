# -*- coding: utf-8 -*-

from __future__ import print_function

__all__ = ['Default','Result','run_cmd','PrintXCollector']

import subprocess
from StringIO import StringIO

class DefaultType:
    def __str__(self):
        return 'Default'

    def __unicode__(self):
        return u'Default'

    def __repr__(self):
        return 'Default'
    
Default = DefaultType()



class Result:

    def __init__(self,success,data):
        self.success = success
        self.data = data



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



def printx(*args,**kwargs):
    print(*args,**kwargs)


class PrintXCollector:

    def __init__(self):
        self.buf = StringIO()
    
    def printx(self,*args,**kwargs):
        print(file=self.buf,*args,**kwargs)

