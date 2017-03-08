# -*- coding: utf-8 -*-

############################################################################
#                                                                          #
#                To see the world in a grain of sand,                      #
#                And a heaven in a wild flower;                            #
#                Hold infinity in the palm of your hand,                   #
#                And eternity in an hour.                                  #
#                                                                          #
############################################################################

from __future__ import division
from __future__ import print_function
from future_builtins import *

import bisect
import collections
import copy
import fractions
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


def func(m, d):
    a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(a[0:m]) + d - 1

def main():
    sys.stdin = open('input.txt')
    sys.stdout = open('output.txt', 'w')
    iterator = itertools.imap(str.rstrip, sys.stdin.readlines())
    n = int(next(iterator))
    tab = {}
    for _ in range(n):
        m, d, p, t = map(int, next(iterator).split())
        x = func(m, d)
        for i in range(t):
           tab[x - i - 1] = tab.get(x - i - 1, 0) + p
    print(max(tab.values()))

if __name__ == '__main__':
    main()
