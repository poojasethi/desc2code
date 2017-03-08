#!/usr/bin/python
"""
http://www.codechef.com/problems/LEBOMBS

Testing:
    nosetests --with-doctest <file>

Input:
3
3
010
5
10001
7
0000000

Output:
0
1
7
"""


def alg(a):
    """
    >>> alg('010')
    0
    >>> alg('10001')
    1
    >>> alg('0000000')
    7
    >>> alg('0')
    1
    >>> alg('1')
    0
    """

    n = len(a)
    res = 0
    for i in xrange(n):
        prev = 1 if i > 0 and a[i-1] == '1' else 0
        cur = 1 if a[i] == '1' else 0
        next = 1 if i < n-1 and a[i+1] == '1' else 0
        if prev + cur + next == 0:
            res += 1
    return res


if __name__ == "__main__":

    for _ in range(input()):
        n = input()
        print alg(raw_input()[:n])  # for some reason we have to cut string, tests are broken
