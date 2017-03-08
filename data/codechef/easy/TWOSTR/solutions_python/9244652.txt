# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:25:32 2016

@author: shashank
"""

T = input()
for i in range(T):
    output = None
    S1 = raw_input()
    S2 = raw_input()
    if len(S1) != len(S2):
        output = "No"
    else:
        for j in range(len(S1)):
            if S1[j] != '?' and S2[j] != '?':
                if S1[j] != S2[j]:
                    output = "No"
                    break
        if output == None:
            output = "Yes"
    print output
        