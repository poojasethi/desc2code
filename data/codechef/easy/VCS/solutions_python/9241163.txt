# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:27:49 2016

@author: shashank
"""

import sys
T = int(sys.stdin.readline())
output = [[] for i in range(T)]
for i in range (T):
    NMK = (sys.stdin.readline().split())
    N = int(NMK[0])
    M = int(NMK[1])
    K = int(NMK[2])
    A = set(int(x) for x in sys.stdin.readline().split())
    B = set(int(x) for x in sys.stdin.readline().split())
    output[i].append(len(A.intersection(B)))
    output[i].append(N - len(A.union(B)))
for item in output:
    print item[0],item[1]
    