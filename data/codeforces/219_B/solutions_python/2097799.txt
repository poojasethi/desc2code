import collections
import functools
import itertools
import math
import operator
import re
import sys


def count(n):
    return len(str(n)) - len(str(n).rstrip('9'))

def main():
    p, d = map(int, raw_input().split())
    m = 10
    res = count(p), p
    while m <= p:
        diff = p % m + 1
        if diff <= d:
            res = max(res, (count(p - diff), p - diff))
        m *= 10
    print res[1]


if __name__ == '__main__':
    main()
