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
import copy
import functools
import heapq
import itertools
import math
import operator
import os
import re
import random
import sys
from pprint import pprint

__author__ = 'Aphrodite'


def main():
    iterator = itertools.imap(str.rstrip, sys.stdin.readlines())
    s, k = map(int, next(iterator).split())
    a = [0, 1]
    while a[-1] < s:
        if (len(a)) < k:
            a.append(sum(a))
        else:
            a.append(sum(a[-k:]))
#    print(a)
    res = []
    while s > 0:
        idx = bisect.bisect(a, s) - 1
        s -= a[idx]
        res.append(a[idx])
    if len(res) == 1:
        res.append(0)
    print(len(res))
    print(' '.join(map(str, res)))


if __name__ == '__main__':
    main()
