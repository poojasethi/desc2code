#!/usr/bin/python

from sys import stdin

s = stdin.readline().strip()
t = stdin.readline().strip()

h = [0]*26
for si in s:
    h[ord(si)-ord('a')] += 1
for ti in t:
    h[ord(ti)-ord('a')] -= 1
for i in xrange(26):
    if h[i] < 0:
        print 'need tree'
        exit(0)

if len(s) == len(t):
    print 'array'
    exit(0)

j = 0
for si in s:
    if si == t[j]:
        j += 1
        if j == len(t):
            print 'automaton'
            exit(0)

print 'both'
