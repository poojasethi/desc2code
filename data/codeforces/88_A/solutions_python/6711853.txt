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
from timeit import itertools
# from functools import lru_cache #@lru_cache(maxsize = None)
"""
#reduce(func,list)
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

def distance(d1,d2):
    if d1>d2:
        return 12+d2-d1
    else:
        return d2-d1

    
notes={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'B':10,'H':11}
triad=[notes[x] for x in readstrings()]
for conf in itertools.permutations(triad):
    d1=distance(conf[0], conf[1])
    d2=distance(conf[1], conf[2])
    if d1==4 and d2==3:
        writeline('major')
        sys.exit()
    elif d1==3 and d2==4:
        writeline('minor')
        sys.exit()
writeline('strange')


