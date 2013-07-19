#-*- coding: utf-8 -*-

import sys
from repolib.common import Default

class ArgParser:

    def __init__(self,pattern):
        self.pattern = pattern
        self.valuemode = VMSingle()
        self.valuemode_stack = []
        self.name = Default
        self.name_stack = []
  
        self.result = None
    
    def reset(self):
        self.value = self.valuemode.initial()

    def push_valuemode(self,valuemode):
        self.valuemode_stack.append((self.valuemode,self.value))
        self.valuemode = valuemode
        self.value = valuemode.initial()
        
    def pop_valuemode(self):
        value = self.valuemode.get_result(self)
        self.valuemode,self.value = self.valuemode_stack.pop()
        self.set_value(value)
    
    def push_name(self,name):
        self.name_stack.append(self.name)
        self.name = name
    
    def pop_name(self):
        self.name = self.name_stack.pop()
    
    def set_value(self,value):
        self.valuemode.set_value(self,value,self.name)
    
    def parse_args(self,seq):
        self.reset()
        
        L = self.pattern.chk_parse(self,seq,0)
        if L is None:
            return False
        elif len(seq)!=L:
            return False
        else:
            self.result = self.valuemode.get_result(self)
            return True


class VMSingle:

    def initial(self):
        return [False,None]
    
    def get_result(self,parser):
        #print "VMSingle get_result:/%s/"%str(parser.value)
        return parser.value[1]
    
    def set_value(self,parser,value,name):
        if not parser.value[0]:
            parser.value = [True,value]
        else:
            raise Exception('Value is already set')
    
    
    
class VMList:

    def initial(self):
        return []

    def get_result(self,parser):
        return parser.value
    
    def set_value(self,parser,value,name):
        parser.value.append(value)
    


class VMDict:

    def initial(self):
        return {}

    def get_result(self,parser):
        return parser.value
    
    def set_value(self,parser,value,name):
        if name is not Default:
            parser.value[name] = value
    


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
    
    def __init__(self,name,pattern,value=Default):
        self.name = name
        self.pattern = pattern
        self.value = Default
    
    def chk_parse(self,parser,seq,pos):
        parser.push_name(self.name)
        r = self.pattern.chk_parse(parser,seq,pos)
        if self.value is not Default:
            parser.set_value(self.value)
        parser.pop_name()
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
                parser.set_value(self.value)
                
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
        

class Arg:
    
    def __init__(self,name,short,after=Default,value=Default,valname=False):
        if value is not Default and after is not Default:
            raise Exception('Forbid to use after and value together')
        
        self.name = name
        self.short = short
        self.after = after
        self.value = value
        self.valname = valname
        
    def chk_parse(self,parser,seq,pos):
        if pos<len(seq):
            if seq[pos]=='--%s'%self.name or seq[pos]=='-%s'%self.short:
                if self.after is Default:
                    if self.value is not Default:
                        parser.push_name(self.name)
                        parser.set_value(self.value)
                        parser.pop_name()
                    else:
                        if self.valname:
                            parser.set_value(self.name)

                    return 1
                
                parser.push_name(self.name)
                l = self.after.chk_parse(parser,seq,pos+1)
                parser.pop_name()
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
        processed = False
        
        for p in self.patterns:
            l = p.chk_parse(parser,seq,curpos)
            if l is None:
                return None
            else:
                curpos += l
                curlen += l
                processed = True
        
        if not processed:
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


class Opt:

    def __init__(self,pattern):
        self.pattern = pattern
    
    def chk_parse(self,parser,seq,pos):
        l = self.pattern.chk_parse(parser,seq,pos)
        if l is None:
            return 0
        else:
            return l
    
    
class Plus:

    def __init__(self,pattern,min=1,max=None):
        self.pattern = pattern
        self.min = min
        self.max = max
    
    def chk_parse(self,parser,seq,pos):
        curpos = pos
        curlen = 0
        count = 0
        while True:
            l = self.pattern.chk_parse(parser,seq,curpos)
            if l is None:
                if count<self.min:
                    return None
                else:
                    break
            else:
                curpos += l
                curlen += l
                count += 1
                if self.max is not None and count>self.max:
                    break
        
        return curlen
        
