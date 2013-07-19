# -*- coding: utf-8 -*-

from repolib.cmdlineargs import (ArgParser,
    No,Fix,Str,Arg,Seq,Alt,Opt,Plus,
    Name,Val,
    VMSingle,VMList,VMDict)

def mk_argparser():
    ap = ArgParser(Val(VMDict(),Alt(
        Name('command',Alt(
            Fix('version',value='version'),
            Arg('version','V',valname=True),
            )),
        
        Name('command',Alt(
            Fix('help',value='help'),
            Arg('help','h',valname=True),
            )),

        Seq(
            Fix('repo'),
            Alt(
                Seq(
                    Name('command',Fix('add', value='repo_add')),
                    Name('name',Str()),
                    Name('type',Str()),
                    Name('path',Str()),
                    ),
                Seq(
                    Name('command',Fix('remove',value='repo_remove')),
                    Name('name',Str()),
                    ),
                Name('command',Fix('list',value='repo_list')),
            ),
        ),
        
        Seq(
            Name('command',Fix('status',value='status')),
            Name('repos',Val(VMList(),Plus(Str(),min=0)))
            ),
        
        Seq(
            Name('command',Fix('pull',value='pull')),
            Name('repos',Val(VMList(),Plus(Str(),min=0)))
            ),
        
        Seq(
            Name('command',Fix('push',value='push')),
            Name('repos',Val(VMList(),Plus(Str(),min=0)))
            ),
        
        No(),
    )))
    
    return ap
