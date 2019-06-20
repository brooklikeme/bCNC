# -*- coding: ascii -*-
# $Id$
#
# Author: zhangqx2008@gmail.com
# Date: 18-Jun-2019

class GPIO(object):
    def __init__(self):
        return

    BCM  = 0
    OUT  = 1
    HIGH = 1
    LOW  = 0

    @staticmethod
    def setmode(mode):
        print 'fake set mode!'

    @staticmethod
    def setup(port, mode):
        print 'fake setup!'

    @staticmethod
    def output(port, ttl):
        print 'fake output'