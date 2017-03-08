# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import generators
from __future__ import nested_scopes
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import with_statement

import bisect
import collections
import functools
import heapq
import itertools
import math
import operator
import re
import random
import sys
from pprint import pprint

__author__ = 'Aphrodite'


def main():
#    sys.stdin = file('/Users/Aphrodite/program/arena/tmp/input-4')
    iterator = itertools.imap(str.rstrip, sys.stdin.readlines())
    n, k = map(int, next(iterator).split())
    a = map(int, next(iterator).split())
    d = {}
    for i, x in enumerate(a):
        d[x] = d.get(x, 0) + 1
        if len(d) == k:
            j = 0
            while d[a[j]] > 1:
                d[a[j]] -= 1
                j += 1
            print(j + 1, i + 1)
            return
    else:
        print(-1, -1)


if __name__ == '__main__':
    main()
