#!/usr/bin/python
import sys
n,x=map(int,raw_input().split())
c=map(int,raw_input().split())
p=sum(c)
print (abs(p)-1)/x+1
