from __future__ import division
from numpy import *
import sys
from collections import namedtuple #x=namedtuple('point','x y')
from math import *
from collections import deque, OrderedDict #append #popleft
from fractions import gcd
from copy import copy ,deepcopy
from collections import Counter #Counter(list)
import re #re.split("[^a-zA-Z]",text)
import operator
# from functools import lru_cache #@lru_cache(maxsize = None)
"""
#reduce(func,list)
#Counter(list)
#map(func,list)
#filter(func,list)
#xor=lambda x,y :x^y
#sign = lambda x: math.copysign(1, x)
#list.reverse() 
#list.sort() list=sorted(list)
list.sort(key=operator.itemgetter(1,2))
#reverse word word[::-1]
#word.islower()
#word.lower() word.upper()
x = x1 if exp1 else x2
any([false,true])
all([true,false])
"a".isalpha()
"1".isdigit()
"""

fin=sys.stdin ;fout=sys.stdout 
# fin=open('../in','r') ; fout=open('../out','w')
def readline():
    return fin.readline().strip()
def readstrings():
    return fin.readline().strip().split(' ')
def writeline(value):
    fout.write(str(value))
    fout.write("\n")
def read_integers():
    return [int(x) for x in fin.readline().strip().split(' ')]
def read_integer():
    return int(fin.readline().strip())
n,k=read_integers()
num=read_integers()
b,a,acc=[],[],[0]
maxi,pos,s=0,0,0
for i in range(0,n):
    s+=num[i]
    acc.append(s)
s=0
for i in range(0,n-k+1):
    x=acc[i+k]-acc[i]
    b.append(x)
    if x>maxi:
        maxi=x
        pos=i
    a.append((maxi,pos))
ap,bp,mx=0,0,0
for i in range(k,n-k+1):
    if b[i]+a[i-k][0]>mx:
        ap=a[i-k][1]
        bp=i
        mx=b[i]+a[i-k][0]
writeline(str(ap+1)+" "+str(bp+1))