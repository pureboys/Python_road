#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


