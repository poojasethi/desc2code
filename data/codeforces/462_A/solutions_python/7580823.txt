n = int(raw_input())

s = []
for i in xrange(n):
  s.append(raw_input())

ds = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    ]

for i in xrange(n):
  for j in xrange(n):
    cnt = 0
    for d in ds:
      x = d[0] + i
      y = d[1] + j
      if x >= 0 and x < n and y >= 0 and y < n:
        if s[x][y] == 'o':
          cnt += 1
    if cnt % 2:
      print 'NO'
      exit(0)

print 'YES'
