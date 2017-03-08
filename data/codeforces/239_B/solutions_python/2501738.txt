# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from future_builtins import *

import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import operator
import os
import re
import random
import subprocess
import sys
import unittest
from pprint import pprint
from StringIO import StringIO

__author__ = 'Aphrodite'


def func(a):
    for idx, x in enumerate(a):
        if x.isdigit():
            a[idx] = int(x)
    cnt = [0] * 10
    last, idx, dir = None, 0, 1
    while 0 <= idx < len(a):
#        print(idx)
#        print(a)
        if a[idx] == '<':
            dir = -1
            if last == '<':
                a.pop(idx + 1)
            if last == '>':
                a.pop(idx - 1)
                idx -= 1
            last = '<'
        elif a[idx] == '>':
            dir = 1
            if last == '<':
                a.pop(idx + 1)
            if last == '>':
                a.pop(idx - 1)
                idx -= 1
            last = '>'
        else:
            cnt[a[idx]] += 1
            last = a[idx]
            a[idx] -= 1
            if a[idx] < 0:
                a.pop(idx)
                if dir == 1:
                    idx -= 1
        idx += dir
#        print(a)
    print(' '.join(map(str, cnt)))


def main():
    iterator = itertools.imap(str.rstrip, sys.stdin.readlines())
    n, q = map(int, next(iterator).split())
    s = next(iterator)
    for _ in range(q):
        a, b = map(int, next(iterator).split())
        func(list(s[a - 1:b]))

if __name__ == '__main__':
    main()
#    func(list('1>3>22<'))
