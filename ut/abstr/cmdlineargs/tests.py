# -*- coding: utf-8 -*-

import unittest

import smp1
import namedval

def suite():
    return unittest.TestSuite([
        smp1.suite(),
        namedval.suite(),
        ])


