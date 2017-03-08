# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def automaton(s, t):
    j = 0
    for i in xrange(len(s)):
        if s[i] == t[j]:
            j += 1
        if j == len(t): break
    return j == len(t)

s = raw_input()
t = raw_input()
ss = "".join(sorted(s))
tt = "".join(sorted(t))

if automaton(s, t):
    print "automaton"
elif ss == tt:
    print "array"
elif automaton(ss, tt):
    print "both"
else:
    print "need tree"
