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


def main():
    iterator = itertools.imap(str.rstrip, sys.stdin.readlines())
    n, m, x, y = map(int, next(iterator).split())
    a = [next(iterator) for _ in range(n)]
    cnt = [[0] * (m + 1) for _ in range(2)]
    for i in range(m):
        b, w = 0, 0
        for j in range(n):
            if a[j][i] == '.':
                b += 1
            else:
                w += 1
        cnt[0][i + 1] = cnt[0][i] + b
        cnt[1][i + 1] = cnt[1][i] + w
    dp = [[float('inf')] * (m + 1) for _ in range(2)]
    dp[0][0] = dp[1][0] = 0
    for i in range(1, m + 1):
        for k in range(x, y + 1):
            if k > i:
                continue
            for j in range(2):
                aux = dp[1 - j][i - k] + (cnt[1 - j][i] - cnt[1 - j][i - k])
#                print(i, k, j, aux)
                dp[j][i] = min(dp[j][i], aux)
    print(min(dp[0][m], dp[1][m]))
#    pprint(dp)


if __name__ == '__main__':
    main()
