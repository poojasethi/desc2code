# -*- coding: utf-8 -*-

"""
  Also can use trie, but we can use polynomial hash
"""

d = set()
ss = set()

MOD = (2**64)-1

p = [0] * 200
for i in xrange(200):
  p[i] = 11**i

prime = 63

def calc(s):
  c = 0
  for i, w in enumerate(s):
    c += p[i%prime]*ord(w)
    c %= MOD
  return c

n, m = map(int, raw_input().split())
for _ in xrange(n):
  s = raw_input()
  ss.add(s)
  c = calc(s)
  d.add(c)


for _ in xrange(m):
  s = raw_input()
  c = calc(s)
  flag = 0
  for i, w in enumerate(s):
    it = ['a', 'b', 'c']
    it.remove(w)
    for r in it:
      k = c + MOD - ord(w)*p[i%prime] + ord(r)*p[i%prime]
      k %= MOD
      if k in d and (s[:i]+r+s[i+1:]) in ss:
        flag = 1
        break
    if flag:break

  if flag:
    print 'YES'
  else:
    print 'NO'
