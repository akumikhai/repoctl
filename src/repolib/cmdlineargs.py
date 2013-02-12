#-*- coding: utf-8 -*-

import sys

class ArgParser:

    def __init__(self,pattern):
        self.pattern = pattern
        
        self.result = None
    
    def reset(self):
        self.value_flag = False
        self.value = None
    
    def set_value(self,value):
        self.value = value
        self.value_flag = True
    
    def parse_args(self,seq):
        self.reset()
        
        L = self.pattern.chk_parse(self,seq,0)
        if L is None:
            return False
        elif len(seq)!=L:
            return False
        else:
            self.result = self.value
            return True

        
class Fix:

    def __init__(self,word):
        self.word = word
        
    def chk_parse(self,parser,seq,pos):
        if pos<len(seq) and seq[pos]==self.word:
            return 1
        else:
            return None


class Str:

    def chk_parse(self,parser,seq,pos):
        if pos<len(seq):
            parser.set_value(seq[pos])
            return 1
        else:
            return None
        

class Opt:
    
    def __init__(self,short,full,after=None):
        self.short = short
        self.full = full
        self.after = after
        
    def chk_parse(self,parser,seq,pos):
        if pos<len(seq):
            if seq[pos]=='-%s'%self.short or seq[pos]=='--%s'%self.full:
                if self.after is None:
                    return 1
                
                l = self.after.chk_parse(parser,seq,pos+1)
                if l is None:
                    return None
                else:
                    return l+1

        return None
        

class Seq:

    def __init__(self,*patterns):
        self.patterns = patterns

    def chk_parse(self,parser,seq,pos):
        curpos = pos
        curlen = 0
        
        for p in self.patterns:
            if curpos<len(seq):
                l = p.chk_parse(parser,seq,curpos)
                if l is None:
                    return None
                else:
                    curpos += l
                    curlen += l
            else:
                return None
        
        if curlen==0:
            return None
            
        return curlen

#class Alt:
#    def __init__(
