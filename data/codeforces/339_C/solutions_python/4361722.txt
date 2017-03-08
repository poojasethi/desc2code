# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(2000)

def printout(result):
    if result[0]:
        print("YES")
        for i in result[1]:
            print(i),
    else:
        print("NO")

def solution(l, w, m):
    if len(l) == m:
        return ( True, l)
    else:
        i = 0
        for i in picknext(l, w):
            tmp = solution(l + [i], w, m)
            if tmp[0]:
                return (True, tmp[1])
        return ( False, )
        
def picknext(seq, weights):
    if seq:
        tmp = abs(sum(seq[0::2]) - sum(seq[1::2]))
        result = [i for i in weights if i > tmp and i != seq[-1]]
        return result
    else:
        return weights

def convert_weights(w):
    result = []
    for i in range(1, len(w) + 1):
        if w[i - 1] == '1':
            result.append(i)
    return result
    
printout(solution([], convert_weights(raw_input()), int(raw_input())))
