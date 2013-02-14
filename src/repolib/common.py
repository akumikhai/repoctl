#-*- coding: utf-8 -*-

__ALL__ = ['Default']

class DefaultType:
    def __str__(self):
        return 'Default'

    def __unicode__(self):
        return u'Default'

    def __repr__(self):
        return 'Default'
    
Default = DefaultType()
