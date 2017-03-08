#!/usr/bin/env python

import sys
import math
from decimal import Decimal


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def calc_expected(n, p, t):
    expected = Decimal(0.0)
    sum_probability = Decimal(0.0)
    ignore_error = Decimal(1E-300)
    for i in range(0, n + 1):
        i_probability = None
        if i == 0:
            i_probability = Decimal(pow(1 - p, t))
        elif (i < n):
            a = None
            b = None
            if (p <= 0.5):
                a = Decimal(pow(p, i))
                if (a < ignore_error):
                    continue
                b = Decimal(pow(1 - p, t - i))
                if (b < ignore_error):
                    continue
            else:
                b = Decimal(pow(1 - p, t - i))
                if (b < ignore_error):
                    continue
                a = Decimal(pow(p, i))
                if (a < ignore_error):
                    continue
            c = Decimal(nCr(t, i))
            i_probability = a * b * c

        else:
            i_probability = Decimal(1) - sum_probability
        expected += i * i_probability
        sum_probability += i_probability
    return expected


def solve():
    token = sys.stdin.readline().rstrip().split(' ')
    n = int(token[0])
    p = float(token[1])
    t = int(token[2])
    result = 0.0

    if (t <= n):
        result = p * t
    else:
        result = calc_expected(n, p, t)

    print result

if __name__ == '__main__':
    solve()

