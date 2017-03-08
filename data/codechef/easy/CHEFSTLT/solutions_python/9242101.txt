# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:36:38 2016

@author: shashank
"""

T = int(raw_input())
for i in range(T):
    S1 = raw_input()
    S2 = raw_input()
    length = len(S1)
    buff = 0
    difference = 0
    for j in range(length):
        if S1[j] == '?' or S2[j] == '?':
            buff += 1
        elif S1[j] != S2[j]:
            difference += 1
    print difference,difference + buff
            
