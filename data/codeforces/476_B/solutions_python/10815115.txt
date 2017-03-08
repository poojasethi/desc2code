#!/usr/bin/env python2.6
import math

def ncr(n, k):
  return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

str1 = raw_input()
str2 = raw_input()

sum1 = { '+': 0, '-': 0 }
sum2 = { '+': 0, '-': 0, '?': 0 }

for i in xrange(len(str1)):
  sum1[str1[i]] += 1
  sum2[str2[i]] += 1

if sum2['+'] > sum1['+'] or sum2['-'] > sum1['-']:
  print float(0)
else:
  print 1.0/(2**sum2['?']) * ncr(sum2['?'], max(sum1['+'] - sum2['+'], sum1['-'] - sum2['-']))
