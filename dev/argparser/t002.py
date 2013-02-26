#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,Opt,Plus,
    Val,VMSingle,VMList)


AP = ArgParser(Val(VMList(),Plus(Str())))

r = AP.parse_args(['abra'])
assert r is True
assert AP.result==['abra']

#r = AP.parse_args(['abra','cadabra'])
#self.assertTrue(r)
#self.assertEquals(AP.result,['abra','cadabra'])

#r = AP.parse_args(['abra','shvabra','cadabra'])
#self.assertTrue(r)
#self.assertEquals(AP.result,['abra','shvabra','cadabra'])

#r = AP.parse_args([])
#self.assertFalse(r)

