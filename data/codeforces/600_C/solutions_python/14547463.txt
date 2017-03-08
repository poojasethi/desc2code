#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 vivek9ru <vivek9ru@Vivek9RU>
#
# Distributed under terms of the MIT license.

from math import acos,asin,atan,sqrt,pi,sin,cos,tan,ceil,floor
import re
from operator import itemgetter as ig

c=[0]*26
s=raw_input()
l=len(s)
n=[]
for i in s:
	c[ord(i)-97]+=1

for i in range(26):
	if c[i]%2==1:
		n.append([i,c[i]])
k=len(n)
if l%2==0:
	for i in range(k/2):
		c[n[i][0]]+=1
		c[n[k-1-i][0]]-=1
elif k>1:
	for i in range((k-1)/2):
		c[n[i][0]]+=1
		c[n[k-1-i][0]]-=1
s=""
e=""
for i in range(26):
	if c[i]>0:
		s+=chr(i+97)*(c[i]/2)
		e=chr(i+97)*(c[i]/2)+e
if k>0 and c[n[k/2][0]]%2==1:
	s+=chr(n[k/2][0]+97)*(1)
print s+e
exit(0)
