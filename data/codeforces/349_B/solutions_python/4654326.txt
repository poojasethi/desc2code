#! /usr/bin/python

import sys
import bisect

def find_max_num(v, a):
    weight_map = {a[i]: i + 1 for i in range(len(a))}
    weights = weight_map.keys()
    weights.sort()
    min_a = weights[0]
    max_len = v / min_a

    if max_len == 0:
        return -1

    min_digit = weight_map[min_a]
    result = [str(min_digit) for i in range(max_len)]

    r = v - max_len * min_a
    for c in range(max_len):
        d = min_digit
        for i in reversed(range(min_digit - 1, 9)):
            if r + min_a - a[i] >= 0:
                r -= (a[i] - min_a)
                d = i + 1
                break
        if d == min_digit:
            break
        result[c] = str(d)

    return ''.join(result)

if __name__ == '__main__':
    V = int(sys.stdin.readline())
    a = map(int, sys.stdin.readline().split(' '))
    print find_max_num(V, a)

