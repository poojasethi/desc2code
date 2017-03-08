#!/usr/bin/python

import sys


def cells(a, b, mod):
    for i in range(a):
        for j in range(b):
            if (i + j) % 2 == mod:
                yield (i, j)


def numbers(n, mod):
    for x in range(n):
        if x % 2 == mod:
            yield x


def main():
    n, a, b = raw_input().strip().split()
    n = int(n)
    a = int(a)
    b = int(b)
    ans = [b * [0] for _ in range(a)]
    for mod in [0, 1]:
        for ((x, y), i) in zip(cells(a, b, mod), numbers(n, mod)):
            ans[x][y] = i + 1

    good = any(n in ans[i] for i in range(a)) and (n == 1 or any(
        (n - 1) in ans[i] for i in range(a)))
    if good:
        for line in ans:
            for x in line:
                print x,
            print
    else:
        print -1

main()
