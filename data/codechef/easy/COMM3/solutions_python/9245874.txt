# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:23:20 2016

@author: shashank
"""
import sys
import math

def distance(x,y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    
T = input()
for i in range(T):
    R = input()
    chef = [int(x) for x in sys.stdin.readline().split()]
    head = [int(x) for x in sys.stdin.readline().split()]
    sous = [int(x) for x in sys.stdin.readline().split()]
    dist1 = distance(chef,head)
    dist2 = distance(chef,sous)
    dist3 = distance(sous,head)
    if ((dist1 <= R and dist2 <= R) or (dist1 <= R and dist3 <= R) or (dist2 <= R and dist3 <= R)):
        print "yes"
    else:
        print "no"
        