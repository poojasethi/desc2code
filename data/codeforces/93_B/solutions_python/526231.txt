#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

eps = 1e-07

def is_zero(x):
    if x<0:
        return -x < eps
    return x < eps

class Bottle:
    def __init__(self, no, milk=0.0):
        self.no = no
        self.milk = milk
    def is_empty(self):
        return is_zero(self.milk)

class Cup:
    capacity = 0.0
    def __init__(self):
        self.milk = 0.0
        self.ingridients = []
    def space_left(self):
        return Cup.capacity - self.milk
    def is_empty(self):
        return is_zero(self.milk)
    def is_full(self):
        return is_zero(self.space_left())
    def __repr__(self):
        return str(self.ingridients)

def put_from_bottle_to_cup(bottle,cup):
    if bottle.is_empty() or cup.is_full():
        return False
    #print 'moving milk from %s bottle (%s left) to cup (has %s)' % (bottle.no,bottle.milk,cup.milk)
    space_in_cup = cup.space_left()
    if bottle.milk <= space_in_cup:
        cup.milk += bottle.milk
        cup.ingridients.append((bottle.no,bottle.milk))
        bottle.milk = 0.0
    else:
        bottle.milk -= space_in_cup
        cup.milk = cup.capacity
        cup.ingridients.append((bottle.no,space_in_cup))
    return True

def solve(n,w,m):
    
    bottles = [Bottle(i+1,w) for i in range(n)]
    
    Cup.capacity = float(n * w) / float(m)
    #print 'capacity:',Cup.capacity
    cups = [Cup() for i in range(m)]
    
    ci = 0
    for bi in range(n):
        bottle = bottles[bi]
        put_from_bottle_to_cup(bottle,cups[ci])
        if not bottle.is_empty():
            if ci+1 > m:
                return []
            put_from_bottle_to_cup(bottle,cups[ci+1])
            if not bottle.is_empty():
                return []
        while ci+1<m and cups[ci].is_full():
            ci += 1

    #print cups
    return [cup.ingridients for cup in cups]
    #return []
    #return [[(1,1000./3)],[(2,1000./3)],[(2,500./3), (1,500./3)]]

S = input.readline().split(' ')
assert len(S)==3
n = int(S[0])
w = int(S[1])
m = int(S[2])
assert 1<=n and n<=50
assert 100<=w and w<=1000
assert 2<=m and m<=50

A = solve(n,w,m)
if A:
    output.write('YES\n')
    for n in range(m):
        S = map(lambda p: '%d %.6f' % p, A[n])
        output.write(' '.join(S))
        output.write('\n')
else:
    output.write('NO\n')
