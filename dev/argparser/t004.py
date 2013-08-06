#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,Plus,
    Name,Val,
    VMSingle,VMList,VMDict)



AP = ArgParser(Val(VMDict(),Seq(
    Plus(min=0,pattern=Alt(
        Arg('abra','a',value=True),
        Arg('cadabra','c',value=True),
    )),
    Name('param',Str()),
)))

r = AP.parse_args(['-a','-c','-c','sample'])
assert r is True
print AP.result
assert AP.result=={'param':'sample','abra':True,'cadabra':True}
