#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

n = int(raw_input())

a = [map(int, raw_input().split()) for _ in xrange(n)]
a.sort()

if n == 1:
    print 1
    exit(0)

ans = 2
pos = a[0][0]

for now, next in zip(a[1:-1], a[2:]):
    if now[0] - now[1] > pos:
        pos = now[0]
        ans += 1
    elif now[0] + now[1] < next[0]:
        pos = now[0] + now[1]
        ans += 1
    else:
        pos = now[0]

print ans
