#-*- coding: utf-8 -*-

import sys
from repolib.common import Default

class ArgParser:

    def __init__(self,pattern):
        self.pattern = pattern
        self.valuemode = VMSingle()
        self.valuemode_stack = []
  
        self.result = None
    
    def reset(self):
        self.value = self.valuemode.initial()

    def push_valuemode(self,valuemode):
        self.valuemode_stack.append((self.valuemode,self.value))
        self.valuemode = valuemode
        self.value = valuemode.initial()
        
    def pop_valuemode(self):
        value = self.value
        self.valuemode,self.value = self.valuemode_stack.pop()
        self.set_value(value)
    
    def set_value(self,value):
        self.valuemode.set_value(self,value)
    
    def parse_args(self,seq):
        self.reset()
        
        L = self.pattern.chk_parse(self,seq,0)
        if L is None:
            return False
        elif len(seq)!=L:
            return False
        else:
            self.result = self.valuemode.result(self)
            return True


class VMSingle:

    def initial(self):
        return [False,None]
    
    def result(self,parser):
        return parser.value[1]
    
    def set_value(self,parser,value):
        if not parser.value[0]:
            parser.value = [True,value]
        else:
            raise Exception('Value is already set')
    
class VMList:

    def initial(self):
        return []

    def result(self,parser):
        return parser.value
    
    def set_value(self,parser,value):
        parser.value.append(value)
    


class VMDict:

    def initial(self):
        return {}

    def result(self,parser):
        return parser.value
    
    def set_value(self,parser,value,name=None):
        parser.value[Name] = value
    


class Val:
    
    def __init__(self,valuemode,pattern):
        self.valuemode = valuemode
        self.pattern = pattern

    def chk_parse(self,parser,seq,pos):
        parser.push_valuemode(self.valuemode)
        
        r = self.pattern.chk_parse(parser,seq,pos)
        
        parser.pop_valuemode()
        
        return r


class Name:
    
    def __init__(self,name,pattern):
        self.name = name
        self.pattern = pattern
    
    def chk_parse(self,parser,seq,pos):
        r = self.pattern.chk_parse(parser,seq,pos)
        return r


class No:

    def chk_parse(self,parser,seq,pos):
        return 0


class Fix:

    def __init__(self,word,value=Default):
        self.word = word
        self.value = value

    def chk_parse(self,parser,seq,pos):
        if pos<len(seq) and seq[pos]==self.word:
            if self.value is not Default:
                parser.set_value(seq[pos])
                
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
    
    def __init__(self,name,short,after=None):
        self.name = name
        self.short = short
        self.after = after
        
    def chk_parse(self,parser,seq,pos):
        if pos<len(seq):
            if seq[pos]=='--%s'%self.name or seq[pos]=='-%s'%self.short:
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



class Alt:
    
    def __init__(self,*patterns):
        self.patterns = patterns
        
    def chk_parse(self,parser,seq,pos):
        
        for p in self.patterns:
            l = p.chk_parse(parser,seq,pos)
            if l is None:
                continue
            else:
                return l
        
        return None

