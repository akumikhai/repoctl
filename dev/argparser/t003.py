#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,
    Name,Val,
    VMSingle,VMList,VMDict)



AP = ArgParser(Val(VMDict(),
    Name('command',
        Fix('version',value=True),
        ),
))

r = AP.parse_args(['version'])
assert r is True
print AP.result
assert AP.result=={'command':'version'}
