# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

hh, mm = map(int, raw_input().split(":"))
a = int(raw_input())
t = 60*hh + mm + a
t %= 1440 
print "%02d:%02d" % (t/60, t%60)
