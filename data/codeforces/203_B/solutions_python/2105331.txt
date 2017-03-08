import collections
import functools
import itertools
import math
import operator
import re
import sys
from pprint import pprint


def main():
    n, m = map(int, raw_input().split())
    a = [[0] * 2000 for i in xrange(2000)]
    for i in xrange(m):
        x, y = map(int, raw_input().split())
        x, y = x + 500, y + 500
        for p in xrange(3):
            for q in xrange(3):
                a[x + p][y + q] += 1
                if a[x + p][y + q] == 9:
                    print i + 1
                    return
    print -1


if __name__ == '__main__':
    main()