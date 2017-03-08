# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split(' '))

result = [0 for x in xrange(n)]
for i in xrange(m):
    votes = map(int, raw_input().split(' '))
    result[votes.index(max(votes))] +=1

print(result.index(max(result)) + 1)
