# -*- coding: utf-8 -*-

from repolib import stuff

_application = type('Application',(),{})()
_application.printx = stuff.printx


def printx(*args,**kwargs):
    _application.printx(*args,**kwargs)

