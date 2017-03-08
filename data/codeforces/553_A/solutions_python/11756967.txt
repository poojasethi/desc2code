#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

import math
import fractions

mod = 1000000007
maxn = 1010

n = int(input())

comb = [[0 for j in range(maxn)] for i in range(maxn)]

for i in range(maxn):
    comb[i][0] = 1
    for j in range(1, maxn):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % mod

colors = []
for i in range(n):
    colors.append(int(input()))

res = 1
total = 0

for i in range(n):
    res = (res * comb[total+colors[i]-1][colors[i]-1]) % mod
    total += colors[i]

print(res)    
