import sys
import itertools
import bisect
import math
from fractions import gcd



def solve():
    a = sys.stdin.readline().strip("\n\r")
    b = sys.stdin.readline().strip("\n\r")
    
    words = [len(a), len(a) + len(b) + 2]

    a += "#" + b
    
    states = []
    
    state0 = [0, 0, {}]
    sz = 0
    last = 0
    
    counters = []
    
    counter0 = [0] * len(words)
    counters.append(counter0)
    state0[0] = 0
    state0[1] = None
    
    states.append(state0)
    sz += 1
    pushback = []
    
    for ci in range(len(a)):
        c = a[ci]
        cur = sz
        sz += 1
        
        state = [states[last][0] + 1, None, {}]
        states.append(state)
        
        counter = [0] * len(words)
        word = bisect.bisect_left(words, ci)
        counter[word] = 1
        counters.append(counter)
            
        pushback.append((states[last][0] + 1, cur))
        
        p = last
        while p <> None and c not in states[p][2]:
            states[p][2][c] = cur
            p = states[p][1]
        
        if p == None:
            states[cur][1] = 0
        else:
            q = states[p][2][c]
            if (states[p][0] + 1 == states[q][0]):
                states[cur][1] = q
            else:
                clone = sz
                state = [states[p][0] + 1, states[q][1], states[q][2].copy()]
                pushback.append((states[p][0] + 1, clone))
                sz += 1
                states.append(state)
                counter = [0] * len(words)
                counters.append(counter)
                while p <> None and states[p][2][c] == q:
                    states[p][2][c] = clone
                    p = states[p][1]
                states[cur][1] = clone
                states[q][1] = clone
        last = cur
    
    pushback.sort(reverse = True)
    for _, i in pushback:
        for j in range(len(counters[i])):
            counters[states[i][1]][j] += counters[i][j]
    
    terminal = set()
    while last <> 0:
        terminal.add(last)
        last = states[last][1]
    
    """print words
    print a
    for i, s in enumerate(states):
        print i, " - ", counters[i], " - ", s"""
    
    best = 10e10
    for i in range(len(states)):
        if counters[i][0] == 1 and counters[i][1] == 1:
            best = min(best, states[states[i][1]][0] + 1)
            
    if best == 10e10:
        print -1
        return
    
    print best               
    
solve()
