import collections
import functools
import itertools
import math
import operator
import re
import sys


def func(lst, k):
    res = lst[:]
    cnt = 0
    for i in xrange(1, len(lst)):
        if res[i] == res[i - 1]:
            for x in xrange(k):
                tmp = chr(ord('A') + x)
                if tmp != res[i - 1] and (i == len(lst) - 1 or i < len(lst) - 1 and tmp != res[i + 1]):
                    res[i] = tmp
                    break
            else:
                for x in xrange(k):
                    tmp = chr(ord('A') + x)
                    if tmp != res[i - 1]:
                        res[i] = tmp
                        break
            cnt += 1
    return cnt, res


def main():
    n, k = map(int, raw_input().split())
    s = raw_input()
    a = list(s)
    if k == 2:
        p1 = p2 = 0
        q1 = ['A' if i % 2 == 0 else 'B' for i in xrange(n)]
        q2 = ['A' if i % 2 == 1 else 'B' for i in xrange(n)]
        p1 = sum(1 if q1[i] != a[i] else 0 for i in xrange(n))
        p2 = sum(1 if q2[i] != a[i] else 0 for i in xrange(n))
    else:
        p1, q1 = func(a, k)
        p2, q2 = func(list(reversed(a)), k)
        q2.reverse()
    res = min((p1, q1), (p2, q2))
    print res[0]
    print ''.join(res[1])


if __name__ == '__main__':
    main()