#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,Opt,Plus,
    Val,VMSingle,VMList)


AP = ArgParser(Val(VMList(),Seq(Str(),Str())))

r = AP.parse_args(['test','abra'])
assert r is True
assert AP.result==['test','abra']
