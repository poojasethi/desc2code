#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''


l = [1,1,2,2,2,3,3,3,3,0,2,2]

from itertools import groupby


n = int(raw_input())
a = map(int, raw_input().split())

d = {}

for idx, i in enumerate(a):
    if i in d:
        d[i][0] += 1
        d[i][2] = idx+1
    else:
        d[i] = [1, idx+1, idx+1]

m = a[0]

for i in a:
    if d[i][0] > d[m][0] or (d[i][0] == d[m][0] and d[i][2]-d[i][1] < d[m][2]-d[m][1]):
        m = i

print d[m][1], d[m][2]
