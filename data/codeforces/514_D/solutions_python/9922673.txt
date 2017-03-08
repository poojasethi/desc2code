# -*- coding: utf-8 -*-

q = [ [] for _ in xrange(5) ]

def add(idx, x):
  while len(q[idx]) and q[idx][-1][1] <= x[1]:
    q[idx].pop()
  q[idx].append(x)

def pop(idx, i):
  if len(q[idx]) and q[idx][0][0] <= i:
    q[idx].pop(0)


n, m, k = map(int, raw_input().split())

ans = 0
out = [0]*m
# two-points
left  = 0
right = -1

def get():
  if not q[0]: return 1
  s = 0
  for i in xrange(m):
    s += q[i][0][1]
    if s > k: return 0
  return 1

while left < n and right < n:
  if get():
    #print left, right, q
    if q[0] and right - left + 1 > ans:
      ans = right - left + 1
      out = []
      for i in xrange(m):
        out.append(q[i][0][1])

    right += 1
    if right >= n: break
    new = map( int, raw_input().split() )
    for i in xrange(m):
      add(i, ( right, new[i] ) )
  else:
    for i in xrange(m):
      pop(i, left)
    left += 1

for i in out:
  print i,
