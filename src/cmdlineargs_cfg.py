# -*- coding: utf-8 -*-

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,
    Name,Val,
    VMSingle,VMList,VMDict)

def mk_argparser():
    ap = ArgParser(Val(VMDict(),Alt(
        Name('command',Alt(
            Fix('version',value=True),
            Arg('version','V',valname=True),
            )),
        Name('command',Alt(
            Fix('help',value=True),
            Arg('help','h',valname=True),
            )),
        Name('command',Fix('pullall',value=True)),
        Name('command',Fix('pushall',value=True)),
        No(),
    )))
    
    return ap
