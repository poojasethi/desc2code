#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
from operator import getitem
from bisect import bisect_left
input = sys.stdin
output = sys.stdout
import itertools

E = 'Exemplary pages.'
FROM_TO = '%d ml. from cup #%d to cup #%d.'
U = 'Unrecoverable configuration.'

def solve(V):
    n = len(V)
    vs = sum(V)
    va,r = divmod(vs,n)
    if r!=0:
        return U

    vd = []
    for i,v in enumerate(V):
        if v != va:
            vd.append((i+1,v))
        if len(vd) > 2:
            return U
    
    if len(vd) == 0:
        return E
    
    if len(vd) == 2:
        v0,v1 = vd[0][1],vd[1][1]
        vaa,r = divmod(v0+v1,2)
        if r!=0:
            return U
        dv,r = divmod(max(v0,v1) - min(v0,v1),2)
        if r!=0:
            return U
        if v0 > v1:
            return FROM_TO % (dv,vd[1][0],vd[0][0])
        else:
            return FROM_TO % (dv,vd[0][0],vd[1][0])
    
    return U

n = int(input.readline())
assert 1<=n and n<=1000

V = []
MAX_V = 10**4
for i in range(n):
    v = int(input.readline())
    assert 0<=v and v<=MAX_V
    V.append(v)

m = solve(V)
output.write('%s\n' % str(m))
