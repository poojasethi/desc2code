#!/usr/bin/python
# from collections import deque
from sys import *
from itertools import *


def main():
    n, m, k = map(int, raw_input().split())
    a = list(map(lambda t: int(t) - 1, raw_input().split()))
    b = list(map(lambda t: int(t) - 1, raw_input().split()))
    a = list(reversed(sorted(a)))
    b = list(reversed(sorted(b)))

    alice = False
    if len(a) > len(b):
        alice = True
    else:
        for i in range(len(a)):
            if a[i] > b[i]:
                alice = True
                break

    print('YES' if alice else 'NO')

if __name__ == '__main__':
    main()
