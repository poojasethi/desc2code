#!/usr/bin/python

str = raw_input()

n = len(str)

m = {}

result = 0

for i in xrange(n):
    for j in xrange(i+result+1, n+1):
        if not m.get(str[i:j], False):
            m[str[i:j]] = True
        else:
            result = max(result, j-i)

print result
