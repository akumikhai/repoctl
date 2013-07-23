#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import subprocess

popen = subprocess.Popen(['git','status'],
                            cwd='/home/mivl/proj/5mp',
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )

print popen

popen.stdin.close()
s_stdout = popen.stdout.read()
s_stderr = popen.stderr.read()

print 'STDERR [%s]'%s_stderr
print 'STDOUT [%s]'%s_stdout
